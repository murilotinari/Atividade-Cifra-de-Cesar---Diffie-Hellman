from socket import *
import random

def cifra_cesar(mensagem, chave):
    resultado = ""
    for char in mensagem:
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

serverName = "10.1.70.40"
serverPort = 1300
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

p = 23 
g = 5  

private_key_client = random.randint(1, p-1)
public_key_client = diffie_hellman(p, g, private_key_client)

clientSocket.send(bytes(str(public_key_client), "utf-8"))

public_key_server = int(clientSocket.recv(65000).decode("utf-8"))

shared_key = calc_shared_key(public_key_server, private_key_client, p)
chave_cifra = shared_key % 26  

sentence = input("Input lowercase sentence: ")
mensagem_criptografada = cifra_cesar(sentence, chave_cifra)

clientSocket.send(bytes(mensagem_criptografada, "utf-8"))

modifiedSentence = clientSocket.recv(65000)
mensagem_decriptografada = decifra_cesar(str(modifiedSentence, "utf-8"), chave_cifra)

print("Received from Server: ", mensagem_decriptografada)

clientSocket.close()
