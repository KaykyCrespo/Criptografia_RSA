from js import document
import math
import random

#---------------------CAIO PACHECO---------------------#

msgAviso = document.querySelector("#aviso") #texto com display none que só aparace quando da erro em criptografar
msgAviso2 = document.querySelector("#aviso2") #texto com display none que só aparace quando da erro em descriptografar
criptografada = document.querySelector("#msgCriptografada-primary") #texto da mensagem criptografa
chave_privada = document.querySelector("#chave-privada1") #texto dos dígitos da chave privada em criptografar
chave_publica = document.querySelector("#chave-publica1") #texto dos dígitos da chave pública em criptografar

# FUNÇÃO PARA CRIPTOGRAFAR
def criptografar(event):
    opcaoMarcada = False
    inputRSA = document.querySelector("#rsa") #botão RSA
    
    if (inputRSA.checked):
        opcaoMarcada = True

    mensagemTexto = document.querySelector("#texto-primary") # texto mensagem para encriptografar
    if mensagemTexto.value == "":
        msgAviso.innerText = "ERRO! Digite a mensagem para encriptografar!"
        msgAviso.style.display = "block"
        msgAviso.style.color = "red"
        criptografada.value = ""
        chave_privada.value = ""
        chave_publica.value = ""
        
    elif not opcaoMarcada:
        msgAviso.innerText = "ERRO! Criptografia em desenvolvimento!"
        msgAviso.style.display = "block"
        msgAviso.style.color = "red"
        criptografada.value = ""
        chave_privada.value = ""
        chave_publica.value = ""
    else:
        msgAviso.style.display = "block"
        msgAviso.innerText = "Mensagem criptografada com sucesso!"
        msgAviso.style.color = "#7f8c8d"
        
        msgAviso2.innerText = ""
        msg = mensagemTexto.value        

        chave_privadaVisivel = document.querySelector("#chavePrivadaVisivel") # texto chave privada
        chave_publicaVisivel = document.querySelector("#chavePublicaVisivel") # texto chave pública
        
        chave_privadaVisivel.style.visibility = "visible"
        chave_publicaVisivel.style.visibility = "visible"
        

#---------------------CAIO PACHECO---------------------#




#---------------------KAYKY CRESPO---------------------#

        #CRIPTOGRAFIA
        msgCifrada = []
        msgCifradaTemp = []
        n,d,e,m = None,None,None,None
        
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
        
        #CHAVE PÚBLICA
        # Escolher um número E em que 1 < E < M
        # e seja co-primo de M
        # e onde o MDC M,E = 1, sendo E > 1.
        tempE = 0
        temp=(get_random_int(1,m))
        e=0
        while(e==0) :
            tempE = mdc(temp,m)
            if tempE==1 : e = temp
            else : temp=(get_random_int(1,m))
        
        #CHAVE PRIVADA
        d = modInverse(e,m)
        
        #Transformou a mensagem de bytes para utf-8
        strBytes = bytes(msg, 'utf-8')
        for byte in strBytes:
            msgCifradaTemp.append(byte)
        
        # criptografia em que pega o mod (o resto da divisão) e divide pelo divisor anterior até dar 1
        
        #Dividimos E por M, no nosso exemplo ﬁcaria:
        # 13 : 640 = 0 com resto 13
        # Dividimos o divisor anterior pelo resto:
        #640 : 13 = 49 com resto 3
        # Novamente, dividimos o divisor anterior pelo resto:
        #13 : 3 = 4 com resto 1


        #FUNÇÃO CRIPTOGRAFAR
        for index in range(len(msgCifradaTemp)):
            temp = pow(msgCifradaTemp[index],e)
            temp2 = temp % n
            msgCifrada.append(temp2)
            
        
        #deixando o resultado da criptografia
        criptografada.value = msgCifrada

        chave_privada.value = n ,d
            
        chave_publica.value = n, p

        mensagemTexto.placeholder = "Mensagem para encriptografar"    

#---------------------KAYKY CRESPO---------------------#





#---------------------CAIO PACHECO---------------------#

