#importa classe bomba de combustivel 
from bomba_de_combustivel import Bomba_combustivel 

#Manipular objeto
objeto_bomba = Bomba_combustivel()
objeto_bomba.setValorLitro(float(input('Infomrar o valor do litro: ')))
objeto_bomba.menu()