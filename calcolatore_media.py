lista_voti = []
lista_prova = [7, 9, 6, 8]

# voto = input("Inserisci un voto ") 

# try:
#     voto_int = int(voto)
    
#     if voto_int > 0 and voto_int <= 10:
#         lista_voti.append(voto_int)
#         print(lista_voti)
# except:
#     voto = input("Inserisci un voto valido ")

######## DEFINISCO LE FUNZIONI PER CALCOLARE LE MIN MAX E MEDIA ###############

def calcola_media(voti):
    media = 0
    for n in voti:
        media += n
    return media / len(voti)


def calcola_voto_massimo(voti):  
    voto_maggiore = 0
    for n in voti:
        if n > voto_maggiore:
            voto_maggiore = n
    return voto_maggiore
    
def calcola_voto_minore(voti):
    voto_minore = 10
    for n in voti:
        if n < voto_minore:
            voto_minore = n
    return voto_minore 

def calcola_suff(voti):
    suff = 0
    for n in voti:
        if n >= 6:
            suff += 1
    return suff

def calcola_insuf(voti):
    insuff = 0
    for n in voti:
        if n <= 5:
            insuff += 1
    return insuff

def converti_lista(voti):
    stringa_voti = ""
    for n in voti:
        stringa_voti += str(n) + " "
    return stringa_voti

#### definisco la funzione per ritornare i voti #########

def genera_statistiche(voti):
    
    text = f"""
I tuoi voti sono: {converti_lista(voti)}
Hai {calcola_suff(voti)} voti sopra la sufficenza
Hai {calcola_insuf(voti)} sotto la sufficenza
Il tuo voto più alto è un {calcola_voto_massimo(voti)}
Il tuo voto più basso è un {calcola_voto_minore(voti)}
La tua media totale è di: {calcola_media(voti)}
"""

    text2 = "Complimenti sei promosso!" if calcola_media(voti) >= 6 else "Peccato non hai superato il corso"
    print(text + text2)


##### metto tutto insieme #####

while True:
    voto = input("Inserisci un voto ") 

    try:
        voto_int = int(voto)
        
        if voto_int > 0 and voto_int <= 10:
            lista_voti.append(voto_int)
        
        genera_statistiche(lista_voti)
            
    except:
        print("Attenzione voto non valido")
    




