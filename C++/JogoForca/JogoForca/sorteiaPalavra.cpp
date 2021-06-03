#include <vector>
#include <ctime>
#include <cstdlib>
#include "leArquivos.hpp"

std::string sorteiaPalavra(){
	std::vector<std::string> palavras = leArquivos();

	srand(time(NULL));
	int sorteio = rand() % palavras.size();

	return palavras[sorteio];
}