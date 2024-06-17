 # Escribe una función que reciba dos palabras (String) y retorne
 # verdadero o falso (Bool) según sean o no anagramas.
 # - Un Anagrama consiste en formar una palabra reordenando TODAS
 #   las letras de otra palabra inicial.
 # - NO hace falta comprobar que ambas palabras existan.
 # - Dos palabras exactamente iguales no son anagrama.


def anagrama(pal1,pal2):
    contador = 0
    if len(pal1)==len(pal2):

        for i in range(len(pal1)):
            for j in range(len(pal1)):
                if pal1[i].lower() == pal2[j].lower():
                    contador = contador+1
        if contador == len(pal1):
            print("¿Son anagramas?: True")
        else:
            print("¿Son anagramas?: False")
    else:
        print("¿Son anagramas?: False")

anagrama("amor","Roma")