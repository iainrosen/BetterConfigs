from src.betterconfigs import *
import os
import pytest
def test_cleanup():
    try:
        os.remove('test.config')
    except:
        pass
    assert(os.path.exists('test.config')==False)
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
    h = config('test.config')
    assert(h['_encrypted']==False)
    assert(h.encKey!=None)
    h['hello']='world'
    assert(h.encryptFile()==0)
    assert(h['hello']=='world')
    assert(h.getRaw('hello')!='world')
    assert(h.getRaw('_version')=='0.8.1')
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
    os.remove('test.config')
def test_encdec():
    h = config('test.config')
    h['hello']='world'
    assert(h.encryptFile()==0)
    h['hello2']='world2'
    encryptionKey = h.encKey
    t = config('test.config')
    t.encKey = encryptionKey
    assert(t['hello']=='world')
    assert(t['hello2']=='world2')
    assert(t.decryptFile()==0)
    os.remove('test.config')
def test_encdec_int():
    h = config('test.config')
    h['hello']='world'
    assert(h.encryptFile()==0)
    h['hello2']=3
    assert(h['hello2']==3)
    os.remove('test.config')
def test_encdec_bool():
    h = config('test.config')
    h['hello']='world'
    assert(h.encryptFile()==0)
    h['hello2']=True
    assert(h['hello2']==True)
    os.remove('test.config')
def test_encdec_list():
    h = config('test.config')
    h['hello']='world'
    assert(h.encryptFile()==0)
    h['hello2']=['hello','world']
    assert(h['hello2']==['hello','world'])
    os.remove('test.config')
def test_encdec_badtype():
    h = config('test.config')
    h['hello']='world'
    assert(h.encryptFile()==0)
    with pytest.raises(Exception):
        h['hello2']=21.49857203958
    os.remove('test.config')