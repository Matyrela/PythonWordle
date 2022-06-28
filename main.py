from random import choice
from colorama import Fore
import os

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):
        command = 'cls'
    os.system(command)


class Game():
    def __init__(self):
        pass

    def Start():
        wordle = choice(list(open('palabras.txt', "r", encoding="utf8")))
        wordle = wordle.lower()
        Game.MakeBox(wordle)
        letra = []
        Game.adivinaPalabra(wordle.strip(), letra)

        Game.Stop(wordle)

    def Stop(palabra):
        print("Juego Finalizado \n")
        print("La palabra era: ", end="")
        print(palabra)
        exit()

    def MakeBox(palabra):
        palabra = palabra.strip()
        x = len(palabra)
        box = "|"
        for i in range(x):
            box = box + (" |")
        return box, box, box, box, box

    def ShowBox(palabra, stput, rows, cont, letras):
        clearConsole()
        ListPalabra = list(palabra)
        cont2 = -1
        listaKey1 = ["Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P", " "]
        listaKey2 = [" ","A", "S", "D", "F", "G", "H", "J", "K", "L", "Ñ"]
        listaKey3 = [" "," ","Z", "X", "C", "V", "B", "N", "M", " ", " "]
        if(stput == ""):
            x0, x1, x2, x3, x4 = Game.MakeBox(palabra)
            rows.append(x0)
            rows.append(x1)
            rows.append(x2)
            rows.append(x3)
            rows.append(x4)
        else:
            box = "|"
            if(cont != 99):
                for i in stput:
                    cont2 += 1
                    if i == ListPalabra[cont2]:
                        box = box + Fore.GREEN + i + Fore.RESET + "|"
                    elif i in palabra:
                        box = box + Fore.YELLOW + i + Fore.RESET + "|"
                    else:
                        box = box + i+"|"
                rows[cont] = box
            elif (cont == 99):
                for row in range(len(rows)):
                    for i in palabra:
                        box = box + Fore.GREEN + i + Fore.RESET + "|"
                    rows[row] = box
                    box = "|"
            else:
                print("Error")
                exit()
        print("--------Wordle---------")
        print("")
        for row in rows:
            print("      " + row.strip())
        print("")
            
        print("|", end="")
        for key in listaKey1:
            norep1 = False
            noma1 = False

            for letter in letras:
                if key == letter:
                    if key in palabra.upper():
                        if (norep1) == False:
                            norep1 = True
                            print(Fore.LIGHTGREEN_EX + key + Fore.RESET, end="|")
                    elif noma1 == False:
                        noma1 = True
                        print(Fore.LIGHTCYAN_EX + key + Fore.RESET, end="|")

            if norep1 == False:
                if noma1 == False:
                    print(key, end="|")
                
        print("")

        print("|", end="")
        for key in listaKey2:
            norep2 = False
            noma2 = False

            for letter in letras:
                if key == letter:
                    if key in palabra.upper():
                        if (norep2) == False:
                            norep2 = True
                            print(Fore.LIGHTGREEN_EX + key + Fore.RESET, end="|")
                    elif noma2 == False:
                        noma2 = True
                        print(Fore.LIGHTCYAN_EX + key + Fore.RESET, end="|")

            if norep2 == False:
                if noma2 == False:
                    print(key, end="|")
                
        print("")


        print("|", end="")
        for key in listaKey3:
            norep3 = False
            noma3 = False

            for letter in letras:
                if key == letter:
                    if key in palabra.upper():
                        if (norep3) == False:
                            norep3 = True
                            print(Fore.LIGHTGREEN_EX + key + Fore.RESET, end="|")
                    elif noma3 == False:
                        noma3 = True
                        print(Fore.LIGHTCYAN_EX + key + Fore.RESET, end="|")

            if norep3 == False:
                if noma3 == False:
                    print(key, end="|")



        print("")
        print("")

        print("-----------------------")
        print("")

        
        if(cont == 4):
            Game.Stop(palabra)
        return rows

    def adivinaPalabra(palabra, letras):
        rows = []
        cont = -2
        strinput = ""
        while strinput != palabra:
            cont += 1
            rows = Game.ShowBox(palabra, strinput, rows, cont, letras)
            strinput = ""
            while len(strinput) != 5:
                strinput = input(
                    f"Ingrese una palabra de {len(palabra)} letras: "
                )
            for letter in strinput:
                if(letter not in letras):
                    letras.append(letter.upper())            

        cont = 99
        strinput = palabra
        print("\n" + Fore.GREEN + "Ganaste!" + Fore.RESET + "\n")
        rows = Game.ShowBox(palabra, strinput, rows, cont, letras)


print(Game.Start())