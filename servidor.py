import socket
from threading import Thread
import time
import os

class Servidor:
    clientes = []
    credenciais_validas = {'admin': 'admin', 'user1': 'senha1', 'user2': 'senha2'}

    def __init__(self, host, porta):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind((host, porta))
        self.socket.listen(10)
        print('Servidor iniciado e aguardando conexões...')

    def aguardar_clientes(self):
        Thread(target=self.ouvir_comandos_admin).start()

        while True:
            cliente_socket, endereco = self.socket.accept()
            print(f'Conexão de: {endereco}')

            credenciais = cliente_socket.recv(1024).decode()
            nome, senha = credenciais.split(':')
            if self.autenticar(nome, senha):
                cliente = {'nome': nome, 'socket': cliente_socket}
                self.enviar_mensagem_global(f"{nome} entrou na sala.")
                Servidor.clientes.append(cliente)
                Thread(target=self.lidar_com_cliente, args=(cliente,)).start()
                cliente_socket.send("Autenticado com sucesso!".encode())
            else:
                cliente_socket.send("Autenticação falhou. Conexão encerrada.".encode())
                cliente_socket.close()

    def autenticar(self, nome, senha):
        return Servidor.credenciais_validas.get(nome) == senha

    def lidar_com_cliente(self, cliente):
        socket_cliente = cliente['socket']
        nome_cliente = cliente['nome']

        while True:
            try:
                mensagem = socket_cliente.recv(1024).decode()
            except:
                break

            if mensagem.strip().lower() == 'exit':
                self.enviar_mensagem_global(f"{nome_cliente} saiu da sala.")
                Servidor.clientes.remove(cliente)
                socket_cliente.close()
                break
            else:
                self.enviar_mensagem_global(f"{nome_cliente}: {mensagem}", remetente=nome_cliente)

    def enviar_mensagem_global(self, mensagem, remetente=None):
        for cliente in Servidor.clientes:
            if cliente['nome'] != remetente:
                try:
                    cliente['socket'].send(mensagem.encode())
                except:
                    pass

    def ouvir_comandos_admin(self):
        while True:
            comando = input()
            if comando.strip().lower() == 'shutdown':
                print("Servidor será desligado em 10 segundos...")
                self.enviar_mensagem_global("Servidor será desligado em 10 segundos...")
                time.sleep(10)
                for cliente in Servidor.clientes:
                    try:
                        cliente['socket'].send("Servidor encerrando conexão.".encode())
                        cliente['socket'].close()
                    except:
                        pass
                print("Servidor encerrado.")
                os._exit(0)

if __name__ == "__main__":
    servidor = Servidor('127.0.0.1', 7632)
    servidor.aguardar_clientes()
