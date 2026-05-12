CREATE DATABASE projetointegrador_db;
USE projetointegrador_db;
CREATE TABLE eleitores (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome_completo VARCHAR(255) NOT NULL,
    cpf_criptografado VARCHAR(255) NOT NULL UNIQUE,
    titulo_eleitor VARCHAR(20) NOT NULL UNIQUE,
    e_mesario BOOLEAN NOT NULL DEFAULT FALSE,
    chave_acesso_criptografada VARCHAR(255) NOT NULL,
    status_voto ENUM('NAO_VOTOU', 'JA_VOTOU') DEFAULT 'NAO_VOTOU',
    criado_em DATETIME DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE candidatos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(255) NOT NULL,
    numero INT NOT NULL UNIQUE,
    partido VARCHAR(100) NOT NULL
);
CREATE TABLE votos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    candidato_id INT,
    data_hora DATETIME NOT NULL,
    protocolo_criptografado VARCHAR(255) NOT NULL,
    
    FOREIGN KEY (candidato_id) REFERENCES candidatos(id)
);
CREATE TABLE logs (
    id INT AUTO_INCREMENT PRIMARY KEY,
    data_hora DATETIME NOT NULL,
    tipo ENUM('ABERTURA', 'ALERTA', 'SUCESSO', 'ENCERRAMENTO') NOT NULL,
    descricao TEXT NOT NULL
);

SELECT * FROM eleitores;
SELECT * FROM candidatos;
SELECT * FROM votos;
SELECT * FROM logs;

ALTER TABLE eleitores
MODIFY e_mesario ENUM('sim','nao') NOT NULL DEFAULT 'nao';
