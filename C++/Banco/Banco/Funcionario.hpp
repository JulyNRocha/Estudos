#pragma once
#include <string>
#include "Pessoa.hpp"
#include "Cpf.hpp"
#include "DiaDaSemana.hpp"

class Funcionario : public Pessoa {
private:
	float salario;
	DiaDaSemana diaPagamento;

public:
	Funcionario(std::string nome, Cpf cpf, float salario, DiaDaSemana diaPagamento);
	virtual float bonificacao() const = 0;
	float getSalario() const;
};

