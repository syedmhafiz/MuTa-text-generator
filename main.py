import random as rd

def raDU(ch):  
    ch = ch.upper()

    return ch

def raDL(ch):    
    ch = ch.lower()

    return ch

def intensify(an):
    if an == 1:
        return rd.randint(2, 10)
    elif an == 2:
        return rd.randint(2, 5)
    else:
        return rd.randint(2, 3)        

def gene(txt):
    new_txt = ""
    for i in range(len(txt)):
        re = intensify(intensity)

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
    intensity = int(input("Enter the intensity level out of 1 to 3: "))
    w = gene(q)
    print("The murad takla version of your text is: ", w)