entrada = input().split()
repete = int(entrada[1])
numero = str(entrada[0])
palavra = ""
soma = 0

for i in range(repete):
  palavra = palavra + numero

while 1:

  tamanho = len(palavra)

  if tamanho == 1:
    break

  for i in range(tamanho):
    soma = soma + int(palavra[i])
  
  palavra = str(soma)
  soma = 0

print(palavra)