#função para dar mensagens para o usuário
def exportadados(event):
    
    msgAviso.style.display = "block"
    if chave_publica.value == "" or chave_privada.value == "" or criptografada.value == "":
        msgAviso.style.color = "red"
        msgAviso.innerText = "ERRO! Criptografe uma mensagem para transferir dados!"
    else:
        msgAviso.style.color = "#7f8c8d"
        msgAviso.innerText = "Dados transferidos para descriptografação!"
        criptografadaTexto = str(criptografada.value)
        chave_privadaTexto = str(chave_privada.value)
        chave_publicaTexto = str(chave_publica.value)
        
        chave_privada2 = document.querySelector("#chave-privada2") #texto dos dígitos da chave privada em descriptografar
        chave_privada2.value = chave_privadaTexto
        chave_publica2 = document.querySelector("#chave-publica2") #texto dos dígitos da chave pública em descriptografar
        chave_publica2.value = chave_publicaTexto
        
        criptografada2 = document.querySelector("#msgCriptografada-second") #texto da mensagem descriptografada
        criptografada2.value = criptografadaTexto


#FUNÇÃO PARA DESCRIPTOGRAFAR
def descriptografar(event):
    msgDecifradaTemp = []
    msgDecifrada = []

    mensagem = document.querySelector("#msgDescriptografada-second") #texto da mensagem descriptografada
    chave_privada = document.querySelector("#chave-privada2") #texto dos dígitos da chave privada em descriptografar
    chave_publica = document.querySelector("#chave-publica2") #texto dos dígitos da chave pública em descriptografar
    criptografada = document.querySelector("#msgCriptografada-second") #texto da mensagem criptografada
    opcaoMarcada = False
    inputRSA = document.querySelector("#rsa2")
    inputTWOFISH = document.querySelector("#twofish2")
    inputDES = document.querySelector("#des2")
    inputTLS = document.querySelector("#tls2")
    inputSAFER = document.querySelector("#safer2")


    #USER FRIENDLY
    if (inputRSA.checked):
        opcaoMarcada = True
    
    if chave_privada.value == "" or chave_publica.value == "" or criptografada.value == "":
        msgAviso2.style.display = "block"
        msgAviso2.style.color = "red"
        msgAviso2.innerText = "ERRO! Complete os campos obrigatórios!"
        mensagem.value = ""
    elif mensagem.value == "" and inputRSA.value == "" or inputTWOFISH.value == "" or inputDES.value == "" or inputTLS.value == "" or inputSAFER.value == "":
        msgAviso2.style.display = "block"
        msgAviso2.style.color = "red"
        msgAviso2.innerText = "ERRO! Selecione uma criptografia!"
        mensagem.value = ""
    elif not opcaoMarcada:
        msgAviso2.style.display = "block"
        msgAviso2.style.color = "red"
        msgAviso2.innerText = "ERRO! Criptografia em desenvolvimento!"
        mensagem.value = ""

    else:
        msgAviso2.style.display = "block"
        msgAviso2.style.color = "#7f8c8d"
        msgAviso2.innerText = "Mensagem descriptografada com sucesso!"
        

        #dividir na lista cada número por uma ","
        chave_privada1 = chave_privada.value
        chave_privada2 = chave_privada1.strip("()")
        listaChavePrivada = chave_privada2.split(",") # lista com as 2 chaves privadas (n, d)
        n = int(listaChavePrivada[0]) #atribuindo o primeiro index com n (int) X
        d = int(listaChavePrivada[1]) #atribuindo o segundo index com d (int) X
        
        chave_publica1 = chave_publica.value
        chave_publica2 = chave_publica1.strip("()")
        listaChavePublica = chave_publica2.split(",") # lista com as 2 chaves publicas (n, p)
        p = int(listaChavePublica[1]) #atribuindo o segundo index com d (int) X
        

        #revertendo para uma lista
        criptografada1 = criptografada.value
        criptografada2 = criptografada1[1: -1] #tira cochete da string
        criptografadaLista = criptografada2.split(",") #virou uma lista
        criptografadaLista2 = [int(i) for i in criptografadaLista] #convertendo pra int


#---------------------CAIO PACHECO---------------------#








