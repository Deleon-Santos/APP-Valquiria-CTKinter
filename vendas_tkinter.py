import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
import json
import customtkinter as ctk
from PIL import Image

valor_pagar=0.0

# Funções dos módulos
#import modulo_pagar as pagar
#import modulo_remover as remover
import modulo_pesquisar as pesquisar
#import modulo_cadastro as cadastrar
#import modulo_limpar as limpar
import modulo_adicionar as adicionar
#import modulo_visualisar as visualizar
import modulo_arquivar as arquivar
#import modulo_cpf

def sistema(usuario, data, empresa):
    carrinho = []
    cupom = int(1000)
    valor_pagar = 0
    num_item = 0
    entado= "CAIXA FECHADO"
    cpf = "000.000.000-00"
    cnpj = '45.333.0001/45'
    lista_dados = []

    # ===================================== Inicio da Interface Grafica=========================================
    
    janela = ctk.CTk()
    janela.title("ENTRADA E PEDIDO")
    janela.geometry("1280x700")

    # Configuração inicial do tema visual da interface
    ctk.set_appearance_mode("light")  # Modo de aparência escura
    ctk.set_default_color_theme("dark-blue")  # Tema de cores azul-escuru

    # Menu
    menu_bar = tk.Menu(janela)
    menu_novo = tk.Menu(menu_bar, tearoff=0)
    
    menu_novo.add_command(label="Nova Compra", command=lambda: nova_compra())
    menu_novo.add_command(label="Nova Pesquisa", command=lambda: nova_pesquisa())
    menu_novo.add_command(label="Novo Item", command=lambda: novo_item())
    menu_bar.add_cascade(label="  Novo  ", menu=menu_novo)

    label_titulo = ctk.CTkLabel(janela, text="CAIXA FECHADO", font=("Arial",24,'bold'))
    label_titulo.pack(pady=10,padx=10)
     
    
    menu_totais = tk.Menu(menu_bar, tearoff=0)
    menu_totais.add_command(label="Venda Cupom", command=lambda: venda_cupom())
    menu_bar.add_cascade(label=" Totais ", menu=menu_totais)

    menu_suporte = tk.Menu(menu_bar, tearoff=0)
    menu_suporte.add_command(label="Ajuda", command=lambda: mostrar_ajuda())
    menu_bar.add_cascade(label=" Suporte ", menu=menu_suporte)

    menu_fechar = tk.Menu(menu_bar, tearoff=0)
    menu_fechar.add_command(label="Fechar", command=lambda: janela.quit())
    menu_bar.add_cascade(label=" Fechar ", menu=menu_fechar)

    janela.config(menu=menu_bar)

    # Cupom
    frame_cupon = ctk.CTkFrame(janela)
    frame_cupon.pack(pady= 0, padx=(1200,0))
    
    label_cupom = ctk.CTkLabel(frame_cupon, text="Cupom N°:",font=('Arial',20,'bold'))
    entry_cupom = ctk.CTkEntry(frame_cupon, font=("Arial", 18),width=145,justify= "right")
    
    label_cupom.grid(row=0, column=0, padx=30, pady=0)
    entry_cupom.grid(row=0, column=1, padx=0, pady=0)
    
    #frame principal
    frame_master = ctk.CTkFrame(janela)
    frame_master.pack(padx=10, pady=10)
    
    #frame la esquerdo
    frame_esquerda = ctk.CTkFrame(frame_master)
    frame_esquerda.grid(row=0, column=0, padx=0, pady=0 )

    # Carregar a imagem usando PIL (precisa da biblioteca Pillow)
    image_baner = "tdt.png"
    image = ctk.CTkImage(dark_image=Image.open(image_baner), size=(500, 305))

    # Criar um rótulo (Label) para exibir a imagem
    label = ctk.CTkLabel(frame_esquerda, image=image, text="")  # Definir text como vazio para mostrar apenas a imagem
    label.pack(pady=(18,20))
    
    # Informações do Produto
    frame_inputs = ctk.CTkFrame(frame_esquerda) 
    frame_inputs.pack(pady=0, padx=0)
    
    # declaração de labels de imputs
    frame_inputs_label = ctk.CTkFrame(frame_inputs,width=200,fg_color="transparent")
    frame_inputs_label.grid(row=0, column=0, padx=(0,0), pady=0, sticky="e")

    #declaração de entryes de imputs
    frame_inputs_entry1 = ctk.CTkFrame(frame_inputs,fg_color="transparent")
    frame_inputs_entry1.grid(row=1, column=0, padx=(0,100), pady=0, sticky="w")

    frame_inputs_entry2 = ctk.CTkFrame(frame_inputs,fg_color="transparent")
    frame_inputs_entry2.grid(row=1, column=0, padx=(0,0), pady=0, sticky="e")
    
    # inputs
    label_cod = ctk.CTkLabel(frame_inputs_label, text="Código do Produto",width=150)
    entry_cod = ctk.CTkEntry(frame_inputs_entry1, font=("Arial", 25),width=200)
    label_qtd = ctk.CTkLabel(frame_inputs_label, text="Qtd",width=60) 
    entry_qtd = ctk.CTkEntry(frame_inputs_entry2, font=("Arial", 25),show="1", width=60)
    
    entry_qtd.insert(0, "1")  # Definindo o valor padrão como 1
    label_descricao = ctk.CTkLabel(frame_inputs, text="Descrição do Produto")  
    entry_descricao = ctk.CTkEntry(frame_inputs, font=("Arial", 25),width=500)
    
    button_pesquisar = ctk.CTkButton(frame_inputs_entry1, text="P", command=lambda: nova_pesquisa(),width=30,height=35)
    
    #posicionamento de imputs
    label_cod.grid(row=0, column=0, padx=(0,100), pady=(10,0))
    entry_cod.grid(row=1, column=0, padx=(0,0), pady=0)
    label_qtd.grid(row=0, column=1, padx=(160,0), pady=(10,0))
    entry_qtd.grid(row=1, column=2, padx=(0,0), pady=0)
    label_descricao.grid(row=2, column=0, padx=(0,0), pady=(30,0))
    entry_descricao.grid(row=3, column=0, padx=(0,0), pady=0)
    
    button_pesquisar.grid(row=1, column=1, padx=(10,10), pady=0)

    # Botões
    frame_butons = ctk.CTkFrame(frame_esquerda )
    frame_butons.pack(pady=(15,0), padx= 0)

    button_adicionar = ctk.CTkButton(frame_butons, text="ADICIONAR",font=('Ariel',16,'bold'),height=40, command=lambda: adicionar_item())
    button_deletar = ctk.CTkButton(frame_butons, text="DELETE",font=('Ariel',16,'bold'), height=40, command=lambda: deletar_item())
    button_pagar = ctk.CTkButton(frame_butons, text="PAGAR",font=('Ariel',16,'bold'), height=40, command=lambda: pagar_items())
    button_voltar = ctk.CTkButton(frame_butons, text="VOLTAR", font=('Ariel',16,'bold'),height=40, command=lambda: voltar())
    
    # posicionamento de 4 botões
    button_adicionar.grid(row=0, column=0, padx=(0,110), pady=(15,15))
    button_deletar.grid(row=0, column=1, padx=(108,0), pady=(15,15))
    button_pagar.grid(row=1, column=0, padx= (0,110), pady=(15,0))
    button_voltar.grid(row=1, column=1, padx=(108,0), pady=(15,0))



    # ***COMPONENTES DO FRAME DA DIREITA*** 
    frame_direita = ctk.CTkFrame(frame_master)
    frame_direita.grid(row=0, column=1, padx=0, pady=0)
    
    # Estilo da tabela Treeview
    style = ttk.Style()

    # Configurando o estilo do heading da Treeview
    style.configure("Treeview.Heading", font=("Arial", 14,))  # Aumenta o tamanho da fonte do cabeçalho
    style.configure("Treeview", font=("Arial", 11))  # Configura a fonte dos valores
    
    # Colunas da Tabela
    columns = ["Item", "Cod", "EAN", "Descrição", "Qtd", "PUni R$", "Preço R$"]
    tree = ttk.Treeview(frame_direita, columns=columns, show="headings", height=27)
    
    # Definindo os cabeçalhos e as larguras das colunas
    tree.heading("Item", text="Item",)
    tree.column("Item", anchor=tk.CENTER, width=50)  # Definindo largura para coluna "Item"

    tree.heading("Cod", text="Cod")
    tree.column("Cod", anchor=tk.CENTER, width=100)  # Definindo largura para coluna "Cod"

    tree.heading("EAN", text="EAN")
    tree.column("EAN", anchor=tk.CENTER, width=200)  # Definindo largura para coluna "EAN"

    tree.heading("Descrição", text="Descrição")
    tree.column("Descrição", anchor=tk.CENTER, width=500)  # Definindo largura para coluna "Descrição"

    tree.heading("Qtd", text="Qtd")
    tree.column("Qtd", anchor=tk.CENTER, width=80)  # Definindo largura para coluna "Qtd"

    tree.heading("PUni R$", text="PUni R$")
    tree.column("PUni R$", anchor=tk.CENTER, width=150)  # Definindo largura para coluna "PUni R$"

    tree.heading("Preço R$", text="Preço R$")
    tree.column("Preço R$", anchor=tk.CENTER, width=150)  # Definindo largura para coluna "Preço R$"

    #podicionamneto da janela
    tree.pack(fill=ctk.BOTH, expand=True,padx=(20,0),pady=20)

    # Valore unitario e totais
    frame_valores= ctk.CTkFrame(frame_direita)
    frame_valores.pack(pady=0, padx=0)

    label_pre_unit = ctk.CTkLabel(frame_valores, text="Preço Unitario R$: ")
    entry_pre_unit = ctk.CTkEntry(frame_valores, font=("Arial", 40),width=270,justify='right')
    label_pre_comb = ctk.CTkLabel(frame_valores, text="Preço Combinado R$:")
    entry_pre_comb = ctk.CTkEntry(frame_valores, font=("Arial", 40),width=300,justify='right')
    label_pre_total = ctk.CTkLabel(frame_valores, text="Valor Total R$:")
    entry_pre_total = ctk.CTkEntry(frame_valores, font=("Arial", 40),width=300,justify='right')
    
    #posicionamento
    label_pre_unit.grid(row=0, column=0, padx=(15,350), pady=1)
    entry_pre_unit.grid(row=1, column=0, padx=(15,190), pady=1)
    label_pre_comb.grid(row=0, column=1, padx=(395,0), pady=1)
    entry_pre_comb.grid(row=1, column=1, padx=(225,0), pady=1)
    label_pre_total.grid(row=2, column=1, padx=(440,0), pady=1)
    entry_pre_total.grid(row=3, column=1, padx=(225,0), pady=1)

    # labels de usuario s e datas
    frame_userdates= ctk.CTkFrame(janela)
    frame_userdates.pack(pady=0, padx=1)

    usuario_label = ctk.CTkLabel(frame_userdates, text=f"Operador: {usuario}", font=("Any", 14))
    data_label = ctk.CTkLabel(frame_userdates, text=f"Data: {data}", font=("Any", 14))

    usuario_label.grid(row=0, column=0, padx=100, pady=0)
    data_label.grid(row=0, column=1, padx=100, pady=0)

   
    #                                                                                     ***INICIO DA FUNÇOES ***

    def adicionar_item():
       
        nonlocal num_item, valor_pagar
        material = entry_cod.get()
        #descricao = entry_descricao.get()
        qtd = int(entry_qtd.get())
        cp= entry_cupom.get()

        #entry_qtd = ctk.StringVar(value="1")  # Valor inicial: 1
        if not cp:
            messagebox.showerror("Erro", "Click em Novo, Nova Compra para inicia uma compra!")
            return

        if not material:
            messagebox.showerror("Erro", "Erro no campo material ou descrição!")
            return

        if qtd < 1 or qtd > 99:
            messagebox.showerror("Erro", "Erro no campo Quantidade!")
            return

        plu_pro = adicionar.achar(material, dic)
        if not plu_pro:
            messagebox.showerror("Erro", "Erro no campo material")
            return

        for item in dic:
            if item["cod"] == plu_pro:
                num_item += 1
                ean = item["ean"]
                material = item["item"]
                preco_unitario = item["preco"]
                preco = item["preco"] * qtd
                valor_pagar += preco
                produto = [num_item, plu_pro, ean, material, qtd, preco_unitario, preco]
                carrinho.append(produto)
                tree.insert("", "end", values=produto)
   
                # Atualizar os campos visuais (Entries)
                entry_descricao.delete(0, ctk.END)  # Limpa a entrada de descrição
                entry_descricao.insert(0, material)  # Atualiza com a descrição correta

                entry_pre_unit.delete(0, ctk.END)  # Limpa o campo de preço unitário
                entry_pre_unit.insert(0, f" {preco_unitario:.2f}")  # Atualiza o preço unitário

                entry_pre_comb.delete(0, ctk.END)  # Limpa o campo de preço combinado
                entry_pre_comb.insert(0, f" {preco:.2f}")  # Atualiza o preço combinado

                entry_pre_total.delete(0, ctk.END)  # Limpa o campo de valor total
                entry_pre_total.insert(0, f" {valor_pagar:.2f}")  # Atualiza o valor total

        # Limpar os campos após a adição
        entry_cod.delete(0, ctk.END)
        #entry_descricao.delete(0, ctk.END)
        entry_qtd.delete(0, ctk.END)
        entry_qtd.insert(0, "1")  # Definir a quantidade como 1 por padrão

    def deletar_item():
        nonlocal valor_pagar
        selected_item = tree.selection()[0]
        valor_pagar = remover.remover(valor_pagar, carrinho, selected_item)
        tree.delete(selected_item)

    def pagar_items():
        nonlocal valor_pagar, carrinho, num_item, cupom
        v_pago = f"{valor_pagar:.2f}"
        valor_pagar = pagar.pagar(valor_pagar)

        if valor_pagar == 0:
            arquivar.arquivo(cupom, data, usuario, cnpj, cpf, v_pago, empresa, carrinho)
            limpar.limpar_saida(carrinho, tree, num_item)
            num_item = 0
            messagebox.showinfo("Info", "Pagamento realizado com sucesso!")
        else:
            messagebox.showerror("Erro", "Erro ao realizar pagamento!")

    def voltar():
        nonlocal valor_pagar, num_item
        limpar.limpar_saida(carrinho, tree, num_item)
        valor_pagar = 0
        num_item = 0

    def nova_compra():
        nonlocal cupom
        count = 1
        cupom += count
        # Limpa os campos e reseta o carrinho
        label_titulo.configure(text="CAIXA ABERTO", font=("Arial", 25, 'bold')) 
        #usuario_label = ctk.CTkLabel(frame_userdates, text=f"Operador: {usuario}", font=("Any", 14))
        entry_cupom.insert(0, cupom)  # Atualiza com a descrição correta

        #voltar()

    def nova_pesquisa():
        ean,material=pesquisar.pesquisar(dic)
        entry_cod.insert(0, ean)
        entry_descricao.insert(0, material)

    def novo_item():
        if usuario == "Administrador":
            cadastrar.novo_item()
            atualizar_dic()
        else:
            messagebox.showerror("Erro", "Seu usuário não tem permissão para cadastrar item!")

    def venda_cupom():
        lista_dados = arquivar.lista_de_vendas()
        visualizar.venda_cupom(lista_dados)

    def mostrar_ajuda():
        try:
            with open('ajuda.txt', 'r') as legenda:
                arquivo = legenda.read()
                messagebox.showinfo("Ajuda", arquivo)
        except FileNotFoundError:
            messagebox.showerror("Erro", "O arquivo 'SUPORTE' não foi encontrado.\nVerifique o caminho ou crie o arquivo.")

    def atualizar_dic():
        nonlocal dic
        try:
            with open('bd.txt', 'r') as adic:
                dic = json.load(adic)
        except FileNotFoundError:
            messagebox.showerror("Erro", "O arquivo 'bd.txt' não foi encontrado!")

    # Inicializa o dicionário de produtos
    dic={}

    atualizar_dic()

    janela.mainloop()

# Teste da função
usuario, data, empresa = "Administrador", '2024-03-21 17:00', "Tem De Tudo ME"
sistema(usuario, data, empresa)



