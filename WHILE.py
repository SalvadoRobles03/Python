

Entra="SI"

while(Entra=="SI"):
    nfl=input("49er, acerero o vaquero: ")
    nfl=nfl.lower()
    nfl=nfl.strip()
    if (nfl=="49er"):
        print("Tu si sabes")
        Entra = "NO"
    else:
        print ("Te quedarás eternamente hasta que veas la luz")
        print("-----------------------------------------")

print("Tortuguita ve a casa")