let conta = {
    titular: "Ana",
    saldo: 150
};

function depositar(conta,valor) {
    conta.saldo = conta.saldo + valor;
    console.log(`Depósito de ${valor} realizado. Novo saldo: ${conta.saldo}`);
}

depositar(conta, 50);
