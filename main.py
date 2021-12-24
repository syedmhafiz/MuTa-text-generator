import random as rd

def raDU(ch):  
    ch = ch.upper()

    return ch

def raDL(ch):    
    ch = ch.lower()

    return ch

def gene(txt):
    new_txt = ""
    for i in range(len(txt)):
        re = rd.randint(2, 5) 

        if ord(txt[i]) in range(97, 123):
           if re % 2:
               new_txt += raDL(txt[i])
           else:
                new_txt += raDU(txt[i])
        elif ord(txt[i]) in range(65, 91):
            if re % 2:
               new_txt += raDL(txt[i])
            else:
                new_txt += raDU(txt[i])               
        else:
            new_txt += txt[i]    
        
    return new_txt        


if __name__ == "__main__":
    q = input("Enter the text(5 - 30 characters max):")
    w = gene(q)
    print("The murad takla version of your text is: ", w)