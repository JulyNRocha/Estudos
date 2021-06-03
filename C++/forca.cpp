#include <iostream>
#include <string>
#include <map>
#include <vector>
#include <fstream>
#include <cstdlib>
#include <ctime>
#include "adicionaP.hpp"
#include "cabecalho.hpp"
#include "chuta.hpp"
#include "escreveArquivos.hpp"
#include "existe.hpp"
#include "imprimeErros.hpp"
#include "imprimeForca.hpp"
#include "leArquivos.hpp"
#include "naoAcertou.hpp"
#include "naoEnforcou.hpp"
#include "sorteiaPalavra.hpp"

using namespace std;

string palavraSecreta;

map<char, bool> chutou;

vector<char> chutesErrados;

int main () {
	leArquivos();
	sorteiaPalavra();
	cabecalho();

	while(naoEnforcou() && naoAcertou()){
		
		imprimeErros();
		imprimeForca();
		chuta();
		
	}

	cout << "Fim de jogo!" << endl;
	cout << "A palavra secreta era: " <<  palavraSecreta << endl;

	if(naoAcertou()){
		cout << "Você perdeu, tente novamente!" << endl;
	} else {
		cout << "Parabens Voce acertou, jogue novamente!" << endl;
		cout << "Voce deseja adicionar uma nova palavra? (S/N)"<< endl;
		char resposta;
		cin >> resposta;
		if(resposta == 'S'){
			adicionaP();
		}
	}

}