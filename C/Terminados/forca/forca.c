#include <stdio.h>
#include <string.h>
#include <time.h>
#include <stdlib.h>
#include "forca.h"

char palavrasecreta[TAMANHO_PALAVRA];
char chutes[26];
int tentativas = 0;

void abertura() {
    printf("###---------------------###\n");
    printf("###--- Jogo de Forca ---###\n");
    printf("###---------------------###\n\n");
}

void chuta() {
    char chute;
    scanf(" %c", &chute);

    chutes[tentativas] = chute;
    tentativas++;
}

int jachutou(char letra) {
    int achou = 0;
    for(int j = 0; j < tentativas; j++) {
        if(chutes[j] == letra) {
            achou = 1;
            break;
        }
    }

    return achou;
}

void desenhaforca() {

	int erros = chuteserrados();

	printf("  _______       \n");
	printf(" |/      |      \n");
	printf(" |      %c%c%c  \n", (erros>=1?'(':' '), (erros>=1?'_':' '), (erros>=1?')':' '));
	printf(" |      %c%c%c  \n", (erros>=3?'\\':' '), (erros>=2?'|':' '), (erros>=3?'/': ' '));
	printf(" |       %c     \n", (erros>=2?'|':' '));
	printf(" |      %c %c   \n", (erros>=4?'/':' '), (erros>=4?'\\':' '));
	printf(" |              \n");
	printf("_|___           \n");
	printf("\n\n");

   for(int i = 0; i < strlen(palavrasecreta); i++) {

      if(jachutou(palavrasecreta[i])) {
         printf("%c ", palavrasecreta[i]);
      } else {
      
		printf("_ ");
      
		}

    }
    printf("\n");

}

void escolhepalavra() {
   FILE* f;
	f = fopen("palavras.txt","r");

	if(f == 0) {
      printf("Banco de dados de palavras nao disponivel\n\n");
      exit(1);
   }

	int qtddepalavras;
	fscanf(f, "%d", &qtddepalavras);
	srand(time(0));
	int randomico = rand() %qtddepalavras;

	for(int i = 0; i<= randomico; i++) {
		fscanf(f, "%s", palavrasecreta);
	}



	fclose(f);
}

void adicionapalavra() {
    char quer;

    printf("Voce deseja adicionar uma nova palavra no jogo (S/N)?");
    scanf(" %c", &quer);

    if(quer == 'S') {
        char novapalavra[TAMANHO_PALAVRA];

        printf("Digite a nova palavra, em letras maiusculas: ");
        scanf("%s", novapalavra);

        FILE* f;

        f = fopen("palavras.txt", "r+");
        if(f == 0) {
            printf("Banco de dados de palavras nao disponivel\n\n");
            exit(1);
        }

        int qtd;
        fscanf(f, "%d", &qtd);
        qtd++;
        fseek(f, 0, SEEK_SET);
        fprintf(f, "%d", qtd);

        fseek(f, 0, SEEK_END);
        fprintf(f, "\n%s", novapalavra);

        fclose(f);

    }

}

int acertou(){
	for (int i = 0; i < strlen(palavrasecreta); i++){
		if(!jachutou(palavrasecreta[i])) {
			return 0;
		}
	}
	return 1;
}

int chuteserrados() {
	int erros = 0;

   for (int i = 0; i < tentativas; i++) {

   	int existe = 0;

      for(int j = 0; j < strlen(palavrasecreta); j++) {
         if(chutes[i] == palavrasecreta[j]) {

            existe = 1;
            break;
         }
      }

      if(!existe) erros++;
   }

	return erros;

}

int enforcou() {

  return chuteserrados() >= 5;
}

int main() {

    abertura();
    escolhepalavra();

    do {

        desenhaforca();
        chuta();

    } while (!acertou() && !enforcou());
	 
	if (acertou()){
		printf("\nParabens, voce ganhou!");
	} else { 
		printf("\nPuxa, voce foi enforcado!\n");
		printf("A palavra secreta era **%s**\n\n", palavrasecreta);
	}
	
}