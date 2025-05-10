from entites.enemy import Enemy

#In class you declare enemies, you can use them easily by enemies.X
class Enemies():

    rat = Enemy("Monster rat","A big rat", '''       ____()()
          /      @@
    `~~~~~\\_;m__m._>o ''', 30, 5,2)
    bird = Enemy("Big bird","A bird of pray", '''  `-`-.
      '( @ >
       _) (
      /    )
     /_,'  / 
       \\  / 
       m""m''', 25, 2,4)
    frog = Enemy("Posion Frog","A poisonus frog",'''              _         _
      __   ___.--'_`. 
     ( _`.'. -   'o` )
     _\\.'_'      _.-' 
    ( \\`. )    //\\`   
     \\_`-'`---'\\\\__,  
      \\`        `-\\   
       `              ''',25,3,3)
    cerberus = Enemy("","",'''                            /\\_/\\____,
              ,___/\\_/\\ \\  ~     /
              \\     ~  \\ )   XXX
                XXX     /    /\\_/\\___,
                   \\o-o/-o-o/   ~    /
                    ) /     \\    XXX
                   _|    / \\ \\_/
                ,-/   _  \\_/   \\
               / (   /____,__|  )
              (  |_ (    )  \\) _|
             _/ _)   \\   \\__/   (_
     b'ger  (,-(,(,(,/      \\,),),)''',80,8,2)