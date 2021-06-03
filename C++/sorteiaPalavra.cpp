#include <vector>
#include <string>
#include <ctime>
#include <cstdlib>
#include "leArquivos.hpp"

extern std::string palavraSecreta;

void sorteiaPalavra(){
	std::vector<std::string> palavras = leArquivos();

	srand(time(NULL));
	int sorteio = rand() % palavras.size();

	palavraSecreta = palavras[sorteio];

}