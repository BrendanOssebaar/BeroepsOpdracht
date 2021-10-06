from time import sleep
while True:
    print("You wake up, cold and wet, you partied too hard last night and now you wake up in the park")
    sleep(2)
    print("People are looking at you disapprovingly")
    sleep(2)
    print("You can:")
    print("A: Yell:'Take a picture it'll last longer!'")
    print("B: Say:'Heyo, how you doin?")
    print("What do you do?")
    choice1 = input()
    if choice1 == "a" or choice1 == "A":
        print("One person calls the cops while another makes sure you don't leave, you are send to jail for public drunkeness. You lose")
        sleep(4)
        print("Do you want to try again? Y/N")
        i = input()
        if i == "N":
            break
    elif choice1 == "b" or choice1 == "B":
        print("One person asks you if you're alright and helps you up. It's a nice looking lady")
        sleep(2)
        print("You can:")
        print("A: Thank the lady and tell her you had a little too much fun last night and you want to go home, but need a little help")
        print("B: You try to grope her")
        print("What do you do?")
        choice2 = input()
        if choice2 == "a" or choice2 == "A":
            print("The nice looking lady helps you find the nearest busstop and gives you money for a ticket and her phone number")
            sleep(2)
            print("You get home after a couple minutes and realize you forgot to ask the nice lady's name")
            sleep(2)
            print("Lukily you got her number, but what to send?")
            sleep(2)
            print("Do you:")
            print("A: Tell her you forgot to ask her name and like to officially thank her with a coffee")
            print("B: Ask her if she's single")
            print("What do you do?")
            choice2a = input()
            if choice2a == "a" or choice2a == "A":
                print("She tells you her name is Sam and she would love that, she tells you to meet her at the coffee shop nearby")
                sleep(2)
                print("You feel ecstatic to meet Sam")
                sleep(2)
                print("but what to wear?")
                print("A: Casual but formal")
                print("B: A fursuit")
                print("What do you choose?")
                choice2aa = input()
                if choice2aa == "a" or choice2aa == "A":
                    print("You meet Sam at the coffee shop, she seems happy to see you")
                    sleep(2)
                    print("You thank her, you have a little chat and drink some coffee")
                    sleep(2)
                    print("That's the last time you see her, you lost")
                    print("Would you like to try again? Y/N")
                    a = input()
                    if a == ("N"):
                        break
                elif choice2aa == "b" or choice2aa == "B":
                    print("You meet Sam at the coffee shop, she is shocked to find out its you in a fursuit")
                    sleep(2)
                    print("But, she is not unhappy to learn that you are a furry, she actually admits to be one as well")
                    sleep(2)
                    print("from that day on, you and Sam go to furrycons together, you build up a relationship together and live happily ever after")
                    sleep(2)
                    print("You win, well done! Want to try other routes? Y/N")
                    b = input("")
                    if b == ("N"):
                        break
            elif choice2a == "b" or choice2a == "B":
                print("She says no, but she has a friend that is single, would you like to meet her?")
                sleep(1)
                print("You say:")
                print("A: That would be nice, shall we meet at the café?")
                print("B: Is she hot??")
                choice2ab = input()
                if choice2ab == "b" or choice2ab == "B":
                    print("She blocks your phone number. You lose, try again? Y/N")
                    c = input
                    if c == ("N"):
                        break
                elif choice2ab == "a" or choice2ab == "A":
                    print("You meet at the café and she introduces herself as Sam and her friend Laura, who is just as pretty as her")
                    sleep(2)
                    print("")

                
                



