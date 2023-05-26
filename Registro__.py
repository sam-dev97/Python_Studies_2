import csv
import tkinter as tk
import funcoes_registro as ff
from funcoes_registro import *
from tkinter import messagebox, ttk

# Criação da interface gráfica da janela principal
janela_principal = tk.Tk()
janela_principal.title('Sistema de Registro')
# Setando o tamanho da janela principal
janela_principal.geometry('350x200')
# Setando uma cor para janela principal
janela_principal.configure(background='#98E6C5')
janela_principal.resizable(width=False, height=False)

# Cores
cor_label = "#98E6C5"

# Label e Entry(text_field) para o nome
label_nome = tk.Label(janela_principal, text='Nome:')
label_nome.place(x=15, y=10)
label_nome.config(bg=cor_label)
entry_nome = tk.Entry(janela_principal, width=44, justify='center')
entry_nome.place(x=65, y=10)

# # Label e Entry(text_field) para e-mail
label_email = tk.Label(janela_principal, text='E-mail:')
label_email.place(x=15, y=45)
label_email.config(bg=cor_label)
entry_email = tk.Entry(janela_principal, width=44,  justify='center')
entry_email.place(x=65, y=45)

# # Label e Entry(text_field) para a idade
label_idade = tk.Label(janela_principal, text='Idade:')
label_idade.place(x=15, y=75)
label_idade.config(bg=cor_label)
entry_idade = tk.Entry(janela_principal, width=5, justify='center')
entry_idade.place(x=65, y=75)

# # Label e Entry(text_field) para a data
label_data = tk.Label(janela_principal, text='Data de cadastro:')
label_data.place(x=125, y=75)
label_data.config(bg=cor_label)
entry_data = tk.Entry(janela_principal, width=16, justify='center')
entry_data.place(x=230, y=75)

# Botão par a ação cadastrar
botao_cadastrar = tk.Button(janela_principal, text='Cadastrar', command=lambda: ff.cadastrar(entry_data, entry_nome, entry_idade, entry_email))
botao_cadastrar.place(x=45, y=100)

# Botão para ação exibir_registros
botao_registros = tk.Button(janela_principal, text='Registros', command=ff.exibir_registros)
botao_registros.place(x=130, y=100)

# Botão para ação apagar_registro
botao_apagar_registros = tk.Button(janela_principal, text='Apagar Registro', command=ff.apagar_registro)
botao_apagar_registros.place(x=215, y=100)

# Barra para pesquisa por nome
label_pesquisa_nome = tk.Label(janela_principal, text="Pesquisa por nome")
label_pesquisa_nome.place(x=45, y=140)
label_pesquisa_nome.config(bg=cor_label)

entry_pesquisa_nome = tk.Entry(janela_principal, width=25)
entry_pesquisa_nome.place(x=160, y=140)

botao_pesquisa_nome = tk.Button(janela_principal, text='Pesquisar', command=lambda: ff.pesquisa_nome(entry_pesquisa_nome))
botao_pesquisa_nome.place(x=150, y=165)

janela_principal.mainloop()
