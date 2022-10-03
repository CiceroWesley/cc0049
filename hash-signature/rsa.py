import rsa
# Lilia Suyane    
(pubkey, privkey) = rsa.newkeys(512)

#base
message = 'Mensagem enviada'.encode()
signature = rsa.sign(hash, privkey, 'SHA-1')
print("\nAssinatura: ", signature, "\n")

#hash de uma mensagem e assinatura do hash 
message = 'Mensagem enviada'.encode()
hash = rsa.compute_hash(message, 'SHA-1')
signature = rsa.sign_hash(hash, privkey, 'SHA-1')
print("\nHash: ", hash)
print("\nAssinatura: ", signature, "\n")


#troca de mensagem ocorre um erro

message = 'Mensagem não enviada'.encode()
hash = rsa.compute_hash(message, 'SHA-1')
signature = rsa.sign_hash(hash, privkey, 'SHA-1')

verificar = rsa.verify(message, signature, pubkey)
print("\nVerificando a assinatura: ", verificar, "\n\n")


