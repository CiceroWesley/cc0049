from cryptography.fernet import Fernet
# Encriptação simétrica
# Gera uma chave secreta
key = Fernet.generate_key()
f = Fernet(key)
#cifra com a chave gerada
token = f.encrypt("Mensagem secreta!".encode())
print(token)
#decifra com a mesma chave
print((f.decrypt(token)).decode())

# <------------------------------------------------------------->

from cryptography.fernet import Fernet
from time import sleep, time

# Encriptação simétrica
# Gera uma chave secreta
key = Fernet.generate_key()
f = Fernet(key)

#cifra com a chave gerada e o tempo atual
token = f.encrypt_at_time("Mensagem secreta!".encode(),current_time = int(time()))
print(token.decode())

#tempo, desde o tempo unix até agora
print(f.extract_timestamp(token))
sleep(4)

#com 5 segundos de validade depois da criação
#descifra com a mesma chave com o tempo atual
print((f.decrypt_at_time(token,5,current_time = int(time()))).decode())


# <------------------------------------------------------------->
#Multifernet
from cryptography.fernet import Fernet, MultiFernet

# geração das chaves
key1 = Fernet(Fernet.generate_key())
key2 = Fernet(Fernet.generate_key())

# multifernet, lista de instâncias fernet
f = MultiFernet([key1, key2])

# token = key2.encrypt("Texto claro".encode())

# encriptação e atribuição ao token
token = f.encrypt("Novo texto".encode())

# mostra o texto cifrado
print(token.decode())

# descriptação do texto
d = f.decrypt(token)

# mostra o texto sem criptografia
print(d.decode())


# <------------------------------------------------------------->


from cryptography.fernet import Fernet, MultiFernet

# geração das chaves
key1 = Fernet(Fernet.generate_key())
key2 = Fernet(Fernet.generate_key())

# Multifernet, instâncias de objetos fernet
f = MultiFernet([key1, key2])

# encriptação
token = f.encrypt("Secret message".encode())

# exibe o texto crifrado
print(token)

# decriptação do texto
d = f.decrypt(token)

# mostra o texto
print(d.decode())

print('Rotate')
key3 = Fernet(Fernet.generate_key())
f2 = MultiFernet([key3, key1, key2])
rotated = f2.rotate(token)
d2 = f2.decrypt(rotated)
print(d2.decode())


# <------------------------------------------------------------->
# José Vinicius

import base64
import os
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

def descriptografar(token, passwordV):
    y = gerarChave(passwordV)
    textD = y.decrypt(token)
    
    return textD
    
def criptografar(text,x):
    token = x.encrypt(text.encode())

    return token

def gerarChave(password):
    x = password.encode()
    salt = os.urandom(16)
    salt = b"askfasofasofse42049124"
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=390000,
    )
    key = base64.urlsafe_b64encode(kdf.derive(x))
    f = Fernet(key)
    print(f)
    return f

def main():
    while True:
        option = int(input("1 - Criar chave\n2 - Criptografar com a senha\n3 - Descriptografar com a senha\n4 - Encerrar programa\n"))
        if option == 1:
            password = input("Insira a senha:")
            x = gerarChave(password)
        elif option == 2:
            text = input("Insira o texto:")
            token = criptografar(text, x)
            print(token.decode())
        elif option == 3:
            passwordV = input("Qual a senha:")
            textD = descriptografar(token, passwordV)
            print(textD.decode())
        elif option == 4:
            break
        else:
            print("Opção inválida")
main()

