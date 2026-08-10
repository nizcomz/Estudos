-- Script: criacao_banco_e_lista.sql
-- Objetivo: Criar o banco de dados da clínica e listar os bancos existentes.

-- 1) Cria o banco de dados 'clinica_estetica'. Caso já exista, este comando
-- tentará criar novamente e gerará erro; em prática, usar 'CREATE DATABASE IF NOT EXISTS'.
CREATE DATABASE clinica_estetica;

-- 2) Define o banco de dados atual para execução das próximas instruções.
USE clinica_estetica;

-- 3) Lista todos os bancos de dados disponíveis no servidor MySQL.
SHOW DATABASES;
