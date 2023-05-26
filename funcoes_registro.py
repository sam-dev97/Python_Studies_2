import csv
import tkinter as tk
from tkinter import messagebox, ttk

def salvar_registro(data, nome, idade, email):
    with open('registros1.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([data, nome, idade, email])

    messagebox.showinfo('Registro', 'Usuário registrado com sucesso!')
    
    
def exibir_registros():
    with open('registros1.csv', mode='r') as file:
        reader = csv.reader(file)
        registros = list(reader)
        
    if registros:
        janela_rg = tk.Toplevel()
        janela_rg.title('Registros')
        janela_rg.geometry("600x250")
            
        tvrg = ttk.Treeview(janela_rg, columns=('data','nome', 'idade', 'email',), show='headings')
         
        tvrg.column('data', minwidth=0, width=90)   
        tvrg.column('nome', minwidth=0, width=200)
        tvrg.column('idade', minwidth=0, width=60)
        tvrg.column('email', minwidth=0, width=300)
        
        tvrg.heading('data', text='DATA')  
        tvrg.heading('nome', text='NOME')
        tvrg.heading('idade', text='IDADE')
        tvrg.heading('email', text='EMAIL')
            
        tvrg.pack()
            
        for (a, b, c, d) in registros:
            tvrg.insert("", 'end', values=(a, b, c, d))
            
        janela_rg.mainloop()
    else:
        messagebox.showwarning('ERROR', 'Não existem registros a serem exibidos.')     
 
 
def cadastrar(entry_data, entry_nome, entry_idade, entry_email):
    nome = entry_nome.get()
    idade = entry_idade.get()
    email = entry_email.get()
    data = entry_data.get()

    if data and nome and idade and email:
        salvar_registro(data, nome, idade, email)
        entry_data.delete(0,tk.END)
        entry_nome.delete(0, tk.END)
        entry_idade.delete(0, tk.END)
        entry_email.delete(0, tk.END)
    else:
        messagebox.showwarning('Campos vazios', 'Por favor, preencha todos os campos.')
        

def pesquisa_nome(entry_pesquisa_nome):
    with open('registros1.csv', mode='r') as file:
        reader = csv.reader(file)
        registros = list(reader)

    nome_pesquisa = entry_pesquisa_nome.get()

    registros_encontrados = [registro for registro in registros if nome_pesquisa in registro[1]]

    def comando_personalizado():
        janela_rg.destroy()
        apagar_registro()
        
    
    if registros_encontrados:
        janela_rg = tk.Toplevel()
        janela_rg.title('Registros')
        janela_rg.geometry("600x250")
            
        tvrg = ttk.Treeview(janela_rg, columns=('data','nome', 'idade', 'email',), show='headings')
         
        tvrg.column('data', minwidth=0, width=90)   
        tvrg.column('nome', minwidth=0, width=200)
        tvrg.column('idade', minwidth=0, width=60)
        tvrg.column('email', minwidth=0, width=300)
        
        tvrg.heading('data', text='DATA')  
        tvrg.heading('nome', text='NOME')
        tvrg.heading('idade', text='IDADE')
        tvrg.heading('email', text='EMAIL')
            
        tvrg.pack()
            
        for (a, b, c, d) in registros_encontrados:
            tvrg.insert("", 'end', values=(a, b, c, d))
            
        janela_rg.mainloop()
    else:
        messagebox.showwarning('ERROR', 'Não existem registros a serem exibidos.')
    
    botao_apagar_2 = tk.Button(janela_rg, text='Apagar Registros', command=comando_personalizado)
    botao_apagar_2.pack()
    
    
def apagar_registro():
    with open('registros1.csv', mode='r') as file:
        reader = csv.reader(file)
        registros = list(reader)

    if registros:
        janela_delete = tk.Toplevel()
        janela_delete.title('Excluir Registros')
        janela_delete.geometry("600x250")
        
        tree = ttk.Treeview(janela_delete, columns=('data', 'nome', 'idade', 'email'), show='headings')
        
        tree.column('data', minwidth=0, width=90)
        tree.column('nome', minwidth=0, width=200)
        tree.column('idade', minwidth=0, width=60)
        tree.column('email', minwidth=0, width=300)
            
        tree.heading('nome', text='NOME')
        tree.heading('idade', text='IDADE')
        tree.heading('email', text='EMAIL')
        
        for (a, b, c, d) in registros:
            tree.insert("", 'end', values=(a, b, c, d))
        
        tree.pack()

        def confirmar_exclusao():
            item_selecionado = tree.selection()[0]
            
            indice_selecionado = int(tree.index(item_selecionado))
            
            registro_selecionado = tree.item(item_selecionado)['values']
            
            registros.pop(indice_selecionado)

            tree.delete(item_selecionado)

            with open('registros1.csv', mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(registros)

            janela_delete.destroy()
            
            messagebox.showinfo('Registro Removido', f'O registro {registro_selecionado} foi removido com sucesso!')
            
        botao_confirmar = tk.Button(janela_delete, text='Deletar registro selecionado', command=confirmar_exclusao)
        botao_confirmar.pack()
    else:
        messagebox.showerror('ERROR', 'NÃO EXISTEM REGISTROS A SEREM APAGADOS!')
    
