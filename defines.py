import requests
import json


def getCreds():
    """ Get creds required for use in the applications

    Returns:
        dictonary: credentials needed globally
    """

    creds = dict()  # dictionary to hold everything
    creds['access_token'] = 'EAAGZC0NO2uTwBAIP5NQ3nngcOTr0v0UolWDhQ2fZA7fs95J5NNFMRGReZA84HdW2HickL4m4tXpKOCOpCmDnxaNP0iQRqLt2pDH3Tj1lxtnmnBiNmiOZBXlZAB1PIy2si3Tj5K6ZC9WUqoZCsobua2iruMgioL795QazyUgsHCWVlDZCZBxHEbpyabG1pR8ZAHUas0UaNmwNOnLSOlstvUPOVC'
    creds['client_id'] = 'FB-APP-CLIENT-ID'  # client id from facebook app IG Graph API Test
    creds['client_secret'] = 'FB-APP-CLIENT-SECRET'  # client secret from facebook app
    creds['graph_domain'] = 'https://graph.facebook.com/'  # base domain for api calls
    creds['graph_version'] = 'v15.0'  # version of the api we are hitting
    creds['endpoint_base'] = creds['graph_domain'] + creds[
        'graph_version'] + '/'  # base endpoint with domain and version
    creds['debug'] = 'no'  # debug mode for api call
    creds['page_id'] = '106871955542221'  # users page id
    creds['instagram_account_id'] = '17841451737769299'  # users instagram account id
    creds['ig_username'] = 'mac.window.112022'  # ig username

    return creds


def makeApiCall(url, endpointParams, debug='no'):
    """ Request data from endpoint with params

    Args:
        url: string of the url endpoint to make request from
        endpointParams: dictionary keyed by the names of the url parameters
    Returns:
        object: data from the endpoint
    """

    data = requests.get(url, endpointParams)  # make get request

    response = dict()  # hold response info
    response['url'] = url  # url we are hitting
    response['endpoint_params'] = endpointParams  # parameters for the endpoint
    response['endpoint_params_pretty'] = json.dumps(endpointParams, indent=4)  # pretty print for cli
    response['json_data'] = json.loads(data.content)  # response data from the api
    response['json_data_pretty'] = json.dumps(response['json_data'], indent=4)  # pretty print for cli

    if ('yes' == debug):  # display out response info
        displayApiCallData(response)  # display response

    return response  # get and return content


def displayApiCallData(response):
    """ Print out to cli response from api call """

    print("\nURL: ", response['url'])
    print("\nEndpoint Params: ", response['endpoint_params_pretty'])
    print("\nResponse: ", response['json_data_pretty'])
