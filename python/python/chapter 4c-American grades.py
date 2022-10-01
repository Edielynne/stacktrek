grade = float(input())
unrounded =  float(grade-int(grade))

if unrounded == 0 or unrounded == 0.5:
    if grade <= 10 and grade >=8.5:
        print("Grade A")
    elif grade <=8 and grade >= 7.5:
        print("Grade B")
    elif grade <=7 and grade >= 6.5:
        print("Grade C")    
    elif grade <=6 and grade >= 5.5:
        print("Grade D") 
    else:
        print("Grade F")
else:
     print( "Grades should be rounded to the nearest half point." )