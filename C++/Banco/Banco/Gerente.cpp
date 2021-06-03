#include "Gerente.hpp"

Gerente::Gerente(std::string nome, Cpf cpf, float salario, DiaDaSemana diaPagamento, std::string senha)
	:Funcionario(nome,cpf,salario,diaPagamento), Autenticavel(senha) {

}
float Gerente::bonificacao() const{
	return getSalario() * 0.5;
}


