import socket
import hashlib
from pathlib import Path

HOST = "0.0.0.0"
PORT = 5000

PASTA_DESTINO = Path.home() / "Pictures"
PASTA_DESTINO.mkdir(exist_ok=True)

servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor.bind((HOST, PORT))
servidor.listen(1)

print(f"Servidor aguardando conexão na porta {PORT}...")

conn, addr = servidor.accept()
print(f"Conexão recebida de {addr}")

tamanho = int.from_bytes(conn.recv(8), byteorder='big')

dados = b""

while len(dados) < tamanho:
    pacote = conn.recv(4096)
    if not pacote:
        break
    dados += pacote

hash_nome = hashlib.sha256(dados).hexdigest()

caminho_arquivo = PASTA_DESTINO / f"{hash_nome}.bin"

with open(caminho_arquivo, "wb") as f:
    f.write(dados)

print(f"Imagem salva em: {caminho_arquivo}")

conn.close()
servidor.close()