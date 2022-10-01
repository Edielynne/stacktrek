day = int(input())
month = input()
a_sign =""
if month == 'december':
    if day < 22:
        a_sign = 'Sagittarius' 
    else:
        a_sign = 'Capricorn' 

elif month == 'january':
    if day < 20:
        a_sign = 'Capricorn' 
    else:
        a_sign = 'Aquarius'

elif month == 'february':
    if day < 19:
       a_sign = 'Aquarius'  
    else:
        a_sign =  'Pisces'

elif month == 'march':
    if day < 21:
        a_sign = 'Pisces' 
    else:
        a_sign='Aries'

elif month == 'april':
    if day < 20:
        a_sign = 'Aries' 
    else:
        a_sign = 'Taurus'
elif month == 'may':
    if day < 21:
         a_sign = 'Taurus'
    else:
        a_sign = 'Gemini'

elif month == 'june':
    if day < 21:
        a_sign = 'Gemini'
    else:
        a_sign =  'Cancer'
elif month == 'july':
    if day < 23:
        a_sign = 'Cancer'
    else:
        a_sign = 'Leo'

elif month == 'august':
    if day < 23:
        a_sign = 'Leo' 
    else:
        a_sign = 'Virgo'
elif month == 'september':
    if day < 23:
        a_sign = 'Virgo' 
    else:
        a_sign = 'Libra'
elif month == 'october':
    if day < 23:
        a_sign = 'Libra' 
    else:
        a_sign = 'Scorpio'
elif month == 'november':
    if day < 22:
        a_sign = 'Scorpio'
    else:
        a_sign = 'Sagittarius'

print (f"Your Astrological sign is : {a_sign}")