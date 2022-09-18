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

def carregarKeys(entity):
    with open('public'+ entity + '.pem', mode='rb') as publicfile:
        keydata = publicfile.read()
    pubKey = rsa.PublicKey.load_pkcs1(keydata)

    with open('private' + entity+ '.pem', mode='rb') as privatefile:
        keydata = privatefile.read()
    privKey = rsa.PrivateKey.load_pkcs1(keydata)
    return pubKey, privKey




