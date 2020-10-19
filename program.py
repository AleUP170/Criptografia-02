import fileinput

# Inicializa vector S
def initVectS(vectS):
    for x in range(0,256):
        vectS.append(x)
    return vectS

# Algoritmo KSA
def KSA(vectS, k, mess):
    j = 0
    lenght = len(k)
    for i in range(0,256):
        j = (j + vectS[i] + ord(k[i%lenght]))%256
        vectS[i], vectS[j] = vectS[j], vectS[i]
    return vectS

# Algoritmo PRGA y cifrado
def PRGA(vectS, mess):
    i, j, k = 0, 0, 0
    out = ""
    while len(mess)>0:
        i = (i + 1)%256
        j = (j + vectS[i])%256
        vectS[i], vectS[j] = vectS[j], vectS[i]
        k = S[((vectS[j] + vectS[i])%256)]
        out += '{:02X}'.format(((ord(mess[0])^(k))%256))
        mess = mess[1:]
    return out
    

# Lee entradas
lines = []
for line in fileinput.input():
    lines.append(line)

# Obtener las llaves y texto plano, limpiando el input
key = lines[0].replace("\n","")
key = key.replace(" ","")
text = lines[1].replace(" ","") 
text = text.replace("\n","")

# Algoritmo main
S = []
S = initVectS(S)
S = KSA(S, key, text)
cif = PRGA(S, text)
print(cif)