#include "Caixa.hpp"

Caixa::Caixa(std::string nome, Cpf cpf, float salario, DiaDaSemana diaPagamento): Funcionario(nome,cpf,salario, diaPagamento) {

}

float Caixa::bonificacao() {
	return getSalario()*0,1;
}