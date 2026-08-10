-- Script: agendamento_servicos_modelo.sql
-- Objetivo: Criar tabelas relacionadas a administrador, serviços e agendamentos

-- Seleciona o banco onde as tabelas serão criadas.
USE clinica_estetica;

-- 1) Tabela 'administrador'
-- Cria a tabela que armazenará os usuários administradores da clínica.
CREATE TABLE administrador (
    -- 'id' é a chave primária autoincremental, identifica unicamente o registro
    id INT AUTO_INCREMENT PRIMARY KEY,
    -- 'usuario' é um texto único (não pode haver duplicados)
    usuario VARCHAR(50) NOT NULL UNIQUE,
    -- 'senha' armazena a senha; em produção deve guardar apenas hash criptografado
    senha VARCHAR(255) NOT NULL
);

-- 2) Tabela 'servicos'
-- Guarda os procedimentos oferecidos pela clínica, sua duração e valor.
CREATE TABLE servicos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    duracao_minutos INT NOT NULL,
    valor DECIMAL(10, 2) NOT NULL
);

-- 3) Tabela 'agendamentos'
-- Armazena cada horário agendado, relacionando cliente e serviço.
CREATE TABLE agendamentos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    -- 'cliente_id' referencia a tabela 'clientes' (deve existir coluna 'id')
    cliente_id INT NOT NULL,
    -- 'servico_id' referencia a tabela 'servicos'
    servico_id INT NOT NULL,
    data_agendamento DATE NOT NULL,
    hora_inicio TIME NOT NULL,
    hora_fim TIME NOT NULL,
    -- 'status' controla o estado do agendamento com valores pré-definidos
    status ENUM('Agendado', 'Concluido', 'Cancelado') DEFAULT 'Agendado',
    criado_em DATETIME DEFAULT CURRENT_TIMESTAMP,
    -- Define as chaves estrangeiras que garantem integridade referencial
    FOREIGN KEY (cliente_id) REFERENCES clientes(id),
    FOREIGN KEY (servico_id) REFERENCES servicos(id)
);

-- 4) Inserção de serviços de exemplo para popular a tabela 'servicos'.
INSERT INTO servicos (nome, duracao_minutos, valor) VALUES 
('Design de Sobrancelha', 30, 45.00),
('Limpeza de Pele', 90, 150.00),
('Peeling de Diamante', 60, 120.00),
('Peeling Químico', 60, 140.00),
('Microagulhamento', 120, 250.00),
('Endermologia', 45, 100.00),
('Massagem Redutora', 60, 110.00),
('Massagem Relaxante', 60, 120.00),
('Lipoenzimática', 45, 200.00),
('Drenagem Linfática (Pré e Pós-operatório)', 60, 130.00);

-- 5) Inserção de usuário administrador inicial. Em produção, substituir
-- 'admin123' por um hash seguro e não deixar credenciais em texto claro.
INSERT INTO administrador (usuario, senha) VALUES 
('admin', 'admin123');

-- Exibe todos os serviços cadastrados para verificação.
SELECT * FROM servicos;
