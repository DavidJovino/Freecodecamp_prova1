def arithmetic_arranger(problems, solve = False): #adicionando arg como true ou false

  linha1x = ""
  linha2x = ""
  linha3x = ""
  resultadox = ""
  solucao = ""

#==== Separando os valores para começar o programa e testar os erros =======
  for  valor in problems:
# ['n1' '+' 'n2'] Separando
      operador = valor.split(" ")
      n1 = operador[0]
      sinal = operador[1]
      n2 = operador[2]

  #======== testando os possíveis erros (tem que testar 4 erros)============
      # teste: não pode ser mais que 4 digitos
      if len(n1) > 4 or len(n2) > 4:
        return "Error: Numbers cannot be more than four digits."

      # teste: tem que ser + ou - apenas
      if sinal not in "-+":
        return "Error: Operator must be '+' or '-'."

      # teste: erro, muitos problemas
      if len(problems) > 5:
        return "Error: Too many problems."

      # teste: apenas numeros
      try:
        int(n1)
        int(n2)
      except:
        return "Error: Numbers must only contain digits."
        
  #========= Começando os calculos do programa e formantando-os =========
  # ajustes contem o tamanho maximo dos numeros para calcular o - e ajustar o sinal.
      soma = ""
      if(sinal == "+"):
        soma = str(int(n1) + int(n2))
      elif(sinal == "-"):
        soma = str(int(n1) - int(n2))

      ajuste = max(len(n1), len(n2)) +2
      linha1 = str(n1).rjust(ajuste)
      linha2 = sinal + str(n2).rjust(ajuste -1)
      linha3 = ""
      resultado = str(soma).rjust(ajuste)

      for s in range(ajuste):
        linha3 += "-"

      if valor != problems[-1]:
        linha1x += linha1 + "    "
        linha2x += linha2 + "    "
        linha3x += linha3 + "    "
        resultadox += resultado + "    "     
      else:
        linha1x += linha1
        linha2x += linha2
        linha3x += linha3
        resultadox += resultado


  if solve: 
    solucao = linha1x + '\n' + linha2x + '\n' + linha3x + '\n' + resultadox
  else:
    solucao = linha1x + '\n' + linha2x + '\n' + linha3x
  return solucao
