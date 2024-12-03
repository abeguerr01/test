import tkinter as tk
import random
import winsound as sound 

n_contador = 0
r_contador = 0
v_contador = 0
bote = 100  # Valor inicial del bote

def ruleta():
    n = random.randint(0, 36)
    digito1 = n // 10
    digito2 = n % 10
    suma = digito1 + digito2
    
    if n == 0:
        resultado.configure(text=f'NÚMERO: {n}', bg='green', fg='black') 
        return 'green'
    elif suma % 2 != 0:
        resultado.configure(text=f'NÚMERO: {n}', bg='red', fg='black')
        return 'red'
    else:
        resultado.configure(text=f'NÚMERO: {n}', bg='black', fg='white')
        return 'black'
    

def actualizar_resultado():
    color_resultado = ruleta()
    actualizar_bote(color_resultado)
    sound.PlaySound(r'C:\Users\USER\OneDrive\Clase D.A.M\PROGRAMACIÓN\Recursos\dado.wav', sound.SND_FILENAME)

def negro1():
    global n_contador, bote
    if bote > 0:
        n_contador += 1
        bote -= 1
        negro2.config(text=str(n_contador))
        actualizar_bote_texto()

def rojo1():
    global r_contador, bote
    if bote > 0:
        r_contador += 1
        bote -= 1
        rojo2.config(text=str(r_contador))
        actualizar_bote_texto()

def verde1():
    global v_contador, bote
    if bote > 0:
        v_contador += 1
        bote -= 1
        verde2.config(text=str(v_contador))
        actualizar_bote_texto()

def actualizar_bote_texto():
    bote_label.config(text=f"Dinero: {bote}")
    #sound.PlaySound(r'C:\Users\USER\OneDrive\Clase D.A.M\PROGRAMACIÓN\Recursos\pick.wav', sound.SND_FILENAME)

def actualizar_bote(color_resultado):
    global bote, r_contador, n_contador, v_contador

    
    if color_resultado == "red":
        bote += r_contador * 2

        r_contador = 0
        n_contador = 0
        v_contador = 0

    elif color_resultado == "black":
        bote += n_contador * 2
        
        r_contador = 0
        n_contador = 0
        v_contador = 0

    elif color_resultado == "green":
        bote += v_contador * 36

        r_contador = 0
        n_contador = 0
        v_contador = 0

    else:
        
        r_contador = 0
        n_contador = 0
        v_contador = 0

    negro2.config(text=str(n_contador))
    rojo2.config(text=str(r_contador))
    verde2.config(text=str(v_contador))
    actualizar_bote_texto()

def reset_resultado():
    global bote
    bote = 100
    bote_label.config(text=str(f'Dinero: {bote}'))
########################################################################################################
'''
from tkinter import PhotoImage, Label
img_fondo = PhotoImage(file="https://imgs.search.brave.com/pf8x08Gi5_ByY1u5B6IHFrfolHVOSYZCIL0PP521DcI/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly9pbWcu/ZnJlZXBpay5jb20v/Zm90b3MtcHJlbWl1/bS9mb25kby1yb2pv/LWNhc2lub18xOTQx/MTgtMTE5Mi5qcGc_/c2VtdD1haXNfaHli/cmlk")
fondo = Label(image=img_fondo)
fondo.place(x=0, y=0, relwidth=1, relheight=1)
'''

app = tk.Tk()
app.geometry("500x500")
app.configure(background='#8b1e4b')
tk.Wm.wm_title(app, 'CASINO - RULETA')

marco = tk.Frame(app)
marco.pack()

etiqueta = tk.Label(
    marco,
    text=" CASINO - RULETA ",
    font=('Helvetica', 42)
)
etiqueta.pack()

######################################################################################################
botones1 = tk.Frame(app)
botones1.pack(pady=10) #Hacer pack a rojo, verde y negro

botones2 = tk.Frame(app)
botones2.pack(pady=10) #Hacer pack a rojo, verde y negro
botones2.configure(background='#8b1e4b')

botonrojo = tk.Button(
    botones1,
    text="ROJO",
    font=('Helvetica', 22),
    bg='red',
    command=rojo1
)
botonrojo.pack(side=tk.LEFT, expand=True)

botonnegro = tk.Button(
    botones1,
    text="NEGRO",
    font=('Helvetica', 22),
    bg='black',
    fg='white',
    command=negro1
)
botonnegro.pack(side=tk.RIGHT, expand=True)

botonverde = tk.Button(
    botones1,
    text="VERDE",
    font=('Helvetica', 22),
    bg='green',
    command=verde1
)
botonverde.pack(side=tk.TOP, expand=True)

####    ####    ####    ####    ####    ####    ####    ####    ####    ####    ####    ####    ####

BotonTirar = tk.Button(
    botones2,
    text="Tirar",
    font=('Helvetica', 28),
    bg='#dc7e00',
    command=actualizar_resultado
)
BotonTirar.pack(side=tk.TOP, expand=True)

BotonRestaurar = tk.Button(
    botones2,
    text="Restaurar",
    font=('Helvetica', 8),
    bg='white',
    fg='black',
    command=reset_resultado
)
BotonRestaurar.pack(side=tk.BOTTOM, expand=True)

########################################################################################################

resultado = tk.Label(
    marco,
    text='"PRESIONA TIRAR"',
    font=('Helvetica', 22)
)
resultado.pack()

negro2 = tk.Label(
    marco,
    text="0",
    font=('Helvetica', 22),
    bg='black',
    fg='white'
)
negro2.pack()

rojo2 = tk.Label(
    marco,
    text="0",
    font=('Helvetica', 22),
    bg='red'
)
rojo2.pack()

verde2 = tk.Label(
    marco,
    text="0",
    font=('Helvetica', 22),
    bg='green'
)
verde2.pack()

bote_label = tk.Label(
    marco,
    text=f"Dinero: {bote}",
    font=('Helvetica', 22),
    bg='yellow'
)
bote_label.pack()

app.mainloop()