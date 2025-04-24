-- Active: 1744742548804@@127.0.0.1@3306@projeto_integrador_fase2
SHOW DATABASES;
CREATE TABLE dados_sustentabilidade (
    Id_dado INT PRIMARY KEY AUTO_INCREMENT, 
    data DATE, 
    consumo_agua INT, 
    consumo_energia INT, 
    porcentagem_reciclagem INT, 
    meio_transporte INT
);
SELECT * FROM dados_sustentabilidade;