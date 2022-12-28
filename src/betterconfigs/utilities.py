import pickle
def ls(path):
    with open(path, 'rb') as handle:
        loadedConfig = pickle.load(handle)
    print("Version: ",loadedConfig['_version'])
    print("Encrypted: ", loadedConfig['_encrypted'])
    try:
        print("Checksum: ", loadedConfig['_checksum'])
    except:
        print("No checksum available")