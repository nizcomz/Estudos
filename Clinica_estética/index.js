const express = require('express');
const mysql = require('mysql2');

const app = express();
app.use(express.json());

// Configuração da conexão com o MySQL
const db = mysql.createConnection({
    host: 'localhost',
    user: 'root',      // Altere se o seu usuário do MySQL for diferente
    password: 'Mayane@estetica',      // Coloque a sua senha do MySQL aqui
    database: 'clinica_estetica'
});

// Testar a conexão
db.connect((err) => {
    if (err) {
        console.error('Erro ao conectar ao MySQL:', err);
        return;
    }
    console.log('Conectado ao banco de dados MySQL com sucesso!');
});

// Rota de teste para buscar os serviços cadastrados
app.get('/servicos', (req, res) => {
    const sql = 'SELECT * FROM servicos';
    db.query(sql, (err, results) => {
        if (err) {
            return res.status(500).json({ erro: 'Erro ao buscar serviços' });
        }
        res.json(results);
    });
});

const PORT = 3000;
app.listen(PORT, () => {
    console.log(`Servidor rodando na porta ${PORT}`);
});