import time
import random
#menu onde novas opções podem ser criadas
#DEIXE O H POR ULTIMO!!!!!!!!
menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
[h] Hackear o banco
=> """
#variaveis e constantes do codigo
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
#O codigo né pae
while True:

    opcao = input(menu)
    #Opção 'D' de: "Denise devolve meus filhos por favor eu sinto falta deles"
    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("ERROR! O valor informado é inválido.")
    #Opção 'S' de: Saudade
    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("ERROR! Você não tem saldo suficiente, pobre.")

        elif excedeu_limite:
            print("ERROR! O valor do saque excede o limite.")

        elif excedeu_saques:
            print("ERROR! Número máximo de saques excedido, otario.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("Operação falhou! O valor informado é inválido.")
         #Opção 'E' de: EU NÃO CONSIGO ME LEMBRAR SE QUER, QUAL ERA O NOME DAQUELA MOLIEEEEEER.....
    elif opcao == "e":
        print("\n================ EXTRATO ================")
        print("E o pix, nada ainda?." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")
        #Opção 'Q' de: Quit Cat, uma das milhares de músicas nas quais eu dedicaria a você
    elif opcao == "q":
        break
         #Opção 'H' de: Super Heroína
    elif opcao == "h":   
        progresso = 0

        while progresso < 100:
           
            incremento = random.randint(1, 15)

            progresso += incremento

            if progresso > 100:

             progresso = 100

            print(f"{progresso}% hackeado...", end="\r")

            time.sleep(0.5)

            saldo= 9999999999999999

            print("HACKEANDO PORRA! Agora você é bilionário!!!!!.")
 
    else:
        print("Operação inválida, só tem 4 opção válida, bixo burro.")


#Se tudo isso der certo, eu prometo, do fundo do meu coração, te dar a vida de princesa que você merece Maria.        
