def solucaoAnagrama1(s1,s2):
    umalista = list(s2)

    pos1 = 0
    aindaOK = True

    while pos1 < len(s1) and aindaOK:
        pos2 = 0
        encontrado = False
        while pos2 < len(umalista) and not encontrado:
            if s1[pos1] == umalista[pos2]:
                encontrado = True
            else:
                pos2 = pos2 + 1

        if encontrado:
            umalista[pos2] = None
        else:
            aindaOK = False

        pos1 = pos1 + 1

    return aindaOK

print(solucaoAnagrama1('abcd','dcba'))