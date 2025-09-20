import getpass
def verificar(log, vlog, sen, vsen):
    if vlog == log and vsen == sen:
        return "Login e senha estão corretos\nVocê esta logado!"    
    return "Login ou senha incorretos, tente novamente"
        
print("Bem vindo à tela de cadastro")
login = input("Digite o que será seu login: ")
senha = getpass.getpass("Digite o que será sua senha: ")
print("Cadastro realizado com sucesso!\n")

while True:
    print("Bem vindo à tela de login")
    vlogin = input("Digite seu login: ")
    vsenha = input("Digite sua senha: ")
    v = verificar(login, vlogin, senha, vsenha)
    print(v)

    if "corretos" in v:
        break

    sair = input("Deseja tentar novamente (s/n): ")
    print()
    if sair.lower() == "s":
        continue
    else:
        print("Saindo...")
        break
