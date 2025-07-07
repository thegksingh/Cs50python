#defined function convert() and gave an argument 'face' whicn is variable 
def convert(face):

#also replaced value to emoji if variable face have :) or :(
    face = face.replace (":)" , "🙂")
    face = face.replace (":(" , "☹️")


#return the input value to user after making desired change 
    return face 

#input is stored in variable face after taking it from user
def main():
    face = input ("what's your name? ")

 #print function convert which has input Variable face as argument    
    print(convert(face))



if __name__ == "__main__":
    main()









