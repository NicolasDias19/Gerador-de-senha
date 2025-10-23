import random
import tkinter as tk
import string
import pyperclip

# Criando a janela principal
janela = tk.Tk()
janela.title("Gerador de Senha")
janela.geometry("900x350+1000+300")
janela.resizable(False, False)
cor_janela = janela.config(bg="#F4F6FB")  # cor de fundo mais suave

# Checkbuttons
marcadocaresp = tk.IntVar() # Caracteres especiais
checkcaresp = tk.Checkbutton(janela, text="")
checkcaresp.config(variable=marcadocaresp, onvalue=1, offvalue=0, bg="#F4F6FB", fg="#4F8EF7", activebackground="#F4F6FB")

marcadomai = tk.IntVar() # Letras maiúsculas
checkmai = tk.Checkbutton(janela, text="")
checkmai.config(variable=marcadomai, onvalue=1, offvalue=0, bg="#F4F6FB", fg="#4F8EF7", activebackground="#F4F6FB")

marcadomin = tk.IntVar() # Letras minúsculas
checkmin = tk.Checkbutton(janela, text="")
checkmin.config(variable=marcadomin, onvalue=1, offvalue=0, bg="#F4F6FB", fg="#4F8EF7", activebackground="#F4F6FB")

marcadonum = tk.IntVar() # Números
checknum = tk.Checkbutton(janela, text="")
checknum.config(variable=marcadonum, onvalue=1, offvalue=0, bg="#F4F6FB", fg="#4F8EF7", activebackground="#F4F6FB")

# criando a variável rotulo para exibir a senha
rotulo = tk.Label(janela, text="", bg="#F4F6FB", fg="#222B45")
rotulo.pack_forget()

# Criando sliders para definir o tamanho da senha
# Criamos variáveis e colocamos eles em none para criar sliders em funções ou serem chamadas posteriormente
slidermai =  None 
slidermin = None
slidernum = None   
slidercaresp = None

# Colocando todas as letras, números e caracteres especiais em uma variável
Letras_Maiusculas = string.ascii_uppercase
Letras_Minusculas = string.ascii_lowercase  
Numeros_senha = string.digits  
Caracteres_Especiais = string.punctuation

# Função para colocar o sliders na janela
def slider_maiusculas(): 
    global slidermai
    if slidermai is None:
        slidermai = tk.Scale(
            janela, 
            from_=3, 
            to=12, 
            orient="horizontal", 
            label="Tamanho da Senha",
            width=11,
            length=115,
            bg="#F4F6FB",
            fg="#222B45",
            troughcolor="#4F8EF7",
            highlightbackground="#F4F6FB"
            ) 
        slidermai.place(
            relx=0.3, 
            rely=0.23
            )

def slider_minusculas():
    global slidermin
    if slidermin is None:
        slidermin = tk.Scale(
            janela,
            from_=3,
            to=12,
            orient="horizontal",
            label="Tamanho da Senha",
            width=12,
            length=115,
            bg="#F4F6FB",
            fg="#222B45",
            troughcolor="#4F8EF7",
            highlightbackground="#F4F6FB"
            ) 
        slidermin.place(
            relx=0.3, 
            rely=0.43
            )

def slider_numeros():
    global slidernum
    if slidernum is None:
        slidernum = tk.Scale(
            janela,
            from_=3,
            to=12,
            orient="horizontal",
            label="Tamanho da Senha",
            width=11,
            length=115,
            bg="#F4F6FB",
            fg="#222B45",
            troughcolor="#4F8EF7",
            highlightbackground="#F4F6FB"
            ) 
        slidernum.place(
            relx=0.3, 
            rely=0.63
            )

def slider_caracteres_especiais():
    global slidercaresp
    if slidercaresp is None:
        slidercaresp = tk.Scale(#para caracteres especiais
            janela, 
            from_=3, 
            to=12, 
            orient="horizontal", 
            label="Tamanho da Senha",
            width=11,
            length=115,
            bg="#F4F6FB",
            fg="#222B45",
            troughcolor="#4F8EF7",
            highlightbackground="#F4F6FB"
            ) 
        slidercaresp.place(
            relx=0.3, 
            rely=0.83
            )

