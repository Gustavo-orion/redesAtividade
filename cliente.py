import socket

HOST = "127.0.0.1"  # IP do servidor
PORT = 5000

CAMINHO_IMAGEM = "imagem.jpg"

with open(CAMINHO_IMAGEM, "rb") as f:
    dados = f.read()

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.connect((HOST, PORT))

# Envia o tamanho da imagem primeiro
cliente.sendall(len(dados).to_bytes(8, byteorder='big'))

# Envia a imagem
cliente.sendall(dados)

print("Imagem enviada com sucesso!")

cliente.close()