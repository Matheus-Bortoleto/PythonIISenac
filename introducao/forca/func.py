from os import path
import random

def imprime_mensagem_abertura():
    print("################################################");
    print("-_-_-_-_-_-* * * Jogo da Forca * * *-_-_-_-_-_-");
    print("################################################");

def definir_tema():
    dica = int(input("""
                Digite a opção para o tema:
                    1 - Carros
                    2 - Cidades do Brasil
                    3 - Paises
                    4 - Nome de Pessoas
                    5 - Frutas
                """))
    dicas = ('carro','cidade','país','nome','fruta')
    return dicas[dica-1]

def carrega_palavra_secreta(tema):
    dirName = path.dirname(path.abspath(__file__));
    arquivo = open(f"{dirName}\\{tema}.txt","r");
    palavras = [];
    for linha in arquivo:
        linha = linha.strip();
        palavras.append(linha)
    arquivo.close()
    numero = random.randrange(0, len(palavras)+1);
    palavra_secreta = palavras[numero].upper()
    return palavra_secreta

def init_letras_acertadas(palavra_secreta):
    return ["_" for letra in palavra_secreta]