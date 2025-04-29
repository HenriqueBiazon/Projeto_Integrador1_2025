-- Active: 1743645348789@@BD-ACD@3306@BD180225117
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
INSERT INTO dados_sustentabilidade (data,consumo_agua,consumo_energia,porcentagem_reciclagem,meios_transporte) VALUES ("DD/MM/AAAA",0,0,0,"0,0,0,0,0,0");
SELECT * FROM dados_sustentabilidade;
SELECT * FROM dados_sustentabilidade WHERE data = "DD/MM/AAAA";
UPDATE dados_sustentabilidade SET consumo_agua = "1" WHERE data = "DD/MM/AAAA";
DELETE FROM dados_sustentabilidade WHERE data = "DD/MM/AAAA";
DROP TABLE dados_sustentabilidade;
