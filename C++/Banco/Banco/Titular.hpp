#pragma once
#include <string>
#include "Pessoa.hpp"
#include "Cpf.hpp"
#include "Autenticavel.hpp"

class Titular : public Pessoa, public Autenticavel {

public:
	Titular(std::string nome, Cpf cpf, std::string senha);

};

