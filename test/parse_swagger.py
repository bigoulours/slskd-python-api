from bs4 import BeautifulSoup
import yaml
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

def parse_swagger():

    with open("test/server_config.yaml", 'r') as f:
        config = yaml.load(f, Loader=yaml.Loader)

    driver = webdriver.Chrome()
    driver.get(config['swagger_url'])
    timeout = 6 # seconds
    WebDriverWait(driver, timeout).until(EC.presence_of_element_located((By.XPATH, "//*[@class='opblock-tag-section is-open']")))

    soup = BeautifulSoup(driver.page_source, "html.parser")

    function_dict = {}

    cats = soup.find_all('div', class_='opblock-tag-section is-open')

    for c in cats:
        title = c.find('h3').find('a', class_='nostyle').find('span').text
        function_dict[title] = []
        funcs = c.find_all('button', class_='opblock-summary-control')
        for f in funcs:
            op = f.find('span', class_='opblock-summary-method').text
            path = f.find('span', class_='opblock-summary-path').attrs['data-path']
            function_dict[title].append((op, path))

    return function_dict


if __name__ == '__main__':
    from pprint import pprint
    r = parse_swagger()
    pprint(r)