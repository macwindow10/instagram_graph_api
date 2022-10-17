import requests
import json


def getCreds():
    """ Get creds required for use in the applications

    Returns:
        dictonary: credentials needed globally
    """

    creds = dict()  # dictionary to hold everything
    creds[
        'access_token'] = 'EAAGZC0NO2uTwBABkuS8nsbsHoRRYsfGQjl7bce3OrXaznUn0LHMmsT3DTZBAlE07xsxpVAELFHUyBH8dGmwIZAjeiRt5vicZCHgEVNYucpH8x1IYASUTwzxmHd8tJ0m8ZAakEWG6Q3Ex26jWMC9UWb9GcWXDSASMjFlxNk7IcwJaIZCZARmXDidJdY4WosZAHlXvIJAZBYpTrzTTVRCi7jp74'
    creds['graph_domain'] = 'https://graph.facebook.com/'  # base domain for api calls
    creds['graph_version'] = 'v15.0'  # version of the api we are hitting
    creds['endpoint_base'] = creds['graph_domain'] + creds[
        'graph_version'] + '/'  # base endpoint with domain and version
    creds['instagram_account_id'] = '17841451737769299'  # users instagram account id
    creds['page_id'] = '106871955542221'  # users page id
    creds['ig_username'] = 'mac.window.112022'

    return creds


def makeApiCall(url, endpointParams, type):
    """ Request data from endpoint with params

    Args:
        url: string of the url endpoint to make request from
        endpointParams: dictionary keyed by the names of the url parameters
    Returns:
        object: data from the endpoint
    """

    if type == 'POST':  # post request
        data = requests.post(url, endpointParams)
    else:  # get request
        data = requests.get(url, endpointParams)

    response = dict()  # hold response info
    response['url'] = url  # url we are hitting
    response['endpoint_params'] = endpointParams  # parameters for the endpoint
    response['endpoint_params_pretty'] = json.dumps(endpointParams, indent=4)  # pretty print for cli
    response['json_data'] = json.loads(data.content)  # response data from the api
    response['json_data_pretty'] = json.dumps(response['json_data'], indent=4)  # pretty print for cli

    return response  # get and return content
