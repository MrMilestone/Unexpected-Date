# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define n = Character("") #narrator
define p = Character("Paul") #Main Character
define m = Character("Miska") #Girl NPC
define b = Character("Brother") #No longer used

define choice1 = False
define choice2 = False
define choice3 = False


$ Name = _return

image bigperson = im.Scale("bigperson.png", 70, 100)

image fr = "forestroad.png"
image frb = "background forest road busstop.png"
image h = "background highway night.png"
image hd = "background highway dusk.png"
image povp = "Car fpov 2 phone on.png"
image povpoff = "car fpov 2 phone off.png"
image rb = "Road block.png"
image miska i = im.Scale ("miskaidlemclosed.png", 500, 500)
image miska it = im.Scale ("Miska Idle talking.png", 500, 500)
image miska p = im.Scale ("Miska pleased mouth closed.png", 500,500)
image miska pt = im.Scale ("Miska pleased talking.png", 500, 500)
image miska c = im.Scale ("Miska crying talking.png", 500, 500)
image miska a = im.Scale ("Miska annoyed talking.png", 500, 500)
image miska ct = im.Scale ("Miska crazy talking.png", 500, 500)

image hearts = im.Scale("Hearts.png", 500 ,500)



#A1 Branching to different Scene
#A2 Branching to different Scene //Nothing yet
#A3 Branching to different Scene //Nothing yet
#A4 is End Good ending Scene
#A5 Bad ending



label start:

    $ Chances = 0
    $ Time = False



    #ACT 1
    scene h
    show povp
    #phone ping sound
    #image phone

    n "it is a late cold night, lights of various christmas decorations are hanging in peoples gardens"

    n "just as you enter your car to head over to the family dinner you hear your phone ring."
    b "Bro! Are you coming over already, we have already waiting the food and we haven't heard a word from you"

    p "ugh friend always gets so impatient during the holidays, most of the family probably isn't going to be on time anyways"



    p "probably shouldn't complain to much though, their christmas dinners always taste the best"


    b "hello... do you even have your phone turned on, if you don't respond we are just gonna start without you"


    menu:
        "phone text: give me 5 minutes, i literally just got inside the car":
            n "..."

        "don't respond":
            n "..."

    b "why is it that you can never show up on time anyways, I messaged you serveral times before hand when to be here"

    menu:
        "turn off phone":
            n "beep"

        "phone text: i'm sorry i will try better next time":
            b "you better..."

    #image road block
    "as you were fiddeling with your phone you suddenly see a large barrier blocking the road"
    hide povp
    show povpoff
    show rb

    p "oh darn it just my luck, now i am gonna be late for sure"

    n "You took a side road that takes you through the forest"
    scene black
    hide povpoff
    hide rb
    n "After some time driving you come to the conclution: You are lost."

    #ACT2
    scene fr
    show povroff

    n "You have been driving for a few hours"

    n "The road splits into two."
    n "The left path looks more used. The right road looks wider"

    menu:
        "I choose right. The wider the better":
            n "You spot a light at the horizon"

        "I choose to go left. I think more people use this road":
            n "You spot a light at the horizon"


    n "You come to a stop where the light is:"
    hide povroff
    show frb
    show povroff

    n "There is an old bus stop and a what looks to be a girl sitting a the bustop."

    n "Maybe she knows the way around"
    menu:
        "I stop infront and lower my car window":
            p "Excuse me, miss"

    hide povroff
    show miska i at top
    show povroff

    m "What's up?"
    menu:
         "I believe Im lost.":
            m "Yeah I noticed."

            p "Do you know a way out of the forest?"
            m "Ofcourse!"


         "Do you know where I am?":
            m "hehe, you lost cutie?"
            p "I believe I am. Do you know a way out of the forest?"
            $ Chances += 1
    hide miska i
    hide povroff
    show miska it at top
    show povroff
    m "What is your name?"



    menu:
        "Paul":
            m "What a lovely name"
            $ Name = "Paul"

        "I rather not say it":
            m "Ohh. I understand cutie"
            $ Name = "cutie"

        #$ Nanem False

    m "Well [Name], I am Miska. What about an deal?"
    m "If you take me home, I will guide you out of the forest aaaand maybe something more."
    hide miska it
    hide povroff
    show hearts
    show miska p at top
    show povroff
    m "How does it sound?"
    hide hearts

    menu:
        "Look, I am kind of running late to the christmas dinner":
            m "Well if you are late, then why dont you join mine?"


        "Im not so sure about that":
            m "Come on [Name], you are not going to leave a girl alone in christmas eve, are you?"


    n "At this point the girl called Miska, is close enough for you to notice how beautiful she is"
    n "Blue eyes, blond hair and amazing lips. She wears a red dress, probably for Christmas eve."

    hide miska p
    hide povroff
    show miska pt at top
    show povroff

    m "Are you sure I cannot change your mind?"
    m "I dont live that far..."
    n "She winks at me"
    jump A1

