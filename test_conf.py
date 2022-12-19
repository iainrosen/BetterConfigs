from src.betterconfigs import *
import os
def test_basic():
    h = config('tests/test.config')
    h['hello'] = 'world'
    assert(h['hello']=='world')
    assert(h['version']==executableVersion)
    os.remove('tests/test.config')
def test_oldconfig():
    h = config('tests/test.config')
    h['version']='B0.3'
    assert(h['version']=='B0.3')
    assert(upgradeConfig('tests/test.config')==0)
    os.remove('tests/test.config')
