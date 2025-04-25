-- Active: 1744742548804@@127.0.0.1@3306@projeto_integrador_fase2
SHOW DATABASES;
CREATE TABLE dados_sustentabilidade (
    Id_dado INT PRIMARY KEY AUTO_INCREMENT, 
    data VARCHAR(20), 
    consumo_agua INT, 
    consumo_energia INT, 
    porcentagem_reciclagem INT, 
    meios_transporte VARCHAR(50)
);
SELECT * FROM dados_sustentabilidade;

--INSERT INTO dados_sustentabilidade (data,consumo_agua,consumo_energia,porcentagem_reciclagem,meio_transporte) VALUES ()

ALTER TABLE dados_sustentabilidade RENAME COLUMN meio_transporte TO meios_transporte;