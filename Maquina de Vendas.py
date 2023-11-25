##Aluno: Carlos Morciani
##Curso: Ciência da Computação

##Função para Imprimir Matriz
def matriz_impressa(matriz,linha_range,coluna_range):
    for linha in range(linha_range):
        for coluna in range(coluna_range):
            print(f"[{matriz[linha][coluna]:^10}]", "",  end="")
        print()


##Função para efetuar o pagamento
def pagamentos(entradas_valores, linha_matriz, coluna_matriz):
    print("Notas permitidas: \nR$ 2.00\nR$ 5.00\nR$ 10.00\nR$ 20.00\nR$ 50.00\nR$ 100.00\nR$ 200.00")
    pagamento = float(input("Coloque o dinheiro:"))
    if pagamento in notas_permitidas:
        for total_pago in range(entradas_valores):
            if pagamento >= matriz_produtos[linha_matriz][coluna_matriz]:
                break
            else:
                novo_pagamento = float(input("Insira um novo valor:"))
                pagamento += novo_pagamento
                print("Valor inserido: {}".format(pagamento))
        
        trocos(pagamento,matriz_produtos[linha_matriz][coluna_matriz],matriz_troco)
        matriz_produtos[linha_matriz][3] -= 1
        
    elif matriz_produtos[linha_matriz][3] == 0:
        print("A bebida não está disponível, por favor outra bebida")
        matriz_impressa(matriz_produtos,6,4)
            
        
    else:
        print("Valor Inválido, tente novamente")


##Função para o Troco
def calculo_trocos(valor_pagamento,valor_produto):
    troco = valor_pagamento - valor_produto
    troco_certo = round(troco, 2)
    print("O troco é: ", troco_certo)
    return troco_certo
    

##Função para contar as moedas e diminuir na matriz do estoque de troco
def contar_nota_moeda(troco_certo, matriz_troco):
    notas_moedas = [100, 50, 20, 10, 5, 2, 1, 0.50, 0.25, 0.10, 0.05, 0.01]
    contador_notas = {}
    
    for notas in  notas_moedas:
        if notas > 0:
            qtd_notas = troco_certo // notas
            if notas == 0.01:
                qtd_notas = troco_certo / notas
        
        
        if qtd_notas > 0:
            contador_notas[notas] = int(qtd_notas)
            total_notas = notas * int(qtd_notas)
            troco_certo -= total_notas
            troco_certo = round(troco_certo, 2)  

            ##Parte responsável por fazer a diminuição do estoque de trocos 
            if notas == 100:
                matriz_troco [1][11] -= int(qtd_notas)
            elif notas == 50:
                matriz_troco [1][10] -= int(qtd_notas)
            elif notas == 20:
                matriz_troco [1][9] -= int(qtd_notas)
            elif notas == 10:
                matriz_troco [1][8] -= int(qtd_notas)
            elif notas == 5:
                matriz_troco [1][7] -= int(qtd_notas)
            elif notas == 2:
                matriz_troco [1][6] -= int(qtd_notas)
            elif notas == 1:
                matriz_troco [1][5] -= int(qtd_notas)
            elif notas == 0.50:
                matriz_troco [1][4] -= int(qtd_notas)
            elif notas == 0.25:
                matriz_troco [1][3] -= int(qtd_notas)
            elif notas == 0.10:
                matriz_troco [1][2] -= int(qtd_notas)
            elif notas == 0.05:
                matriz_troco [1][1] -= int(qtd_notas)
            elif notas == 0.01:
                matriz_troco [1][0] -= int(qtd_notas)
                               
    return contador_notas
    


##Definição da função trocos
def trocos(valor_pagamento,valor_produto, matriz_troco):
    troco_certo = calculo_trocos(valor_pagamento,valor_produto) 
    contador_notas = contar_nota_moeda(troco_certo, matriz_troco)

    for notas, qtd_notas in contador_notas.items():
        if notas > 1:
            print(f"A quantidade total de notas de R$ {notas} é [{qtd_notas}]")
        else:
            print(f"A quantidade total de moedas de R$ {notas} é [{qtd_notas}]")

        
##Inicio da montagem da Máquina de Vendas
print("Bebidas dispóniveis:")
print()


