-- Active: 1744742548804@@127.0.0.1@3306@projeto_integrador_fase2
SHOW DATABASES;
CREATE TABLE dados_sustentabilidade (
    Id_dado INT PRIMARY KEY AUTO_INCREMENT, 
    data VARCHAR(20), 
    consumo_agua VARCHAR(20), 
    consumo_energia VARCHAR(20), 
    porcentagem_reciclagem VARCHAR(20), 
    meios_transporte VARCHAR(50)
);
SELECT * FROM dados_sustentabilidade;
INSERT INTO dados_sustentabilidade (data,consumo_agua,consumo_energia,porcentagem_reciclagem,meios_transporte) VALUES ("DD/MM/AAAA",0,0,0,"0,0,0,0,0,0");
SELECT * FROM dados_sustentabilidade;
SELECT * FROM dados_sustentabilidade WHERE data = "DD/MM/AAAA";
UPDATE dados_sustentabilidade SET consumo_agua = "1" WHERE data = "DD/MM/AAAA";
DELETE FROM dados_sustentabilidade WHERE data = "DD/MM/AAAA";
--DROP TABLE dados_sustentabilidade;
ALTER TABLE dados_sustentabilidade ADD COLUMN Id_usuario INT;
CREATE TABLE usuarios (
    Id_usuario INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(50) UNIQUE,
    senha VARCHAR(30)
    );
ALTER TABLE dados_sustentabilidade ADD FOREIGN KEY (Id_usuario) REFERENCES usuarios(Id_usuario);
