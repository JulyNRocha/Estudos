# coding: utf-8
from time import sleep,time
from random import randint,uniform,choice

configQuantidade = 5
configJogadores = 1
configRandom = False
configModo = 1


#-------------DEFININDO LISTA DE PALAVRAS E FRASES DEFOUT--------------

palavrasDefault = ["nozes","leite","uva","tomate","pescada","vinagre","aveia","abacaxi","manga","espinafre","fruta","groselha","rabanete","banana","farinha","marmelo","nectarina","ameixa","pão","comida","aspargos","laranja","arroz","cebola","kiwi","carne","sardinha","vegetais","cevada","comida","coco","pera","caqui","cevada","ovos","damasco","repolho","alface","figo","abobrinha","trigo","cenoura","ervilha","salmão","vinagre","queijo","macarrão","tamara","melancia","maracuja","macaco","coala","mula","pomba","ouriço","caracol","besouro","tatu","atum","pavão","bacalhau","vaca","pinguim","avestruz","iguana","ovelha","carpa","baleia","zebra","galinha","lesma","borboleta","bolo","iguana","javali","chinchila","veado","baiacu","gorila","polvo","golfinho","canguru","coruja","elefante","aranha","coelho","tartaruga","sapo","camelo","tigre","rato","cachorro","lula","barata","lagosta","girafa","crocodilo","leão","rinoceronte","carangueijo","verde","branco","marrom","branca","roxo","amarelo","laranja","azul","vermelho","roxo","cinza","rosa","azul","preto","castanho","lilás","dourado","prateado","ambar","magenta","turquesa","violeta","bege","bordô","cereja","carmim","ciano","creme","ébano","fuligem","índigo","jade","lima","linho","malva","neve","ouro","pardo","pêssego","sépia","terracota","urucum","rubi","ferrugem","baunilha","mostarda","prata","carvão","esmeralda","menta"]

frasesDefault = ["a avareza perde tudo ao pretender ganhar tudo","o mundo está perdido para aqueles que querem ganhar","a maior caridade é habilitar o pobre a ganhar a sua vida","perder para a razão sempre é ganhar","escolher o seu tempo é ganhar tempo","o medo de perder tira a vontade de ganhar","é melhor conquistar a si mesmo do que vencer mil batalhas","vossa coragem e sacrifício serão lembradas para todo o sempre","ele irá reduzir o tempo necessário para o nosso programa na inicialização","áreas plantadas são protegidos por barreiras de onda para minimizar a erosão","uma pequena relíquia descoberta incrível e misteriosamente intacta","você ainda será vulnerável à vigilância direcionada","só é preciso uma pequena quantidade","ficaremos extremamente felizes se cantar alguma coisa","tenho estado a evitar a sua inevitabilidade","não me faça mandar duas vezes","leia cuidadosamente as informações a seguir","só é preciso uma centelha","espelhos permitem a nós ver objetos que não conseguimos ver diretamente","a paz mundial não é somente possível mas inevitável","note que a vulnerabilidade é no processo de geração de chaves","ele tinha ordens para observar mas não interferir","temos que examinar cuidadosamente este caso","temos que escrutinar este caso","as pessoas devem olhar para mim para a consistência e perseverança","coisas pequenas se tornam grandes quando feitas com amor","seja o amor da sua vida","a tua graça me basta","faça o que você ama todos os dias","se eu quisesse palavras eu comprava um dicionário","esta frase é a última ou será que não","java e C são melhores que python","não plante nada nessa terra","para cada coisa o seu tempo","se fosse fácil todo mundo saberia explicar como fazer","a vida é infinita para aqueles que sabem aproveitar","cuidado para não esperar de mim aquilo que não recebi de você","o veneno está em cima do piano de calda","distância não significa nada quando alguém significa tudo","é preciso aprender a viver sem as pessoas que vivem sem você","estou ficando sem ideias de frases","o planeta terra em sua maior parte é composto por água","gatos tem sete vidas pois tem preguiça de morrer","é você que está jogando o jogo ou o jogo que está te testando","este jogo tem exatamente 50 frases e 150 palavras","que fome acho que vou comer lasanha","ironicamente lasanha não é uma palavra no jogo","o bolo é e sempre será uma mentira","o significado da vida e do universo e todo resto é 42","não quis colocar virgulas nas frases pois não gosto delas","se você viu o código fonte Obrigada por vir até aqui"]

