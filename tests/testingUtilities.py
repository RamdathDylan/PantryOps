import requests

"""
Testing utility for GET API calls. Calls a GET request to the provided URL. 

Parameters:
test — the test that this method is called in. (self)
URL — the URL endpoint that is being tested.
params — provided URL parameters, defaults to an empty list.
get_header - provides headers for the request, defaults to an empty list.
expected_code - the expected response code to an operation, defaults to 200. 

Returns:
    response - HTTP response entity in json format. 

""" 
def get_rest_call(test, url, params = {}, get_header = {}, expected_code = 200):
    response = requests.get(url, params, headers = get_header)
    test.assertEqual(expected_code, response.status_code,
                     f'Response code to {url} not {expected_code}')
    return response.json()


"""
Testing utility for POST API calls.

Parameters:
test — the test that this method is called in. (self)
URL — the URL endpoint that is being tested.
params — provided URL parameters, defaults to an empty list.
get_header - provides headers for the request, defaults to an empty list.
expected_code - the expected response code to an operation, defaults to 200. 

Returns:
    response - HTTP response entity in json format. 
""" 
def post_rest_call(test, url, params = {}, post_header = {},expected_code = 200):
    '''Implements a REST api using the POST verb'''
    response = requests.post(url, params, headers = post_header)
    test.assertEqual(expected_code, response.status_code,
                     f'Response code to {url} not {expected_code}')
    return response.json()

"""
Testing utility for PUT API calls.

Parameters:
test — the test that this method is called in. (self)
URL — the URL endpoint that is being tested.
params — provided URL parameters, defaults to an empty list.
get_header - provides headers for the request, defaults to an empty list.
expected_code - the expected response code to an operation, defaults to 200. 

Returns:
    response - HTTP response entity in json format. 
""" 
def put_rest_call(test, url, params = {}, put_header = {},expected_code = 200):
    '''Implements a REST api using the PUT verb'''
    response = requests.put(url, params, headers = put_header)
    test.assertEqual(expected_code, response.status_code,
                     f'Response code to {url} not {expected_code}')
    return response.json()

"""
Testing utility for DELETE API calls.

Parameters:
test — the test that this method is called in. (self)
URL — the URL endpoint that is being tested.
params — provided URL parameters, defaults to an empty list.
get_header - provides headers for the request, defaults to an empty list.
expected_code - the expected response code to an operation, defaults to 200. 

Returns:
    response - HTTP response entity in json format. 
""" 
def delete_rest_call(test, url, delete_header={}, expected_code = 200):
    '''Implements a REST api using the DELETE verb'''
    response = requests.delete(url, headers = delete_header)
    test.assertEqual(expected_code, response.status_code,
                     f'Response code to {url} not {expected_code}')
    return response.json()