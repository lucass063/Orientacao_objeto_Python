#importar classe funcionario
from funcionario import Funcionario

#Manipular objetos
objeto_funcionario = Funcionario()
objeto_funcionario.setNome(input('Digite seu nome: '))
objeto_funcionario.setLogin(input('Login: '))
objeto_funcionario.setSenha(int(input('Senha: ')))
objeto_funcionario.setSalario(float(input('Salario: ')))
if objeto_funcionario.validar_login() :
    objeto_funcionario.menu()
else :
    print('Login ou senha incorretos!')