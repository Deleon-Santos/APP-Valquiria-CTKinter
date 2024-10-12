import customtkinter as ctk
from PIL import Image, ImageTk  # Pillow para manipulação de imagens
#import modulo_registrar as vendas
import json
from tkinter import messagebox
#from tkcalendar import Calendar  # Biblioteca para o calendário

# Configuração inicial do tema visual da interface
ctk.set_appearance_mode("light")  # Modo de aparência escura
ctk.set_default_color_theme("dark-blue")  # Tema de cores azul-escuro

# Função para autenticação do usuário ao sistema
def autenticar_usuario():
    # Coleta os dados das variáveis associadas aos campos de entrada
    usuario = usuario_var.get()
    senha = senha_var.get()
    data = data_var.get()
    empresa = empresa_var.get()

    # Verifica se todos os campos estão preenchidos
    if not usuario or not senha or not data or not empresa:
        messagebox.showerror("Erro", "Usuário, Senha ou Data\nnão devem ser nulos")
        return

    try:
        autenticado = False  # Inicializa o status de autenticação como falso
        # Percorre a lista de usuários cadastrados no arquivo JSON
        for user in dados_usuario:
            if user['nome'] == usuario and user['senha'] == senha:
                # Se o usuário for autenticado, fecha a janela e inicia o sistema de vendas
                janela.destroy()
                messagebox.showerror("conectado")
                #vendas.sistema(usuario, data, empresa)
                autenticado = True  # Autenticação bem-sucedida
                break

        # Se não houver autenticação, exibe mensagem de erro
        if not autenticado:
            messagebox.showerror("Erro", "Usuário ou Senha Incorretos")

    except Exception as e:
        # Em caso de erro inesperado, exibe uma mensagem com a descrição do erro
        messagebox.showerror("Erro", f"Erro inesperado:\n {str(e)}")
        print(e)

# Função para exibir as informações de suporte
def abrir_suporte():
    try:
        # Tenta abrir o arquivo de suporte e exibe seu conteúdo em uma popup
        with open('usuarios.txt', 'r') as legenda:
            arquivo = legenda.read()
            messagebox.showinfo("Suporte", arquivo)
    except FileNotFoundError:
        # Caso o arquivo não seja encontrado, exibe uma mensagem de erro
        messagebox.showerror("Erro", "O arquivo 'usuarios.txt' não foi encontrado.\nVerifique o caminho ou crie o arquivo.")

# Carregamento dos dados de usuários a partir de um arquivo JSON
try:
    with open('usuarios.txt', 'r') as bd:
        # Carrega os dados dos usuários em um dicionário
        dados_usuario = json.load(bd)
except FileNotFoundError:
    print(bd)
    # Caso o arquivo não seja encontrado, exibe uma mensagem de erro
    messagebox.showerror("Erro", "O arquivo 'usuarios.txt' não foi encontrado.\nVerifique o caminho ou crie o arquivo.")

# Criação da janela principal
janela = ctk.CTk()  # Cria a instância da janela usando CustomTkinter
janela.geometry("740x350")  # Define o tamanho da janela
janela.resizable(width=False, height=False) # janela pode ser flexivel ou nao
janela.title("LOGIN VENDAS")  # Título da janela

# Variáveis que armazenam os dados dos campos de entrada
usuario_var = ctk.StringVar(value="Administrador")  # Valor inicial: Administrador
senha_var = ctk.StringVar(value="1234")  # Valor inicial: 1234
data_var = ctk.StringVar(value="2024-03-21 17:41:22")  # Valor inicial de data
empresa_var = ctk.StringVar(value="Tem De Tudo ME")  # Empresa padrão

# Configuração do layout da interface
frame = ctk.CTkFrame(master=janela)  # Frame principal que contém os elementos
frame.pack(pady=20, padx=20, fill="both", expand=True  )  # Posição e preenchimento do frame

# Carregar a imagem usando PIL (precisa da biblioteca Pillow)
image_baner = "tdt.png"
image = ctk.CTkImage(dark_image=Image.open(image_baner), size=(100, 100))

