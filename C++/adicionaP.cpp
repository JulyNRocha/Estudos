#include <iostream>
#include <string>
#include <vector>
#include "leArquivos.hpp"
#include "escreveArquivos.hpp"

void adicionaP(){
	std::cout << "Digite a nova palavra, usando letra maiúscula" << std::endl;
	std::string novaP;
	std::cin >> novaP;

	std::vector<std::string> listaP = leArquivos();
	listaP.push_back(novaP);

	escreveArquivos(listaP);
}