class DataConso(object):
    def __init__(self):
        self.l_conso = []


if __name__ == '__main__':
    maconso = DataConso()
    maconso.l_conso.append(10)
    maconso.l_conso.append(20)
    maconso.l_conso.append(30)
    maconso.l_conso.append(40)

    maconso_copie = maconso
    maconso_copie.l_conso[2] = 100

    print('affichage liste originale : ', maconso.l_conso)
    print('affichage liste modifiée : ', maconso_copie.l_conso)
