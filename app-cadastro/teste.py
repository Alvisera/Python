import tkinter as tk
from tkinter import messagebox
import mysql.connector

# Função para conectar ao banco de dados
def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="1234",
        database="cadastro_db"
    )

# Função para salvar o usuário
def salvar_usuario():
    nome = entry_nome.get()
    email = entry_email.get()
    senha = entry_senha.get()

    if nome and email and senha:
        try:
            conn = connect_db()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO usuarios (nome, email, senha) VALUES (%s, %s, %s)", (nome, email, senha))
            conn.commit()
            conn.close()
            messagebox.showinfo("Sucesso", "Usuário cadastrado com sucesso!")
        except Exception as e:
            messagebox.showerror("Erro", str(e))
    else:
        messagebox.showwarning("Aviso", "Todos os campos são obrigatórios")

# Configuração da GUI
root = tk.Tk()
root.title("Cadastro de Usuário")

tk.Label(root, text="Nome:").grid(row=0, column=0)
tk.Label(root, text="Email:").grid(row=1, column=0)
tk.Label(root, text="Senha:").grid(row=2, column=0)

entry_nome = tk.Entry(root)
entry_email = tk.Entry(root)
entry_senha = tk.Entry(root, show="*")

entry_nome.grid(row=0, column=1)
entry_email.grid(row=1, column=1)
entry_senha.grid(row=2, column=1)

tk.Button(root, text="Cadastrar", command=salvar_usuario).grid(row=3, column=1)

root.mainloop()