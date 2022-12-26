Distancia=float(input("Escriba su distancia en metros: "))

if (Distancia>0):
    
    pies=((Distancia*100)/2.54/12)
    
    print(Distancia, "metros son", pies, "pies")
    
else:
    
    print(" Ponga valores validos")