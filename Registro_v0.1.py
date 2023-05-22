import csv
import tkinter as tk
from tkinter import messagebox

# Função para salvar os registros efetuados
def salvar_registro(nome, idade, email):
    # Abrindo o arquivo CSV que contem as informações de registro
    with open('registros1.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([nome, idade, email])
    # Exibe uma mensagem quando algum usuário é registrado(apenas para confirmar mesmo)
    messagebox.showinfo('Registro', 'Usuário registrado com sucesso!')

# Exibe os registros existentes
def exibir_registros():
    # Abrindo o arquivo CSV que contem as informações de registro
    with open('registros1.csv', mode='r') as file:
        reader = csv.reader(file)
        registros = list(reader)
    # Condicioinal + list comprehensionzinha básica para checar/imprimir os registros existentes
    if registros:
        mensagem = '\n'.join([f'Nome: {registro[0]} |||| Idade: {registro[1]} |||| Email: {registro[2]}' for registro in registros])
    else:
        # Se não tiver nada registrado, o que estiver abaixo será exibido posterior mente como msg de erro
        mensagem = 'Nenhum registro encontrado.'
    # Chamada da msg de erro apenas com uma "infobox"
    #messagebox.showinfo('Registros', mensagem)
    # Criando uma janela para exibir as informações, anters com messagebox o tamanho deixava feio
    janela_registros = tk.Toplevel()
    janela_registros.title("Registros")
    janela_registros.geometry("500x150")
    # Não permitir alteração no tamanho da janela com as informações
    janela_registros.resizable(width= False, height=False)
    # Pequeno título
    label_registros = tk.Label(janela_registros, text= "Registros:")
    label_registros.pack()
    # Informações de registro
    label_registros_2 = tk.Label(janela_registros, text= mensagem, justify='left')
    label_registros_2.pack()
    # Botão para fechar a janela de exibição de registros
    botao_fechar_registros = tk.Button(janela_registros, text="Fechar", command=janela_registros.destroy)
    botao_fechar_registros.pack()

# Função para inserir o registro
def cadastrar():
    # Aqui coletamos o conteúdo das text_box para adicionarmos no arquivo de registro
    nome = entry_nome.get()
    idade = entry_idade.get()
    email = entry_email.get()
    # Checando se existe algo escrito nos campos nome e idade, o registro deve ser completo
    if nome and idade and email:
        salvar_registro(nome, idade, email)
        entry_nome.delete(0, tk.END)
        entry_idade.delete(0, tk.END)
        entry_email.delete(0, tk.END)
    else:
        # showwarning exibe uma mensagem de "aviso" alertando que tem falta alguma informação
        messagebox.showwarning('Campos vazios', 'Por favor, preencha todos os campos.')
        
# Aqui deu um trabalho da peste, mas no fim brilhei
# Função para apagar algum registro
def apagar_registro():
    # Abrindo o arquivo CSV que contem as informações de registro
    with open('registros1.csv', mode='r') as file:
        reader = csv.reader(file)
        registros = list(reader)
    # Tradução literal: Se existirem registros...
    if registros:
        # Exibindo uma caixa de diálogo com a lista de registros para o usuário escolher qual excluir
        # Odeio list comprehension, que fique claro
        opcoes = [f'Nome: {registro[0]}, Idade: {registro[1]}, E-mail: {registro[2]}' for registro in registros]
        escolha = tk.StringVar()  # Armazena temporatiamente a escolha do usuário
        escolha.set(opcoes[0])  # Definindo o valor padrão da escolha como o primeiro registro(**spoiler: não funcionou) 

        # Criando uma janela para exibir a lista de registros
        janela = tk.Toplevel()
        janela.title('Excluir Registro')

        # Criando uma list box com as opções de registros
        lista_registros = tk.Listbox(janela, height=10)
        # Insere ao final da lista as opções de registro
        for opcao in opcoes:
            lista_registros.insert(tk.END, opcao)
        lista_registros.pack()

        def confirmar_exclusao():
            # Obtendo o índice do registro selecionado
            indice = lista_registros.curselection()[0]
            # Obtendo o registro selecionado
            registro_selecionado = registros[indice]
            # Removendo o registro da lista
            registros.pop(indice)

            # Sobrescrevendo o arquivo CSV com os registros atualizados
            with open('registros1.csv', mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(registros)

            janela.destroy()  # Fecha a janela de seleção de registros
            messagebox.showinfo('Registro Removido', f'O registro {registro_selecionado} foi removido com sucesso!')

        # Botão para confirmar a exclusão
        botao_confirmar = tk.Button(janela, text='Confirmar', command=confirmar_exclusao)
        botao_confirmar.pack()
        # Essa bobagem mantem a janela aberta
        janela.mainloop()

    else:
        messagebox.showinfo('Nenhum Registro', 'Nenhum registro encontrado para exclusão.')

# Criação da interface gráfica da janela principal
janela_principal = tk.Tk()
janela_principal.title('Sistema de Registro')
# Setando o tamanho da janela principal
janela_principal.geometry('350x150')
# Setando uma cor para janela principal
janela_principal.configure(background='#98E6C5')

# Label e Entry(text_field) para o nome
label_nome = tk.Label(janela_principal, text='Nome:')
label_nome.place(x=15, y=10)
label_nome.config(bg='#98E6C5')
entry_nome = tk.Entry(janela_principal, width=30, justify='center')
entry_nome.place(x=65, y=10)


# # Label e Entry(text_field) para a idade
label_idade = tk.Label(janela_principal, text='Idade:')
label_idade.place(x=260, y=10)
label_idade.config(bg='#98E6C5')
entry_idade = tk.Entry(janela_principal, width=5, justify='center')
entry_idade.place(x=300, y=10)

# # Label e Entry(text_field) para e-mail
label_email = tk.Label(janela_principal, text='E-mail:')
label_email.place(x=15, y=45)
label_email.config(bg='#98E6C5')
entry_email = tk.Entry(janela_principal, width=44,  justify='center')
entry_email.place(x=65, y=45)

# Botão par a ação cadastrar
botao_cadastrar = tk.Button(janela_principal, text='Cadastrar', command=cadastrar)
botao_cadastrar.place(x=45, y=80)

# Botão para ação exibir_registros
botao_registros = tk.Button(janela_principal, text='Registros', command=exibir_registros)
botao_registros.place(x=130, y=80)

# Botão para ação apagar_registro
botao_apagar_registros = tk.Button(janela_principal, text='Apagar Registro', command=apagar_registro)
botao_apagar_registros.place(x=215, y=80)

janela_principal.mainloop()
