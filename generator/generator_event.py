import requests
import json
import os
import base64
import collections
import urlparse
import markdown2

from logging import getLogger, INFO
from simple_log import LoggingSetup

log_error = getLogger('API_error')
setup_log = LoggingSetup(process_name='API_error',
                         daily_file=True,
                         console_level=INFO,
                         file_level=INFO)
setup_log.init_logging()

def convert_text_to_anchor_url(text):
    if not text:
        return 'not defined'
    return text.strip().replace(' ', '-').lower()


def convert_unit_name(unit):
    return unit.replace('_', ' ').title().strip()


def html_encode_angle_brackets(text):
    return text.replace('<', '&lt;').replace('>', '&gt;')


# read config file
config_data = open('./event-config.json', mode='r').read()
config = json.loads(config_data)

if not isinstance(config, dict):
    raise 'Invalid config file'

username = config['username']
password = config['password']
base64_string = base64.b64encode('%s:%s' % (username, password))

try:
    for directory in config['output_directories']:
        os.mkdir(directory)
except OSError:
    pass

all_endpoints = []

# iterate over endpoints
for endpoint in config['endpoints']:
    print 'Building: {} description'.format(endpoint['endpoint_parameter'])

    all_endpoints.append({
        'title': endpoint['endpoint_title'],
        'url': endpoint['display_url'],
        'parameter': endpoint['endpoint_parameter'],
        'description': endpoint['endpoint_description']
    })

    markdown_output = '''
{title}
======

`{endpoint_example}`

{description}

'''.format(title=endpoint['endpoint_title'],
           description=endpoint['endpoint_description'],
           endpoint_example=endpoint['display_url'])

    # build methods description table
    markdown_output += '''### Methods

Method | URL | Description
--- | --- | ---
'''

    # iterate over examples
    for example in endpoint['examples']:
        markdown_output += '''**[{method}](/documentation/endpoint/{parameter}#{anchor})** | `{url}` | {description}
'''.format(method=example['method'],
           url=example['display_url'],
           anchor=convert_text_to_anchor_url(example['title']),
           description=example['title'],
           parameter=endpoint['endpoint_parameter'])

    # build attribute description table
    markdown_output += '''
### Object Attributes

Attribute | Type | Readonly | Nullable | Has Default
--- | --- | --- | --- | ---
'''

    # make HTTP OPTIONS call to get object information
    url = config['api_base_url'] + endpoint['endpoint_url']
    response = requests.options(url,
                                auth=(username, password),
                                headers={
                                    'Origin': config['api_base_url']
                                })

    # build attribute table
    attributes = response.json()
    attributes = collections.OrderedDict(sorted(attributes.items()))

    for attribute, value in attributes.iteritems():
        attr_type = value['type']
        if attr_type == 'uom' and value['unit']:
            attr_type += ': ' + convert_unit_name(value['unit'])
        readonly = '&bullet;' if value['read_only'] is True else '&nbsp;'
        nullable = '&bullet;' if value['nullable'] is True else '&nbsp;'
        has_default = '&bullet;' if value['has_default'] is True else '&nbsp;'
        markdown_output += '''`{attribute}` | {type} | {readonly} | {nullable} | {has_default}
'''.format(attribute=attribute,
           type=attr_type,
           readonly=readonly,
           nullable=nullable,
           has_default=has_default)

    # iterate over examples
    for example in endpoint['examples']:
        print 'Building: {} - {} {}'.format(endpoint['endpoint_parameter'], example['method'], example['url'])

        # set title and description
        markdown_output += '''
{title}
------
<code request-method="{method}">**{method}** {url}</code>

'''.format(title=example['title'],
           method=example['method'],
           url=html_encode_angle_brackets(example['display_url']))

        try:
            markdown_output += example['description'] + '\r\n'
        except KeyError:
            pass

        # build query parameter table
        try:
            parameters = collections.OrderedDict(
                sorted(example['query_parameters'].items()))
            markdown_output += '''
### Query Parameters

Parameter | Type | Description
--- | --- | ---
'''
            for key, parameter in parameters.iteritems():
                markdown_output += '''`{param}` | {type} | {description}
'''.format(param=key,
                    type=parameter['type'], description=parameter['description'])

            markdown_output += '\r\n\r\n'
        except KeyError:
            pass

        # make API request
        auth = (username, password)
        url = config['api_base_url'] + example['url']
        method = example['method'].upper()

        # set headers
        headers = {}
        if example['headers']:
            headers = example['headers']
        headers['Origin'] = config['api_base_url']
        headers['Host'] = urlparse.urlparse(config['api_base_url']).netloc

        # add body
        request_body = ''
        payload = None
        if example['body']:
            payload = example['body']
            if headers['Content-Type'] and headers['Content-Type'] == 'application/json' and isinstance(payload, (list, dict)):
                payload = json.dumps(payload, indent=4, sort_keys=True)
                request_body = payload
            else:
                request_body = str(payload)
            request_body = '\r\n\r\n' + payload
            headers['Content-Length'] = str(len(payload))

        headers = collections.OrderedDict(sorted(headers.items()))
        request_headers = '{method} {url}\r\nAuthorization: Basic {auth}'.format(method=example['method'],
                                                                                 url=url,
                                                                                 auth=base64_string,
                                                                                 origin=config['api_base_url'])
        for header, value in headers.iteritems():
            if header and value:
                request_headers += '\r\n{header}: {value}'.format(
                    header=header, value=value)

        # make request
        response = None
        verify = False
        timeout = 60
        if method == 'GET':
            response = requests.get(
                url, auth=auth, headers=headers, verify=verify, timeout=timeout)
        elif method == 'POST':
            response = requests.post(
                url, auth=auth, headers=headers, data=payload, verify=verify, timeout=timeout)
        elif method == 'PUT':
            response = requests.put(
                url, auth=auth, headers=headers, data=payload, verify=verify, timeout=timeout)
        elif method == 'DELETE':
            response = requests.delete(
                url, auth=auth, headers=headers, verify=verify, timeout=timeout)
        else:
            response = requests.options(
                url, auth=auth, headers=headers, verify=verify, timeout=timeout)

        headers = collections.OrderedDict(sorted(response.headers.items()))
        code_description = requests.status_codes._codes[response.status_code][0]
        code_description = code_description.replace('_', ' ').title()
        http_version = str(response.raw.version)
        if len(http_version) > 1:
            http_version = http_version[0] + '.' + http_version[1:]
        response_headers = 'HTTP/{http_version} {code} {code_description}'.format(http_version=http_version,
                                                                                  code=response.status_code,
                                                                                  code_description=code_description)
        for header, value in headers.iteritems():
            if header and value:
                response_headers += '\r\n{header}: {value}'.format(
                    header=header, value=value)

        response_body = ''
        try:
            response_json = response.json()
            response_body = '\r\n\r\n' + \
                json.dumps(response_json, indent=4, sort_keys=True)
        except ValueError:
            response_body = '\r\n\r\n' + str(response.content)

        markdown_output += '''
### Example
```http
{request_headers}{request_body}
```

```http
{response_headers}{response_body}
```

'''.format(request_headers=request_headers,
           request_body=request_body,
           response_headers=response_headers,
           response_body=response_body)

        html_output = markdown2.markdown(markdown_output, extras=[
                                         'code-friendly', 'fenced-code-blocks', 'tables', 'header-ids', 'metadata'])

        # write out markdown output to file for each endpoint
        directory = config['output_directories']
        output_file = os.path.join(
            directory, endpoint['endpoint_parameter'] + '.md')
        md_file = open(output_file, 'w+')
        md_file.write(markdown_output)
        md_file.close()


# write out list of all pages
json_endpoints = json.dumps(all_endpoints)
directory = config['output_directories']
output_file = os.path.join(
    directory, 'index.json')
text_file = open(output_file, 'w+')
text_file.write(json_endpoints)
text_file.close()
