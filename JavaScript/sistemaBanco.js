let conta = {
    titular: "Ana",
    saldo: 150
};

function depositar(conta, valor) {
    conta.saldo = conta.saldo + valor;
    console.log(`Depósito de ${valor} realizado. Novo saldo: ${conta.saldo}`);
}


function saque(conta, valor) {
    if (conta.saldo >= valor) {
        conta.saldo -= valor;
        console.log(`Saque de ${valor} realizado com sucesso! Novo saldo: ${conta.saldo}`);
    } else {
        console.log(`Saldo insuficiente!`);
    }

}


saque(conta, 100);
depositar(conta, 50);

