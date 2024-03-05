print('''
                                   ._
                                 ,(  `-.
                               ,': `.   `.
                             ,` *   `-.   \
                           ,'  ` :+  = `.  `.
                         ,~  (o):  .,   `.  `.
                       ,'  ; :   ,(__) x;`.  ;
                     ,'  :'  itz  ;  ; ; _,-'
                   .'O ; = _' C ; ;'_,_ ;
                 ,;  _;   ` : ;'_,-'   i'
               ,` `;(_)  0 ; ','       :
             .';6     ; ' ,-'~
           ,' Q  ,& ;',-.'
         ,( :` ; _,-'~  ;
       ,~.`c _','
     .';^_,-' ~
   ,'_;-''
  ,,~
  i'
  :
  ''')

print("Hello and Welcome to the TreasureQuest.")
print("Your mission is to find the treasure.")

choice_1 = input("You're at a crossroad. Where do you want to go? Type \"left\" or \"right\": ")
if choice_1 == "left":

    c01 = input("You've come to a lake. There is an island in the middle of the lake. Type \"wait\" to wait for a boat. Type \"swim\" to swim across. ")

    if c01 == "wait":
        c02 = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow, and one blue. Which color do you choose? ")

        if c02 == "red":
            print("It's a room full of fire. Game Over.")
        elif c02 == "yellow":
            print("You found the treasure! You Win!")
        else:
            print("You enter a room of beasts. Game Over.")
    else:
        print("You get attacked by an angry trout. Game Over.")

else:
    print("You fell into a hole. Game Over.")

