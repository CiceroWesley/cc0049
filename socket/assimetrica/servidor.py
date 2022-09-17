import socket
import rsa
import generateKeys

def server(host = 'localhost', port=8082):
    with open('publicServer.pem', mode='rb') as publicfile:
        keydata = publicfile.read()
    pubServerkey = rsa.PublicKey.load_pkcs1(keydata)

    with open('privateServer.pem', mode='rb') as privatefile:
        keydata = privatefile.read()
    privServerkey = rsa.PrivateKey.load_pkcs1(keydata)

    with open('publicClient.pem', mode='rb') as publicfile:
        keydata = publicfile.read()
    pubClientkey = rsa.PublicKey.load_pkcs1(keydata)
    
    data_payload = 2048 #The maximum amount of data to be received at once
    # Create a TCP socket
    sock = socket.socket(socket.AF_INET,  socket.SOCK_STREAM)
    # Enable reuse address/port
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # Bind the socket to the port
    server_address = (host, port)
    print ("Iniciando servidor na porta %s %s" % server_address)
    sock.bind(server_address)
    # Listen to clients, argument specifies the max no. of queued connections
    sock.listen(5)
    i = 0
    while True:
        print ("Esperando mensagem do cliente")
        client, address = sock.accept()

        mensagem = client.recv(data_payload)
        mensagemDec = rsa.decrypt(mensagem, privServerkey)
        '''
        o que fazer com a mensagem recebida ?
        '''
        if mensagemDec:
            print ("Dados: %s" %mensagemDec.decode())
            mensagemEncC = rsa.encrypt(mensagemDec, pubClientkey)
            client.send(mensagemEncC)
            print ("sent %s bytes back to %s" % (mensagemEncC, address))
            # end connection
            client.close()
            i+=1
            if i>=3: break


while(True):
    print("Caso seja a 1° execução, gerar as keys.")
    i = int(input("1-Gerar keys \n2-Acessar Server \nOutro-sair"))
    if(i == 1):
        generateKeys.gerarKeys('Server')
    elif(i == 2):
        server()
    else:
        break
