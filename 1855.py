entrada = input().split()
tamanho = len(entrada)
aux_list = [] 

for i in range(tamanho):
  aux_list.append(int(entrada[i]))

aux_list.sort()

soma = aux_list[3] - aux_list[0]

print(soma)
