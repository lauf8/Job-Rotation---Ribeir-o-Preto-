string = input("Insira a string que você deseva inverterola") # escreva A cara rajada da jararaca

string_list = list(string) #a função list em py faz com que todos os caracteres formem uma lista, se digitar "olá" por exemplo vai acontcer o seguinte ['o', 'l', 'a']
string_list_invertida = []
for i in reversed(string_list): #aqui eu uso o reversed, mas ele não é para invcerter a string é só a forma que eu conseguir de fazer um for reverso em py
    string_list_invertida.append(i)  # aqui eu faço com que o elemento i seja inserido na ultima posição da lista

string_invertida = "".join(string_list_invertida) # a lista invertida dsa string é transformada novamente em uma string

print(string_invertida)