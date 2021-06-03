#include <iostream>
#include <vector>

extern std::vector<char> chutesErrados;

void imprimeErros(){
	std::cout << "Chutes errados: ";
	for(char letra: chutesErrados){
		std::cout << letra << " ";
	}
	std::cout << std::endl;
}