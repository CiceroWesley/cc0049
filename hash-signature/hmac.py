from hashlib import sha256
import hmac

#mensagem a ser passada para o hash
message = "secret"
#chave secreta para hashear a mensagem
key = "chave1"
#objeto hmac
hmac1 = hmac.new(msg=message.encode(), key=key.encode(), digestmod=sha256)
#geração do hash
hash1 = hmac1.digest()

print(hash1)

#atualização da mensagem
message2 = "public"
hmac1.update(message2.encode())
#hash atualizado com a nova mensagem
hash2 = hmac1.digest()

#comparação com o update, é uma concatenação
message3 = "secretpublic"
hmac2 = hmac.new(msg=message3.encode(),key=key.encode(),digestmod=sha256)
#gerando hash da mensagem 3
hash3 = hmac2.digest()

print(hash2)
print(hash3)
#tamanho do digest (hash) e tamanho do bloco interno (do algoritmo de hash) em bytes
print(hmac1.digest_size,hmac1.block_size)
print(hmac2.digest_size,hmac2.block_size)


#gerando um hash sem uma instância do hmac
hash4 = hmac.digest(msg=message3.encode(),key=key.encode(), digest=sha256)

print(hash4)

#comparando dois digest (hashs)
print(hmac.compare_digest(hash2,hash3))

