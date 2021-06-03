#include <iostream>
#include <vector>
#include <string>
#include "leArquivos.hpp"
#include "escreveArquivos.hpp"

void adicionaP(){
	std::cout << "Digite a nova palavra, usando letra maiuscula" << std::endl;
	std::string novaP;
	std::cin >> novaP;

	std::vector<std::string> listaP = leArquivos();
	listaP.push_back(novaP);

	escreveArquivos(listaP);
}