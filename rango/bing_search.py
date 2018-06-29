import json
import urllib
import requests
def read_bing_key():
    bing_api_key = None
    try:
        with open('D:/Soliver/tango_with_django_project/rango/bing.key','r') as f:
            bing_api_key = f.readline()
    except:
        raise IOError('bing.key file not found')
    return bing_api_key
def run_query(search_items):
    bing_api_key = read_bing_key()
    if not bing_api_key:
        raise KeyError('not a bing key')
    root_url = 'https://api.cognitive.microsoft.com/bing/v7.0/search'
    headers = {"Ocp-Apim-Subscription-Key" : bing_api_key}
    params  = {"q": search_items, "textDecorations":True, "textFormat":"HTML"}
    response = requests.get(root_url, headers=headers, params=params)
    response.raise_for_status()
    search_results = response.json()
    print(search_results)
    return search_results
    # service = 'Web'
    # results_per_page =10
    # offset = 0
    # query = "'{0}'".format(search_items)
    # query = urllib.parse.quote(query)
    # search_url = "{0}{1}?$format=json&$top={2}&$skip={3}&Query={4}".format(
    # root_url,
    # service,
    # results_per_page,
    # offset,
    # query)
    # username = ''
    # password_mgr = urllib.request.HTTPPasswordMgrWithDefaultRealm()
    # password_mgr.add_password(None,search_url,username,bing_api_key)
    # results = []
    # try:
    #     handler = urllib.request.HTTPBasicAuthHandler(password_mgr)
    #     opener = urllib.request.build_opener(handler)
    #     urllib.request.install_opener(opener)
    #     response = urllib.request.urlopen(search_url).read()
    #     response = response.decode('urf-8')
    # except:
    #     print('Error when quering Bing API')
    # return results
def main():
    run_query('Manohar')
if __name__ == '__main__':
    main()