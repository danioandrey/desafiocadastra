import mysql.connector
from config import mysql_connection



def connection():
    try:

        conn = mysql.connector.connect(
        host=mysql_connection['host'],
        user=mysql_connection['user'],
        password=mysql_connection['password'],
        database=mysql_connection['database']
        )
        return conn
    except mysql.connector.Error as err:
        if err.errno == 2003:  
            print(f"Error: Não foi possível conectar no Mysql, verifique se o serviço está ativo.")
        elif err.errno == 1045: 
            print(f"Error: Acesso Negado")
        elif err.errno == 1049: 
            print(f"Error: Schema  '{mysql_connection['database']}' não localizado.")
        else:
            print(f"Não foi possível conectar no Mysql: {err}")



def insert_fato(conn, df):
    try:
        cursor = conn.cursor()
        query = """
        INSERT INTO fat_precos_criptomoedas (id_moeda, preco_usd, volume_24h, market_cap, variacao_24h)
        VALUES (%s, %s, %s, %s, %s) 
        """
        for index, row in df.iterrows():
            cursor.execute(query, (row['id'], row['priceUsd'], row['volumeUsd24Hr'], row['marketCapUsd'], row['changePercent24Hr']))
        conn.commit()
        cursor.close()
        print("Insert realizado com sucesso na Fato!")
    except mysql.connector.Error as err:
        print(f"Erro ao inserir dados na tabela fat_precos_criptomoedas: {err}")

def insert_dimensao(conn, df):
    try:
        cursor = conn.cursor()
        query = """
        INSERT INTO dim_moeda (id_moeda, nome, simbolo, max_circulacao, explorer)
        VALUES (%s, %s, %s, %s, %s) 
            ON DUPLICATE KEY UPDATE nome = VALUES(nome),
            simbolo = VALUES(simbolo),
            max_circulacao = VALUES(max_circulacao),
            explorer = VALUES(explorer)
        """

        for index, row in df.iterrows():
            cursor.execute(query,(row['id'], row['name'], row['symbol'], row['maxSupply'], row['explorer']))
        
        print("Insert realizado com sucesso na dim_moeda!")
        conn.commit()
        cursor.close()
    except mysql.connector.Error as err:
        print(f"Erro ao inserir dados na tabela dim_moeda: {err}")

    
def close_connection(conn):
    conn.close()

    
