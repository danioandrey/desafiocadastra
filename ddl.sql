create database criptomoedas;

CREATE TABLE IF NOT EXISTS fat_precos_criptomoedas (
		id_fato int auto_increment PRIMARY KEY,
        data_hora DATETIME DEFAULT CURRENT_TIMESTAMP,
        id_moeda varchar(255),
        preco_usd DECIMAL(65,30),
        volume_24h DECIMAL(65,30),
        market_cap DECIMAL(65,30),
        variacao_24h DECIMAL(65,30),
        FOREIGN KEY (id_moeda) REFERENCES dim_moeda(id_moeda)
    );
   
CREATE TABLE IF NOT EXISTS dim_moeda(
	id_moeda varchar(255) PRIMARY KEY,
    nome varchar(255),
    simbolo varchar(20),
    max_circulacao DECIMAL(65,30), 
    explorer varchar(255),
    dtupdate DATETIME DEFAULT CURRENT_TIMESTAMP
);