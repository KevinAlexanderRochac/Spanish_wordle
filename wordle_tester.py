
# Project 1
# Spring 2023

from wordle import *

print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print('Testing check_word function')
print(check_word("OPENS","EPICS"))    # ( "EPICS", ["yellow", "green", "grey", "grey", "green"] )
print(check_word("MISTS","MISTY"))    # ( "MISTY", ["green", "green", "green", "green", "grey"] )
print(check_word("LERED","DRUID"))    # ( "DRUID", ["grey", "yellow", "grey", "grey", "green"] )
print(check_word("ELUDE","LEDGE"))    # ( "LEDGE", ["yellow", "yellow", "yellow", "grey", "green"] )
print(check_word("CRANE","BEEPS"))    # ( "BEEPS", ["grey", "yellow", "grey", "grey", "grey"] )
print(check_word("ROBOT","REORG"))    # ( "REORG", ["green", "grey", "yellow", "grey", "grey"] )
print('check_word completed')
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print()
print('Testing known_word function')
print(known_word([('EPICS', ['yellow', 'green', 'grey', 'grey', 'green'])]))               #_P__S
print(known_word([('LEAPS', ['grey', 'yellow', 'grey', 'grey', 'grey']), ('THRID',['grey','green','yellow','grey','grey'])]))   #_H___
print(known_word([('LEAPS', ['grey', 'yellow', 'grey', 'grey', 'grey']), ('THRID',['grey','green','yellow','grey','grey']),('CHEER',['grey','green','green','yellow','yellow'])]))   #_HE__
print(known_word([('LEAPS', ['grey', 'yellow', 'grey', 'grey', 'grey']), ('THRID',['grey','green','yellow','grey','grey']),('CHEER',['grey','green','green','yellow','yellow']),('THERE',['grey','green','green','green','green'])]))   #_HERE
print(known_word([('LEAPS', ['grey', 'yellow', 'grey', 'grey', 'grey']), ('THRID',['grey','green','yellow','grey','grey']),('CHEER',['grey','green','green','yellow','yellow']),('THERE',['grey','green','green','green','green']),('WHERE',['green','green','green','green','green'])]))   #WHERE
print('known_word completed')
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print()
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print('Testing no_letters function')
print(no_letters([('EPICS', ['yellow', 'green', 'grey', 'grey', 'green'])]))               #CI
print(no_letters([('LEAPS', ['grey', 'yellow', 'grey', 'grey', 'grey']), ('THRID',['grey','green','yellow','grey','grey'])]))   #ADILPST
print(no_letters([('LEAPS', ['grey', 'yellow', 'grey', 'grey', 'grey']), ('THRID',['grey','green','yellow','grey','grey']),('CHEER',['grey','green','green','yellow','yellow'])]))   #ACDILPST
print(no_letters([('LEAPS', ['grey', 'yellow', 'grey', 'grey', 'grey']), ('THRID',['grey','green','yellow','grey','grey']),('CHEER',['grey','green','green','yellow','yellow']),('THERE',['grey','green','green','green','green'])]))   # ACDILPST
print(no_letters([('LEAPS', ['grey', 'yellow', 'grey', 'grey', 'grey']), ('THRID',['grey','green','yellow','grey','grey']),('CHEER',['grey','green','green','yellow','yellow']),('THERE',['grey','green','green','green','green']),('WHERE',['green','green','green','green','green'])]))   #ACDILPST
print('no_letters completed')
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print()
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print('Testing yes_letters function')
print(yes_letters([('EPICS', ['yellow', 'green', 'grey', 'grey', 'green'])]))               #EPS
print(yes_letters([('LEAPS', ['grey', 'yellow', 'grey', 'grey', 'grey']), ('THRID',['grey','green','yellow','grey','grey'])]))   #EHR
print(yes_letters([('LEAPS', ['grey', 'yellow', 'grey', 'grey', 'grey']), ('THRID',['grey','green','yellow','grey','grey']),('CHEER',['grey','green','green','yellow','yellow'])]))   #EHR not EHREER
print(yes_letters([('LEAPS', ['grey', 'yellow', 'grey', 'grey', 'grey']), ('THRID',['grey','green','yellow','grey','grey']),('CHEER',['grey','green','green','yellow','yellow']),('THERE',['grey','green','green','green','green'])]))   #EHR
print(yes_letters([('LEAPS', ['grey', 'yellow', 'grey', 'grey', 'grey']), ('THRID',['grey','green','yellow','grey','grey']),('CHEER',['grey','green','green','yellow','yellow']),('THERE',['grey','green','green','green','green']),('WHERE',['green','green','green','green','green'])]))   #EHRW
print('yes_letters completed')
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print()