def esconder(widget): #Para esconder os sliders e não fuder as outras funções
    try:
        widget.place_forget()
    except:
        pass

# Função para colocar checks na janela
def checkbox_maiusculas():
    global slidermai
    checkmai.config(
        text="Com letras maiúsculas", 
        variable=marcadomai,
        command=checkbox_maiusculas,
        bg="#F4F6FB",
        fg="#4F8EF7",
        activebackground="#F4F6FB"
    )
    checkmai.place(
        relx=0.02, 
        rely=0.3, 
        anchor="sw"
        )
    if marcadomai.get() == 1:
        slider_maiusculas()
    else:
        if slidermai is not None:
            slidermai.destroy()
            slidermai = None

def checkbox_minusculas():
    global slidermin
    checkmin.config(
        text="Com letras minúsculas",
        variable=marcadomin,
        command=checkbox_minusculas,
        bg="#F4F6FB",
        fg="#4F8EF7",
        activebackground="#F4F6FB"
    )
    checkmin.place(
        relx=0.02, 
        rely=0.5, 
        anchor="sw"
        )
    if marcadomin.get() == 1:
        slider_minusculas()
    else:
        if slidermin is not None:
            slidermin.destroy()
            slidermin = None

def checkbox_numeros():
    global slidernum
    checknum.config(
        text="Com números", 
        variable=marcadonum,
        command=checkbox_numeros
        )
    checknum.place(
        relx=0.02, 
        rely=0.7, 
        anchor="sw"
        )
    if marcadonum.get() == 1:
        slider_numeros()
    else:
        if slidernum is not None:
            slidernum.destroy()
            slidernum = None

def chekbox_caresp():
    global slidercaresp
    checkcaresp.config(
        text="Com caracteres especiais", 
        variable=marcadocaresp,
        command=chekbox_caresp,
        bg="#F4F6FB",
        fg="#4F8EF7",
        activebackground="#F4F6FB"
    )
    checkcaresp.place(
        relx=0.02,
        rely=0.9,
        anchor="sw"
        )
    if marcadocaresp.get() == 1:
        slider_caracteres_especiais()
    else:
        if slidercaresp is not None:
            slidercaresp.destroy()
            slidercaresp = None

# Função para colocar textos, botões na janela
def mostrar_texto(texto):
    rotulo.config(text=texto, font=("new roman", 20, "bold"), bg="#F4F6FB", fg="#222B45")
    rotulo.place(relx=0.5, rely=0.1, anchor="center")

def texto_pequeno():
    tp = tk.Label(janela, text="Program made by: @itsmenicolasvinicius", font=("Arial", 8, "bold"), bg="#F4F6FB", fg="#888")
    tp.pack()
    tp.place(relx=0.87, rely=1, anchor="s")

def texto_explicativo2():
    te = tk.Label(janela, text="Mínimo de caracteres: 3", font=("Arial", 9, "bold"), bg="#F4F6FB", fg="#F76F4F")
    te.pack()
    te.place(relx=0.98, rely=0.86, anchor="se")

def texto_explicativo():
    te = tk.Label(janela, text="Máximo de caracteres: 12", font=("Arial", 9, "bold"), bg="#F4F6FB", fg="#F76F4F")
    te.pack()
    te.place(relx=0.989, rely=0.92, anchor="se")

def texto_copy():
    tc = tk.Label(janela, text="✔️", font=("Arial", 9, "bold"), bg="#F4F6FB", fg="#4F8EF7")
    tc.pack()
    tc.place(relx=0.867, rely=0.49, anchor="ne")

def copiar_senha():
    modtxt= rotulo.cget("text")
    if modtxt.strip() != "" and "Senha Gerada:" in modtxt:
        senha = modtxt.replace("Senha Gerada: ", "")
        pyperclip.copy(senha)
        texto_copy()

def botao_açao():
    if senhasMai() == "" and senhasMin() == "" and senhasnum() == "" and sencaresp() == "":
        senha = senha_fim()
        mostrar_texto(senha)
    else:
        senha = senha_fim()
        mostrar_texto("Senha Gerada: " + senha_fim())

