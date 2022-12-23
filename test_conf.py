from src.betterconfigs import *
import os
import pytest
def test_basic():
    h = config('test.config')
    h['hello'] = 'world'
    assert(h['hello']=='world')
    assert(h['configurationVersion']==executableVersion)
    os.remove('test.config')
def test_remove():
    h = config('test.config')
    h['hello'] = 'world'
    assert(h['hello']=='world')
    assert(h['configurationVersion']==executableVersion)
    del(h['hello'])
    with pytest.raises(Exception):
        h['hello']
    os.remove('test.config')
    
