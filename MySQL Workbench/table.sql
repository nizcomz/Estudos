-- Passo 1: Seleciona o banco de dados onde as operações serão executadas.
-- O comando abaixo altera o contexto atual para o banco 'clinica_estetica',
-- ou seja, todas as instruções seguintes serão executadas nesse banco.
USE clinica_estetica;

-- Passo 2: Cria a tabela 'clientes' com suas colunas e restrições.
-- CREATE TABLE clientes (...); define uma nova tabela chamada 'clientes'.
CREATE TABLE clientes (
    -- 'id INT AUTO_INCREMENT PRIMARY KEY' cria uma coluna inteira que
    -- incrementa automaticamente para cada novo registro e serve como
    -- identificador único (chave primária) da tabela.
    id INT AUTO_INCREMENT PRIMARY KEY,
    -- 'nome VARCHAR(100) NOT NULL' cria uma coluna de texto com tamanho
    -- máximo de 100 caracteres; 'NOT NULL' impede que o campo fique vazio.
    nome VARCHAR(100) NOT NULL,
    -- 'telefone VARCHAR(20) NOT NULL' armazena números/strings de telefone
    -- com até 20 caracteres; usado texto para preservar formatações.
    telefone VARCHAR(20) NOT NULL,
    -- 'criado_em DATETIME DEFAULT CURRENT_TIMESTAMP' registra a data e hora
    -- de criação do registro; se nenhum valor for informado, o banco usa o
    -- timestamp atual automaticamente.
    criado_em DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- Passo 3: Mostra a estrutura da tabela criada.
-- DESCRIBE clientes; exibe as colunas, tipos de dados, se aceitam NULL e
-- outras informações como chaves e valores padrão.
DESCRIBE clientes;


