# Send a GET request to the URL
def Get_URL_Data(URL):
    import requests
    from bs4 import BeautifulSoup
    try:
        response = requests.get(URL)
        response.raise_for_status()
        print(response)
    except Exception as ex:
        print(f'ERROR: {ex}')

