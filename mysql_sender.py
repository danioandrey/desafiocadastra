import mysql.connector
from config import mysql_connection



def connection():
    conn = mysql.connector.connect(
    host=mysql_connection['host'],
    user=mysql_connection['user'],
    password=mysql_connection['password'],
    database=mysql_connection['database']
    )
    return conn



def insert_fato(conn, asset):
    cursor = conn.cursor()
    cursor.execute("""
    INSERT INTO fat_precos_criptomoedas (id_moeda, preco_usd, volume_24h, market_cap, variacao_24h)
    VALUES (%s, %s, %s, %s, %s) 
    """, (
        asset['id'], asset['priceUsd'], asset['volumeUsd24Hr'], asset['marketCapUsd'], asset['changePercent24Hr']
    ))
    conn.commit()

def insert_dimensao(conn, asset):
    cursor = conn.cursor()
    cursor.execute("""
    INSERT INTO dim_moeda (id_moeda, nome, simbolo, max_circulacao, explorer)
    VALUES (%s, %s, %s, %s, %s) 
        ON DUPLICATE KEY UPDATE nome = VALUES(nome),
        simbolo = VALUES(simbolo),
        max_circulacao = VALUES(max_circulacao),
        explorer = VALUES(explorer)
    """, (asset['id'], asset['name'], asset['symbol'], asset['maxSupply'], asset['explorer']))
    conn.commit()

def close_connection(conn):
    conn.close()

    
