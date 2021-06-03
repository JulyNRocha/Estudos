#include <iostream>
#include <string>
#include <map>

extern std::string palavraSecreta;

extern std::map<char, bool> chutou;

void imprimeForca(){
	for(char letra : palavraSecreta){
		if(chutou[letra]){
			std::cout << letra << " ";
		} else {
			std::cout << "_ ";
		}
	}
}
