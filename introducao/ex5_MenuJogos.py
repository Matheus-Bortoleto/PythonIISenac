from os import system, name;
import ex2_AdivinheNumero;
import ex3_PedraPapelTesoura;
import ex4_aForca;

opcao = 's';
while opcao.upper()=='S':
    system('cls') if(name== 'nt') else system('clear')
    qualJogo = input("Tecle o número para escolher um jogo:\n"
                    "1 - Adivinhação Número\n"
                    "2 - Pedra Papel Tesoura\n"
                    "3 - Jogo da Forca\n")
    
    if(qualJogo == 1):
        ex2_AdivinheNumero.AdivinheNumero();

    if(qualJogo == 2):
        ex3_PedraPapelTesoura.PedraPapelTesoura();

    if(qualJogo == 3):
        ex4_aForca.gg();
    
    opcao = input("Jogar novamente? Aperte S(sim) para jogar");