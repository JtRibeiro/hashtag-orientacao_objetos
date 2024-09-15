class TV:

    cor = "preta"

    def __init__(self, tamanho):
        self.ligado ="False"
        self.tamanho = tamanho
        self.canal = "Netflix"

    def mudar_canal(self):
        self.canal = "Amazon"

tv_sala = TV(70)
tv_quarto = TV(50)

print(tv_sala.tamanho)
print(tv_quarto.tamanho)

TV.cor = "branca"

print(tv_quarto.cor)
print(tv_sala.cor)
