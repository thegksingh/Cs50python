from plates import is_valid

def test_valid():
    assert is_valid("CS50") == True
    assert is_valid("XYS39") == True

def test_nonumber():
    assert is_valid("SC50H") == False
    assert is_valid("HGSs3h") == False

def test_firstalpha():
    assert is_valid("3HDHD") == False
    assert is_valid("237") == False
    assert is_valid("He23") == True

def test_len():
    assert is_valid("HSHC2HH") == False
    assert is_valid("H") == False
    assert is_valid("Wp") == True
     
def test_ch():
    assert is_valid("Hg#7") == False





