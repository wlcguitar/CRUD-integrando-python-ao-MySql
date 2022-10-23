def titulo(txt, linha = True):
    """Função para formatar titulo
    parâmentro txt 
    linha se True adicioana uma linha extra inferior
    """
    x = str(txt).title()
    print("="*40)
    print(x.center(40))
    if linha == True:
        print("="*40)


def leia_int(txt):
    """Função criada para validar um número inteiro
    param: txt convertido para um valor int"""
    while True:
        try:
            n = int(input(txt))
        except ValueError:
            print("Erro!!!Digite um numero inteiro válido.")
        else:
            return n


def menu_opcao(txt):
    while True:
        titulo("1 - Cadastrar\n2 - Ver cadastro\n3 - Deletar\n4 - Sair")
        opcao = leia_int(txt)
        if opcao == 4:
            print("Saindo do sistema...")
            break
        if opcao == 3:
            titulo("Exclusão")
            nome = str(input("Nome: "))
            delete(nome)
        elif opcao == 2:
            titulo("Cadastrados")
            ler_cadastro()
        elif opcao == 1:
            titulo("tela de cadastro.")
            nome = str(input("Nome: ").title().strip())
            sobrenome = str(input("Sobrenome: ").title().strip())
            email = str(input("Email: ").title().strip())
            cadastrar(nome, sobrenome, email)
        else: 
            print("Erro!!!Digite um valor válido.")
 

def ler_cadastro():
    import mysql.connector as mc

    objt_conexao = mc.connect(
        host = "localhost",
        user = "root",
        password = "5028",
        database = "mydatabase"
    )

    cursor = objt_conexao.cursor()
    sql ="SELECT Nome, SobreNome, Email FROM pessoas"
    cursor.execute(sql)
    cadastro = cursor.fetchall()

    c = 1
    for nome, sobrenome, email in cadastro:
        print("{}º Cadastro: {}, {}, {}".format(c, nome, sobrenome, email))
        c+=1
    
    cursor.close()
    objt_conexao.close()

   
def cadastrar(nome, sobrenome, email):
    import mysql.connector as mc

    objt_conexao = mc.connect(
        host = "localhost",
        user = "root",
        password = "5028",
        database = "mydatabase"
    )

    cursor = objt_conexao.cursor()
    
    sql = "INSERT INTO pessoas (Pessoas_id, Nome, SobreNome, Email) VALUES (NULL, %s, %s, %s)"  
    dados = (nome, sobrenome, email)

    cursor.execute(sql, dados)
    objt_conexao.commit()
    print("Cadastro realizado.")

    cursor.close()
    objt_conexao.close()


def delete(nome):
    import mysql.connector  
    #DELETE ==> sql = DELETE FROM pessoas WHERE Nome = nome
    objt_conexão = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "5028",
        database = "mydatabase"
    )

    cursor = objt_conexão.cursor()
    sql = "DELETE FROM pessoas WHERE Nome = '{}'".format(nome)  
        
    cursor.execute(sql)
    objt_conexão.commit()
    
    print("Cadastro deletado.")
    cursor.close()
    objt_conexão.close()


titulo("tela de cadastro", False)
menu_opcao("Digite sua opção: ")
