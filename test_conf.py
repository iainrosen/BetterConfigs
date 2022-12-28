from src.betterconfigs import *
import os
import pytest
def test_basic():
    h = config('test.config')
    h['hello'] = 'world'
    assert(h['hello']=='world')
    assert(h['_version']==executableVersion)
    os.remove('test.config')
def test_remove():
    h = config('test.config')
    h['hello'] = 'world'
    assert(h['hello']=='world')
    assert(h['_version']==executableVersion)
    del(h['hello'])
    with pytest.raises(Exception):
        h['hello']
    os.remove('test.config')
def test_change_protected():
    h = config('test.config')
    h['hello'] = 'world'
    assert(h['hello']=='world')
    with pytest.raises(Exception):
        h['_version'] = 'test'
    os.remove('test.config') 
def test_encryption_checks():
    h = config('test.config')
    assert(h['_encrypted']==False)
    assert(h.encKey!=None)
    t = config('test.config')
    assert(t['_encrypted']==False)
    assert(t.encKey==None)
    os.remove('test.config')
def test_encryption():
    h = config('test.config')
    assert(h['_encrypted']==False)
    assert(h.encKey!=None)
    h['hello']='world'
    assert(h.encryptFile()==0)
    assert(h['hello']=='world')
    assert(h.getRaw('hello')!='world')
    assert(h.getRaw('_version')=='0.7')
    encryptionKey = h.encKey
    t = config('test.config')
    assert(t.getRaw('_encrypted')==True)
    with pytest.raises(Exception):
        t['hello']='world'
    os.remove('test.config')
def test_decryption():
    h = config('test.config')
    assert(h['_encrypted']==False)
    assert(h.encKey!=None)
    h['hello']='world'
    assert(h.encryptFile()==0)
    assert(h['hello']=='world')
    assert(h.getRaw('hello')!='world')
    assert(h.decryptFile()==0)
    assert(h['hello']=='world')
    assert(h.getRaw('hello')=='world')
    os.remove('test.config')
def test_checksum():
    h = config('test.config')
    assert(h['_encrypted']==False)
    assert(h.encKey!=None)
    h['hello']='world'
    assert(h.encryptFile()==0)
    assert(h.checkEncryptionValidity()==0)