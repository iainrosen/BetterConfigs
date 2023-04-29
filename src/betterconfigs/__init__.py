import pickle
import os
import warnings
from cryptography.fernet import Fernet
executableVersion = "0.8"
class config:
    def __init__(self, path) -> None:
        self.path = path
        self.encKey = None
        if os.path.exists(path)==False:
            try:
                loadConfig = {}
                loadConfig['_version'] = executableVersion
                loadConfig['_encrypted'] = False
                self.encKey = Fernet.generate_key()
                with open(self.path, 'wb') as handle:
                    pickle.dump(loadConfig, handle, protocol=pickle.HIGHEST_PROTOCOL)
            except:
                raise Exception("attempted to initialize the configuration file but was unable to write")
    def __getitem__(self, key):
        self.checkReady()
        try:
            if self.getRaw('_encrypted'):
                return self.decryptValue(key)
            with open(self.path, 'rb') as handle:
                loadedConfig = pickle.load(handle)
            return loadedConfig[key]
        except FileNotFoundError:
            raise Exception("configuration might not be initialized")
        except:
            raise NameError("property doesn't exist in configuration")
    def __setitem__(self, key, value):
        self.checkReady()
        if key.startswith('_'):
            raise Exception("unable to change configuration property")
        try:
            if self.getRaw('_encrypted'):
                value = self.encryptValue(value)
            with open(self.path, 'rb') as handle:
                loadedConfig = pickle.load(handle)
            loadedConfig[key] = value
            with open(self.path, 'wb') as handle:
                pickle.dump(loadedConfig, handle, protocol=pickle.HIGHEST_PROTOCOL)
            return 0
        except FileExistsError:
            raise Exception("unable to find the configuration")
        except:
            raise Exception("error writing configuration file")
    def __delitem__(self, key):
        self.checkReady()
        if key.startswith('_'):
            raise Exception("unable to delete configuration property")
        try:
            with open(self.path, 'rb') as handle:
                loadedConfig = pickle.load(handle)
            loadedConfig.pop(key)
            with open(self.path, 'wb') as handle:
                pickle.dump(loadedConfig, handle, protocol=pickle.HIGHEST_PROTOCOL)
            return 0
        except FileExistsError:
            raise Exception("unable to find the configuration")
        except:
            raise Exception("error writing configuration file or property could not be deleted")
    def getRaw(self, key):
        try:
            with open(self.path, 'rb') as handle:
                loadedConfig = pickle.load(handle)
            return loadedConfig[key]
        except FileNotFoundError:
            raise Exception("configuration might not be initialized")
        except:
            raise NameError("property doesn't exist in configuration")
    def checkReady(self):
        if self.encKey==None and self.getRaw('_encrypted')==True:
            raise Exception('configuration is marked encrypted, but no encKey provided')
        if self.getRaw('_version')!=executableVersion:
            warnings.warn("version mismatch!")
    def checkEncryptionValidity(self):
        self.checkReady()
        if self.decryptValue('_checksum')==self.encKey.decode():
            return 0
        else:
            return 1
    def encryptValue(self, value):
        self.checkReady()
        fernet = Fernet(self.encKey)
        return fernet.encrypt(value.encode())
    def decryptValue(self, key):
        self.checkReady()
        fernet = Fernet(self.encKey)
        return fernet.decrypt(self.getRaw(key)).decode()
    def encryptFile(self):
        self.checkReady()
        with open(self.path, 'rb') as handle:
                loadedConfig = pickle.load(handle)
        for i in loadedConfig:
            if not i.startswith("_"):
                loadedConfig[i] = self.encryptValue(loadedConfig[i])
        loadedConfig['_encrypted']=True
        loadedConfig['_checksum']=self.encryptValue(self.encKey.decode())
        with open(self.path, 'wb') as handle:
                pickle.dump(loadedConfig, handle, protocol=pickle.HIGHEST_PROTOCOL)
        return 0
    def decryptFile(self):
        self.checkReady()
        with open(self.path, 'rb') as handle:
                loadedConfig = pickle.load(handle)
        for i in loadedConfig:
            if not i.startswith("_"):
                loadedConfig[i] = self.decryptValue(i)
        loadedConfig['_encrypted']=False
        loadedConfig.pop('_checksum')
        with open(self.path, 'wb') as handle:
                pickle.dump(loadedConfig, handle, protocol=pickle.HIGHEST_PROTOCOL)
        return 0