#---------------------KAYKY CRESPO---------------------#

        #função para o número primo
        #num seria o número máx
        # ex num = 100, todos os números primos de 1 à 100 e escolher um primo
        primos = sort_prime(300)

        #dois números aleatórios dentro dos primos do range do número máximo de primos
        #usando a função get random do import
        #- 60 para remover o 2 e 3, pois são 62 primos  
        q = primos[get_random_int(len(primos)-60,len(primos))]

        #Co-primo (M)
        m = (p-1)*(q-1)

        #CHAVE PÚBLICA
        # Escolher um número E em que 1 < E < M
        # e seja co-primo de M
        # e onde o MDC M,E = 1, sendo E > 1.
        tempE = 0
        temp=(get_random_int(1,m))
        e=0
        while(e==0) :
            tempE = mdc(temp,m)
            if tempE==1 : e = temp
            else : temp=(get_random_int(1,m))



        #DESCRIPTOGRAFAR / faz o inverso da função de criptografar (LINHA 140)
        for index in range(len(criptografadaLista2)):
            temp = pow(criptografadaLista2[index],e)
            msgDecifradaTemp.append(pow(criptografadaLista2[index],d) % n)

        #transformando em bytes
        msgDecifrada = bytes(msgDecifradaTemp)
        msgDecifradaUTF8 = msgDecifrada.decode('utf-8')

        #mostrando aonde mandar a mensagem descriptografada
        mensagem.value = msgDecifradaUTF8
        msgAviso.style.display = "none"



# função para o número primo
# num seria o número máx
# ex num = 100, todos os números primos de 1 à 100 e escolher um primo
def sort_prime(num):
    prime_num1 = []   # lista vazia para armazenar os números primos 
    prime_num2 = [True] * (num + 1) # Lista booleana inicializada com TRUE e tem comprimento num + 1   / Esta lista serve como um rastreador para verificar se um número é primo ou não.
    for i in range(2, num + 1):  # 2 até num
        if prime_num2[i]:    # Se prime_num2[i] é True, isso significa que i é um número primo. 
            prime_num1.append(i)  # O código adiciona i à lista prime_num1.
            for j in range(2, int(num / i) + 1):  # os múltiplos de i para marcá-los como não primos. Ele marca cada múltiplo de i como False na lista prime_num2.
                prime_num2[i * j] = False
    return prime_num1

#função para um número aleatório
def get_random_int(min, max):
    min = math.ceil(min)  # arredonda para cima o valor mínimo, garantindo que o número mínimo seja um número inteiro.
    max = math.floor(max) # arredonda para baixo o valor máximo, assegurando que o número máximo seja um número inteiro.
    return math.floor(random.random() * (max - min + 1)) + min  # "random.random()" gera um número aleatório entre 0 e 1.

# "(max - min + 1)" representa a amplitude do intervalo desejado, adicionando 1 para incluir o próprio limite superior no intervalo.
# "math.floor(random.random() * (max - min + 1))" gera um número inteiro aleatório dentro do intervalo desejado.
# "+ min" é adicionado ao resultado para garantir que o número aleatório gerado esteja no intervalo original especificado por min e max.


#MDC (máximo divisor comum)
#números primos entre si possuim apenas o 1 como divisor comum
def mdc(x,y):
    while(y) :
        t=y
        y=x%y
        x=t
    return x

# 'y' se torna zero, indicando que o MDC foi encontrado e é igual a x.
# t recebe y
# y recebe o resto da divisão de x/y
# x recebe t
# O processo continua até que y seja zero, momento em que o valor atual de x é retornado, representando o máximo divisor comum dos valores originais de x e y.



def modInverse(a, m):
    for x in range(1, m):
        if ((a % m) * (x % m)) % m == 1:
            return x
        
# o número para o qual queremos encontrar o inverso modular e m é o módulo.

# para cada valor de x, ele verifica se o produto de (a % m) e (x % m) quando é feito o módulo m é igual a 1. 
# Isso significa que encontramos o inverso modular de a em relação a m com o valor de x.

        #---------------------KAYKY CRESPO---------------------#