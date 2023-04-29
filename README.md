# BetterConfigs

A small package to simplify configuration storing and retrieving

## Usage

Using BetterConfigs is as simple as importing the package, calling a new configuration object, and saving whatever you need to a file.

### Example Code

* Import the package with `import betterconfigs`
* Create a configuration file object with `objectname = betterconfigs.config(filename)` where *objectname* is a blank variable and *filename* is the string of the configuration file.
* You can now set properties using `objectname[property]=key`. Note you cannot use the property *version* as this is specific to the configuration file and must not be changed.

```
import betterconfigs
t = betterconfigs.config('test.config')
t['hello'] = 'world'
print(t['hello'])
```

## Encrypting/Decrypting
With version 0.8 of BetterConfigs, you can now encrypt and decrypt your configuration files on the fly. This is great in the case you need to sync configurations, and don't want them to be available to prying eyes.

To get started, use the `encryptFile()` function after you've created the `config` object. This will encrypt all existing configurations in the file, as well as provide you with an encryption key stored in the property `encKey`. When the configuration object is destroyed, the `encKey` value is also unloaded from memory, so make sure you save it!

To open an encrypted configuration file, create the object again, and set the `encKey` value to the same one used to encrypt it previously. Then, just access the configuration as normal, and BetterConfigs handles everything for you.

Finally, to decrypt the file, make sure the `encKey` value is set correctly, and use the `decryptFile()` function.