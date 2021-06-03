#pragma once
#include <string>
#include "Titular.hpp"


class Conta {
private:
    static int numeroDeContas;

public:
    static int getNumeroDeContas();

protected:
    std::string numero;
    Titular titular;
    float saldo;

public:
    Conta(std::string numero, Titular titular);
    void saca(float saque);
    void deposita(float deposito);
    void operator+=(float deposito);

    virtual float taxaDeSaque() const = 0;

    std::string getNumero();
    float getSaldo() const;

};