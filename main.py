#Metodo da bisseccao

def f(x):
  return x**3-9.0*x+3.0                      ##Funcao Teste

def bissecao(f,erro,iter):           #f=funcao/ erro=número de casa depois da virgula
                                    #iter=numero maximo de iteracoes
  
  a=float(input("Digite o valor de A do refinamento: "))  #Valor de A do refinamento
  b=float(input("Digite o valor de A do refinamento: "))  #Valor de A do refinamento
  
  FuncaoA=f(a)          #Calcula a funcao A
  FuncaoB=f(b)          #Calcula a funcao B

  if FuncaoA*FuncaoB>0:            #Se o refinamento for invalido apresenta erro
    print("Erro, funcaoAXFuncaoB não é menor que ZERO")
    return (True,None)

  print("k\t\ta\t\t\tb\t\t\tx\t\t FuncaoA\tFuncaoB\t\t FuncaoX\t intervalo\t\n")
  intervalo =abs(b-a)          #Calcula o intervalo em modulo
  x= (a+b)/2.0                 #Funcao de X
  FuncaoX= f(x)

  k=1

  
  print("%d\t%3f\t%3f\t%3f\t%3f\t%3f\t%3f\t%3f" %(k,a,b,x,FuncaoA,FuncaoB,FuncaoX,intervalo))
  
  if intervalo <= erro:        #Se o intervalo for menor que o erro, sai da funcao
    return (False,x)

  k=1           #Comeca o looping com a primeira interacao

  while k<=iter:
    if FuncaoA*FuncaoX>0:
      a=x
      FuncaoA=FuncaoX
    else:
      b=x  
      FuncaoB=FuncaoX

    intervalo =abs(b-a)
    x= (a+b)/2
    FuncaoX= f(x)

    k=k+1

    print("%d \t%3f\t%3f\t%3f\t%3f\t%3f\t%3f\t%3f" %(k,a,b,x,FuncaoA,FuncaoB,FuncaoX,intervalo))

    if (intervalo <= erro):             #Se o intervalo for menor que o erro apresenta a raiz encontrada
      print("\nA raiz é:%3f "% x)
      return (False,x)
    
  print("Maximo de interacoes!")    #Se passar do numero de interacoes, imprime uma mensagem
  return (True,x)                  #e sai do programa

bissecao (f,0.01,50)
