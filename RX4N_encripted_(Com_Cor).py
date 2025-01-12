from time import sleep as s


def hud(msg="CIFRA DE RX4N"):
    print("\033[34m=\033[m"*50)
    print()
    print(f"{msg:^50}")
    print()
    print("\033[34m=\033[m"*50)
    s(1)


def linha():
    print("\033[37m-\033[m"*50)


escolha = 1
while True:
    while True:
        hud()
        print("""\033[33m[1]\033[m \033[36mCriptografar Mensagem\033[m
\033[33m[2]\033[m \033[36mDescriptografar Mensagem\033[m
\033[33m[3]\033[m \033[36mConfigurar\033[m
\033[33m[4]\033[m \033[36mComo Funciona?\033[m
    
\033[33m[0]\033[m \033[31mExit\033[m""")
        try:
            opc = int(input("\033[33m>>\033[m "))
        except:
            print("\033[31mDigite um valor valido!\033[m\n")
            s(2)
        else:
            linha()
            s(1)
            print("\n"*100)
            opc = opc
            break
    if opc == 3:
        hud()
        while True:
            print("\033[33m[1]\033[m \033[36mTrocar C por K\033[m\n\033[33m[2]\033[m \033[36mTrocar K por C\033[m\n")
            print("\033[4;35mPADRÃO = 1\033[m\n\n")
            try:
                escolha = int(input("\033[33m>>\033[m "))
            except:
                print("\033[31mValor Invalido!\033[m")
                s(2)
            else:
                if escolha > 2 or escolha < 1:
                    print("\033[31mValor Invalido!\033[m")
                    s(2)
                else:
                    linha()
                    s(1)
                    escolha = escolha
                    print("\n"*100)
                    break
    if opc == 4:
        hud()
        print("""
    \033[32mO codigo foi totalmente criado e desenvolvido por \033[1;36mRian Batista\033[m\033[32m,
nesse codigo a proposta foi criar um cripitador e descripitador de textos.
    \033[4;32mA principio, a letra K e C podem ser trocadas, por conta do formato do alfabeto,
elas podem ser tanto uma letra C quanto a letra K tem horas, mas, podem ser configuradas.\033[32m
    O alfabeto criado para funcionar nesse algoritmo é o seguinte:\033[m""")
        s(1)
        print()
        print("""
\033[1;36m    1  2  3  4  5  6\033[m

\033[31m1\033[m   A  B  C  D  E  0
\033[31m2\033[m   F  G  H  I  J  1
\033[31m3\033[m   L  M  N  O  P  2
\033[31m4\033[m   Q  R  S  T  U  3
\033[31m5\033[m   V  W  X  Y  Z  4
\033[31m6\033[m   5  6  7  8  9    
""")
        s(1)
        print()
        print("""\033[32m
    \033[4;32mComo pode ser observado, a letra K nem aparece, por motivo de que no ingles
a letra K pode ter o mesmo som que C como por exemplo: NICK; PICK ou MIC...
É importante entender que durante o codigo as letras K ou C seram trocadas \033[1;32;107m(\033[1;33;107m[3] \033[1;36;107mConfigurar\033[1;32;107m)\033[m\033[4;32m por sua oposta,
sendo assim com os mesmo exemplos: NICC; PICC... ou NIKK; MIK...\033[m
    \033[31mAtenção! É proibido \033[1;31;107m(Não recomendado)\033[m \033[31mescrever um texto que tenha simbolos ou acentos\033[m""")
        s(1)
        print("""\033[4mSe o código for parecido com de algum outro desenvolvedor eu sinto muito, minha intenção não foi copiar.
Caso o ''Alfabeto'' a qual eu digo que pensei e criei for já algo que existe ou semelhante, por favor entrar em contado,
para mim deixar a fonte de inspiração e também de crédito.\033[m""")
        s(1)
        linha()
        s(1)
        input("Aperte \033[32mENTER\033[m para prosseguir...")
        linha()
        s(1)
        print("\n"*100)
    if opc == 0:
        print("\033[31mCriado por \033[4;36mRX4N\033[m\n\033[32mObrigado por utilizar!!\033[m\n\033[1;31m<3\033[m")
        s(5)
        break
    if opc == 2:
        hud()
        while True:
            texto = str(input("\033[35mDigite os valores para Descriptografar:\033[m\n\033[33m>>\033[m ")).upper().strip()
            text = texto.replace(" ", "")

            if text.isnumeric():
                if len(text) % 2 == 0:
                    s(1)
                    print("\033[32mDescripitando as informações...\033[m")
                    linha()
                    s(2)
                    break
                else:
                    print("\033[31mFalta 1 Número, talvez tenha mais erros!\033[m\n")
                    s(2)
            else:
                print("\033[31mSó é possivel usar números!\033[m\n")
                s(2)
        print("\n"*100)
        hud()
        s(1)
        linha()
        print()
        digito = 0
        repetindo = len(text)
        while True:
            if repetindo == 0:
                break
            if int(text[digito]) == 1:
                if int(text[digito+1]) == 1:
                    print("A", end='')
                elif int(text[digito+1]) == 2:
                    print("F", end='')
                elif int(text[digito+1]) == 3:
                    print("L", end='')
                elif int(text[digito+1]) == 4:
                    print("Q", end='')
                elif int(text[digito+1]) == 5:
                    print("V", end='')
                elif int(text[digito+1]) == 6:
                    print("5", end='')
            elif int(text[digito]) == 2:
                if int(text[digito+1]) == 1:
                    print("B", end='')
                elif int(text[digito+1]) == 2:
                    print("G", end='')
                elif int(text[digito+1]) == 3:
                    print("M", end='')
                elif int(text[digito+1]) == 4:
                    print("R", end='')
                elif int(text[digito+1]) == 5:
                    print("W", end='')
                elif int(text[digito+1]) == 6:
                    print("6", end='')
            elif int(text[digito]) == 3:
                if int(text[digito+1]) == 1:
                    if escolha == 1:
                        print("K", end='')
                    else:
                        print("C", end='')
                elif int(text[digito+1]) == 2:
                    print("H", end='')
                elif int(text[digito+1]) == 3:
                    print("N", end='')
                elif int(text[digito+1]) == 4:
                    print("S", end='')
                elif int(text[digito+1]) == 5:
                    print("X", end='')
                elif int(text[digito+1]) == 6:
                    print("7", end='')
            elif int(text[digito]) == 4:
                if int(text[digito+1]) == 1:
                    print("D", end='')
                elif int(text[digito+1]) == 2:
                    print("I", end='')
                elif int(text[digito+1]) == 3:
                    print("O", end='')
                elif int(text[digito+1]) == 4:
                    print("T", end='')
                elif int(text[digito+1]) == 5:
                    print("Y", end='')
                elif int(text[digito+1]) == 6:
                    print("8", end='')
            elif int(text[digito]) == 5:
                if int(text[digito+1]) == 1:
                    print("E", end='')
                elif int(text[digito+1]) == 2:
                    print("J", end='')
                elif int(text[digito+1]) == 3:
                    print("P", end='')
                elif int(text[digito+1]) == 4:
                    print("U", end='')
                elif int(text[digito+1]) == 5:
                    print("Z", end='')
                elif int(text[digito+1]) == 6:
                    print("9", end='')
            elif int(text[digito]) == 6:
                if int(text[digito+1]) == 1:
                    print("0", end='')
                elif int(text[digito+1]) == 2:
                    print("1", end='')
                elif int(text[digito+1]) == 3:
                    print("2", end='')
                elif int(text[digito+1]) == 4:
                    print("3", end='')
                elif int(text[digito+1]) == 5:
                    print("4", end='')
                elif int(text[digito+1]) == 6:
                    print(" ", end='')
            digito += 2
            repetindo -= 2
        print()
        print()
        linha()
        s(1)
        print("Aperte \033[32mENTER\033[m para prosseguir...")
        linha()
        input()
        print("\n"*100)

    if opc == 1:
        hud()
        texto = str(input("\033[35mDigite um texto para Criptografar:\033[m\n\033[33m>>\033[m ")).lower().strip()
        digito = 0
        repetir = len(texto)
        s(1)
        print("\033[32mCriptografando...\033[m")
        linha()
        s(2)
        print("\n"*100)
        hud()
        s(1)
        linha()
        print()
        while True:
            if repetir == 0:
                break
            if texto[digito] == 'a':
                print("11", end='')
            elif texto[digito] == 'b':
                print("21", end='')
            elif texto[digito] == 'c':
                print("31", end='')
            elif texto[digito] == 'd':
                print("41", end='')
            elif texto[digito] == 'e':
                print("51", end='')
            elif texto[digito] == 'f':
                print("12", end='')
            elif texto[digito] == 'g':
                print("22", end='')
            elif texto[digito] == 'h':
                print("32", end='')
            elif texto[digito] == 'i':
                print("42", end='')
            elif texto[digito] == 'j':
                print("52", end='')
            elif texto[digito] == 'k':
                print("31", end='')
            elif texto[digito] == 'l':
                print("13", end='')
            elif texto[digito] == 'm':
                print("23", end='')
            elif texto[digito] == 'n':
                print("33", end='')
            elif texto[digito] == 'o':
                print("43", end='')
            elif texto[digito] == 'p':
                print("53", end='')
            elif texto[digito] == 'q':
                print("14", end='')
            elif texto[digito] == 'r':
                print("24", end='')
            elif texto[digito] == 's':
                print("34", end='')
            elif texto[digito] == 't':
                print("44", end='')
            elif texto[digito] == 'u':
                print("54", end='')
            elif texto[digito] == 'v':
                print("15", end='')
            elif texto[digito] == 'w':
                print("25", end='')
            elif texto[digito] == 'x':
                print("35", end='')
            elif texto[digito] == 'y':
                print("45", end='')
            elif texto[digito] == 'z':
                print("55", end='')
            elif texto[digito] == '0':
                print("61", end='')
            elif texto[digito] == '1':
                print("62", end='')
            elif texto[digito] == '2':
                print("63", end='')
            elif texto[digito] == '3':
                print("64", end='')
            elif texto[digito] == '4':
                print("65", end='')
            elif texto[digito] == '5':
                print("16", end='')
            elif texto[digito] == '6':
                print("26", end='')
            elif texto[digito] == '7':
                print("36", end='')
            elif texto[digito] == '8':
                print("46", end='')
            elif texto[digito] == '9':
                print("56", end='')
            elif texto[digito] == ' ':
                print("66", end='')
            digito += 1
            repetir -= 1
        print()
        print()
        linha()
        s(1)
        print("Aperte \033[32mENTER\033[m para prosseguir...")
        linha()
        input()
        print("\n"*100)
