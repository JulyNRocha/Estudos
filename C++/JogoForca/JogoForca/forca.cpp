#include <iostream>
#include <string>
#include <map>
#include <vector>
#include "adicionaP.hpp"
#include "cabecalho.hpp"
#include "chuta.hpp"
#include "escreveArquivos.hpp"
#include "existe.hpp"
#include "imprimeErros.hpp"
#include "imprimeForca.hpp"
#include "leArquivos.hpp"
#include "naoAcertou.hpp"
#include "sorteiaPalavra.hpp"

using namespace std;


static map<char, bool> chutou;
static string palavraSecreta;
static vector<char> chutesErrados;

int main () {
	std::string palavraSecreta = sorteiaPalavra();
	cabecalho();

	while(naoAcertou(palavraSecreta, chutou) && chutesErrados.size() < 5 ){
		
		imprimeErros(chutesErrados);
		imprimeForca(palavraSecreta, chutou);
		chuta(chutesErrados, chutou, palavraSecreta);
		
	}

	cout << "Fim de jogo!" << endl;
	cout << "A palavra secreta era: " <<  palavraSecreta << endl;

	if(naoAcertou(palavraSecreta, chutou)){
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