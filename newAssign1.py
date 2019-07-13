from sys import exit
import csv

class Student(object):

    def __init__(self, name):
        self.name = name
        self.coins = 0
        self.steps = 0
        self.count = 0

# --------------Functions---------------------------

    def getName(self):
        return self.name

    def print_name(self):
        print(self.name)


    def score(self):
        self.coins = self.coins + 20

    def print_score(self):
        print("Total no. of coins ", end = '')
        print(self.coins)
        return self.coins

    def moves(self):
        self.steps = self.steps + 1

    def print_moves(self):
        print("Total no. of moves ", end = '')
        print(self.steps)
        return self.steps

    def setChoice(self, choice):
        self.choice = choice

    def getChoice(self):
        return self.choice

    def start(self):
        self.ellHall()

    def numLives(self):
        self.count = self.count + 1

    def print_numLives(self):
        print("no. of counts", self.count)

    def check(self):

        self.print_moves()
        self.print_score()
        self.numLives()
        self.print_numLives()

        if self.count == 3:
            print("As you have no lives left, You are DEAD")
            ls = []
            ls.append(self.name)
            ls.append(str(self.print_score()))
            ls.append(str(self.print_moves()))
            print("list is",ls)
            outF = open("assign1.txt", "w")
            for line in ls:
                outF.write(line)
                outF.write(",")
            outF.close()


            exit(0)

        else:
            self.game()



    def game(self):

        print("Your Total Score")


        print("Do you want to play again? (y/n)")

        choice = input("please enter your choice")

        #while self.setChoice(choice) != "y" and self.setChoice(choice) == "n":

        if choice == "y" or choice == 'Y':

            self.start()

        elif choice == "n" or choice == 'N':
            print("Your Total Score")
            self.print_moves()
            self.print_score()
            exit(0)

        else:
            print('Invalid Choice')
            self.game()

    # EllHall

    def ellHall(self):

        print("You want to take admission at Northeastern University")
        print("You are at Ell Hall where you can pay the fees, So you have to select which floor you want to go ")
        print("There are 5 choices 1, 2,3,4, 5 ")
        print("Lets START THE GAME")

        choice = input("> ")

        self.moves()

        self.print_moves()

        if "1" in choice:
            print("You are at Blackmann Auditorium")
            print('you lose the game')
            self.check()


        elif choice == '2':
            print('YOU LOSE THE GAME, This is not the right choice, You reached OGS')
            self.check()

        elif choice == '3':
            print("You are at Sacred Space")
            print('you lose the game')
            self.check()

        elif choice == '4':
            print("You are at Financial Center, Pay the fees")
            print("So You cleared 1st level")
            print("Now let's move to next level")
            self.score()
            self.print_score()
            self.curryCenter()



        elif choice == '5':
            print("You chose the wrong floor, there is no 5th floor. So you lose the game")
            print('you lose the game')
            self.check()


        else:
            self.ellHall()



    def curryCenter(self):

        print("Now you are at Curry Center and you want to grab Husky Id ")
        print("So you have to select which floor you want to go to grab husky id ")
        print("There are 5 choices 1, 2,3,4, 5 ")
        print("Lets START THE GAME")

        choice = input("> ")

        self.moves()
        self.print_moves()

        if choice == '1':
            print("You are at 1st, It seems you are hungry so you can have food from Popeye's or can go to After Hours to have some fun")

            print('you lose the game')
            self.check()

        elif "2" in choice:
            print("You are at 2nd Floor, where You can get the Husky Id")
            print("you selected the correct choice and now you are at 3rd level")
            print("Now let's move to next level")
            self.score()
            self.print_score()
            self.library()




        elif choice == '3':
            print("You can go to Info Session in 303 Room")
            print('you lose the game')
            self.check()

        elif choice == '4':
            print("You are at Financial Center, Pay the fees")
            print("So You cleared 1st level")
            print('you lose the game')
            self.check()


        elif choice == '5':
            print("So you wanna hang out and play games but still you have to find the husky id")
            print('you lose the game')
            self.check()

        else:
            self.curryCenter()

    def library(self):

        print("Now you are at library and you want to take prints of your resume ")
        print("So you have to select on which floor you can get the resume ")
        print("There are 5 choices 1, 2,3,4,5 , 5th is basement")
        print("Let's START ")

        choice = input("> ")

        self.moves()
        self.print_moves()

        if choice == '1':
            print("You are at 1st, It seems you can take the prints of your resume and then what, YOU CLEARED THE STAGE")
            print("Now let's move to next level")
            self.score()
            self.print_score()
            self.stearnsCenter()



        elif "2" in choice:
            print("You are at 2nd Floor, It seems you can take the prints of your resume and then what, YOU CLEARED THE STAGE")
            print("Now let's move to next level")
            self.score()
            self.print_score()
            self.stearnsCenter()

        elif choice == '3':
            print("You can go to Quiet Study space where you can study")
            print('you lose the game')
            self.check()

        elif choice == '4':
            print("You are very serious and you like to study in a quiet space, so here you are at 4th Floor")
            print('you lose the game')
            self.check()

        elif choice == '5':
            print("It seems you have classes, go fast Don't be late")
            print('you lose the game')
            self.check()

        else:
            self.library()


    def stearnsCenter(self):

        print("You are at Stearns Hall")
        print("You have to grab a card to enter cabot center for career fair So you have to select in which gates you want to go ")
        print("There are 5 choices 1, 2,3,4, 5 ")
        print("Lets START ")

        choice = input("> ")
        self.moves()
        self.print_moves()


        if "1" in choice:
            print("You came to review your resume")
            print('you lose the game')
            self.check()

        elif '2' in choice:
            print("You can grab entry card to go to the career fair")
            self.cabotCenter()
            self.score()
            self.print_score()


        elif '3' in choice:
            print("It seems you are hungry and that's why you chose the gate where there is Dunkin, Go grab some coffee and food stuff from Dunkin")
            print('you lose the game')
            self.check()

        elif choice == '4':
            print("You can review your cover letter")
            print('you lose the game')
            self.check()

        elif choice == '5':
            print("It seems you forgot your resume at the front desk in library.You chose this magic door from where you'll directly go to library. Go and take your resume. ")
            self.library()
            print('you lose the game')
            self.check()

        else:
            self.stearnsCenter()


    def cabotCenter(self):
        print("Finally you are at Cabot center")
        print("You have to grab a card to enter cabot center for career fair So you have to select in which gates you want to go ")
        print("There are 5 choices 1, 2,3,4, 5 ")
        print("Lets START ")

        choice = input("> ")
        self.moves()
        self.print_moves()

        if "1" in choice:
            print("You came to review your resume")
            print('you lose the game')
            self.check()

        elif '2' in choice:
            print("YOU WON THE GAME")
            print("You can grab entry card to go to the career fair")
            self.score()
            self.print_score()


        elif '3' in choice:
            print("It seems you are hungry and that's why you chose the gate where there is Dunkin, Go grab some coffee and food stuff from Dunkin")
            print('you lose the game')
            self.check()

        elif choice == '4':
            print("You can review your cover letter")
            print('you lose the game')
            self.check()

        elif choice == '5':
            print("It seems you forgot your resume at the front desk in library.You chose this magic door from where you'll directly go to library. Go and take your resume. ")
            self.library()
            self.check()


        else:
            self.stearnsCenter()


def name():
    s = input("please enter your First name  -  ")
    s = s.strip()
    if s.isalpha():

        print("Let's Start")
        st = Student(s)
        st.getName()
        print("after getName")
        st.print_name()
        print("b4 start")
        st.start()
        print("after start")

    else:
        print("invalid characters, please include only strings")
        name()


print("Hello, what is your name?")

name()
