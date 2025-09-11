def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    if not (2 <= len(s) <= 6):
        return False
    if not (s[0].isalpha() and s[1].isalpha()):
        return False
    number_started = False
    for ch in s:
        if ch.isdigit():
            if not number_started:
                number_started = True
                if ch == "0":    
                    return False
        else:
            if number_started:   
                return False
    return s.isalnum()
          
                                                                                                                                                                                                                
    

    
                                    


main()