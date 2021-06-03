#include <iostream>
#include <fstream>
#include "leArquivos.hpp"


std::vector<std::string> leArquivos(){
	std::ifstream arquivo;
	arquivo.open("palavras.txt");
	if(arquivo.is_open()){

		int qttPalavras;
		arquivo >> qttPalavras;

		std::vector<std::string> palavrasDoAquivo;

		for(int i = 0; i < qttPalavras; i++){
			std::string palavraLida;
			arquivo >> palavraLida;
			palavrasDoAquivo.push_back(palavraLida);
		}

		arquivo.close();
		return palavrasDoAquivo;

	} else {
		std::cout << "Arquivo nao encontrado"<< std::endl;
		exit(0);
	}
}