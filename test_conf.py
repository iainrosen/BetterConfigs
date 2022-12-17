from betterconfigs import *
import os
def test_basic():
    h = config('tests/test.config')
    h['hello'] = 'world'
    assert(h['hello']=='world')
    assert(h['version']==executableVersion)
    os.remove('tests/test.config')
def test_listing():
    h = config('tests/test.config')
    h['hello']='world'
    assert(h['version']==executableVersion)
    assert(listConfigurations('tests', 'hello')==['world'])
    os.remove('tests/test.config')
