import socket
import rsa 
import generateKeys

def client(host = 'localhost', port=8082):
    pubClientkey, privClientkey = generateKeys.carregarKeys('Client')
    pubServerkey = generateKeys.carregarKeys('Server')
    pubServerkey = pubServerkey[0]
    
    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Connect the socket to the server
    server_address = (host, port)
    print ("Connecting to %s port %s" % server_address)
    sock.connect(server_address)
    
    try:
        # enviando mensagem criptografa com a chave publica do servidor
        message = input("Digite a mensagem a ser enviada: ")
        crypto = rsa.encrypt(message.encode(), pubServerkey)
        print(crypto)
        sock.sendall(crypto)

        #Look for the response
        data = sock.recv(2048)
        mens = rsa.decrypt(data, privClientkey)

        print ("Received: %s" % mens.decode())
    except socket.error as e:
        print ("Socket error: %s" %str(e))
    except Exception as e:
        print ("Other exception: %s" %str(e))
    finally:
        print ("Closing connection to the server")
        sock.close()



while(True):
    print("Caso seja a 1° execução, gerar as keys.")
    i = int(input("1-Gerar keys \n2-Acessar Client \nOutro-sair"))
    if(i == 1):
        generateKeys.gerarKeys('Client')
    elif(i == 2):
        client()
    else:
        break
