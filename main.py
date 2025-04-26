import requests
import json
from mysql_sender import connection, insert_dimensao, insert_fato,close_connection
from config import api_config

api_key = api_config['key']
url_api = "https://rest.coincap.io/v3"

def fetch_assets():
    headers = {
        "Authorization": f"Bearer {api_key}" if api_key else None
    }
    try:
        response = requests.get(f"{url_api}/assets/", headers=headers)
        response.raise_for_status() 
        data = response.json().get('data')
        return data
    except requests.exceptions.RequestException as e:
        print(f"Erro ao conectar com a API: {e}")
        raise

if __name__ == "__main__":
    assets_data = fetch_assets()
    
    if assets_data:
        conn = connection()
        print(type(assets_data))
        for asset in assets_data:    
            insert_dimensao(conn,asset)
            insert_fato(conn,asset)

        close_connection(conn)
    else:
        print("Não foi possível obter os dados dos ativos.")