def zero():
    print(" ")
    print(" +---+")
    print(" |   |")
    print("     |")
    print("     |")
    print("     |")
    print("     |")
    print("========")

def one():
    print(" ")
    print(" +---+")
    print(" |   |")
    print(" O   |")
    print("     |")
    print("     |")
    print("     |")
    print("========")

def two():
    print(" ")
    print(" +---+")
    print(" |   |")
    print(" O   |")
    print(" |   |")
    print("     |")
    print("     |")
    print("========")

def three():
    print(" ")
    print(" +---+")
    print(" |   |")
    print(" O   |")
    print("/|   |")
    print("     |")
    print("     |")
    print("========")
    
def four():
    print(" ")
    print(" +---+")
    print(" |   |")
    print(" O   |")
    print("/|\  |")
    print("     |")
    print("     |")
    print("========")
    
def five():
    print(" ")
    print(" +---+")
    print(" |   |")
    print(" O   |")
    print("/|\  |")
    print("/    |")
    print("     |")
    print("========")

def final():
    print(" ")
    print(" +---+")
    print(" |   |")
    print(" O   |")
    print("/|\  |")
    print("/ \  |")
    print("     |")
    print("========")


val = 0
def test():
    global val
    updatedWord = []
    Secret = "arin"
    for i in range (0, len(Secret)):
        updatedWord.append("_")
    def guesses(fail):
        for i in range (0, len(Secret)):
            print(updatedWord[i], end =" ")
        Letter = str(input("What is your guess: "))
        val = Secret.find(Letter)
        if Secret.find(Letter) == -1:
            return "Wrong Letter"
            fail = fail + 1
            if fail == 1:
                one()
                guesses(1)
            if fail == 2:
                two()
                guesses(2)
            if fail == 3:
                three()
                guesses(3)
            if fail == 4:
                four()
                guesses(4)
            if fail == 5:
                five()
                guesses(5)
            if fail == 6:
                final()
                
            if final():
                print ("Failed")
        else:
            del updatedWord[val]
            updatedWord.insert(val, Letter)
            for i in range (0, len(Secret)):
                print(updatedWord[i], end =" ")
            if fail == 0:
                zero()
            if fail == 1:
                one()
            if fail == 2:
                two()
            if fail == 3:
                three()
            if fail == 4:
                four()
            if fail == 5:
                five()
        
    guesses(0)           
    