# Funções para gerar partes da senha
def senhasMai ():
    if marcadomai.get() == 1 and slidermai is not None:
        if slidermai.get() == 12:
            marcadomin.set(0) if marcadomin.get() == 1 else None
            marcadonum.set(0) if marcadonum.get() == 1 else None
            marcadocaresp.set(0) if marcadocaresp.get() == 1 else None

            esconder(slidermin)
            esconder(slidernum)
            esconder(slidercaresp)

            return "".join(random.choice(Letras_Maiusculas) for _ in range((slidermai.get())))
        elif slidermai.get() >= 3:
            return "".join(random.choice(Letras_Maiusculas) for _ in range((slidermai.get())))
    else:
        return ""

def senhasMin ():
    if marcadomin.get() == 1 and slidermin is not None:
        if slidermin.get() == 12:
            marcadomai.set(0)
            marcadonum.set(0)
            marcadocaresp.set(0)

            esconder(slidermai)
            esconder(slidernum)
            esconder(slidercaresp)

            return "".join(random.choice(Letras_Minusculas) for _ in range((slidermin.get())))
        elif slidermin.get() >= 3:
            return "".join(random.choice(Letras_Minusculas) for _ in range((slidermin.get())))
    else:
        return ""

def senhasnum ():
    if marcadonum.get() == 1 and slidernum is not None:
        if slidernum.get() == 12:
            marcadomai.set(0)
            marcadomin.set(0)
            marcadocaresp.set(0)

            slidermai.place_forget()
            slidermin.place_forget()
            slidercaresp.place_forget()

            return "".join(random.choice(Numeros_senha) for _ in range((slidernum.get())))
        elif slidernum.get() >= 3:
            return "".join(random.choice(Numeros_senha) for _ in range((slidernum.get())))
    else:
        return ""

def sencaresp ():
    if marcadocaresp.get() == 1 and slidercaresp is not None:
        if slidercaresp.get() == 12:
            marcadomai.set(0)
            marcadomin.set(0)
            marcadonum.set(0)

            esconder(slidermai)
            esconder(slidermin)
            esconder(slidernum)

            return "".join(random.choice(Caracteres_Especiais) for _ in range((slidercaresp.get())))
        elif slidercaresp.get() >= 3:
            return "".join(random.choice(Caracteres_Especiais) for _ in range((slidercaresp.get())))
    else:
        return ""

# Gerando a senha final
def senha_fim():
    global Senha_Juntada
    if senhasMai() == "" and senhasMin() == "" and senhasnum() == "" and sencaresp() == "":
        return "Por favor, selecione pelo menos uma opção para gerar a senha." 
    else:
        Senha_Juntada = list(senhasMai() + senhasMin() + senhasnum() + sencaresp())
        if len(Senha_Juntada) > 12:
            random.shuffle(Senha_Juntada)
            Senha_Final = "".join(Senha_Juntada[:12])
            return Senha_Final
        else:
            random.shuffle(Senha_Juntada)
            Senha_Final = "".join(Senha_Juntada)
            return Senha_Final

# botão fora de uma função pra ele ficar "publico"
botao_widget = tk.Button(janela, text="Gerar Senha", font=("arial", 8, "bold"), command=botao_açao, width=20, height=2, bg="#4F8EF7", fg="#FFFFFF", activebackground="#356AC3", activeforeground="#FFFFFF")
botao_widget.pack()
botao_widget.place(relx=0.9, rely=0.8, anchor="s")

#criando o botão de copiar senha
botao_copiar = tk.Button(janela, text="Copiar", font=("arial", 8, "bold"), command=copiar_senha, width=7, height=2, bg="#F76F4F", fg="#FFFFFF", activebackground="#D95D39", activeforeground="#FFFFFF")
botao_copiar.pack()
botao_copiar.place(relx=0.867, rely=0.5, anchor="w")

# Mostrando a senha na janela
checkbox_maiusculas()
checkbox_minusculas()
checkbox_numeros()
chekbox_caresp()
texto_pequeno()
texto_explicativo()
texto_explicativo2()
janela.mainloop()