#include <iostream>
#include "chuta.hpp"
#include "existe.hpp"


void chuta(std::vector<char>& chutesErrados, std::map<char, bool>& chutou, std::string palavraSecreta){
	std::cout << std::endl;
	std::cout << "Seu chute: ";
	char chute;
	std::cin >> chute;
	chutou[chute] = true;

	if(existe(chute, palavraSecreta)){
		std::cout << "Voce acertou" << std::endl;
	} else {
		std::cout << "Voce errou" << std::endl;
		chutesErrados.push_back(chute);
	}
	std::cout << std::endl;
}
