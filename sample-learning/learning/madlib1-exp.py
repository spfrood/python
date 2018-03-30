#!/usr/bin/env python3
"""
String Substitution for a Mad Lib
Adapted from code by Kirby Urner
"""                                                  

storyFormat = """                                       
1 is {animal}
2 is {animal}
3 is {food}
4 is {food}
5 is {animal}
6 is {food} middle
7 is {animal}
8 is {city}
9 is {food}
10 is {animal}
11 is {food}.

The End
"""                                                 

def tellStory():                                     
    userPicks = dict()                              
    addPick('animal', userPicks)            
    addPick('food', userPicks)            
    addPick('city', userPicks)            
    story = storyFormat.format(**userPicks)
    print(story)
    print (userPicks)
                                                    
def addPick(cue, dictionary):
    '''Prompt for a user response using the cue string,
    and place the cue-response pair in the dictionary.
    '''
    prompt = 'Enter an example for ' + cue + ': '
    response = input(prompt).strip() # 3.2 Windows bug fix
    dictionary[cue] = response                                                             

tellStory()                                         
input("Press Enter to end the program.")        
