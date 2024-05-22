#汎用的な関数を記述しているファイル
import requests,math

# fetchdata(players, {'name':search_query, 'limit': 200})
def fetch_data_from_api(continuation_api_url,params=None):
    """
    overfast(API)からデータを取得し、データをjson形式で返す関数

    Parameters
    ----------
    continuation_api_url : str
        base_api_urlの続きのurl
    params : dictionary, optional
        パラメータが必要な際に{パラメータ：値}の形式で入力する。 デフォルトはNone

    Returns
    -------
    dictionary
        APIから取得した値
    """
    base_api_url = "https://overfast-api.tekrop.fr/"

    #例）https://overfast-api.tekrop.fr/players
    api_url = f"{base_api_url}{continuation_api_url}"
    response  = requests.get(api_url,params)
    json_data = response.json()

    return json_data


def rate_calculation(divisor,dividend,digits_after_point=None):
    try:
        if digits_after_point:
            divided_num = round((divisor / dividend),digits_after_point)
        else:
            divided_num = round((divisor / dividend),digits_after_point)

    except ZeroDivisionError:
        divided_num = "-"

    return divided_num


def seconds_to_hour_and_minutes(seconds):
    hours = math.floor(seconds / 3600)
    minutes = math.floor((seconds % 3600) / 60)
    return f"{hours:02d}:{minutes:02d}"

