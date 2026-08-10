-- Script: clientes_inserts_e_consultas.sql
-- Objetivo: Inserir registros de exemplo na tabela 'clientes' e demonstrar
-- consultas básicas (SELECT) para aprendizado.

USE clinica_estetica;

-- Inserção de múltiplos clientes em uma única instrução INSERT.
INSERT INTO clientes (nome, telefone) VALUES 
('Maria Silva', '(31) 99999-1111'),
('Ana Souza', '(31) 98888-2222'),
('Carla Dias', '(31) 97777-3333');

-- ---------------------------------------------------------------

-- Consulta 1: Retorna todas as colunas de todos os clientes.
SELECT * FROM clientes;

-- Consulta 2: Retorna apenas as colunas 'nome' e 'telefone'.
SELECT nome, telefone FROM clientes;

-- Consulta 3: Retorna o cliente cujo 'id' é igual a 2 (filtro WHERE).
SELECT * FROM clientes WHERE id = 2;
