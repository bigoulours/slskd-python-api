from os import listdir
from os.path import join
import re

API_PATH = "slskd_api/apis"
fct_pat = re.compile(r'def .*?    return', re.MULTILINE + re.DOTALL)
url_pat = re.compile(r'url\s*=\s*(.*)', re.MULTILINE)
op_pat = re.compile(r'response\s*=\s*self\.session\.(.*?)\(', re.MULTILINE)

def parse_api_fcts(API_VERSION = 0):
    apis = listdir(API_PATH)
    function_dict = {}
    for fn in apis:
        if not fn.startswith('_'):
            title = fn[:-3]
            function_dict[title] = []
            with open(join(API_PATH, fn), 'r') as f:
                content = f.read()
            funcs = re.findall(fct_pat, content)
            for f in funcs:
                url_str = re.search(url_pat, f).group(1).replace('self.api_url', f'/api/v{API_VERSION}')
                url_str = re.sub(r'''("|( f)?'| |\+)''', '', url_str)
                url_str = url_str.replace('event_type', 'type')
                url_str = re.sub(r'quote\((.*?)\)', r'\g<1>', url_str)
                op = re.search(op_pat, f).group(1).upper()
                function_dict[title].append((op, url_str))
            
    return function_dict
    

if __name__ == '__main__':
    from pprint import pprint
    r = parse_api_fcts()
    pprint(r)