def PedraPapelTesoura():
    from os import system, name;
    import random;

    opcao = 's';
    while opcao.upper()=='S':
        system('cls') if(name== 'nt') else system('clear')

        #randomiza a opção do CPU
        computador = random.randint(0,2);
        jogador = int(input('''Escolha uma opção para se jogar: 
        [1]Pedra;
        [2]Papel;
        [3]Tesoura;
        Digite sua escolha: '''))-1;
        pecas = ("Pedra", "Papel", "Tesoura");

            #Tupla Multi-diemnsional
    tabela = (
        ('NINGUEM', 'JOGADOR', 'CPU')
        ('CPU', 'NINGUEM', 'JOGADOR')
        ('JOGADOR', 'CPU', 'NINGUEM')
    );

    print(f'Voce escolheu {pecas[jogador]}');
    print(f'CPU escolheu {pecas[computador]}');
    print(f'{tabela[computador][jogador]} GANHOU!!!');
    opcao = input("Jogar novamente? Aperte S(sim) para jogar");

if(__name__ == "__main__"):
    PedraPapelTesoura();