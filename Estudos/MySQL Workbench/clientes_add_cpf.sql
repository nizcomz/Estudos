-- Script: clientes_add_cpf.sql
-- Objetivo: Adicionar a coluna 'cpf' na tabela 'clientes' com restrição de unicidade

-- Seleciona o banco de dados 'clinica_estetica' para que as operações
-- seguintes sejam executadas neste banco específico.
USE clinica_estetica;

-- ALTER TABLE clientes ... adiciona uma nova coluna chamada 'cpf' do tipo
-- VARCHAR(14). 'NOT NULL' obriga que o campo seja informado e 'UNIQUE'
-- impede a inserção de registros com o mesmo valor de CPF.
ALTER TABLE clientes 
ADD COLUMN cpf VARCHAR(14) NOT NULL UNIQUE AFTER nome;

-- DESCRIBE clientes; mostra a estrutura atual da tabela, incluindo a nova
-- coluna 'cpf' para confirmação visual.
DESCRIBE clientes;
