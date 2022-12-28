import pickle
import os
import warnings
from cryptography.fernet import Fernet
executableVersion = "0.7"
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