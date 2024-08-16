from socket import *
import random

def cifra_cesar(mensagem, chave):
    resultado = ""
    for i in range(len(mensagem)):
        char = mensagem[i]
        resultado += chr(ord(char) + chave)
    return resultado

def decifra_cesar(mensagem, chave):
    return cifra_cesar(mensagem, -chave)

def diffie_hellman(p, g, private_key):
    public_key = pow(g, private_key, p)
    return public_key

def calc_shared_key(public_key, private_key, p):
    shared_key = pow(public_key, private_key, p)
    return shared_key

serverPort = 1300
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(("", serverPort))
serverSocket.listen(5)
print("TCP Server\n")

connectionSocket, addr = serverSocket.accept()

p = 23  
g = 5   

private_key_server = random.randint(1, p-1) 
public_key_server = diffie_hellman(p, g, private_key_server)  

public_key_client = int(connectionSocket.recv(65000).decode("utf-8"))

connectionSocket.send(bytes(str(public_key_server), "utf-8"))

shared_key = calc_shared_key(public_key_client, private_key_server, p)

chave_cifra = shared_key % 26  

sentence = connectionSocket.recv(65000)
mensagem_recebida = decifra_cesar(str(sentence, "utf-8"), chave_cifra)
print("Received From Client: ", mensagem_recebida)

capitalizedSentence = mensagem_recebida.upper()

mensagem_criptografada = cifra_cesar(capitalizedSentence, chave_cifra)
connectionSocket.send(bytes(mensagem_criptografada, "utf-8"))

print("Sent back to Client: ", mensagem_criptografada)

connectionSocket.close()