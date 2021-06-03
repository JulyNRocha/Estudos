#include <iostream>
#include "imprimeForca.hpp"


void imprimeForca(std::string& palavraSecreta,std::map<char, bool>& chutou){
	for(char letra : palavraSecreta){
		if(chutou[letra]){
			std::cout << letra << " ";
		} else {
			std::cout << "_ ";
		}
	}
}
