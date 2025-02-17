# versione rivista e corretta
def inserisci_voti():
    n = int(input("Quanti voti vuoi inserire? "))

    voti = []

    for v in range(n):
        while True:
            try:
                voto = int(input("Inserisci voto (0-10): "))
                
                if voto >= 0 and voto <= 10:
                    voti.append(voto)
                    break # esco dal ciclo while
                else:
                    print("Inserire un numero da 0 a 10")
            except ValueError:
                print("Inserire un numero")
                
    return voti


def calcola_media(voti):
    media = sum(voti) / len(voti) # SUM funzione di python
    
    return media


def stampa_promosso():
    print(f"La media dei voti è {media}")
    
    if media >= 6:
        print("Promosso")
    else:
        print("Bocciato")
        
def stampa_analisi_avanzata(voti):
    voto_max = max(voti) # MAX funzione di python
    voto_min = min(voti) # MIN funzione di python
    media = calcola_media(voti)
    sopra_media = 0
    sotto_media = 0
    insufficiente = 0
    
    for voto in voti:
        if voto > media:
            sopra_media +=1
        
        if voto < media:
            sotto_media += 1
            
        if voto < 6:
            insufficiente += 1
            
    print(f"Voto massimo: {voto_max}")
    print(f"voto minimo: {voto_min}")
    print(f"Sopra la media: {sopra_media}")
    print(f"Sotto la media: {sotto_media}")
    print(f"Insufficienti: {insufficiente}")
    
    
voti = inserisci_voti()
media = calcola_media(voti)
stampa_promosso(media)
stampa_analisi_avanzata(voti)