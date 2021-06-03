#include "Funcionario.hpp"

Funcionario::Funcionario(std::string nome, Cpf cpf, float salario, DiaDaSemana diaPagamento)
	:Pessoa(nome,cpf),salario(salario), diaPagamento(diaPagamento) {

}

float Funcionario::bonificacao() const {

}

float Funcionario::getSalario() const{
	return salario;
}