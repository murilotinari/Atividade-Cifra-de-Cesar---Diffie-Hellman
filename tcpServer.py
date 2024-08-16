from socket import *
import random

# Função para cifrar uma mensagem usando a cifra de César
def cifra_cesar(mensagem, chave):
    resultado = ""
    for i in range(len(mensagem)):
        char = mensagem[i]
        resultado += chr(ord(char) + chave)  # Aumenta o código ASCII do caractere pela chave
    return resultado

# Função para decifrar uma mensagem usando a cifra de César
def decifra_cesar(mensagem, chave):
    return cifra_cesar(mensagem, -chave)  # Decifra usando a chave negativa

# Função para calcular a chave pública usando Diffie-Hellman
def diffie_hellman(p, g, private_key):
    public_key = pow(g, private_key, p)  # g^private_key % p
    return public_key

# Função para calcular a chave compartilhada usando Diffie-Hellman
def calc_shared_key(public_key, private_key, p):
    shared_key = pow(public_key, private_key, p)  # public_key^private_key % p
    return shared_key

# Configuração inicial do servidor TCP
serverPort = 1300
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(("", serverPort))  # Liga o socket à porta local
serverSocket.listen(5)  # Ouve até 5 conexões simultâneas
print("TCP Server\n")

connectionSocket, addr = serverSocket.accept()  # Aceita uma conexão

# Gera um número grande aleatório para usar como base 'g' para Diffie-Hellman
g = random.randint(1, 1000000000)  

# Recebe o número primo 'p' do cliente
public_p = int(connectionSocket.recv(65000).decode("utf-8"))
if (public_p > 0):
    print(f"P recebido: {public_p}")

# Envia a base 'g' para o cliente
print(f"G enviado: {g}")
connectionSocket.send(bytes(str(g), "utf-8"))

# Gera a chave privada do servidor e calcula sua chave pública
private_key_server = random.randint(1, public_p-1) 
public_key_server = diffie_hellman(public_p, g, private_key_server)  

# Recebe a chave pública do cliente
public_key_client = int(connectionSocket.recv(65000).decode("utf-8"))

# Envia a chave pública do servidor para o cliente
connectionSocket.send(bytes(str(public_key_server), "utf-8"))

# Calcula a chave compartilhada usando a chave pública do cliente
shared_key = calc_shared_key(public_key_client, private_key_server, public_p)

# Determina a chave de cifra usando a chave compartilhada
chave_cifra = shared_key % 26  

# Recebe a mensagem cifrada do cliente
sentence = connectionSocket.recv(65000)
mensagem_recebida = decifra_cesar(str(sentence, "utf-8"), chave_cifra)
print("Received From Client: ", mensagem_recebida)

# Processa a mensagem recebida (por exemplo, transforma em maiúsculas)
capitalizedSentence = mensagem_recebida.upper()

# Cifra novamente a mensagem processada para enviar de volta ao cliente
mensagem_criptografada = cifra_cesar(capitalizedSentence, chave_cifra)
connectionSocket.send(bytes(mensagem_criptografada, "utf-8"))

# Exibe a mensagem que foi enviada de volta ao cliente
print("Sent back to Client: ", mensagem_criptografada)

# Fecha a conexão
connectionSocket.close()
