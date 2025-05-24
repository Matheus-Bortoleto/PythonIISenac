def AdivinheNumero():
    from os import system;
    import random;

    system('cls');

    print("######################################");
    print("Adivinhe um número entre 0 a 100");
    print("######################################");

    dificuldade = input("Escolha a dificuldade desejada:\n"
                        "normal = 10 tentativas\n"
                        "dificil = 5 tentativas\n"
                        "deus = 1 tentiva, está com sorte?\n")

    #variavel com o método de escolha de um número aleatoriamente entre 0 a 100
    numero_secreto = random.randrange(0,101);

    #definindo o numero total de tentativas
    if(dificuldade == "normal"):
        total_tentativas = 10;

    if(dificuldade == "dificil"):
        total_tentativas = 6;

    if(dificuldade == "deus"):
        total_tentativas = 1;

    #loop comportamental das tentativas
    for rodada in range(1, total_tentativas +1):
        print(f'\nTentativa {rodada:02d} de {total_tentativas}');

        tentativa = input("Tente acertar o número de 1 a 100: ");
        print("Você digitou: ", tentativa);

        #converção de string para int
        tentativa_int = int(tentativa);
        if(tentativa_int < 1 or tentativa_int > 100):
            print("Tentativa INVÁLIDA! Somente números entre 0 a 100!");
            continue;

        #respotas das tentativas
        acerto = tentativa_int == numero_secreto;
        ehmaior = tentativa_int > numero_secreto;
        ehmenor = tentativa_int < numero_secreto;

        if(acerto):
            print("boa tentativa. Acertou!");
            break;
            
        if(ehmaior):
            print("Você errou! Número citado é maior, tente novamente");

        if(ehmenor):
            print("Você errou! Número citado é menor, tente novamente");

    print(f'O número secreto sorteado foi: {numero_secreto}');
    input('\nObrigado por participar\n');

if(__name__ == "__main__"):
    AdivinheNumero();