#------------- DEFININDO FUNÇÕES QUE GERAM ITENS -----------------

def randomizarNumero(quantosNumeros):
	'''Gera uma Arrey de Numeros Aleatorios entre 0 e 100
	:param quantosNumeros: int '''

	listaDeNumero = []

	while (len(listaDeNumero) < quantosNumeros):

		number_str = (round(randint(0,100)))
		number = str(number_str)
		if(number not in listaDeNumero):

			listaDeNumero.append(number)

	return (listaDeNumero)

def randomizarLetra(quantasLetras):
	'''Gera uma Arrey de Letras Aleatores
	:param quantasLetras: int'''

	listaDeLetras = []

	while (len(listaDeLetras) < quantasLetras):
		letra = '%c' % randint(97,122)

		if(letra not in listaDeLetras):

			listaDeLetras.append(letra)
	
	return (listaDeLetras)

def randomizarPalavras(quantasPalavras,palavraRandom):
	'''Gera uma Arrey de Palavras Aleatorias
	:param quantasPalavras: int
	:param palvraRandom: bool'''

	listaDePalavras = []

	while(len(listaDePalavras) < quantasPalavras ):
		if(palavraRandom):
			palavra = ""

			for i in range(randint(3,8)):
				palavra += '%c' % randint(97,122)

			if(palavra not in listaDePalavras):

				listaDePalavras.append(palavra)
		else:
			palavra = choice(palavrasDefault)
			if(palavra not in listaDePalavras):
				listaDePalavras.append(palavra)

	return (listaDePalavras)		

def randomizarFrases (quantasFrases,frasesRandom):
	'''Gera as Frases
	:param quantasFrases: int
	:param frasesRandom: bool'''

	listaDeFrases = []
	while(len(listaDeFrases) < quantasFrases ):
		if(frasesRandom):
			frase = ""
			quantidadeDePalavrasNaFrase = randint(5,8)
			for i in range(quantidadeDePalavrasNaFrase):
				palavra = randomizarPalavras(1,True)
	
				if(i == (quantidadeDePalavrasNaFrase-1)):
					frase += palavra
				else:
					frase += palavra				
					frase += " "

			if(frase not in listaDeFrases):
				listaDeFrases.append(frase)	
		else:
			frase = choice(frasesDefault)
			if(frase not in listaDeFrases):
				listaDeFrases.append(frase)	
			
	return (listaDeFrases)

#-------------DEFININDO FUNÇÕES DOS MENUS DO JOGO--------------

def menuPrincipal():
	"""Menu Principal"""

	while(True):
		head(1)

		print("1 - Jogar\n"
		+ "2 - Alterar configurações do jogo\n"
		+ "3 - Configurações atuais\n"
		+ "4 - Sair\n")

		menuEscolhido = verificaEscolha(input('> '))
		print() #Espaçamento

		if(menuEscolhido == False):
			print(mensagemDeErro())
			continue

		if(menuEscolhido == 1):
			resultadoDoJogo(configModo, configJogadores)

		elif(menuEscolhido == 2):
			menuConfig()
		
		elif(menuEscolhido == 3):
			telaConfigAtual()

		elif(menuEscolhido == 4):
			print("Obrigada por jogar ^-^")
			print("Pressione qualquer tecla para sair")
			ready = input()
			exit()

		else:
			print(mensagemDeErro())

def menuConfig():
	"""Menu de Configuração
	:param escolhaConfig: int"""

	while(True):
		head(2)

		print("1 - Configurar o Modo de jogo\n"
		+ "2 - Configurar a quantidade de jogadores\n"
		+ "3 - Configurar a quantidade de itens a serem sorteados\n"
		+ "4 - Configurar o modo Palavras ou Frases\n"
		+ "5 - Voltar ao menu Principal\n")

		escolhaConfig = verificaEscolha(input('> '))
		print() #Espaçamento

		if(escolhaConfig == False):
			print(mensagemDeErro())
			continue

		if(escolhaConfig == 1):
			return menuConfigModo()

		elif(escolhaConfig == 2):
			return menuJogadores()

		elif(escolhaConfig == 3):
			return menuQuantidade()

		elif(escolhaConfig == 4):
			return menuRandom()

		elif(escolhaConfig == 5):
			return

		else:
			print(mensagemDeErro())
			continue

