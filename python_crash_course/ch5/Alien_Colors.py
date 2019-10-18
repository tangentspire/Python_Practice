alien_color_1 = 'green'
alien_color_2 = 'yellow'
alien_color_3 = 'red'

def add_score(alien_type):
    score = 0
    if alien_type == 'green':
        score += 5
        print("You earned 5 points")
    elif alien_type == 'yellow':
        score += 10
        print("You earned 10 points")
    elif alien_type == 'red': 
        score += 15
        print("You earned 15 points")
    
add_score(alien_color_1)
add_score(alien_color_2)
add_score(alien_color_3)
