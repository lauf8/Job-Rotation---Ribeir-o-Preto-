num = int(input("Número na sequencia de Finonacci"))
a = 0
b = 1
resposta = ""

lista_finonacci = [0,1]
# a e b são os valores inicias da sequencia de Finonacci 0 1

while b < num: # faz um while até o numero inserido
    soma = a+b
    lista_finonacci.append(soma) #adiciona a lista da equação o numero que foi gerado, para depois haver a comparação
    a = b
    b = soma


for i in lista_finonacci:
    if i == num:
        resposta = "O número está presente na lista de Finonacci"
    else:
        resposta = "O número não está presente na lista de Finonacci"

print(resposta)
print(lista_finonacci)





