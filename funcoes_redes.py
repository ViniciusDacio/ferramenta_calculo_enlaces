import math

'''
Shannon - Capacidade Máxima de Canal:
Calcular a capacidade máxima de transmissão de dados em um canal de comunicação.
Capacidade Máxima de Canal (bps) = largura de banda (Hz) * log2(1 + Sinal-Ruído), 
onde Sinal-Ruído é a relação sinal-ruído em decibéis.
'''
def shannon(largura_banda, frequencia):
    sn = 10 ** (largura_banda / 10)
    return round((frequencia * math.log2(1 + sn)),2)

#print(shannon(40, 100000)) #PASSOU

'''
Nyquist - Taxa de Nyquist:
Determinar a taxa de amostragem mínima necessária para recuperar um sinal adequadamente.
Taxa de Nyquist (bps) = 2 * largura de banda do sinal (Hz) * Mdodulação multinível .
'''
def nyquist(largura_banda, modulacao):
    return round((2 * largura_banda * modulacao),2)

#print(nyquist(6000, 6)) PASSOU

'''
Conversão de mW para dBm:
Realizar a conversão de potência de miliwatts (mW) para decibéis-milliwatts (dBm).
Potência (dBm) = 10 * log10(Potência em mW).
'''
def mW_dBm(potencia):
    return round((10 * math.log10(potencia)),2)

#print(mW_dBm(150)) #PASSOU

'''
Conversão de dBm para mW:
Efetuar a conversão de decibéis-milliwatts (dBm) para miliwatts (mW).
 Potência (mW) = 10 (Potência em dBm / 10).
'''
def dBm_mW(potencia):
    return round((10 ** (potencia / 10)),2)

#print(dBm_mW(5)) PASSOU

'''
EIRP (Effective Isotropic Radiated Power):
Calcular a potência efetiva irradiada isotropicamente por uma antena.
EIRP (dBm) = Potência de Transmissão (dBm) + Ganho da Antena (dBi) - Perdas no Cabo (dB).
'''
def eirp(potencia, ganho, perdas):
    return round((mW_dBm(potencia) + ganho - perdas),2)

#print(eirp(100, 12, 7.43)) #PASSOU 24.57
#print(eirp(80, 9, 4.54)) #PASSOU 23.49

'''
FSLP (Free Space Loss Path):
Determinar a perda de potência em uma transmissão sem fio em um espaço livre de obstáculos.
FSLP (dB) = 32,4 + 20 * log10(d) + 20 * log10(f), onde d é a distância em Km, f é a frequência em MHz.
'''
def fslp(distancia, frequencia):
    return round((32.4 + 20 * math.log10(distancia) + 20 * math.log10(frequencia)),2)

#print(fslp(0.72, 2412)) #PASSOU
#print(fslp(0.45, 6798)) #PASSOU

'''
RSL (Received Signal Level):
Calcular o nível de sinal recebido em um enlace de comunicação sem fio.
RSL (dBm) = Potência de Transmissão (dBm) + Ganho da Antena TX (dBi) - Perdas no Cabo TX (dB) 
- Free Space Loss Path  + Ganho da Antena RX (dBi) - Perdas no Cabo RX (dB) .
'''
def rsl(potencia, ganho_tx, perdas_tx, distancia, frequencia, ganho_rx, perdas_rx):
    return round((eirp(potencia, ganho_tx, perdas_tx) - fslp(distancia, frequencia) + ganho_rx - perdas_rx),2)

#print(rsl(200, 16, 4.1, 0.5, 2437, 12, 2.5)) #PASSOU

'''
Fresnel Zone:
Determinar o raio da zona de Fresnel, uma área crucial que deve ser mantida livre de obstruções para 
garantir uma comunicação confiável. Raio da zona de Fresnel (m) = 550 * √(DAO * DBO / ( D * f )), 
onde DAO eDBO são as distâncias do transmissor e receptor até o obstáculo, f é a frequência em MHz e D é 
a distância entre o transmissor e o receptor.
'''
def fresnel(distancia, frequencia, dao, dbo):
    return round((550 * math.sqrt((dao * dbo) / (distancia * frequencia))),2)

#print(fresnel(6, 2412, 3.2, 2.8)) #PASSOU

def apenas_numeros(P):
    # P é o valor que o campo terá se a edição for permitida
    if P == "":
        return True
    try:
        float(P)
        return True
    except ValueError:
        return False
