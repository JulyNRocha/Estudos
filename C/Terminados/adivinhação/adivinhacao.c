#include <stdio.h>
#include <stdlib.h>
#include <time.h>


int main() {

	printf("        P  /_\\  P\n"); 
	printf("       /_\\_|_|_/_\\ \n");
	printf("     n_n | ||. .|| | n_n         Bem vindo ao\n");
	printf("     |_|_|nnnn nnnn|_|_|     Jogo de Adivinhacao!\n");
	printf("    |\" \"  |  |_|  |\"  \" |\n");
	printf("    |_____| ' _ ' |_____|\n");
	printf("          \\__|_|__/\n\n");
   printf("************************************\n");
   printf("* Bem vindo ao Jogo de Adivinhação *\n");
   printf("************************************\n");

   int chute;
   int acertou = 0;
   int tentativas = 1;
   double pontos = 1000;

   srand(time(0));
   int numerosecreto = rand() % 100;

	int nivel;
    printf("Qual o nível de dificuldade?\n");
    printf("(1) Fácil (2) Médio (3) Difícil\n\n");
    printf("Escolha: ");
    scanf("%d", &nivel);

    int numerodetentativas;

    switch(nivel) {
        case 1:
            numerodetentativas = 20;
				break;

        case 2:
            numerodetentativas = 15;
				break;

        case 3:
            numerodetentativas = 6;
		}

   for(int i=1 ; i <= numerodetentativas; i++) {

   	printf("Qual é o seu %do. chute? ", tentativas);
      scanf("%d", &chute);

      if(chute < 0) 
		{
         printf("Você não pode chutar números negativos\n");
         continue;
      }

      printf("Seu %do. chute foi %d\n", tentativas, chute);

      acertou = chute == numerosecreto;
      int maior = chute > numerosecreto;

      if(acertou) {

         printf("Parabéns! Você acertou!\n");
			break;

      } else if(maior) {

         printf("Seu chute foi maior do que o número secreto!\n");

      } else {

         printf("Seu chute foi menor do que o número secreto!\n");
      }

      tentativas++;

      double pontosperdidos = abs(chute - numerosecreto) / 2.0;
      pontos = pontos - pontosperdidos;

    }

   printf("Você fez %.2f pontos\n", pontos);
   printf("Obrigado por jogar!\n");

}