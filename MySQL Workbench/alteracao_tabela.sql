USE clinica_estetica;

-- Nota: este arquivo original foi mantido como backup. Prefira o script
-- 'clientes_add_cpf.sql' que contém comentários linha-a-linha explicativos.

-- Adiciona a coluna 'cpf' e a torna única (evita CPFs duplicados).
ALTER TABLE clientes 
ADD COLUMN cpf VARCHAR(14) NOT NULL UNIQUE AFTER nome;

-- Verifica a estrutura da tabela após a alteração.
DESCRIBE clientes;

