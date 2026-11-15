# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
define false = False
define true = True 
define none = None 
define a = Character("Aveline")
define c = Character("Commissioner")
define dis = dissolve


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg house
    with dis

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show Aveline
    with dis
    "{i}Another day, another commission.{/i}"
    "{i}I don't know how I've kept up so far. None of my commissions so far have looked right{/i}"

    # These display lines of dialogue.

    e "You've created a new Ren'Py game."

    e "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.

    return
