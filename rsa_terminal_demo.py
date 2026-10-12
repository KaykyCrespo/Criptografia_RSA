#importando para funcionar os cálculos matemáticos (números mínimos e maximos)
import io
import math 

# importando para conseguir randomizar números (números aleatórios)
import random


msg = input("Escreva a mensagem que deseja criptografar: ")
msgCifrada = []
msgCifradaTemp = []
msgDecifrada = []
msgDecifradaTemp = []
n,d,e,m = None,None,None,None

#função para o número primo
#num seria o número máx
# ex num = 100, todos os números primos de 1 à 100 e escolher um primo
def sort_prime(num):
    prime_num1 = []
    prime_num2 = [True] * (num + 1)
    for i in range(2, num + 1):
        if prime_num2[i]:
            prime_num1.append(i)
            for j in range(2, int(num / i) + 1):
                prime_num2[i * j] = False
    return prime_num1


#função para um número aleatório
def get_random_int(min, max):
    min = math.ceil(min)
    max = math.floor(max)
    return math.floor(random.random() * (max - min + 1)) + min

#MDC (máximo divisor comum)
#números primos entre si possuim apenas o 1 como divisor comum
def mdc(x,y):
    while(y) :
        t=y
        y=x%y
        x=t
    return x


#
def modInverse(a, m):
    for x in range(1, m):
        if ((a % m) * (x % m)) % m == 1:
            return x

primos = sort_prime(300)

#dois números aleatórios dentro dos primos do range do número máximo de primos
#usando a função get randown do import
#- 60 para remover o 2 e 3, pois são 62 primos
p = primos[get_random_int(len(primos)-60,len(primos))]
q = primos[get_random_int(len(primos)-60,len(primos))]



# multiplicar os primos (N)
n = p*q

#Co-primo (M)
m = (p-1)*(q-1)

tempE = 0
temp=(get_random_int(1,m))
e=0
while(e==0) :
  tempE = mdc(temp,m)
  if tempE==1 : e = temp
  else : temp=(get_random_int(1,m))

d = modInverse(e,m)

print('\n')
print("As variáveis são: ")
print("p:",p)
print("q:",q)
print("n:",n)
print("m:",m)
print("e:",e)
print("d:",d)
print('\n')




#Transformou a mensagem de bytes para utf-8
strBytes = bytes(msg, 'utf-8')
for byte in strBytes:
    msgCifradaTemp.append(byte)

print('mensagem convertida para bytes: ')
print(msgCifradaTemp)

for index in range(len(msgCifradaTemp)):
  temp = pow(msgCifradaTemp[index],e)
  temp2 = temp % n
  msgCifrada.append(temp2)

print('\n')
print('mensagem criptografada: ')
print(msgCifrada)








public = n, p
privada = n,d


for index in range(len(msgCifrada)):
  temp = pow(msgCifrada[index],e)
  temp2 = temp % n
  msgDecifradaTemp.append(pow(msgCifrada[index],d) % n)

  
print('\n')
print('mensagem decriptografada: ')
print(msgDecifradaTemp)

msgDecifrada = bytes(msgDecifradaTemp)

for i in range(len(msgDecifradaTemp)):
    msgDecifrada.append(str(msgDecifradaTemp[i],'utf-8'))


print('\n')
print("mensagem traduzida: ")
print(msgDecifrada)