def menuConfigModo():
	"""Menu de Configuração do Modo de Jogo
	:param escolhaModo: int"""

	global configModo

	while(True):
		head(3)

		print("1 - Modo Número ( Fácil )\n"
		+ "2 - Modo Letras ( Médio )\n"
		+ "3 - Modo Palavra ( Difícil )\n"
		+ "4 - Modo Frase ( Extremo )\n")

		escolhaModo = verificaEscolha(input('> '))
		print() #Espaçamento

		if(escolhaModo == False):
			print(mensagemDeErro())
			continue

		if(escolhaModo == 1):
			print("Eu te entendo, tambem acho dificil digitar rápido :P")
			print("Agora seu modo de jogo é: Modo Numero")

		elif(escolhaModo == 2):
			print("Modo Justo, nem mais, nem menos >.<")
			print("Agora seu modo de jogo é: Letras")

		elif(escolhaModo == 3):
			print("Agora sim um desafio hein! Quero ver o quão rapido você digita (ง'̀-'́)ง")
			print("Agora seu modo de jogo é: Palavras")

		elif(escolhaModo == 4):
			print("⚆ _ ⚆ Tu é o bichão mermo hein")
			print("Agora seu modo de jogo é: Frases. Tenho até medo de pensar >.<")

		else:
			print(mensagemDeErro())
			continue

		configModo = escolhaModo
		print("Pressione qualquer tecla para voltar ao menu")
		ready = input()

		return

def menuJogadores():
	"""Menu de Quantidade de Jogadores
	:param escolhaJogadores: int"""
	global configJogadores

	while(True):
		head(4)
		print("Quantos jogadores estão jogando?\n")

		quantidadeJogadores = verificaEscolha(input('> '))
		print() #Espaçamento

		if(quantidadeJogadores == False):
			print(mensagemDeErro())
			continue

		if(quantidadeJogadores > 0 and quantidadeJogadores < 5):
			configJogadores = quantidadeJogadores
			print("Pronto! agora seu Jogo tem", configJogadores, "Jogadore(s) ^-^", sep = " ")
			print("Pressione qualquer tecla para voltar ao menu")
			ready = input()
			return

		elif(quantidadeJogadores <= 0):
			print("Assim não dá ¬_¬ ! Até onde eu sei, não tem como \"ninguém\" jogar esse jogo")
			continue

		elif(quantidadeJogadores > 5):
			print("Oh-oh, Acho que tem gente demais jogando. Não é melhor vocês revezarem?")
			continue

		else:
			print(mensagemDeErro())
			continue

def menuQuantidade():
	"""Menu Para Esoclher as Quantidades de itens"""
	global configQuantidade

	while(True):
		head(5)
		print("Quantos itens você quer sortear?\n")

		quantidade = verificaEscolha(input('> '))
		print() #Espaçamento

		if(quantidade == False):
			print(mensagemDeErro())
			continue

		if(quantidade > 1 and quantidade < 20):
			configQuantidade = quantidade
			print("Pronto! agora seu Desafio tem", configQuantidade, "itens ^-^", sep = " ")
			print("Pressione qualquer tecla para voltar ao menu")
			ready = input()
			return

		elif(quantidade == 1):
			print("Assim não dá ¬_¬ , tem que ser um número pelo menos maior que 1 para a brincadeira funcionar")
			continue

		elif(quantidade >= 20):
			print("Oh-oh, Sei que você gosta muito desse jogo, mas esse seu desafio está muito grande. Tenta um número menor que 20")
			continue

		else:
			print(mensagemDeErro())
			continue

def menuRandom():
	"""Menu Para escolher Se as palavras vão ser randomicas ou não"""	
	global configRandom

	while(True):
		head(6)
		print("Você quer que as palavras e frases do jogo tenham sentido ou podem ser letras embaralhadas?:\n"
		+" 1 - Para que os caracteres apareçam embaralhados\n"
		+" 2 - Para que as palavras e as frases façam sentido\n")
		
		escolhaRandom = verificaEscolha(input('> '))
		print() #Espaçamento

		if(escolhaRandom == False):
			print(mensagemDeErro())
			continue

		if(escolhaRandom == 1):
			configRandom = True
			print("Agora você tem palavras e frases que são geradas Randomicamente")

		elif(escolhaRandom == 2):
			configRandom = False
			print("Agora você tem palavras e frases que tem sentido")

		else:
			mensagemDeErro()
			continue

		print("Pressione qualquer tecla para voltar ao menu")
		ready = input()

		return

