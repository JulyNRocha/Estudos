#include <iostream>
#include "Conta.hpp"
#include "ContaPoupanca.hpp"
#include "Titular.hpp"
#include "Funcionario.hpp"
#include "Pessoa.hpp"
#include "ContaCorrente.hpp"
#include "DiaDaSemana.hpp"
#include "Gerente.hpp"
#include "Caixa.hpp"

using namespace std;

void ExibeSaldo(const Conta& conta) {
    cout << "Saldo da conta: " << conta.getSaldo() << endl;
}

void FazLogin(Autenticavel& alguem, string senha) {
    if (alguem.autentica(senha)) {
        cout << "login relizado com sucesso" << endl;
    }
    else {
        cout << "senha invalida" << endl;
    }
}

int main()
{
    ContaCorrente Conta1("123", Titular("Julyane", Cpf("123.456.789-10"),"umaSenha"));
    ContaPoupanca Conta2("456", Titular("Iago Lobato", Cpf("987.654.321-10"),"outraSenha"));

    Gerente Gerente1("Delaide", Cpf("000.000.000-00"), 1500, DiaDaSemana::Terca, "123456");
    
    Conta1 += 500;

 

    ExibeSaldo(Conta1);
    ExibeSaldo(Conta2);

    cout << "Numero de contas: " << Conta::getNumeroDeContas();
    
}
