import json
from haralyzer import HarParser


def get_info_from_har(file_path):
    with open(file_path, 'r', encoding='UTF8') as f:
        har_parser = HarParser(json.loads(f.read()))

    method = har_parser.pages[0].actual_page['request']['method']
    url = har_parser.pages[0].actual_page['request']['url']
    headers = {}
    for header in har_parser.pages[0].actual_page['request']['headers']:
        key = header['name']
        value = header['value']
        headers[key] = value

    queryString = har_parser.pages[0].actual_page['request']['queryString']
    cookies = har_parser.pages[0].actual_page['request']['cookies']

    context = {
        'method': method,
        'url': url,
        'headers': headers,
        'queryString': queryString,
        'cookies': cookies
    }

    return context


file_path = 'resources/gatling.har'
context = get_info_from_har(file_path)
