#include <iostream>
#include <fstream>
#include "escreveArquivos.hpp"

void escreveArquivos(std::vector<std::string> listaPalavras){
	std::ofstream arquivo;
	arquivo.open("palavras.txt");
	if(arquivo.is_open()){
		arquivo << listaPalavras.size() << std::endl;
		for(std::string palavra : listaPalavras){
			arquivo << palavra << std::endl;
		}
		arquivo.close();

	} else {
		std::cout << "Arquivo nao encontrado"<< std::endl;
		exit(0);
	}
}
