-- Active: 1744742548804@@127.0.0.1@3306@projeto_integrador_fase2
CREATE TABLE dados_sustentabilidade (
    Id_dado INT PRIMARY KEY AUTO_INCREMENT, 
    data VARCHAR(20) UNIQUE, 
    consumo_agua INT, 
    consumo_energia FLOAT, 
    porcentagem_reciclagem INT, 
    meios_transporte VARCHAR(50)
);
CREATE TABLE classificacao_sustentabilidade (
    Id_classificacao INT PRIMARY KEY AUTO_INCREMENT, 
    data VARCHAR(20) UNIQUE, 
    classificacao_agua VARCHAR(25), 
    classificacao_energia VARCHAR(25), 
    classificacao_reciclagem VARCHAR(25), 
    classificacao_transporte VARCHAR(25)
);
ALTER TABLE classificacao_sustentabilidade ADD FOREIGN KEY (data) REFERENCES dados_sustentabilidade(data);
SHOW TABLES;