##Comandos permintidos para entrada de produtos e do dinheiro para o pagamento 
notas_permitidas = [2,5,10,20,50,100,200]
produtos = [1,2,3,4,5,6,7]


##Matriz dos produtos ofertados
matriz_produtos = [ ["ID","PRODUTO","VALOR (R$)","ESTOQUE"],
                    ["1","Coca-Cola", 3.75, 2],
                    ["2","Pepsi", 3.67, 5],
                    ["3","Monster", 9.96, 1],
                    ["4","Café", 1.25, 100],
                    ["5","RedBull", 13.99, 2]] 


##Matriz do estoque de troco
matriz_troco = [["R$ 0.01", "R$ 0.05", "R$ 0.10", "R$ 0.25", "R$ 0.50", "R$1.00", "R$ 2.00", "R$ 5.00", 
                "R$ 10.00", "R$ 20.00", "R$ 50.00", "R$ 100.00"],
                [50, 50, 60, 40, 40, 60, 50, 50, 50, 50, 10, 3]]

matriz_impressa(matriz_produtos,6,4)


print() 
print("-"*50)
print()


##Laço de repetição para fazer a maquina operar em loop
maquina = True
contador_pagamento = 0
while maquina: 
    entrada_cliente = int(input("Digite o ID da bebida desejada:"))
    if entrada_cliente in produtos:
    

        ##Coca-Cola
        if entrada_cliente == 1:
            print("Você escolheu: {}".format(matriz_produtos[1][1]))
            if matriz_produtos[1][3] == 0:
                print("Sem estoque, por favor escolha outra bebida".format(maquina))

            else: 
                pagamentos(3, 1,2)
                matriz_impressa(matriz_produtos,6,4)


        ##Pepsi
        if entrada_cliente == 2:
            print("Você escolheu: {}".format(matriz_produtos[2][1]))
            if matriz_produtos[2][3] == 0:
                print("Sem estoque, por favor escolha outra bebida".format(maquina))

            else: 
                pagamentos(2, 2,2)
                matriz_impressa(matriz_produtos,6,4)


        ##Monster        
        if entrada_cliente == 3:
            print("Você escolheu: {}".format(matriz_produtos[3][1]))
            if matriz_produtos[3][3] == 0:
                print("Sem estoque, por favor escolha outra bebida".format(maquina))

            else: 
                pagamentos(5, 3,2)
                matriz_impressa(matriz_produtos,6,4)
        

        ##Café
        if entrada_cliente == 4:
            print("Você escolheu: {}".format(matriz_produtos[4][1]))
            if matriz_produtos[4][3] == 0:
                print("Sem estoque, por favor escolha outra bebida".format(maquina))

            else: 
                pagamentos(5, 4,2)
                matriz_impressa(matriz_produtos,6,4)


        ##RedBull
        if entrada_cliente == 5:
            print("Você escolheu: {}".format(matriz_produtos[5][1]))
            if matriz_produtos[5][3] == 0:
                print("Sem estoque, por favor escolha outra bebida".format(maquina))

            else: 
                pagamentos(8, 5,2)
                matriz_impressa(matriz_produtos,6,4)
        

        ##Implementação do Sistema de Administrador    
        if entrada_cliente == 6:
            entrada_administrador = input("Insira a senha para acessar a Area de Administrador:")
            if entrada_administrador == "admin":
                linha_alteracao = int(input("Insira a linha que deseja alterar:"))
                coluna_alteracao = int(input("Insira a coluna que que deseja alterar:"))
                alteracao = float(input("Coloque o produto que desejado:"))
                matriz_produtos[linha_alteracao][coluna_alteracao] = alteracao
                matriz_impressa(matriz_produtos,6,4)
            else:
                print("Senha Inválida")
                print("Acesso Negado")
                print()
                matriz_impressa(matriz_produtos,6 ,4)
                
        

        ##Comando para imprimir a Matriz de trocos atualizada
        if entrada_cliente == 7:
            print("O estoque atual de trocos é:")
            matriz_impressa(matriz_troco,2,12)

    
    else:
        print("Produto Indispónivel, tente novamente")
        matriz_impressa(matriz_produtos,6 ,4)
        
##Aluno: Carlos Morciani
##Curso: Ciência da Computação