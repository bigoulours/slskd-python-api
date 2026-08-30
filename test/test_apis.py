from os import path
import sys
import yaml
import functools
from itertools import chain
from inspect import isclass, signature
from requests import HTTPError
sys.path.append(path.abspath('.'))
import slskd_api

from pydantic import TypeAdapter, ValidationError


def rgetattr(obj, attr, *args):
    def _getattr(obj, attr):
        return getattr(obj, attr, *args)
    return functools.reduce(_getattr, [obj] + attr.split('.'))


with open("test/server_config.yaml", 'r') as f:
    config = yaml.load(f, Loader=yaml.Loader)
        
slskd = slskd_api.SlskdClient(config['server_url'], api_key=config['api_key'])


def test_method(m, *args):
    print(f'Testing {m}...')
    method = rgetattr(slskd, m)
    t = signature(method).return_annotation
    ta = TypeAdapter(t)
    res = method(*args)
    
    t_repr = t.__name__ if isclass(t) else t

    try:
        ta.validate_python(res)
        print(f'{m} succesfully returned an object of type {t_repr}.')
    except ValidationError as e:
        print(e)
        
    return res


search_text = t if (t:=config.get('search_text')) else 'something'
   
# list of t-uples with the following structure: (<method>, <method_args>)
api_tests = [
    ('application.state', ),
    ('application.version', ),
    ('application.check_updates', ),
    ('conversations.get_all', ),
    ('events.get', ),
    ('files.get_downloads_dir', ),
    ('files.get_incomplete_dir', ),
    ('logs.get', ),
    ('options.get', ),
    ('options.get_startup', ),
    ('rooms.get_all_joined', ),
    ('rooms.get_all', ),
    ('searches.search_text', search_text),
    ('searches.get_all', ),
    ('server.state', ),
    ('session.auth_valid', ),
    ('session.security_enabled', ),
    ('shares.get_all', ),
    ('shares.all_contents', ),
    ('telemetry.get_metrics', ),
    ('telemetry.get_kpis', ),
    ('telemetry.get_transfer_summary', ),
    ('telemetry.get_transfer_histogram', ),
    ('telemetry.get_transfer_leaderboard', 'Download'),
    ('telemetry.get_transfer_exceptions', 'Upload'),
    ('telemetry.get_transfer_exceptions_pareto', 'Upload'),
    ('telemetry.get_most_dl_directories', ),
    ('transfers.get_all_downloads', ),
    ('transfers.get_all_uploads', ),
]

res_dict = {}

for method, *args in api_tests:
    res = test_method(method, *args)
    match method:
        case 'conversations.get_all':
            res_dict['conversations'] = res
        case 'files.get_downloads_dir':
            res_dict['downloads_dir'] = res
        case 'files.get_incomplete_dir':
            res_dict['incomplete_dir'] = res
        case 'rooms.get_all_joined':
            res_dict['joined_rooms'] = res
        case 'rooms.get_all':
            res_dict['all_rooms'] = res
        case 'searches.get_all':
            res_dict['all_searches'] = res
        case 'shares.get_all':
            res_dict['all_shares'] = res
        case 'transfers.get_all_downloads':
            res_dict['all_downloads'] = res
        case 'transfers.get_all_uploads':
            res_dict['all_uploads'] = res
            

if (convs := res_dict.get('conversations')):
    usr = next(c['username'] for c in convs)
    test_method('conversations.get', usr)
    test_method('conversations.get_messages', usr)
    

if (dl_dir := res_dict.get('downloads_dir')):
    dir_name = next(d['name'] for d in dl_dir.get('directories'))
    test_method('files.get_downloaded_directory', dir_name)
    
    
if (inc_dir := res_dict.get('incomplete_dir')):
    dir_name = next(d['name'] for d in inc_dir.get('directories'))
    test_method('files.get_incomplete_directory', dir_name)
    

if (rooms := res_dict.get('all_rooms')):
    joined_rooms = res_dict.get('joined_rooms', [])
    new_room = next(r['name'] for r in rooms if r['name'] not in joined_rooms)
    test_method('rooms.join', new_room)
    test_method('rooms.get_joined', new_room)
    test_method('rooms.get_messages', new_room)
    test_method('rooms.get_users', new_room)
    test_method('rooms.leave', new_room)
    

if (searches := res_dict.get('all_searches')):
    search_id = next(s['id'] for s in searches)
    test_method('searches.state', search_id)
    test_method('searches.search_responses', search_id)
    

if (shares := res_dict.get('all_shares')):
    share_id = next(s['id'] for s in shares['local'])
    test_method('shares.get', share_id)
    test_method('shares.contents', share_id)
    
    
if (all_dl := res_dict.get('all_downloads')):
    dl_user = next(dl['username'] for dl in all_dl)
    dls = test_method('transfers.get_downloads', dl_user)
    dl_id = next(f['id'] for d in dls['directories'] for f in d['files'])
    test_method('transfers.get_download', dl_user, dl_id)
    
    
if (all_ul := res_dict.get('all_uploads')):
    ul_user = next(ul['username'] for ul in all_ul)
    uls = test_method('transfers.get_uploads', ul_user)
    ul_id = next(f['id'] for d in uls['directories'] for f in d['files'])
    test_method('transfers.get_upload', ul_user, ul_id)


user_src = chain(res_dict.get('conversations', []), res_dict.get('all_downloads', []), res_dict.get('all_uploads', []))
user = next((e['username'] for e in user_src if slskd.users.status(e['username'])['presence']=='Online'), None)

if not user:
    print("No user found to test users API")
else:
    print(f"Testing user API on {user}...") 
    test_method('users.address', user)
    usr_root_dir = test_method('users.browse', user)
    some_dir = next(d['name'] for d in chain(usr_root_dir['directories'], usr_root_dir['lockedDirectories']))
    test_method('users.directory', user, some_dir)
    try:
        test_method('users.browsing_status', user)
    except HTTPError:
        pass
    test_method('users.info', user)
    test_method('users.status', user)