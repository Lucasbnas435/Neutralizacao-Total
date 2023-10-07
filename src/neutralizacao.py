def principal():
    print("Realizaremos uma reação de neutralização total!!!")
    acido = input("Por favor, digite a fórmula molecular do ácido: ")
    base = input("Por favor, digite a fórmula molecular da base: ")
    h_ionizavel = descobre_h_ionizavel(acido)
    oh_ionizavel = descobre_oh_ionizavel(base)
    anion = descobre_anion(acido, h_ionizavel)
    cation = descobre_cation(base)
    repeticao_de_carga = 0
    if h_ionizavel == oh_ionizavel:
        repeticao_de_carga = h_ionizavel
        h_ionizavel, oh_ionizavel = 1, 1
    sal = forma_sal(cation, anion, oh_ionizavel, h_ionizavel)
    escreve_reacao(acido, base, h_ionizavel, oh_ionizavel, sal, repeticao_de_carga)
    
    
def descobre_h_ionizavel(acido):
    numero = 1
    for x in range(len(acido)):
        if acido[x] == "H":
            if acido[x+1].isnumeric():
                numero = int(acido[x+1])
                
    return numero
    
    
def descobre_oh_ionizavel(base):
    numero = 1
    for x in range(len(base)):
        if base[x] == "O" and base[x+1] == "H" and (x+1) <= (len(base) - 3):
            numero = int(base[x+3])
                
    return numero
    
    
def descobre_anion(acido, quant_ionizaveis):
    anion = ""
    if quant_ionizaveis == 1:
        for x in range(1, len(acido)):
            anion = anion + acido[x]
    else:
        for y in range(2, len(acido)):
            anion = anion + acido[y]
    
    return anion
            

def descobre_cation(base):
    cation = ""
    for x in range(len(base)):
        if (base[x] == "O" and base[x+1] == "H") or (base[x] == "(" and base[x+1] == "O"):
            return cation
        else:
            cation = cation + base[x]
    
    return cation
   
   
def forma_sal(cation, anion, carga_cation, carga_anion):
    retornar = ""
    if ("O" in anion and (anion[len(anion) - 1].isnumeric()) and carga_cation > 1) or (anion == "CN" and carga_cation > 1):
        anion = "(" + anion + ")"
    if len(cation) >= 3 and (cation[len(cation) - 1].isnumeric()) and carga_anion > 1:
        cation = "(" + cation + ")"
    
    sal = cation + str(carga_anion) + anion + str(carga_cation)
    for x in range(len(sal)):
        if sal[x] != "1":
            retornar = retornar + sal[x]

    return retornar
    
            
def escreve_reacao(acido, base, h_ionizavel, oh_ionizavel, sal, repeticao_de_carga):
    print("A reação de neutralização total é:")
    aguas = h_ionizavel * oh_ionizavel
    if repeticao_de_carga != 0:
        aguas = repeticao_de_carga
    print(oh_ionizavel, acido, "+", h_ionizavel, base, "-->", sal, "+", aguas, "H2O")
    

principal()
