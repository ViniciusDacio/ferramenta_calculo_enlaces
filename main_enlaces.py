import funcoes_redes as fr
import tkinter as tk
from tkinter import ttk
import math

# Criação da janela com 8 abas
janela = tk.Tk()
janela.title("Calculadora de Enlaces")
janela.geometry("600x600")
janela.resizable(False, False)

# Criação das abas
abas = ttk.Notebook(janela)
aba1 = tk.Frame(abas)
aba2 = tk.Frame(abas)
aba3 = tk.Frame(abas)
aba4 = tk.Frame(abas)
aba5 = tk.Frame(abas)
aba6 = tk.Frame(abas)
aba7 = tk.Frame(abas)
aba8 = tk.Frame(abas)

# Adicionando as abas
abas.add(aba1, text="Shannon ")
abas.add(aba2, text="Nyquist")
abas.add(aba3, text="mW para dBm ")
abas.add(aba4, text="dBm para mW ")
abas.add(aba5, text="EIRP ")
abas.add(aba6, text="FSLP ")
abas.add(aba7, text="RSL ")
abas.add(aba8, text="Fresnel Zone ")

# Adicionando as abas ao widget do notebook
abas.pack(expand=1, fill='both')

'''Funções'''

validacao = janela.register(fr.apenas_numeros)

def shannon():
    largura = float(campo1.get())
    snr = float(campo1_2.get())
    snr = snr * 1000
    resultado = fr.shannon(largura, snr)
    
    Resultado1.configure(text="Resultado: " + str(resultado) + " bps")

def nyquist():
    largura = float(campo2.get())
    modulacao = float(campo2_2.get())
    largura = largura * 1000
    resultado = fr.nyquist(largura, modulacao)
    
    Resultado2.configure(text="Resultado: " + str(resultado) + " bps")

def conversao_mw():
    potencia = float(campo3.get())
    resultado = fr.mW_dBm(potencia)
    
    Resultado3.configure(text="Resultado: " + str(resultado) + " dBm")

def conversao_dbm():
    potencia = float(campo4.get())
    resultado = fr.dBm_mW(potencia)
    
    Resultado4.configure(text="Resultado: " + str(resultado) + " mW")

def eirp():
    potencia = float(campo5.get())
    ganho = float(campo5_2.get())
    perdas = float(campo5_3.get())
    resultado = fr.eirp(potencia, ganho, perdas)
    
    Resultado5.configure(text="Resultado: " + str(resultado) + " dBm")

def fslp():
    distancia = float(campo6.get())
    frequencia = float(campo6_2.get())
    resultado = fr.fslp(distancia, frequencia)
    
    Resultado6.configure(text="Resultado: " + str(resultado) + " dB")

def rsl():
    potencia = float(campo7.get())
    ganho_tx = float(campo7_2.get())
    perdas_tx = float(campo7_3.get())
    distancia = float(campo7_4.get())
    frequencia = float(campo7_5.get())
    ganho_rx = float(campo7_6.get())
    perdas_rx = float(campo7_7.get())
    resultado = fr.rsl(potencia, ganho_tx, perdas_tx, distancia, frequencia, ganho_rx, perdas_rx)
    
    Resultado7.configure(text="Resultado: " + str(resultado) + " dBm")

def fresnel_zone():
    distancia = float(campo8.get())
    frequencia = float(campo8_2.get())
    dao = float(campo8_4.get())
    dbo = float(campo8_5.get())
    resultado = fr.fresnel(distancia, frequencia, dao, dbo)

    primeira_zona = round((resultado * 0.6),2)
    zona_fresnel.configure(text="Primeira Zona de Fresnel: " + str(primeira_zona) + " m")
    
    Resultado8.configure(text="Resultado: " + str(resultado) + " dBm")

'''Interface'''

# Aba 1 - Shannon
label1 = tk.Label(aba1, text="Largura de Banda (KHz)")
label1.grid(column=0, row=1)
campo1 = tk.Entry(aba1, validate="key", validatecommand=(validacao, '%P'), width=20)
campo1.grid(column=1, row=1)

