from numb3rs import validate

def test_validate_true():
    assert validate("1.1.1.1") == True
    assert validate("234.244.4.4") == True
    assert validate("0.0.0.0") == True
     
def test_validate_false():
    assert validate("123.34.44") == False
    assert validate("cat") == False      
    assert validate("334.5.5.5") == False 
