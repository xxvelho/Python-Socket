import socket
from threading import Thread
import time
import os
import base64


class Servidor:
    # Lista de clientes conectados e credenciais pré-definidas
    clientes = []
    credenciais_validas = {
        "admin": "admin",
        "user1": "senha1",
        "user2": "senha2",
        "user3": "senha3",
        "user4": "senha4",
        "user5": "senha5",
        "user6": "senha6",
        "user7": "senha7",
        "user8": "senha8",
        "user9": "senha9",
        "user10": "senha10",
    }

    def __init__(self, host, porta):
        # Cria socket TCP e inicia servidor ouvindo conexões
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind((host, porta))
        self.socket.listen(10)
        print("Servidor iniciado e aguardando conexões...")

    def aguardar_clientes(self):
        # Inicia thread para comandos administrativos (ex: shutdown)
        Thread(target=self.ouvir_comandos_admin).start()

        while True:
            # Aceita nova conexão
            cliente_socket, endereco = self.socket.accept()
            print(f"Conexão de: {endereco}")

            # Recebe credenciais do cliente e autentica
            credenciais = cliente_socket.recv(1024).decode()
            nome, senha = credenciais.split(":")
            if self.autenticar(nome, senha):
                # Cliente autenticado com sucesso
                cliente = {"nome": nome, "socket": cliente_socket}
                self.enviar_mensagem_global(f"{nome} entrou na sala.")
                Servidor.clientes.append(cliente)
                Thread(target=self.lidar_com_cliente, args=(cliente,)).start()
                cliente_socket.send("Autenticado com sucesso!".encode())
            else:
                # Falha na autenticação
                cliente_socket.send("Autenticação falhou. Conexão encerrada.".encode())
                cliente_socket.close()

    def autenticar(self, nome, senha):
        # Valida nome e senha
        return Servidor.credenciais_validas.get(nome) == senha

    def lidar_com_cliente(self, cliente):
        # Gerencia comunicação com cliente específico
        socket_cliente = cliente["socket"]
        nome_cliente = cliente["nome"]

        while True:
            try:
                mensagem = socket_cliente.recv(
                    4096
                ).decode()  # Aumentei buffer para arquivos
            except:
                break

            if mensagem.strip().lower() == "exit":
                # Cliente saiu voluntariamente
                self.enviar_mensagem_global(f"{nome_cliente} saiu da sala.")
                Servidor.clientes.remove(cliente)
                socket_cliente.close()
                break
            elif mensagem.startswith("FILE:"):
                # Transferência de arquivo
                self.processar_arquivo(mensagem, nome_cliente)
            else:
                # Repassa mensagem para outros clientes
                self.enviar_mensagem_global(
                    f"{nome_cliente}: {mensagem}", remetente=nome_cliente
                )

    def processar_arquivo(self, mensagem_arquivo, remetente):
        # Processa transferência de arquivo: FILE:nome_arquivo:dados_base64
        try:
            partes = mensagem_arquivo.split(":", 2)
            nome_arquivo = partes[1]
            dados_base64 = partes[2]

            # Anuncia o arquivo para todos
            self.enviar_mensagem_global(
                f"📁 {remetente} enviou o arquivo: {nome_arquivo}", remetente
            )

            # Repassa o arquivo para todos os outros clientes
            for cliente in Servidor.clientes:
                if cliente["nome"] != remetente:
                    try:
                        cliente["socket"].send(mensagem_arquivo.encode())
                    except:
                        pass
        except Exception as e:
            print(f"Erro ao processar arquivo: {e}")

    def enviar_mensagem_global(self, mensagem, remetente=None):
        # Envia mensagem a todos clientes conectados (exceto remetente)
        for cliente in Servidor.clientes:
            if cliente["nome"] != remetente:
                try:
                    cliente["socket"].send(mensagem.encode())
                except:
                    # Ignora erros de envio (ex: cliente desconectado)
                    pass

    def ouvir_comandos_admin(self):
        # Loop para ouvir comandos administrativos no console do servidor
        while True:
            comando = input()
            if comando.strip().lower() == "shutdown":
                print("Servidor será desligado em 10 segundos...")
                self.enviar_mensagem_global("Servidor será desligado em 10 segundos...")
                time.sleep(10)
                for cliente in Servidor.clientes:
                    try:
                        cliente["socket"].send("Servidor encerrando conexão.".encode())
                        cliente["socket"].close()
                    except:
                        pass
                print("Servidor encerrado.")
                os._exit(0)


if __name__ == "__main__":
    servidor = Servidor("127.0.0.1", 7632)
    servidor.aguardar_clientes()
