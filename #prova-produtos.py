#cadastros de produtos

class produtos:

 def  init_ (self, codigo, nome, preço, quantidade):
self.codigo = codigo
self.nome = nome
self.preço = preço
self.quantidade = quantidade

def __str__(self):
    return f"codigo:{self,codigo}nome:{self,nomo}preço:R${self,preço:.4f}quantidade{self,quantidade}"
    def iniciar_cadastro():
        produtos =[]
        while true:
            codigo = input("digite o codigo do produto:")
            nome =input("digite o nome do produto:")
            preço = float(input("digite o preço do produto:"))
            quantidade =int(input("digite a quantidade do produto"))
            produto = produto(codigo, nome, preço,quantidade)
            produto.append("produto")
            continua = input("deseja cadastra outro produto?"(s/n):)
            if continuar .lower()!"s":
break
return produtos
def exibir_produtos(produto):
print("\n produtos cadastrados:")
    for produtos in produtos
    print (produtos)
    #executar o prcesso de cadastro do produtos
    produtos_cadastrados = iniciar_cadastro()
    exibir_produtos(produtos_cadastrados)

#cadastro de cliente 
def iniciar_cadastro():
    cadastro = ()
    #coleta dos dados do usuario
def menu_pricipal
    cadastro["nome"]=input("digite o seu nome")
    cadastro["cpf"]=int(input("digite aqui seu cpf:"))
    cadastro["e-mail"]=input("digite seu e-mail:")
    return cadastro
def exibir_cadastro(cadastra):
    print("dados cadastrados")
    for chave , valor ,in cadastro.item():
        print(f"chave.capitulização(){valor}")
#executar o  cadastro 
    cadastro_usuario = iniciar_cadastro ()
     exibir_cadastro=cadastro_usuario ()
     
#cadastro dos vendedores
import sqlite3
from tkinter import Tk, Label, Entry,Button, messagebox

def get_db_connection():
    conn=sqlite3.connect('verdedores.db')
    conn.row_factory=sqlite3.Row return conn
    #função para cria uma tabela de vendedores

def creat_table():
    conn= get_db_connection()
    conn.execute ("create table in not exists vendedores(id integer primary  key autoincrement, nome ,text not null, email text not null, telefone text not null)")
    conn.commit()
    conn.close()

    #função para cadastrar um novo vendedor
def cadastra_vendedores():
    nome=entry_nome.get()
    email=Entry_email.get()
    telefone=Entry_telefone.get()

if  nome and email and telefone:
    conn=get_db_connection()
    conn.execute("insert into vendedores(nome ,telefone ,email)values(? , ? , ?)"):
    (nome , email , telefone)
    conn.commit()
    conn.close()
    messagebox.showinfo("sucesso, vendedores cadastrado com sucesso!")
    entry_nome.delete(0 , and)
    entry_email.delete(0 , and)
    Entry_telefone.delete(0 , and)
else:
        messagebox.showinfo("error por favor preencha todos os campos,")

    # cofiguração
    root=tk()
    root=title("cadastro de vendedores")
    Label(root text="nome").grid(row=0,colunn=0,padx=10,pady=10)
    Label(root, text="email").grid(row=1,colunn=0,padx=10,pady=10)
    Label(root,text= "telefone").grid(row=2,column=0,padx=10,pady=10)   
    entry_nome=Entry(root)
    entry_nome.grid(row=0,column=1,padx=10,pady=10)
    entry_email=Entry(root)
    entry_email.grid(root=1,column=1,padx=10,pady=10)
    Entry_telefone=Entry(root)
    Entry_telefone.grid(row=2,column=1,padx=10,pady=10)

    bottom(root,text="cadastra",connand=cadastra_vendedores).grid(row=3,colunn=0,colunnspan=2,pady=10



