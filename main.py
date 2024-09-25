import math

#Creiamo la funzione bto10, che prende due valori
# number -> il numero da portare in base 10
# base -> la base del numero, da portare a 10
def bto10(number, base):
    tt = number
    result = 0
    array = [] #una lista delle cifre di number
    while number > 0:
        temp = number % 10 #l'operazione % ritorna il resto della divisione number / 10
        array.append(temp) #aggiunge il resto alla lista
        if temp >= base: #se il resto è maggiore o uguale alla base, il numero non ha senso
            #Esempio: 343 non può essere in base 4, perché 4 non esiste nei numeri di base 4 (che hanno solo 0 1 2 3)
            raise Exception("La cifra " + temp + " in " + tt + " è maggiore o uguale alla base " + base)
        number //= 10 #divisione in integer, una divisione senza resto
    for i in range(len(array)): #per i che è l'index della lista array
        # lista: [3, 5, 1, 2, 8]
        # index: [0, 1, 2, 3, 4]
        k = array[i] #elemento i della lista
        result += k * math.pow(base, i) #aggiungiamo al risultato l'elemento * la potenza della base alla i
    return result #la funzione ridà result
# Creiamo la funzione tentob, che prende due valore
# number -> il numero da portare in base 'base'
# base -> la base a cui portare il numero
def tentob(number, base):
    array = [] #una lista delle cifre di number
    while True:
        array.append(number % base)#aggiungiamo alla lista il resto della divisione tra number e base
        number //= base #divisione integer
        if number == 0: #se il numero è zero, abbiamo finito di dividere e quindi rompiamo il while
            break
    result = 0 #Il risultato
    for i in range(len(array)): #loop per i che è l'index della lista array
        result += array[i] * math.pow(10, i) #aggiungiamo al risultato l*elemento per la potenza tra 10 e i
    return result#ridiamo il risultato

#Codice da eseguire all'avvio
num = int(input("Numero da convertire"))
base1 = int(input("Base 1"))
base2 = int(input("Base 2"))

#chiamo la funzione bto10
to10 = bto10(num, base1)

print("Convertiamo ", num , " da base " , base1 , " a base 10 -> " , to10)

#chiamo la funzione tentob
to7 = tentob(to10, base2)

print("Convertiamo " , to10 , " da base 10 a base " , base2 , "-> " , to7)