label1_2 = tk.Label(aba1, text="Sinal/Ruído (dB)")
label1_2.grid(column=0, row=2)
campo1_2 = tk.Entry(aba1, validate="key", validatecommand=(validacao, '%P'))
campo1_2.grid(column=1, row=2)

button1 = tk.Button(aba1, text="Calcular", command=shannon)
button1.grid(column=0, row=3)

Resultado1 = tk.Label(aba1, text="Resultado: ")
Resultado1.grid(column=0, row=4)

# Aba 2 - Nyquist
label2 = tk.Label(aba2, text="Largura de Banda (KHz)")
label2.grid(column=0, row=1)
campo2 = tk.Entry(aba2, validate="key", validatecommand=(validacao, '%P'))
campo2.grid(column=1, row=1)

label2_2 = tk.Label(aba2, text="Modulação")
label2_2.grid(column=0, row=2)
campo2_2 = tk.Entry(aba2, validate="key", validatecommand=(validacao, '%P'))
campo2_2.grid(column=1, row=2)

button2 = tk.Button(aba2, text="Calcular", command=nyquist)
button2.grid(column=0, row=3)

Resultado2 = tk.Label(aba2, text="Resultado: ")
Resultado2.grid(column=0, row=4)

# Aba 3 - mW para dBm
label3 = tk.Label(aba3, text="Potência (mW)")
label3.grid(column=0, row=1)
campo3 = tk.Entry(aba3, validate="key", validatecommand=(validacao, '%P'))
campo3.grid(column=1, row=1)

button3 = tk.Button(aba3, text="Calcular", command=conversao_mw)
button3.grid(column=0, row=2)

Resultado3 = tk.Label(aba3, text="Resultado: ")
Resultado3.grid(column=0, row=3)

# Aba 4 - dBm para mW
label4 = tk.Label(aba4, text="Potência (dBm)")
label4.grid(column=0, row=1)
campo4 = tk.Entry(aba4, validate="key", validatecommand=(validacao, '%P'))
campo4.grid(column=1, row=1)

button4 = tk.Button(aba4, text="Calcular", command=conversao_dbm)
button4.grid(column=0, row=2)

Resultado4 = tk.Label(aba4, text="Resultado: ")
Resultado4.grid(column=0, row=3)

# Aba 5 - EIRP
label5 = tk.Label(aba5, text="Potência de Transmissão (mW)")
label5.grid(column=0, row=1)
campo5 = tk.Entry(aba5, validate="key", validatecommand=(validacao, '%P'))
campo5.grid(column=1, row=1)

label5_2 = tk.Label(aba5, text="Ganho da Antena (dBi)")
label5_2.grid(column=0, row=2)

campo5_2 = tk.Entry(aba5, validate="key", validatecommand=(validacao, '%P'))
campo5_2.grid(column=1, row=2)

label5_3 = tk.Label(aba5, text="Perdas no Cabo (dB)")
label5_3.grid(column=0, row=3)

campo5_3 = tk.Entry(aba5, validate="key", validatecommand=(validacao, '%P'))
campo5_3.grid(column=1, row=3)

button5 = tk.Button(aba5, text="Calcular", command=eirp)
button5.grid(column=0, row=4)

Resultado5 = tk.Label(aba5, text="Resultado: ")
Resultado5.grid(column=0, row=5)

# Aba 6 - FSLP
label6 = tk.Label(aba6, text="Distância (Km)")
label6.grid(column=0, row=1)
campo6 = tk.Entry(aba6, validate="key", validatecommand=(validacao, '%P'))
campo6.grid(column=1, row=1)

label6_2 = tk.Label(aba6, text="Frequência (MHz)")
label6_2.grid(column=0, row=2)
campo6_2 = tk.Entry(aba6, validate="key", validatecommand=(validacao, '%P'))
campo6_2.grid(column=1, row=2)

