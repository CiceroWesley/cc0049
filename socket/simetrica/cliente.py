import socket
from criptografia import *

def client(host = 'localhost', port=8082):
    key = gerarChave('chave1')
    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Connect the socket to the server
    server_address = (host, port)
    print ("Connecting to %s port %s" % server_address)
    sock.connect(server_address)
    # Send data
    try:
        # Send data
        message = input("Digite a mensagem a ser enviada: ")
        message = encriptar(message,key)
        print ("Sending %s" % message)
        sock.sendall(message)
        # Look for the response
        data = sock.recv(2048)
        data = decriptar(data.decode(),key)
        print ("Received: %s" % data)
    except socket.error as e:
        print ("Socket error: %s" %str(e))
    except Exception as e:
        print ("Other exception: %s" %str(e))
    finally:
        print ("Closing connection to the server")
        sock.close()



client()