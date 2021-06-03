#include <iostream>
#include "imprimeErros.hpp"


void imprimeErros(const std::vector<char>& chutesErrados){
	std::cout << "Chutes errados: ";
	for(char letra: chutesErrados){
		std::cout << letra << " ";
	}
	std::cout << std::endl;
}

