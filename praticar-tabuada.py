import random
import os
import time

numeros = [2,3,4,5,6,7,8,9]

def limpar_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

limpar_terminal()

def perguntar():
    while True: # Roda a função até o break
        x1 = random.choice(numeros)
        x2 = random.choice(numeros)

        userInput = input(f"Quanto é {x1}*{x2}?:")

        resposta_correta = x1*x2

        try:
            if userInput.lower() == 'sair':
                limpar_terminal()
                print("Até mais ヾ(＾ ∇ ＾).")
                break

            if int(userInput) == resposta_correta:
                limpar_terminal()
                print("Boa! ദ്ദി(˵ •̀ ᴗ - ˵ ) ✧")
                time.sleep(3)
                limpar_terminal()
            else:
                limpar_terminal()
                print(f"Errou a resposta correta é: {resposta_correta} (•ˋ _ ˊ•)")
                time.sleep(3)
                limpar_terminal()
        except:
            print("Digita certo animal ヽ( `д´*)ノ")

perguntar()