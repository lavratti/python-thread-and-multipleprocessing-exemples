import threading
import time

class Trabalhador(threading.Thread):

    def __init__(self, nome):
        super().__init__()
        self.nome = nome
        self.continuar_contando = False

    def run(self):
        self.continuar_contando = True
        contagem = 0
        while self.continuar_contando:
            time.sleep(1)
            contagem += 1
            print(f"{self.nome} já contou até {contagem}")

    def parar_de_contar(self):
        self.continuar_contando = False


if __name__ == "__main__":

    minhas_threads = []
    for nome_da_pessoa in ["João", "Maria", "José"]:
        thread = Trabalhador(nome_da_pessoa)
        minhas_threads.append(thread)

    for th in minhas_threads:
        th.start()

    # join vai falhar, pois a tarefa está em um loop sem fim
    for th in minhas_threads:
        th.join(timeout=5)

    for th in minhas_threads:
        print(f"pedindo para {th.nome} parar de contar.")
        th.parar_de_contar()
    
    for th in minhas_threads:
        th.join(timeout=5)

    print("Fim.")
