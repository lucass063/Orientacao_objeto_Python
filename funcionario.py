#classe funcionario
class Funcionario :
    def __init__ (self):
        self.nome = None
        self.login = None
        self.senha = None
        self.salario = None
        
    #get e set de nome 
    def getnome (self):
        return self.nome
    def setNome(self, funcionario):
        self.nome = funcionario
    
    #get e set de login
    def getlogin (self):
        return self.login
    def setLogin(self, usuario):
        self.login = usuario
    
    #get e set de senha
    def getsenha (self):
        return self.senha
    def setSenha(self, senha1):
        self.senha = senha1
    
    #get e set de salario
    def getsalario (self):
        return self.salario
    def setSalario(self, salario1):
        self.salario = salario1
    
    #validar login
    '''
    Login : usuario
    Senha : 12345
    '''
    def validar_login (self):
        if self.login == 'usuario' and self.senha == 12345 :
            return True
        else :
            return False
        
    #calcular IRPF
    def calcular_IRPF (self):
             if self.salario <= 2500 :
                 return 'Insento'
             else :
                 salario_irpf = self.salario
                 return  (15 * salario_irpf ) / 100
    
    #aumentar salario
    def aumentar_salario (self):
             porcento_salario = int(input('Porcentual para aumento do salario: '))
             return self.setSalario ( self.getsalario() + (self.getsalario()*porcento_salario/100))
         
    #auterar senha
    def auterar_senha (self):
                self.senha = int(input('Digite a nova senha: '))
                return 'Senha auterada com sucesso!'
    #Mostrar dados
    def mostrar_dados (self):
          print('Nome: ', self.nome)
          print('Login: ', self.login)
          print('Senha: ', self.senha)
          print('Salario: ', self.salario)
          print('IRPF: ', objeto_funcionario.calcular_IRPF())
    
    #Menu 
    def menu (self):
        print('1 - Aumentar Salario')
        print('2 - Auterar Senha')
        print('3 - Mostrar IRPF')
        print('4 - Mostrar Dados')
        opcao = int(input('Digite a opcao desejada: '))
        if opcao == 1 :
             objeto_funcionario.aumentar_salario()
             volta = input('Digite v para voltar ao menu: ')
             if volta == 'v':
                 return objeto_funcionario.menu()
             else :
                 return 'Opcao invalida!'
        elif opcao == 2 :
            objeto_funcionario.auterar_senha()
            volta = input('Digite v para voltar ao menu: ')
            if volta == 'v':
                return objeto_funcionario.menu()
            else :
                return 'Opcao invalida!'
        elif opcao == 3 :
            print('IRPF: ', objeto_funcionario.calcular_IRPF())
            volta = input('Digite v para voltar ao menu: ')
            if volta == 'v':
                return objeto_funcionario.menu()
            else :
                return 'Opcao invalida!'
        elif opcao == 4 :
             objeto_funcionario.mostrar_dados()
             volta = input('Digite v para voltar ao menu: ')
             if volta == 'v':
                 return objeto_funcionario.menu()
             else :
                 return 'Opcao invalida!'
        else :
             return 'Opcao invalida!'
   
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