peso = float(input("Peso: "))
kgOrlbs = input("(K)g Or (L)bs: ")  
if kgOrlbs.upper() == "K":
    convert = peso / 0.45 
    print("Peso em Lbs: " + str(convert) + "lbs")
elif kgOrlbs.upper() == "L":
    convert = peso * 0.45 
    print("Peso em Kg: " + str(convert) + "Kg")
else: 
    print("Tens que inserir os valores corretos!")
