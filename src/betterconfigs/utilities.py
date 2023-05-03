import pickle
from cryptography.fernet import Fernet
def info(path):
    with open(path, 'rb') as handle:
        loadedConfig = pickle.load(handle)
    print("Version: ",loadedConfig['_version'])
    print("Encrypted: ", loadedConfig['_encrypted'])
    try:
        print("Checksum: ", loadedConfig['_checksum'])
    except:
        print("No checksum available")
def ls(path):
    with open(path, 'rb') as handle:
        loadedConfig=pickle.load(handle)
        if loadedConfig['_encrypted']==True:
            encKey=input("Configuration is encrypted, to view unencrypted values, enter the key here, or hit ENTER to load raw values: ")
            if encKey!="":
                decryptedKeys=[]
                try:
                    fernet = Fernet(encKey)
                    print("Decrypted Checksum: "+str(fernet.decrypt(loadedConfig['_checksum'].decode())))
                except:
                    print("Encryption key didn't pass checksum!")
                    exit()
                decConf = []
                for i in loadedConfig:
                    if not i.startswith("_"):
                        decConf.append(fernet.decrypt(i).decode())
                print("Configurations: "+str(decConf))
            else:
                decConf = []
                for i in loadedConfig:
                    if not i.startswith("_"):
                        decConf.append(i)
                print("Configurations: " + str(decConf))
