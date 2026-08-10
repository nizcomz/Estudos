USE clinica_estetica;

-- Nota: este arquivo original foi mantido como backup. Prefira o script
-- 'agendamento_servicos_modelo.sql' que contém comentários linha-a-linha.

-- Cria a tabela 'administrador' para gerenciar acessos administrativos.
CREATE TABLE administrador (
    id INT AUTO_INCREMENT PRIMARY KEY,
    usuario VARCHAR(50) NOT NULL UNIQUE,
    senha VARCHAR(255) NOT NULL
);

-- Cria a tabela 'servicos' para armazenar os procedimentos oferecidos.
CREATE TABLE servicos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    duracao_minutos INT NOT NULL,
    valor DECIMAL(10, 2) NOT NULL
);

-- Cria a tabela 'agendamentos' relacionando clientes e serviços.
CREATE TABLE agendamentos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    cliente_id INT NOT NULL,
    servico_id INT NOT NULL,
    data_agendamento DATE NOT NULL,
    hora_inicio TIME NOT NULL,
    hora_fim TIME NOT NULL,
    status ENUM('Agendado', 'Concluido', 'Cancelado') DEFAULT 'Agendado',
    criado_em DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (cliente_id) REFERENCES clientes(id),
    FOREIGN KEY (servico_id) REFERENCES servicos(id)
);

-- Insere serviços de exemplo e usuário administrador de teste.
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

INSERT INTO administrador (usuario, senha) VALUES 
('admin', 'admin123');

SELECT * FROM servicos;


