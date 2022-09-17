import rsa 

def gerarKeys(entity):
    if(entity == 'Client' or entity == 'Server'):
        (key_pub, key_priv) = rsa.newkeys(512)
        pub = key_pub.save_pkcs1()
        pubFile = open('public'+entity+'.pem','wb')
        pubFile.write(pub)
        pubFile.close()
        priv = key_priv.save_pkcs1()
        privFile = open('private'+entity+'.pem','wb')
        privFile.write(priv)
        privFile.close()
    else:
        return None