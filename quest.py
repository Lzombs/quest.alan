#=======================================================================================================
#teste
#=======================================================================================================
n = input("Digite seu nome: ")
print(f"Olá! {n}")

# questoes da primeira lista 
#=======================================================================================================
# exercicio 1 
#=======================================================================================================
# resposta: Um algoritmo é um passo a passo que orienta o computador sobre o que fazer, Ele é essencial no desenvolvimento de software, pois faz o programa funcionar de forma correta e eficiente. # type: ignore

#=======================================================================================================
#exercicio 2
#=======================================================================================================
print("hello programming world")

#=======================================================================================================
#exercicio 3 
#=======================================================================================================
n1=float(input("digite o primeiro numero: "))
n2=float(input("digite o segundo numero: "))
media= (n1+n2) / 2
print (media)

#=======================================================================================================
#exercicio 4 
#=======================================================================================================
num_int= 4
num_real= 4.67
is_true= True
letter= 'L'

print("integer", num_int)
print("real", num_real)
print("boolean", is_true)
print("character", letter)

#=======================================================================================================
#exercicio 5
#=======================================================================================================
num1=float(input("digite um numero: "))
num2=float(input("digite um numero: "))

soma= num1+num2
sub= num1-num2
mult= num1*num2
div=num1/num2
if  num2 !=0 :
    print ("Divisão", div)
else:
   print ("não é possivel dividir por zero")
print("Soma", soma)
print("Subtração", sub)
print("multiplicação", mult)

#=======================================================================================================
#exercicio 6
#=======================================================================================================
pi= 3.14159
raio= float(input("digite o raio do circulo"))
area= pi*raio**2
print("A area do circulo é:", area)

#=======================================================================================================
#exercicio 7 
#=======================================================================================================
pv1=float(input("digite a nota da primeira prova: "))
pv2=float(input("diigite a nota da segunda prova: "))
mediaf= (pv1+pv2)/2
print ("a media das suas provas é:", mediaf)
#=======================================================================================================
#exercicio 8
#=======================================================================================================
h= int(input("digite as horas de viagem(somente horas, digite os minutos abaixo): "))
min= int(input("digite os minutos de viagem: "))
velo_media=float(input("digite a velocidade media em km/h: "))

temp= h + min /60
dist= temp * velo_media
cons= dist/12
print("voce percorreu", dist, "km")
print("durante o percurso o consumo foi de", cons, "litros de combustível")

#=======================================================================================================
#exercicio 9
#=======================================================================================================
nb=int(input("digite um numero: "))
if nb >0 :
    print ("O numero: ", nb, "é positivo")
elif nb == 0:
    print("esse é o numero zero:", nb)
else:   
    print("Esse numero: ", nb, "é negativo")

#=======================================================================================================
#exercicio 10
#=======================================================================================================
nt1=float(input("digite sua primeira nota: "))
nt2=float(input("digite a sua segunda nota: "))
mediaN= (nt1+nt2)/2
if mediaN <=5.9:
    print("voce foi reprovado com media: ", mediaN)
else:
    print("voce foi aprovado com media:", mediaN, "Parabens!!")

#=======================================================================================================
#exercicio 11
#=======================================================================================================
a=float(input("digite um numero: "))
b=float(input("digite um numero: "))
c=float(input("digite um numero: "))
if a> b and a> c:
    print("O maior desses numeros é: ", a)
elif b> a and b> c :
    print("O maior desses numeros é: ", b)
elif c> a and c> b:
    print("O maior desses numeros é: ", c)
else:
    print("Os numeros são iguais")

#=======================================================================================================
#exercicio 12
#=======================================================================================================
sal= int(input("digite o seu salario e descubra o seu aumento: "))
sal15= sal* (15/100)
ns1= sal+sal15
sal10= sal*(10/100)
ns2= sal+sal10
if sal<=1500:
    print("seu aumento foi de: ", sal15, "e seu salrio atual é: ", ns1)
else:
    print("seu aumento foi de: ", sal10, "seu salario atual é: ", ns2)

#=======================================================================================================
#exercicio 13
#=======================================================================================================
L= 1
while L <= 10:
    print(L)
    L += 1

#=======================================================================================================
#exercicio 14
#=======================================================================================================
soma1= 0
for E in range(10):
    nume=float(input(f"digite o {E + 1} numero: " ))
    soma1 += nume
media1= soma1/10
print("a media desses numeros é: ", media1)

#=======================================================================================================
#exercicio 15
#=======================================================================================================
numtab= int(input("Digite um número para ver sua tabuada : "))

print(f"\nTabuada do {numtab}:")

for B in range(1, 11):
    print(f"{numtab} x {B} = {numtab * B}")