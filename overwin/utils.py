#汎用的な関数を記述しているファイル
import requests

# fetchdata(players, {'name':search_query, 'limit': 200})
def fetch_data_from_api(continuation_api_url,params):
    base_api_url = "https://overfast-api.tekrop.fr/"

    #例）https://overfast-api.tekrop.fr/players
    api_url = f"{base_api_url}{continuation_api_url}"

    #例）https://overfast-api.tekrop.fr/players?name=sara&limit=200
    response  = requests.get(api_url, params=params)
    json_data = response.json()

    return json_data