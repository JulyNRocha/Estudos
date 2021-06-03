#include "Pessoa.hpp"

Pessoa::Pessoa(std::string nome, Cpf cpf)
    :nome(nome), cpf(cpf) {

    Pessoa::verTamanhoDoNome();

}

void Pessoa::verTamanhoDoNome() {
    if (nome.size() < 5) {
        std::cout << "Nome muito curto" << std::endl;
        exit(1);
    }
}

std::string Pessoa::getNome() {
    return nome;
}