#------------------ DEFININDO FUNÇÕES DE MENSAGEM ------------------------

def telaConfigAtual():
	if(configRandom):
		configRandom_str = "Palavras e Frases sem sentido (geradas com caracteres aleatórios)"

	else:
		configRandom_str = "Palavras e Frases com sentido (tiradas de um banco de dados)"
	
	if(configModo == 1):
		configModo_str = "Modo Numero"

	elif(configModo == 2):
		configModo_str = "Modo Letra"

	elif(configModo == 3):
		configModo_str = "Modo Palavras"

	elif(configModo == 4):
		configModo_str = "Modo Frases"

	configJogadores_str = str(configJogadores)
	configQuantidade_str = str(configQuantidade)

	while(True):
		head(7)

		print("Modo De Jogo atual: " + configModo_str + "\n"
		+ "-Modo Palavras e Modo Frases: " + configRandom_str + "\n\n"
		+ "Quantidade de Jogadores: " + configJogadores_str + " jogador(es)\n"
		+ "Quantidade de Itens sorteados: " + configQuantidade_str + " itens\n")

		print("Pressione qualquer tecla para voltar ao menu")
		ready = input()
		return
	
def verificaEscolha(escolha):
	"""Verifica se o input é valido"""
	
	try:
		return int(escolha)
	except ValueError:
		return False

def head(tela):
	"""Oque aparece no começo de Cada Tela
	:param tela: int"""

	if(tela == 1):
		print("###--------------------------------------------###\n"
		+ "###-------------- MENU PRINCIPAL --------------###\n"
		+ "###------------- KEYBOARD WHEELS --------------###\n"
		+ "###--------------------------------------------###\n")

	elif(tela == 2):
		print("###--------------------------------------------###\n"
		+ "###----------------- MENU DE ------------------###\n"
		+ "###--------------- CONFIGURAÇÃO ---------------###\n"
		+ "###--------------------------------------------###\n")

	elif(tela == 3):
		print("###--------------------------------------------###\n"
		+ "###----------------- MENU DE ------------------###\n"
		+ "###--------------- MODO DE JOGO ---------------###\n"
		+ "###--------------------------------------------###\n")

	elif(tela == 4):
		print("###--------------------------------------------###\n"
		+ "###----------------- MENU DE ------------------###\n"
		+ "###---------- QUANTIDADE DE JOGADORES ---------###\n"
		+ "###--------------------------------------------###\n")

	elif(tela == 5):
		print("###--------------------------------------------###\n"
		+ "###----------------- MENU DE ------------------###\n"
		+ "###------------ QUANTIDADE DE ITENS -----------###\n"
		+ "###--------------------------------------------###\n")

	elif(tela == 6):
		print("###--------------------------------------------###\n"
		+ "###------------ MENU DE CONFIGURAÇÃO ----------###\n"
		+ "###------ DE RANDOMIZAR PALAVRAS E FRASES -----###\n"
		+ "###--------------------------------------------###\n")

	elif(tela == 7):
		print("###--------------------------------------------###\n"
		+ "###-------------- CONFIGURAÇÕES ---------------###\n"
		+ "###----------------- ATUAIS -------------------###\n"
		+ "###--------------------------------------------###\n")

def mensagemFinal(jogadores,podium):
	"""Mostra a mensagem final dependendo Da quantidade de Jogadores
	:param jogadores: int
	:param podium: list"""

	if(jogadores == 1):
		print("###---------------------------------------###\n"
		+ "###----------- RESULTADO FINAL -----------###\n"
		+ "###---------------------------------------###\n")
		print("Parabéns,", podium[0][0],"!\nVocê levou", podium[0][1], "segundos para terminar o jogo!")
		print("(☞ﾟ∀ﾟ)☞\n")

	elif(jogadores >= 2):
		print("###---------------------------------------###\n"
		+ "###----------- RESULTADO FINAL -----------###\n"
		+ "###---------------------------------------###\n")
		for i in range(jogadores):
			if( i == 0):
				print(u'\U0001f947',(1+i),"º Lugar ￫", podium[i][0], ", com o tempo de :", podium[i][1])
			elif( i == 1):
				print(u'\U0001f948',(1+i),"º Lugar ￫", podium[i][0], ", com o tempo de :", podium[i][1])
			elif( i == 2):
				print(u'\U0001f949',(1+i),"º Lugar ￫", podium[i][0], ", com o tempo de :", podium[i][1])
			else:
				print((1+i),"º Lugar ￫", podium[i][0], ", com o tempo de :", podium[i][1])

	while(True):
		ready = input("Pressione enter para Voltar ao Menu Principal\n")
		if(ready == ""):
			return

