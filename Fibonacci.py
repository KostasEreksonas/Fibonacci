#!/usr/bin/env python3

# Importuojamos naudojamos bibliotekos
import time
from matplotlib import pyplot as plt
import os

# Fibonačio skaičiaus gavimas rekursiniu būdu
# Šaltinis - https://www.geeksforgeeks.org/program-for-nth-fibonacci-number/
def rekursinis(x):
    if x == 0:
        return 0
    elif x == 1:
        return 1
    else:
        return(rekursinis(x-1) + rekursinis(x-2))

# Fibonačio skaičiaus gavimas linijiniu būdu
# Šaltinis - https://www.geeksforgeeks.org/program-for-nth-fibonacci-number/
def linijinis(x):
    a = 0 # Pirmas Fibonačio skaičius
    b = 1 # Antras Fibonačio skaičius
    if x == 0: # Spausdinamas pirmas Fibonačio skaičius
        return a
    elif x == 1: # Spausdinamas antras Fibonačio skaičius
        return b
    else:
        for i in range(2,x+1):
            # Fibonačio skaičiui gauti atliekamas 2-jų prieš jį buvusių skaičių sumavimas
            c = a + b
            # Du sumuojami fibonačio skaičiai perstumiami į priekį per 1 poziciją
            a = b
            # Du sumuojami fibonačio skaičiai perstumiami į priekį per 1 poziciją
            b = c
        return b

#  ------------------
# | Matricinis būdas |
#  ------------------
# Šaltinis - https://www.geeksforgeeks.org/program-for-nth-fibonacci-number/
# Atliekama matricų F ir M daugyba
# Kiekvienoje matricos F pozicijoje gaunamas tolimesnis Fibonačio skaičius
def multiply(F, M):
    # 1-a F matricos eilutė X 1-as M matricos stulpelis
    F11 = (F[0][0] * M[0][0] +
           F[0][1] * M[1][0])
    # 1-a F matricos eilutė X 2-as M matricos stulpelis
    F12 = (F[0][0] * M[0][1] +
           F[0][1] * M[1][1])
    # 2-a F matricos eilutė X 1-as M matricos stulpelis
    F21 = (F[1][0] * M[0][0] +
           F[1][1] * M[1][0])
    # 2-a F matricos eilutė X 2-as M matricos stulpelis
    F22 = (F[1][0] * M[0][1] +
           F[1][1] * M[1][1])
    # Gauti tolimesni Fibonačio skaičiai įtraukiami į F matricą
    F[0][0] = F11 # 1-a eilutė, 1-as stulpelis
    F[0][1] = F12 # 1-a eilutė, 2-as stulpelis
    F[1][0] = F21 # 2-a eilutė, 1-as stulpelis
    F[1][1] = F22 # 2-a eilutė, 2-as stulpelis

def power(F, x):
    # Pradinė Fibonačio skaičių matrica (Fibonačio skaičių eilės numeriai yra 2,1,1,0)
    M = [[1, 1],
         [1, 0]]
    # Fibonačio matrica F dauginama iš savęs x kartų
    # x - ieškomas Fibonačio skaičius
    for i in range(2, x):
        multiply(F, M)

def matricinis(x):
    # Fibonačio skaičių matrica
    F = [[1, 1],
         [1, 0]]
    if (x == 0):
        return 0
    # Fibonačio skaičių matrica yra perduodama į laipsnio kėlimo funkciją
    # Fibonačio skaičių matrica F yra dauginama pati iš savęs x kartų
    power(F, x)
    # Ieškomas Fibonačio skaičius yra F matricos pirmoje eilutėje bei pirmame stulpelyje
    return F[0][0]

def skaiciavimas(sk, metodas):
    graph = []
    start = time.perf_counter()
    if int(metodas) == 1:
        for x in range(1,int(sk)+1):
            result = rekursinis(x)
            end = time.perf_counter()
            graph.append([x, end-start, result])
    elif int(metodas) == 2:
        for x in range(1,int(sk)+1):
            result = linijinis(x)
            end = time.perf_counter()
            graph.append([x, end-start, result])
    elif int(metodas) == 3:
        for x in range(1,int(sk)+1):
            result = matricinis(x)
            end = time.perf_counter()
            graph.append([x, end-start, result])
    else:
        print(f"Toks modelis neaprašytas")
    print(f"{graph[-1][0]} Fibonačio skaičius yra {graph[-1][2]}, suskaičiuota per {graph[-1][1]} sekundes")
    grafikas(graph)

def grafikas(data):
    laikas,eile = [[] for x in range(2)]
    for x in range(len(data)):
        laikas.append(data[x][1])
        eile.append(data[x][0])
    plt.plot(laikas,eile)
    plt.xlabel("Laikas, s")
    plt.ylabel("Eilės numeris")
    plt.show()

def main():
    sk = input(f"Kelintą Fibonačio skaičių rasti: ")
    metodas = input(f"Pasirinkite Fibonačio skaičiaus gavimo metodą (1 - Rekursinis, 2 - Linijinis, 3 - Matricinis). Įveskite skaičių: ")
    skaiciavimas(sk, metodas)

if __name__ == "__main__":
    main()
