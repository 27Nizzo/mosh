#range function serve para gerar uma sequencia de numeros

numbers = range(5)
print(numbers)
#com isto obtemos o output: range(0,5), outra forma:

numbers2 = range(5)
for number in numbers2: 
    print(number)
#nesta forma obtemos o output de 0 a 4, ou seja, range(n) vai de 0 até n-1
#outra forma de usar range

numbers3 = range(5,10) #desta vez vai de 5 até 10-1 = 9 
for number in numbers3:
    print(number)

#se quisermos saltar de x em x numero(como na função enumFromThenTo em PF) podemos utilizar a função range da 
    #seguinte forma:

numbers4 = range(0,10,2) # ou seja, isto vai de zero até 9 de dois em dois 
for number in numbers4:
    print(number) 