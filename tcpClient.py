from socket import *
import random
import math

# Função para cifrar uma mensagem usando a cifra de César
def cifra_cesar(mensagem, chave):
    resultado = ""
    for char in mensagem:
        resultado += chr(ord(char) + chave)  # Cifra cada caractere ajustando seu código ASCII
    return resultado

# Função para decifrar uma mensagem usando a cifra de César
def decifra_cesar(mensagem, chave):
    return cifra_cesar(mensagem, -chave)  # Decifra invertendo a chave

# Função para calcular a chave pública usando Diffie-Hellman
def diffie_hellman(p, g, private_key):
    public_key = pow(g, private_key, p)  # Calcula g^private_key % p
    return public_key

# Função para calcular a chave compartilhada usando Diffie-Hellman
def calc_shared_key(public_key, private_key, p):
    shared_key = pow(public_key, private_key, p)  # Calcula public_key^private_key % p
    return shared_key

# Função para gerar um número primo grande aleatoriamente
def random_prime():
    while True:
        num = random.randint(2, 99999999999999)
        i = 2
        while i < num:
            R = num % i
            i += 1
            if R == 0:  # Se num não é primo
                break
            if math.pow(i,2) > num:  # Verificação de primalidade otimizada
                return num  # Retorna num se for primo

# Configuração do socket e conexão ao servidor
serverName = "10.1.70.40"
serverPort = 1300
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

# Geração e envio do número primo 'p' para o servidor
p = random_prime()
clientSocket.send(bytes(str(p), "utf-8"))  # Envia 'p' ao servidor
print(f"P enviado: {p}")

# Recebe o valor 'g' do servidor
public_g = int(clientSocket.recv(65000).decode("utf-8"))
print(f"G recebido: {public_g}")

# Geração da chave privada do cliente e cálculo da chave pública
private_key_client = random.randint(1, p-1)
public_key_client = diffie_hellman(p, public_g, private_key_client)
clientSocket.send(bytes(str(public_key_client), "utf-8"))

# Recebe a chave pública do servidor
public_key_server = int(clientSocket.recv(65000).decode("utf-8"))

# Cálculo da chave compartilhada e determinação da chave de cifra
shared_key = calc_shared_key(public_key_server, private_key_client, p)
chave_cifra = shared_key % 26  # Chave de cifra baseada no módulo 26 para a cifra de César

# Recebe entrada de usuário, cifra e envia a mensagem cifrada para o servidor
sentence = input("Input lowercase sentence: ")
mensagem_criptografada = cifra_cesar(sentence, chave_cifra)
clientSocket.send(bytes(mensagem_criptografada, "utf-8"))

# Recebe mensagem cifrada do servidor, decifra e exibe
modifiedSentence = clientSocket.recv(65000)
mensagem_decriptografada = decifra_cesar(str(modifiedSentence, "utf-8"), chave_cifra)
print("Received from Server: ", mensagem_decriptografada)

# Fecha a conexão
clientSocket.close()
