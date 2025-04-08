-- Active: 1744119843432@@BD-ACD@3306@BD180225117
SHOW DATABASEs;
CREATE TABLE usuariosPI(Id int PRIMARY KEY AUTO_INCREMENT, nome VARCHAR(100),senha VARCHAR(20));
INSERT into usuariosPI(nome,senha) VALUES('Henrique','1234');
CREATE Table classificação_sustentabilidade(Id_usuario int,data DATE PRIMARY KEY, sus_agua VARCHAR(50),sus_energia VARCHAR(50), sus_reciclagem VARCHAR(50), sus_transporte VARCHAR(50));
