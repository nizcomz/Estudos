USE clinica_estetica;

-- Nota: este arquivo original foi mantido como backup. Prefira o script
-- 'clientes_inserts_e_consultas.sql' que contém comentários linha-a-linha.

-- Inserindo múltiplos clientes em uma única instrução SQL.
INSERT INTO clientes (nome, telefone) VALUES 
('Maria Silva', '(31) 99999-1111'),
('Ana Souza', '(31) 98888-2222'),
('Carla Dias', '(31) 97777-3333');

-- ---------------------------------------------------------------

-- Consulta: retorna todas as colunas de todos os clientes.
SELECT * FROM clientes;

-- Consulta: retorna apenas o nome e o telefone.
SELECT nome, telefone FROM clientes;

-- Consulta: filtra o cliente com id = 2.
SELECT * FROM clientes WHERE id = 2;




