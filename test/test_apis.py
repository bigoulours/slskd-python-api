from os import path
import sys
import yaml
import functools
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


def test_method(m, t, args):
    print(f'Testing {m}...')
    ta = TypeAdapter(t)
    method = rgetattr(slskd, m)
    res = method(*args)

    try:
        ta.validate_python(res)
        print(f'{m} succesfully returned an object of type {t.__name__}.')
    except ValidationError as e:
        print(e)

   
# list of t-uples with the following structure: (<method>, <return_type>, <method_args>)
api_tests = [
    ('application.state', slskd_api.apis._types.AppState),
    ('application.version', str),
    ('application.check_updates', slskd_api.apis._types.AppVersion),
]

for test in api_tests:
    test_method(test[0], test[1], test[2:])