def mensagemDeErro():
	"""Mostra uma mensagem de Erro"""
	return "Errr, não sei se você leu, mas o que você digitou não é válido o.O. Volta e escolhe direito ಠ_ಠ"
#------------------ DEFININDO FUNÇÕES PRINCIPAIS DO JOGO ------------------------

def verificandoEscrita(mostrar):
	'''
	Verifica o que foi Digitado
	:param mostrar: str
	'''
	print("digite: ",mostrar)
	digitado = input('> ')
	print("")
	while(digitado != mostrar):
		print("Você errou D: ... Tente de novo!\n")
		print("digite: ",mostrar)
		digitado = input('> ')
		print() #Espaçamento

def multiJogadores(configJogadores):
	'''Cria uma listacom todos os Jogadores
	:param mostrar: str
	:returns: list '''

	if(configJogadores != 1):
		listaDeJogadores = []
		for l in range(configJogadores):
			print("Ok, vamos lá! Quem vai ser o ",(l + 1),"º player?", sep = "")
			jogador = input("\n> Nome do player: ")
			listaDeJogadores.append(jogador)
	else:
		listaDeJogadores = []
		jogador = input("Ok, vamos lá! Como você quer ser chamado?\n> Nome do player: ")
		listaDeJogadores.append(jogador)
	return(listaDeJogadores)

def salvandoJogadorMaisTempo(modoDeJogo,jogadores):
	'''Salva o Player + o seu Tempo em uma Arrey
	:param modoDeJogo: int
	:paran jogadores: int
	:returns: list'''

	listaDeJogadores = multiJogadores(jogadores)
	jogadorMaisOTempo = []
	listaDeJogadoresComTempo = []
	for i in range(len(listaDeJogadores)):
		contagemRegressiva(listaDeJogadores[i])
		inicio = time()
		rodandojogo(modoDeJogo)
		fim = time()
		tempo = (fim - inicio)
		jogadorMaisOTempo.append(listaDeJogadores[i])
		jogadorMaisOTempo.append(tempo)
		listaDeJogadoresComTempo.append(jogadorMaisOTempo)
		jogadorMaisOTempo = []
	return(listaDeJogadoresComTempo)

def rodandojogo(modoDeJogo):
	'''Roda o Jodo
	:param modoDeJogo: int'''
	if (modoDeJogo == 1):
		lista = randomizarNumero(configQuantidade)
		for i in range(len(lista)):
			verificandoEscrita(lista[i])
	elif (modoDeJogo == 2):
		lista = randomizarLetra(configQuantidade)
		for i in range(len(lista)):
			verificandoEscrita(lista[i])
	elif (modoDeJogo == 3):
		lista = randomizarPalavras(configQuantidade,configRandom)
		for i in range(len(lista)):
			verificandoEscrita(lista[i])
	elif (modoDeJogo == 4):
		lista = randomizarFrases(configQuantidade,configRandom)
		for i in range(len(lista)):
			verificandoEscrita(lista[i])	

def contagemRegressiva(jogador):
	"""Verifica se o jogador esta prepardo pra jogar
	:param: str"""

	enterPressionado = False
	while(enterPressionado == False):
		print("\n" + jogador + ", pressione QUALQUER TECLA quando estiver preparado e quiser começar o jogo!")
		ready = input()
		for cont in range(3, 0, -1):
			print(cont)
			sleep(1)
		print("VALENDO!!\n")
		sleep(0.5)
		return

def resultadoDoJogo(modoDeJogo,jogadores):
	"""Mostra o Reultadodo Geral do Jogo
	:param modoDeJogo: int
	:param jogadores: int"""
	resultadoGeral = salvandoJogadorMaisTempo(modoDeJogo,jogadores)	
	podium = resultadoGeral
	podium.sort(key=lambda x:x[1])

	return(mensagemFinal(jogadores,podium))

#----------------INICIA O JOGO CHAMANDO O MENU-----------------

print("###------- Bem-Vindo ao KEYBOARD WHEELS -------###\n")
menuPrincipal()
