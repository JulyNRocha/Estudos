#pragma once
#include <string>
#include <iostream>
#include "Cpf.hpp"

class Pessoa {
protected:
	std::string nome;
	Cpf cpf;

	void verTamanhoDoNome();

public:
	Pessoa(std::string nome, Cpf cpf);

	std::string getNome();

};


