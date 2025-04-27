import requests
import sys
from mysql_sender import connection, insert_dimensao, insert_fato,close_connection
from config import api_config
import pandas as pd

api_key = api_config['key']
url_api = "https://rest.coincap.io/v3"

def get_assets(slug=None):
    headers = {
        "Authorization": f"Bearer {api_key}" if api_key else None
    }
        
    try:
        if slug == None:
            response = requests.get(f"{url_api}/assets/", headers=headers)
            response.raise_for_status() 
            data = response.json().get('data')
            return data
        else:
            response = requests.get(f"{url_api}/assets/{slug}", headers=headers)
            response.raise_for_status() 
            data = response.json().get('data')
            return [data]
    except requests.exceptions.HTTPError as http_err:
        if response.status_code == 404:
            print(f"Erro 404: URL não encontrada Error: {http_err}")
        else:
            print(f"Erro HTTP: {http_err}")

    except requests.exceptions.RequestException as e:
        print(f"Erro ao conectar com a API: {e}")
        raise

if __name__ == "__main__":
    if len(sys.argv) == 1:
        assets_data = get_assets()
    else:
        slug = sys.argv[1]
        assets_data = get_assets(slug)        
    
    if assets_data:
        conn = connection()
        df = pd.DataFrame(assets_data)  
        insert_dimensao(conn,df)
        insert_fato(conn,df)
        close_connection(conn)
    else:
        print("Não foi possível obter os dados dos ativos.")