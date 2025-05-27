-- Active: 1744742548804@@127.0.0.1@3306@projeto_integrador_fase2
CREATE TABLE dados_sustentabilidade (
    Id_dado INT PRIMARY KEY AUTO_INCREMENT, 
    data VARCHAR(20), 
    consumo_agua VARCHAR(20), 
    consumo_energia VARCHAR(20), 
    porcentagem_reciclagem VARCHAR(20), 
    meios_transporte VARCHAR(50)
);
CREATE TABLE usuarios (
    Id_usuario INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(50) UNIQUE,
    senha VARCHAR(30)
);
ALTER TABLE dados_sustentabilidade ADD COLUMN Id_usuario INT;
ALTER TABLE dados_sustentabilidade ADD FOREIGN KEY (Id_usuario) REFERENCES usuarios(Id_usuario);
CREATE TABLE classificacao_sustentabilidade (
    Id_classificacao INT PRIMARY KEY AUTO_INCREMENT, 
    Id_dado INT,
    data VARCHAR(20), 
    classificacao_agua VARCHAR(20), 
    classificacao_energia VARCHAR(20), 
    classificacao_reciclagem VARCHAR(20), 
    classificacao_transporte VARCHAR(50)
);
ALTER TABLE classificacao_sustentabilidade ADD FOREIGN KEY (Id_dado) REFERENCES dados_sustentabilidade(Id_dado);
SHOW TABLES;