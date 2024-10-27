import customtkinter as ctk
from tkinter import ttk
from tkinter import messagebox
import tkinter
import modulo_arquivar as arquivar

# Lista de cupons disponíveis (será preenchida pelo loop)
cupom_disponivel = []

# Função principal de venda por cupom
def venda_por_cupom(lista_dados):
    lista_itens = []
    lista_info = []
    cupom_disponivel.clear()
    # Preenchendo `cupom_disponivel` com números de cupom disponíveis
    for dado in lista_dados:
        cupom_disponivel.append(str(dado[0]))  # Adiciona o número do cupom

    # Criando a janela principal
    janela = ctk.CTkToplevel()
    janela.title("VENDA CUPOM")
    janela.geometry('800x600')
    janela.focus_force()
    janela.grab_set()

    # Configuração dos frames
    frame_master = ctk.CTkFrame(janela)
    frame_master.pack(padx=10, pady=10)
    frame1 = ctk.CTkFrame(frame_master)
    frame1.grid(row=0, column=0)

    # Configuração da interface
    ctk.CTkLabel(frame1, text="CNPJ ").grid(row=0, column=0, padx=20, sticky="w")
    ctk.CTkLabel(frame1, text="Empresa ").grid(row=0, column=1, padx=20, sticky="w")
    ctk.CTkLabel(frame1, text="Cliente").grid(row=0, column=2, padx=20, sticky="w")

    cnpj_entry = ctk.CTkEntry(frame1, width=160, font=('Ariel', 18))
    cnpj_entry.grid(row=1, column=0, padx=20)

    empresa_entry = ctk.CTkEntry(frame1, width=330, font=('Ariel', 16))
    empresa_entry.grid(row=1, column=1, padx=20)

    cliente_entry = ctk.CTkEntry(frame1, width=160, font=('Ariel', 16))
    cliente_entry.grid(row=1, column=2, padx=20)

    frame_2 = ctk.CTkFrame(frame_master)
    frame_2.grid(row=2, column=0)

    ctk.CTkLabel(frame_2, text="Valor Cupom R$").grid(row=2, column=0, padx=20, sticky="w")
    ctk.CTkLabel(frame_2, text="Data da Compra").grid(row=2, column=1, padx=20, sticky="w")
    ctk.CTkLabel(frame_2, text="Operador").grid(row=2, column=2, padx=20, sticky="w")
    ctk.CTkLabel(frame_2, text="N° Cupom").grid(row=2, column=3, padx=20, sticky="w")

    valor_entry = ctk.CTkEntry(frame_2, width=110)
    valor_entry.grid(row=3, column=0, padx=20)

    data_entry = ctk.CTkEntry(frame_2, width=200)
    data_entry.grid(row=3, column=1, padx=20)

    usuario_entry = ctk.CTkEntry(frame_2, width=200)
    usuario_entry.grid(row=3, column=2, padx=20)
    
    # ComboBox para selecionar o número do cupom
    cupom_var = ctk.StringVar(value="1001")
    cupom_combobox = ctk.CTkComboBox(frame_2, values=cupom_disponivel, variable=cupom_var, width=100, font=('Ariel', 16))
    cupom_combobox.grid(row=3, column=3, padx=20)

    frame_botoes = ctk.CTkFrame(frame_master)
    frame_botoes.grid(row=4, column=0)

    # Botões
    ctk.CTkButton(frame_botoes, text="PESQUISAR", command=lambda: pesquisar_cupom(cupom_var, lista_dados, cnpj_entry, empresa_entry, cliente_entry, valor_entry, data_entry, usuario_entry, tree)).grid(row=4, column=0, padx=20, pady=20)
    ctk.CTkButton(frame_botoes, text="IMPRIMIR", command=lambda: imprimir_cupom(lista_info, lista_itens)).grid(row=4, column=1, padx=20, pady=20)
    ctk.CTkButton(frame_botoes, text="SAIR", command=janela.destroy, fg_color='red').grid(row=4, column=2, padx=20, pady=20)

    # Configuração da Treeview para exibir os itens
    tree = ttk.Treeview(frame_master, columns=("ITEM", "EAN", "Descrição", "Qtd", "Valor"), show='headings', height=20)
    tree.heading("ITEM", text="ITEM")
    tree.heading("EAN", text="EAN")
    tree.heading("Descrição", text="Descrição")
    tree.heading("Qtd", text="Qtd")
    tree.heading("Valor", text="Valor")

    tree.column("ITEM", anchor=tkinter.CENTER, width=90)
    tree.column("EAN", anchor=tkinter.CENTER, width=200)
    tree.column("Descrição", anchor=tkinter.CENTER, width=400)
    tree.column("Qtd", anchor=tkinter.CENTER, width=80)
    tree.column("Valor", anchor=tkinter.CENTER, width=150)

    tree.grid(row=6, column=0, columnspan=5, padx=20, pady=20)

    janela.wait_window()

# Função para imprimir o cupom
def imprimir_cupom():
    informacao = '\n'  # Composição da string formatada de dados de venda
    
    if lista_info:
        informacao += f"Razão Social: {lista_info[0]}\n"
        print(informacao)
        print(lista_itens)
    else:
        print("Erro: lista_info está vazia ou não foi preenchida corretamente.")
# Função para pesquisar cupons e preencher campos


def pesquisar_cupom(cupom_var, lista_dados, cnpj_entry, empresa_entry, cliente_entry, valor_entry, data_entry, usuario_entry, tree):
    tree.delete(*tree.get_children())
    cupom_select = int(cupom_var.get())
    print(f"Cupom selecionado: {cupom_select}")
    
    for dado in lista_dados:
        if dado[0] == cupom_select:
            lista_info = dado
            print(f"Lista info: {lista_info}")
            
            cnpj_entry.delete(0, 'end')
            cnpj_entry.insert(0, lista_info[4])
            empresa_entry.delete(0, 'end')
            empresa_entry.insert(0, lista_info[5])
            cliente_entry.delete(0, 'end')
            cliente_entry.insert(0, lista_info[3])
            valor_entry.delete(0, 'end')
            valor_entry.insert(0, lista_info[2])
            data_entry.delete(0, 'end')
            data_entry.insert(0, lista_info[1])
            usuario_entry.delete(0, 'end')
            usuario_entry.insert(0, lista_info[6])
            break

    lista_itens = arquivar.lista_item_por_carrinho(cupom_select)
    print(f"Itens do cupom {cupom_select}: {lista_itens}")

    for item in lista_itens:
        tree.insert('', 'end', values=(item[1], item[3], item[4], item[5], f"{item[7]:.2f}"))

    return lista_info, lista_itens
