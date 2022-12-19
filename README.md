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