button6 = tk.Button(aba6, text="Calcular", command=fslp)
button6.grid(column=0, row=3)

Resultado6 = tk.Label(aba6, text="Resultado: ")
Resultado6.grid(column=0, row=4)

# Aba 7 - RSL
label7 = tk.Label(aba7, text="Potência de Transmissão (mW)")
label7.grid(column=0, row=1)
campo7 = tk.Entry(aba7, validate="key", validatecommand=(validacao, '%P'))
campo7.grid(column=1, row=1)

label7_2 = tk.Label(aba7, text="Ganho da Antena TX (dBi)")
label7_2.grid(column=0, row=2)
campo7_2 = tk.Entry(aba7, validate="key", validatecommand=(validacao, '%P'))
campo7_2.grid(column=1, row=2)

label7_3 = tk.Label(aba7, text="Perdas no Cabo TX (dB)")
label7_3.grid(column=0, row=3)
campo7_3 = tk.Entry(aba7, validate="key", validatecommand=(validacao, '%P'))
campo7_3.grid(column=1, row=3)

label7_4 = tk.Label(aba7, text="Distância (Km)")
label7_4.grid(column=0, row=4)
campo7_4 = tk.Entry(aba7, validate="key", validatecommand=(validacao, '%P'))
campo7_4.grid(column=1, row=4)

label7_5 = tk.Label(aba7, text="Frequência (MHz)")
label7_5.grid(column=0, row=5)
campo7_5 = tk.Entry(aba7, validate="key", validatecommand=(validacao, '%P'))
campo7_5.grid(column=1, row=5)

label7_6 = tk.Label(aba7, text="Ganho da Antena RX (dBi)")
label7_6.grid(column=0, row=6)
campo7_6 = tk.Entry(aba7, validate="key", validatecommand=(validacao, '%P'))
campo7_6.grid(column=1, row=6)

label7_7 = tk.Label(aba7, text="Perdas no Cabo RX (dB)")
label7_7.grid(column=0, row=7)
campo7_7 = tk.Entry(aba7, validate="key", validatecommand=(validacao, '%P'))
campo7_7.grid(column=1, row=7)

button7 = tk.Button(aba7, text="Calcular", command=rsl)
button7.grid(column=0, row=8)

Resultado7 = tk.Label(aba7, text="Resultado: ")
Resultado7.grid(column=0, row=9)

# Aba 8 - Fresnel Zone
label8 = tk.Label(aba8, text="Distância (Km)")
label8.grid(column=0, row=1)
campo8 = tk.Entry(aba8, validate="key", validatecommand=(validacao, '%P'))
campo8.grid(column=1, row=1)

label8_2 = tk.Label(aba8, text="Frequência (MHz)")
label8_2.grid(column=0, row=2)
campo8_2 = tk.Entry(aba8, validate="key", validatecommand=(validacao, '%P'))
campo8_2.grid(column=1, row=2)

label8_4 = tk.Label(aba8, text="DAO - Distancia Receptor até obstáculo (Km)")
label8_4.grid(column=0, row=3)
campo8_4 = tk.Entry(aba8, validate="key", validatecommand=(validacao, '%P'))
campo8_4.grid(column=1, row=3)

label8_5 = tk.Label(aba8, text="DBO - Distancia Transmissor até obstáculo (Km)")
label8_5.grid(column=0, row=4)
campo8_5 = tk.Entry(aba8, validate="key", validatecommand=(validacao, '%P'))
campo8_5.grid(column=1, row=4)

button8 = tk.Button(aba8, text="Calcular", command=fresnel_zone)
button8.grid(column=0, row=5)

Resultado8 = tk.Label(aba8, text="Resultado: ")
Resultado8.grid(column=0, row=7)

zona_fresnel = tk.Label(aba8, text="Primeira Zona de Fresnel até 3Ghz (m): ")
zona_fresnel.grid(column=0, row=8)

# Iniciando o loop principal
janela.mainloop()
