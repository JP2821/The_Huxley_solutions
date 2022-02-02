entrada = input().split()
tamanho = len(entrada)
aux_list = [] 

for i in range(tamanho):
  aux_list.append(int(entrada[i]))

a1 = aux_list[0]
a2 = aux_list[1]
b1 = aux_list[1]
b2 = aux_list[0]

print(f'a: {a1} b: {b1}')
print(f'a: {a2} b: {b2}')
