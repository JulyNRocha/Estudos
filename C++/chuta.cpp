#include <iostream>
#include <vector>
#include <map>
#include "existe.hpp"

extern std::vector<char> chutesErrados;
extern std::map<char, bool> chutou;

void chuta(){
	std::cout << std::endl;
	std::cout << "Seu chute: ";
	char chute;
	std::cin >> chute;
	chutou[chute] = true;

	if(existe(chute)){
		std::cout << "Voce acertou" << std::endl;
	} else {
		std::cout << "Voce errou" << std::endl;
		chutesErrados.push_back(chute);
	}
	std::cout << std::endl;
}
