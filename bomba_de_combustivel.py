#Classe bomba de combustivel 
class Bomba_combustivel :
    def __init__(self) :
        self.valorLitro = None
        self.qtCombustivel = None 
        
    #get e set de valor do litro
    def getValorLitro(self):
        return self.valorLitro
    def setValorLitro(self, vl):
        self.valorLitro = vl
    
    #get e set de quantidade de combustivel
    def getQtCombustivel(self):
        return self.qtCombustivel
    def setQtCombustivel(self, qt):
        self.qtCombustivel = qt
    
    #Abastecer por valor 
    def abastecer_valor(self):
        valor = float(input('Informe o valor para abastecer: '))
        qt_abastecida = valor / self.getValorLitro()
        return  print('A quantidade abastecida foi ', qt_abastecida, ' litros')
    
    #Abastecer por litro
    def abastecer_litro(self):
        litro = float(input('Informe a quantidade de litros para abastecer: '))
        valor_paga = litro * self.getValorLitro()
        return print('Valor a pagar é R$', valor_paga)
    
    #Alterar valor do litro combustivel
    def alterar_valor_litro (self):
        novo_valor = float(input('Informe o novo valor do litro de combustivel: '))
        return self.setValorLitro (novo_valor)
    
    #Autera quantidade de combustivel na bomba
    def altera_qt_combustivel (self):
        nova_qt = float(input('Informe a quantidade de combustivel para a bomba: '))
        return self.setQtCombustivel (nova_qt)
    
    #Verificar combustivel na bomba
    def verifica_combustivel (self):
        if self.setQtCombustivel <= 0:
            return 'Sem combustivel na bomba!'
        else:
            return 'Combustivel na bomba!'
    
    #menu
    def menu (self):
        print('1 - Abastecer por valor')
        print('2 - Abastecer por litro')
        print('3 - Alterar valor do litro')
        print('4 - Alterar combustivel na bomba')
        print('5 - Verificar se tem combustivel na bomba')
        opcao = int(input('Digite a opcao desejada: '))
        if opcao == 1:
            objeto_bomba.abastecer_valor()
            volta = input('Digite v para voltar ao menu: ')
            if volta == 'v':
                 return objeto_bomba.menu()
            else :
                 return 'Opcao invalida!'
        elif opcao == 2:
            objeto_bomba.abastecer_litro()
            volta = input('Digite v para voltar ao menu: ')
            if volta == 'v':
                 return objeto_bomba.menu()
            else :
                 return 'Opcao invalida!'
        elif opcao == 3:
            objeto_bomba.alterar_valor_litro()
            volta = input('Digite v para voltar ao menu: ')
            if volta == 'v':
                 return objeto_bomba.menu()
            else :
                 return 'Opcao invalida!'
        elif opcao == 4:
            objeto_bomba.altera_qt_combustivel()
            volta = input('Digite v para voltar ao menu: ')
            if volta == 'v':
                 return objeto_bomba.menu()
            else :
                 return 'Opcao invalida!'
        elif opcao == 5:
            print(objeto_bomba.verifica_combustivel())
            volta = input('Digite v para voltar ao menu: ')
            if volta == 'v':
                 return objeto_bomba.menu()
            else :
                 return 'Opcao invalida!'
    

#Manipular objeto
objeto_bomba = Bomba_combustivel()
objeto_bomba.setValorLitro(float(input('Infomrar o valor do litro: ')))
objeto_bomba.menu()
        
    