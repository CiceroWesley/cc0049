#José Vinicius
import rsa

def criarChaves():
    (pubkey, privkey) = rsa.newkeys(512, poolsize=4)
    
    with open('keys/publicKey.pem', 'wb') as p:
        p.write(pubkey.save_pkcs1('PEM'))
    with open('keys/privateKey.pem', 'wb') as p:
        p.write(privkey.save_pkcs1('PEM'))

    return 0

def loadKeys():
    with open('keys/publicKey.pem', 'rb') as p:
        publicKey = rsa.PublicKey.load_pkcs1(p.read())
    with open('keys/privateKey.pem', 'rb') as p:
        privateKey = rsa.PrivateKey.load_pkcs1(p.read())
    return publicKey, privateKey

def encrypt (message, key):
    return rsa.encrypt(message.encode('ascii'), key)

def decrypt(ciphertext, key):
    try:
	    return rsa.decrypt(ciphertext, key).decode('ascii')
    except:
	    print('A chave não pode decriptar a mensagem !')
	    return False


def main():
    while True:
	    option = int(input("1 - Criar par de chaves\n2 - Criptografar com chave publica k\n3 - Descriptografar\n4 - Printar texto\n5 - Encerrar\n"))
    if option == 1:
	    criarChaves()
        publicKey, privateKey = loadKeys()
	elif option == 2:
	    message = input('Esreva o texto: ')
	    cipherText = encrypt(message, publicKey)
	    print(f'Cipher text: {cipherText}')
	elif option == 3:
	    text = decrypt(cipherText, privateKey)
	elif option == 4:
	    if text:
            print(f'Texto: {text}')
	    else:
	        print(f'Texto não decriptado')
	elif option == 5:
	    break
	else:
	    print("Opção inválida")
        
if __name__ == '__main__':
    main()