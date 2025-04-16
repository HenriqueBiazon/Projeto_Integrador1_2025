-- Active: 1744806189365@@BD-ACD@3306@BD180225117
SHOW DATABASES;
CREATE TABLE usuarios_PI(Id_usuario INT PRIMARY KEY AUTO_INCREMENT, nome VARCHAR(100), senha VARCHAR(20));
INSERT INTO usuarios_PI(nome, senha) VALUES('Henrique', '1234');
SELECT * FROM usuarios_PI;
CREATE TABLE classificação_sustentabilidade (
    Id_classificação INT PRIMARY KEY AUTO_INCREMENT, 
    Id_usuario INT, 
    data DATE, 
    sus_agua INT, 
    sus_energia INT, 
    sus_reciclagem INT, 
    sus_transporte INT
);
ALTER TABLE classificação_sustentabilidade RENAME COLUMN Id_classificação TO Id_classificacao;
SELECT * FROM classificação_sustentabilidade;
ALTER Table classificação_sustentabilidade ADD Foreign Key (Id_usuario) REFERENCES usuarios_PI(Id_usuario);
SELECT * FROM classificação_sustentabilidade;
SELECT nome FROM usuarios_PI;