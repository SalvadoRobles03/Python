#Diccionario={key1:value1, key2:value2}

#LISTA
mascolista=[["Sofi",3,"Blanca","NO"],["Lucifer",5,"Negro","NO"],["Duke",10,"Café","SI"],["messi",2,"Sin color","NO"]]

print(mascolista[1][0], "es", mascolista[1][2] )


#DICCIONARIO
mascolista2={"Sofi":[3,"Blanca","NO"],"Lucifer":[5,"Negro","NO"],"Duke":[10,"Café","SI"],"messi":[2,"Sin color","NO"]}

print("Lucifer es", mascolista2["Lucifer"][1] )
print(mascolista2["Lucifer"] )




#Pruebas
print("\n**********************")
for i in mascolista2:
    print(i, "pesa", mascolista2[i][0])
    print("\n**********************")
    