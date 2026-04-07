from os import path
import sys
import yaml
import functools
from inspect import isclass, signature
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


def test_method(m, args):
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
    res = test_method(method, args)
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
        case 'shares.all_contents':
            res_dict['shares_contents'] = res
        case 'transfers.get_all_downloads':
            res_dict['all_downloads'] = res
        case 'transfers.get_all_uploads':
            res_dict['all_uploads'] = res
            
