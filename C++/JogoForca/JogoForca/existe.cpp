#include <string>
#include "existe.hpp"

bool existe(char chute, std::string palavraSecreta){
	for(char letra : palavraSecreta){
		if(chute == letra){
			return true;
		}
	}
	return false;

}