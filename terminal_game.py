#character data
import random
name=input("Enter your name, adventurer: ")
role=int(input("Select your role: \n1) Wizard \n2) Knight \n3) Healer \n"))
list_movements_wiz= ["Fireball","Magic healing","Total Block"] #from this list the player will have 1 randomly
list_movements_heal=["Healing","Revive","Posioning"] #only can have it doing training
list_movements_knight=["Stocade","Barricade","Fire Fist"] #same as wizard
movements_wiz=random.sample(list_movements_wiz,1) #wizard movements only
movements_knight=random.sample(list_movements_knight,1) #same but knight
heal=100 #same for all the roles
goblin_hp=100 #for the unique combat of the game

#adventure for wizard character
if role==1:
    print("Congratulations, you are now a Wizard",name)
    print("This are your first known movements " + str(movements_wiz), "when you level up, you can choose more movements and know more and more, this is only the beggining!")
    path_wiz = int(input( "Let`s start with your adventure!, First, where do you want to go? \n1) City \n2) Training camp \n3) Forest \n"))
   #1rst path, MISSING FOREST
    if path_wiz == 1:
        #end of adventure, Resting on the city
        print("The city seems quiet now, let`s rest for a while")
        print("End of your adventure! for now...you are resting on the city while thinking where to go on your next mission")
    elif path_wiz == 2:
        #training to improve your habilities
        train_wiz = int(input("Lets train ! what training do you want to do? \n1) Healer training \n2) Wizard training \n3) Knight training \n"))
        if train_wiz == 1:
            movements_wiz = random.sample(list_movements_heal, 1) + movements_wiz
            print("Congratulations! the trainning was succesfull! your movements now are: " + str(movements_wiz))
            path2_wiz = int(input("Where do you want to go now? \n1) City \n2) Training camp (You are currently here) \n3) Forest \n"))
           #2nd path DONE
            if path2_wiz == 1:
                #end of the adventure, resting in the city
                print("The city seems quiet now, let`s rest for a while")
                print("End of your adventure! for now...you are resting on the city while thinking where to go on your next mission")
            elif path2_wiz == 2:
                train2_wiz = int(input("What training do you want to do? \n1) Healer training (Done, cant be repeated) \n2) Wizard training \n3) Knight training \n"))
                if train2_wiz == 1:
                    #end of the adventure, fell asleep on training camp
                    print("You already have done this training! Rest for a while while you think what do you want to do...")
                    print("You fell asleep in the training camp, end of your adventure, for now...")
                elif train2_wiz == 2:
                    movements_wiz=random.sample(list_movements_wiz,1) + movements_wiz
                    print("Congratulations! the trainning was succesfull! your movements now are: " + str(movements_wiz))
                    path3_wiz=int(input("Where do you want to go now? \n1) City \n2) Training camp (Currently here) \n3) Forest \n"))
                   #3rd path, DONE
                    if path3_wiz == 1:
                        #end of the adventure, resting in the city
                        print("The city seems quiet now, let`s rest for a while")
                        print( "End of your adventure! for now...you are resting on the city while thinking where to go on your next mission")
                    elif path3_wiz == 2:
                        train3_wiz = int(input("What training do you want to do? \n1) Healer training (Done, cant be repeated) \n2) Wizard training (Done, cant be repeated) \n3) Kninght trainning \n"))
                        if train3_wiz == 1 or 2:
                            # end of the adventure, fell asleep on training camp
                            print("You already have done this training! Rest for a while while you think what do you want to do...")
                            print("You fell asleep in the training camp, end of your adventure, for now...")
                        elif train3_wiz == 3:
                            movements_wiz=random.sample(list_movements_knight,1) + movements_wiz
                            print("Congratulations! the trainning was succesfull! your movements now are: " + str(movements_wiz))
                            path4_wiz = int(input( "Where do you want to go now? \n1) City \n2) Training camp (Currently here, you already have done all your tasks here) \n3) Forest \n"))
                           #4th path, DONE
                            if path4_wiz == 1:
                                #end of adventure, resting in the city
                                print("The city seems quiet now, let`s rest for a while")
                                print("End of your adventure! for now...")
                            elif path4_wiz == 3:
                                print("You walk into the forest...but a goblin jumps out of a bush! ")
                                print("Starting combat.... \n Heal of player: " ,heal, "Heal of the goblin: " ,goblin_hp)
                                attack1=int(input("What movement do you want to use? " , movements_wiz))
                                if attack1== movements_wiz[1]:
                                    goblin_hp-=15
                                    print("HIT! -15Hp, goblin hp: " ,goblin_hp)
                                    print("Watch out! here it comes the goblin attack! ")
                                    dodge=random.randint(1,2)
                                    if dodge == 1:
                                        print("Dodged succesfully!")
                                        attack2=int(input("What movement do you want to use now? " , movements_wiz))
                                        if attack2 == movements_wiz[2]:
                                            goblin_hp-=85
                                            #end of adventure for now, fight won succesfully
                                            print("CRITICAL HIT!, you defeated the goblin, congratulations!")
                                            print("You are tired of the combat, so you search for an inn to rest")
                                            print("End of your adventure! for now...")
                                        else:
                                            heal-=30
                                            print("You are hit!, your hp is now",heal)
                                            attack3=int(input("What movement do you want to use? " , movements_wiz))
                                            if attack3 == movements_wiz[1]:
                                                goblin_hp-=15
                                                print("HIT! -15Hp, goblin hp: ", goblin_hp)
                                                attack4=int(input("What movement do you want to use? ",movements_wiz))
                                                if attack4==movements_wiz[2]:
                                                    goblin_hp-=85
                                                    # end of adventure for now, fight won succesfully
                                                    print("CRITICAL HIT!, you defeated the goblin, congratulations!")
                                                    print("You are tired of the combat, so you search for an inn to rest")
                                                    print("End of your adventure! for now...")
                                    else:
                                        heal-=30
                                        print("You are hit!, your hp is now",heal)
                                        attack5=int(input("What movement do you want to use? " , movements_wiz))
                                        if attack5==movements_wiz[2]:
                                            goblin_hp -= 85
                                            #end of adventure for now, fight won succesfully
                                            print("CRITICAL HIT!, you defeated the goblin, congratulations!")
                                            print("You are tired of the combat, so you search for an inn to rest")
                                            print("End of your adventure! for now...")
                            else:
                                #end of adventure, trainning camp completed
                                print("You already completed all of your tasks here! take a rest, adventurer")
                    else:
                        print("You walk into the forest...but a goblin jumps out of a bush! ")
                        print("Starting combat.... \n Heal of player: ", heal, "Heal of the goblin: ", goblin_hp)
                        attack1 = int(input("What movement do you want to use? ", movements_wiz))
                        if attack1 == movements_wiz[1]:
                            goblin_hp -= 15
                            print("HIT! -15Hp, goblin hp: ", goblin_hp)
                            print("Watch out! here it comes the goblin attack! ")
                            dodge = random.randint(1, 2)
                            if dodge == 1:
                                print("Dodged succesfully!")
                                attack2 = int(input("What movement do you want to use now? ", movements_wiz))
                                if attack2 == movements_wiz[2]:
                                    goblin_hp -= 85
                                    # end of adventure for now, fight won succesfully
                                    print("CRITICAL HIT!, you defeated the goblin, congratulations!")
                                    print("You are tired of the combat, so you search for an inn to rest")
                                    print("End of your adventure! for now...")
                                else:
                                    heal -= 30
                                    print("You are hit!, your hp is now", heal)
                                    attack3 = int(input("What movement do you want to use? ", movements_wiz))
                                    if attack3 == movements_wiz[1]:
                                        goblin_hp -= 15
                                        print("HIT! -15Hp, goblin hp: ", goblin_hp)
                                        attack4 = int(input("What movement do you want to use? ", movements_wiz))
                                        if attack4 == movements_wiz[2]:
                                            goblin_hp -= 85
                                            # end of adventure for now, fight won succesfully
                                            print("CRITICAL HIT!, you defeated the goblin, congratulations!")
                                            print("You are tired of the combat, so you search for an inn to rest")
                                            print("End of your adventure! for now...")
                            else:
                                heal -= 30
                                print("You are hit!, your hp is now", heal)
                                attack5 = int(input("What movement do you want to use? ", movements_wiz))
                                if attack5 == movements_wiz[2]:
                                    goblin_hp -= 85
                                    # end of adventure for now, fight won succesfully
                                    print("CRITICAL HIT!, you defeated the goblin, congratulations!")
                                    print("You are tired of the combat, so you search for an inn to rest")
                                    print("End of your adventure! for now...")
            else:
                print("You walk into the forest...but a goblin jumps out of a bush! ")
                print("Starting combat.... \n Heal of player: ", heal, "Heal of the goblin: ", goblin_hp)
                attack1 = int(input("What movement do you want to use? ", movements_wiz))
                if attack1 == movements_wiz[1]:
                    goblin_hp -= 15
                    print("HIT! -15Hp, goblin hp: ", goblin_hp)
                    print("Watch out! here it comes the goblin attack! ")
                    dodge = random.randint(1, 2)
                    if dodge == 1:
                        print("Dodged succesfully!")
                        attack2 = int(input("What movement do you want to use now? ", movements_wiz))
                        if attack2 == movements_wiz[2]:
                            goblin_hp -= 85
                            # end of adventure for now, fight won succesfully
                            print("CRITICAL HIT!, you defeated the goblin, congratulations!")
                            print("You are tired of the combat, so you search for an inn to rest")
                            print("End of your adventure! for now...")
                        else:
                            heal -= 30
                            print("You are hit!, your hp is now", heal)
                            attack3 = int(input("What movement do you want to use? ", movements_wiz))
                            if attack3 == movements_wiz[1]:
                                goblin_hp -= 15
                                print("HIT! -15Hp, goblin hp: ", goblin_hp)
                                attack4 = int(input("What movement do you want to use? ", movements_wiz))
                                if attack4 == movements_wiz[2]:
                                    goblin_hp -= 85
                                    # end of adventure for now, fight won succesfully
                                    print("CRITICAL HIT!, you defeated the goblin, congratulations!")
                                    print("You are tired of the combat, so you search for an inn to rest")
                                    print("End of your adventure! for now...")
                    else:
                        heal -= 30
                        print("You are hit!, your hp is now", heal)
                        attack5 = int(input("What movement do you want to use? ", movements_wiz))
                        if attack5 == movements_wiz[2]:
                            goblin_hp -= 85
                            # end of adventure for now, fight won succesfully
                            print("CRITICAL HIT!, you defeated the goblin, congratulations!")
                            print("You are tired of the combat, so you search for an inn to rest")
                            print("End of your adventure! for now...")
    else:
        print("You walk into the forest...but a goblin jumps out of a bush! ")
        print("Starting combat.... \n Heal of player: ", heal, "Heal of the goblin: ", goblin_hp)
        attack1 = int(input("What movement do you want to use? ", movements_wiz))
        if attack1 == movements_wiz[1]:
            goblin_hp -= 15
            print("HIT! -15Hp, goblin hp: ", goblin_hp)
            print("Watch out! here it comes the goblin attack! ")
            dodge = random.randint(1, 2)
            if dodge == 1:
                print("Dodged succesfully!")
                attack2 = int(input("What movement do you want to use now? ", movements_wiz))
                if attack2 == movements_wiz[2]:
                    goblin_hp -= 85
                    # end of adventure for now, fight won succesfully
                    print("CRITICAL HIT!, you defeated the goblin, congratulations!")
                    print("You are tired of the combat, so you search for an inn to rest")
                    print("End of your adventure! for now...")
                else:
                    heal -= 30
                    print("You are hit!, your hp is now", heal)
                    attack3 = int(input("What movement do you want to use? ", movements_wiz))
                    if attack3 == movements_wiz[1]:
                        goblin_hp -= 15
                        print("HIT! -15Hp, goblin hp: ", goblin_hp)
                        attack4 = int(input("What movement do you want to use? ", movements_wiz))
                        if attack4 == movements_wiz[2]:
                            goblin_hp -= 85
                            # end of adventure for now, fight won succesfully
                            print("CRITICAL HIT!, you defeated the goblin, congratulations!")
                            print("You are tired of the combat, so you search for an inn to rest")
                            print("End of your adventure! for now...")
            else:
                heal -= 30
                print("You are hit!, your hp is now", heal)
                attack5 = int(input("What movement do you want to use? ", movements_wiz))
                if attack5 == movements_wiz[2]:
                    goblin_hp -= 85
                    # end of adventure for now, fight won succesfully
                    print("CRITICAL HIT!, you defeated the goblin, congratulations!")
                    print("You are tired of the combat, so you search for an inn to rest")
                    print("End of your adventure! for now...")
else:
    print("Invalid input")