# Criar um rótulo (Label) para exibir a imagem
label = ctk.CTkLabel(frame_esquerdo, image=image, text="")  # Definir text como vazio para mostrar apenas a imagem
label.pack(pady=20)
# Carregando a imagem
imagem = Image.open("imagem_login.png")  # Caminho da imagem
imagem = imagem.resize((392, 287))  # Redimensiona a imagem para caber na interface
imagem_tk = ImageTk.PhotoImage(imagem)  # Converte 

# Coluna 1: Imagem (não há funcionalidade, mas pode ser associada a um arquivo de imagem)
imagem_label = ctk.CTkLabel(master=frame, image=imagem_tk, text="login image")
imagem_label.grid(row=0, column=0, padx=10, pady=10)  # Posição da imagem no layout

# Coluna 2: Formulário de login
form_frame = ctk.CTkFrame(master=frame)  # Frame que contém o formulário
form_frame.grid(row=0, column=1, padx=50, pady=10)  # Posição do formulário no layout

# Campo para seleção da empresa
empresa_label = ctk.CTkLabel(master=form_frame, text="Empresa", font=('any', 12))  # Rótulo
empresa_label.grid(row=0, column=0, sticky="w")  # Posição do rótulo
empresa_combo = ctk.CTkComboBox(master=form_frame, values=["Tem De Tudo ME"], variable=empresa_var, font=('any', 17), width=300)  # Combobox para empresa
empresa_combo.grid(row=1, column=0)  # Posição da combobox

# Campo para seleção do usuário
usuario_label = ctk.CTkLabel(master=form_frame, text="Usuário", font=('any', 12))  # Rótulo
usuario_label.grid(row=2, column=0, sticky="w")  # Posição do rótulo
usuario_combo = ctk.CTkComboBox(master=form_frame, values=["Administrador", "Operador do Turno 1", "Operador do Turno 2"], variable=usuario_var, font=('any', 18), width=300)  # Combobox para usuário
usuario_combo.grid(row=3, column=0)  # Posição da combobox

# Campo para entrada da senha
senha_label = ctk.CTkLabel(master=form_frame, text="Senha", font=('any', 12))  # Rótulo
senha_label.grid(row=4, column=0, sticky="w")  # Posição do rótulo
senha_entry = ctk.CTkEntry(master=form_frame, show="*", textvariable=senha_var, font=('any', 18), width=300)  # Campo de entrada de senha (oculta os caracteres)
senha_entry.grid(row=5, column=0)  # Posição do campo de senha

# Campo para entrada da data
data_label = ctk.CTkLabel(master=form_frame, text="Data", font=('any', 12))  # Rótulo
data_label.grid(row=6, column=0, sticky="w")  # Posição do rótulo
data_entry = ctk.CTkEntry(master=form_frame, textvariable=data_var, font=('any', 16), width=300)  # Campo de entrada de data
data_entry.grid(row=7, column=0)  # Posição do campo de data

# Criação dos botões
button_frame = ctk.CTkFrame(master=janela)  # Frame para os botões
button_frame.pack(pady=1)  # Posição do frame de botões

# Botão OK para confirmar o login
ok_button = ctk.CTkButton(master=button_frame, text="OK", command=autenticar_usuario, font=('any', 10, 'bold'), width=100)
ok_button.grid(row=0, column=0, padx=10)  # Posição do botão OK

# Botão SAIR para fechar a aplicação
sair_button = ctk.CTkButton(master=button_frame, text="SAIR", command=janela.quit, font=('any', 10, 'bold'), fg_color="red", width=100)
sair_button.grid(row=0, column=1, padx=10)  # Posição do botão SAIR

# Botão SUPORTE para abrir a janela de suporte
suporte_button = ctk.CTkButton(master=button_frame, text="SUPORTE", command=abrir_suporte, font=('any', 10, 'bold'), width=100)
suporte_button.grid(row=0, column=2, padx=10)  # Posição do botão SUPORTE

# Executa o loop principal da janela
janela.mainloop()  # Inicia a aplicação e mantém a janela aberta até que seja fechada