label A1:



    scene frb
    show miska p at top
    show povroff
if  choice1  and choice2 and choice3 :

    jump A5

else:
    menu:
        "If you dont live that far, how did you end up here?":
            jump A2

        "Can you not call some one to pick you up?":
            jump A3

        "Why don't you take the bus?":
            jump A4




label A2:
    scene frb
    show miska it at top
    show povroff
    m "I came from a friends home"
    m "I took the bus across but there was a deviation and I had to change the bus here"
    show miska c
    m "The driver promised me there was another bus, but as you can see...I have been waiting for an hour now..."
    $ choice1 = True

    jump A1




label A3:
    scene frb
    show miska c at top
    show povroff at top
        #show pov view with woman
    m "My phone died an a hour ago"
    menu:
        "I could call someone to pick you up":
            hide povroff
            hide miska c
            show miska a at top
            show povroff
            m "I tried before [Name], but they are all partying"

            hide povroff
            hide miska a
            show miska pt at top
            show povroff
            m "You could join me and call your family to let them know that you will be ok..."
            show hearts at top
            m "I promise you [Name], you will have a night you wont forget"
            $ choice2 = True

            jump A1

label A4:
    scene frb
    show miska c at top
    show povroff
    m "I have been waiting for ever for the last bus!"
    m "I think there are no more buses"
    $ choice3 = True
    jump A1





        #ACT 3
label A5:
    scene frb
    show miska pt at top
    show povroff

    m "so [Name], do you wanna come to my place?"

    menu:

        "You know what? At this point I have been lost for so long that all the food has probably been eaten already. So sure, why not":
            jump A6

            # good ending
        "i am sorry but I really have to get going now":
            hide povroff
            hide miska pt
            show miska a at top
            show povroff
            m "i really don't think that you should"

    p "Well it's not your choice now is it"
    hide povroff
    hide miska a
    show miska ct at top
    show povroff
    m "i don't think you understand how much effort i put into this [Name]"
    p "what?"
    n "you suddenly feel miska grabing tightly onto your arm"
    m "open the door [Name]"
        #knife drawing effect
    scene black

    n "before you can protest, you can feel a knife being held tigthly to your throat"
    n "fear paralyzes you unable to move miska reaches her hand through the window to pull the door open"
    n "at this point you have accepted your fate when you suddenly see headlights in the distance"
        #car honking noise

    n "the moment this happens the presure on your arm is gone as miska has run off into the forest"
    b "Paul what are you doing all the way out here, who was that woman standing next to your car"
    p "I will explain later let's get home quickly!"

    n "the moment this happens the presure on your arm is gone as miska has run off into the forest"
    b "hey paul what's going on, who was that woman standing next to your car"
    p "i will explain later let's get home for now"



        #epiloge
    p "that night i ended up calling the police to make a report, but in the end they were never able to find a suspect"
    p "i do wonder sometimes what they would have done if they had managed to get inside my car"
    p "she has seen my license plate, hopefully she doesn't come back to finish the job"
    p "one thing is for sure, i am never driving alone at night again"



    return

label A6:
    scene frb
    show hearts at top
    show miska pt at top
    show povroff
        # bad ending

    m "i'm so happy right now, let me get in, this is gonna be a very short drive"
    hide miska pt
    n "you unlock the car door and she gets into the passanger seat on your left"
        #engine starts
    n "after a few minutes of following her directions you notice that the road seems to go deeper and deeper into the forest"
    n "while glancing from the road she seems to be  figeting a lot with her hands"
    hide povroff
    show hd
    show rb
    show povroff
    n "after a while the road stops and you hit a dead end"

    p "uhm... miska what exactly is this place?"

    m "Paul i'm sorry but i haven't been enterily honest with you"
        #knife drawing effect
    show black
    n "before you can even say a word you can feel a knife enter your arm"
    n "you try to get out of the car but as you do you can feel the knife going through your back paralyzing you"
    n "your vision goes dark as the repeated stabbing in your back starts to feel faint"
        #epiloge
    n "after not showing up to the christmas dinner the family reported you missing in the early morning"
    n "a search and resque team was sent out finding you 7 hours later laying right outside of your car in a pool of blood"
    n "after a medical examination you were detirmend to have past away from your injuries 12 hours ago"
    n "with no finger prints or witnesses the trail quickly ran cold and no one suspect was ever found"





    return
