#include <iostream>
#include "Conta.hpp"


int Conta::numeroDeContas = 0;

Conta::Conta(std::string numero, Titular titular)
    :numero(numero),
    titular(titular),
    saldo(0) {
    
    numeroDeContas++;
 }

int Conta::getNumeroDeContas() {
    return numeroDeContas;
}

float Conta::taxaDeSaque() const {

}

void Conta::saca(float saque) {
    if (saque < 0) {
        std::cout << "O valor a ser sacado não pode ser negativo" << std::endl;
        return;
    }

    float tarifaDeSaque = saque * taxaDeSaque();
    float valorDoSaque = saque + tarifaDeSaque;

    if (saque > saldo) {
        std::cout << "Saldo o insuficiente" << std::endl;
        return;
    }

    saldo -= valorDoSaque;
}

void Conta::deposita(float deposito) {
    if (deposito < 0) {
        std::cout << "O valor a ser a ser depositado não pode ser negativo" << std::endl;
        return;
    }

    saldo += deposito;
}

void Conta::operator+=(float deposito) {
    deposita(deposito);
}

float Conta::getSaldo() const{
    return saldo;
}

std::string Conta::getNumero() {
    return numero;
}

