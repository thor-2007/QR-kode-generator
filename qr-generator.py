import qrcode  # Importerer biblioteket for å lage QR-koder
import os      # Importerer biblioteket for å jobbe med filer og operativsystemet

# Lager en nydelig array for å huske alle bildene (filnavnene) vi lager
bilder = []



# Leser inn gamle bilder fra fil hvis den finnes
if os.path.exists("bilder.txt"):  # Sjekker om filen "bilder.txt" finnes i mappen
    with open("bilder.txt", "r") as fil:  # Åpner filen for lesing
        for linje in fil:                 # Går gjennom hver linje i filen
            bilder.append(linje.strip())  # Fjerner linjeskift og legger til i listen



# Funksjon for å lage en QR-kode
def lag_qr():
    data = input("Hva vil du lage QR-kode for? (lim inn en lenke) ")  # Spør brukeren om tekst/lenke
    filnavn = input("Hva vil du at filnavnet skal være?: ")  # Spør om filnavn
    
    print(" ")

    # Her sørger jeg for at filen alltid har .png på slutten sånn at det blir til ett bilde:
    if not filnavn.lower().endswith(".png"):
        filnavn = filnavn + ".png"


    img = qrcode.make(data)     # Lager QR-koden
    img.save(filnavn)           # Lagrer QR-koden som bilde
    bilder.append(filnavn)      # Legger filnavnet til i listen
    print(f"Laget: {filnavn}")


    # Skriver alle filnavnene til "bilder.txt" slik at de huskes neste gang
    with open("bilder.txt", "w") as fil:
        for navn in bilder:
            fil.write(navn + "\n")  # Skriver ett filnavn per linje



# Funksjon for å slette et bilde
def slett_bilde():
    if not bilder:  # Sjekker om den vakre arrayen er tom
        print(" ")
        print("Ingen QR-koder å slette.")
        return
    print(" ")
    print("QR-koder:")
    for i, navn in enumerate(bilder):  # Skriver ut alle bilder med nummer foran
        print(f"{i+1}: {navn}")

    print(" ")
    valg = input("Hvilken QR-kode vil du slette? Skriv nummeret: ")
    try:
        indeks = int(valg) - 1  # Gjør om til tall og tilpasser til liste (starter på 0)
        if 0 <= indeks < len(bilder):  # Sjekker at nummeret er gyldig
            navn = bilder.pop(indeks)  # Fjerner filnavnet fra listen
            if os.path.exists(navn):   # Sjekker om filen faktisk finnes på PC-en
                os.remove(navn)        # Sletter bildefilen fra datamaskinen
                print(f"{navn} er slettet...")
                print(" ")
            else:
                print("Filen finnes ikke.")
            # Oppdaterer "bilder.txt" slik at det slettede bildet ikke står der lenger
            with open("bilder.txt", "w") as fil:
                for n in bilder:
                    fil.write(n + "\n")
        else:
            print("Ugyldig nummer.")  # Hvis brukeren skriver et nummer som ikke finnes
    except ValueError:
        print("Du må skrive et tall.")  # Hvis brukeren ikke skriver et tall



# Funksjon for å åpne et bilde
def apne_bilde():
    if not bilder:  # Sjekker om det finnes noen bilder å åpne
        print(" ")
        print("Ingen QR-koder å åpne.")
        return
    print(" ")
    print("Dine QR-koder:")
    for i, navn in enumerate(bilder):  # Skriver ut alle bilder med nummer foran
        print(f"{i+1}: {navn}")
    
    print(" ")
    valg = input("Hvilken QR-kode vil du åpne? Skriv nummeret: ")
    try:
        indeks = int(valg) - 1  # Gjør om til tall og tilpasser til liste
        if 0 <= indeks < len(bilder):  # Sjekker at nummeret er gyldig
            navn = bilder[indeks]
            if os.path.exists(navn):   # Sjekker at filen finnes
                os.startfile(navn)     # Åpner bildet med standard bildeviser i Windows
            else:
                print("Filen finnes ikke.")
        else:
            print("Ugyldig nummer.")   # Hvis brukeren skriver et nummer som ikke finnes
    except ValueError:
        print("Du må skrive et tall.") # Hvis brukeren ikke skriver et tall



# Hovedmeny som kjører helt til brukeren velger å avslutte
while True:
    print("1: Lag QR-kode")
    print("2: Slett QR-kode")
    print("3: Åpne QR-kode")
    print("4: Avslutt")
    print(" ")


    valg = input("- Velg: ")
    if valg == "1":
        lag_qr()         # Lager en ny QR-kode
    elif valg == "2":
        slett_bilde()    # Sletter et bilde
    elif valg == "3":
        apne_bilde()     # Åpner et bilde
    elif valg == "4":
        print(" ")
        print("Programmet avsluttet...")
        break            # Avslutter programmet
    else:
        print("Ugyldig valg.")  # Hvis brukeren skriver noe annet enn 1, 2, 3 eller 4