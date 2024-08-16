### README para Projeto de Criptografia: Cifra de César e Diffie-Hellman 🚀🔒

Este repositório contém um projeto de demonstração de criptografia utilizando a cifra de César para cifragem de texto e o protocolo Diffie-Hellman para a segura troca de chaves. O sistema é dividido em duas partes principais: um cliente e um servidor, que juntos, exemplificam um método de comunicação segura sobre uma rede.

#### 📜 Descrição dos Componentes

1. **Cliente**:
   - **Função**: Inicia a comunicação com o servidor, envia e recebe dados criptografados.
   - **Processo**:
     - Gera um número primo e o envia para o servidor.
     - Recebe a base `g` do servidor.
     - Calcula e envia sua chave pública baseada no protocolo Diffie-Hellman.
     - Recebe a chave pública do servidor e calcula a chave compartilhada.
     - Cifra uma mensagem utilizando a cifra de César com a chave derivada da chave compartilhada e envia ao servidor.
     - Recebe, decifra a mensagem processada do servidor, e a exibe.

2. **Servidor**:
   - **Função**: Escuta e aceita conexões dos clientes, processa e reenvia dados criptografados.
   - **Processo**:
     - Aguarda a recepção do número primo `p` do cliente.
     - Gera e envia a base `g` para o cliente.
     - Recebe a chave pública do cliente, calcula sua própria chave pública e a envia de volta.
     - Recebe a mensagem cifrada, decifra, processa (por exemplo, converte para maiúsculas), recifra e a envia de volta ao cliente.

#### ⚙️ Requisitos Técnicos

- **Python 3.x**: O código é escrito em Python e utiliza funções básicas da linguagem.
- **Módulos Python**: `socket` para a comunicação de rede, `random` e `math` para operações matemáticas e geração de números.

#### 🚀 Instruções de Uso

1. **Servidor**:
   - Inicie o script do servidor em um ambiente que possa aceitar conexões na rede.
   - O servidor rodará na porta 1300 por padrão (certifique-se de que está disponível).

2. **Cliente**:
   - Execute o script do cliente após o servidor estar ativo.
   - Forneça o IP do servidor se estiver rodando em uma rede diferente.
   - Digite uma mensagem para ser cifrada e enviada ao servidor.

#### 🔐 Segurança

- O uso do protocolo Diffie-Hellman garante que a chave compartilhada seja conhecida apenas pelos participantes da comunicação.
- A cifra de César é utilizada para fins didáticos; em aplicações práticas, recomenda-se substituí-la por métodos mais robustos.

#### 🛑 Limitações

- A cifra de César oferece uma segurança muito básica e pode ser facilmente quebrada.
- A geração de números primos não está otimizada para eficiência em grandes intervalos.

#### 📊 Evidências

##### 🖥️ Client:
![Terminal Client](https://github.com/user-attachments/assets/082c2e91-70ae-40b5-b123-6d7eadf636dd)
![Wireshark Client](https://github.com/user-attachments/assets/94dfcc85-c932-421f-83bc-3b47fe45caa0)

##### 🌐 Server:
![image](https://github.com/user-attachments/assets/4d9743f1-1c42-49ff-852e-457e6ef7b43e)
![image](https://github.com/user-attachments/assets/715f2a07-32ed-460d-a15e-df420958fcf1)

#### 👥 Integrantes

 - André Vitor Pereira Cini;
 - Gustavo Peterlini de Oliveira;
 - Lucas Leite Vaz de Lima;
 - Murilo Tinari Abdalla.

#### 📬 Suporte

Se tiver dúvidas ou sugestões, fique à vontade para abrir uma `issue` ou enviar um `pull request`. Suas contribuições são muito bem-vindas!

#### 🌟 Apoio

Se gostou do projeto, dê uma ⭐ no repositório!


