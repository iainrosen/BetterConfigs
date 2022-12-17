import pickle
import os
executableVersion = "B0.4"
class config:
    def __init__(self, path) -> None:
        self.path = path
        if os.path.exists(path)==False:
            try:
                loadConfig = {}
                loadConfig['version'] = executableVersion
                with open(self.path, 'wb') as handle:
                    pickle.dump(loadConfig, handle, protocol=pickle.HIGHEST_PROTOCOL)
            except:
                raise Exception("attempted to initialize the configuration file but was unable to write")
    def __getitem__(self, key):
        try:
            with open(self.path, 'rb') as handle:
                loadedConfig = pickle.load(handle)
            return loadedConfig[key]
        except FileNotFoundError:
            raise Exception("configuration might not be initialized")
        except:
            raise NameError("property doesn't exist in configuration")
    def __setitem__(self, key, value):
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