#pragma once
#include "Funcionario.hpp"
#include "DiaDaSemana.hpp"

class Caixa final:
    public Funcionario
{
public:
    Caixa(std::string nome,Cpf cpf,float salario, DiaDaSemana diaPagamento);
    float bonificacao();
};

