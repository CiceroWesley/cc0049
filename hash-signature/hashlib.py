import hashlib
from hashlib import pbkdf2_hmac
from hashlib import blake2b
from os import urandom

#criação de objeto hash
m = hashlib.sha256()
m2 = hashlib.sha256()
#atualiza objeto hash com bytes
#update a+b
m.update("hash1".encode())
m.update("hash2".encode())

m2.update("hash1hash2".encode())

#digest dos dois objetos criados
hash1 = m.digest()
hash2 = m2.digest()

print(hash1)
print(hash2)

#hash com md5
m3 = hashlib.md5()
#atualização da mensagem
m3.update('hash3'.encode())

#hexdigest retorna em caracteres hexadecimais
hash3 = m3.hexdigest()
hash31 = m3.digest()

print(hash3)
print(hash31)


#key derivation
message = "senha"
#sha256, salt gerado pelo urandom, 500000 iteracoes
dk = pbkdf2_hmac('sha256', message.encode(), urandom(20), 500000)
messageH = dk.hex()

print(messageH)


#hash criptografico co blake

h = blake2b()
h.update('Ola, Mundo'.encode())
h1 = h.hexdigest()

print(h1)