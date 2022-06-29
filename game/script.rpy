# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

image lisa_c2 = "lisa_c.png"
define e = Character("Suzuran")
transform shotcut:
    subpixel True
    zoom 1 alpha 0.0
    ease 0.2 alpha 1.0

    on idle:
        ease_cubic 1.0 zoom 1

    on hover:
        ease_cubic 1.0 zoom 1.25

    on selected:
        ease_cubic 1.0 zoom 1.0

    on hide:
        ease 0.2 alpha 0.0
default menuu = False
screen shortcut():
    vbox:
        spacing 10

        imagebutton at shotcut :
            idle "gui/shortcut-button/idle.png"
            hover "gui/shortcut-button/hover.png"
            selected_idle  "gui/shortcut-button/hover.png"
            action ToggleVariable("menuu",True)

        if menuu>0:

            imagebutton at shotcut:
                idle "gui/shortcut-button/idle.png"
                hover "gui/shortcut-button/hover.png"
                selected_idle  "gui/shortcut-button/hover.png"
                action Jump("opsi1")

            imagebutton at shotcut:
                idle "gui/shortcut-button/idle.png"
                hover "gui/shortcut-button/hover.png"
                selected  "gui/shortcut-button/hover.png"
                action Jump("opsi2")

            imagebutton at shotcut:
                idle "gui/shortcut-button/idle.png"
                hover "gui/shortcut-button/hover.png"
                selected_idle "gui/shortcut-button/hover.png"
                action Jump("opsi3")
# The game starts here.

label start:
    $interfacee =1
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene basement
    show screen shortcut
    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.



    # These display lines of dialogue.

    "You've created a new Ren'Py game."

    "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.

    return
label opsi1:
    scene basement
    $interfacee =1
    transform merah_ke_biru (x_start = 0.5):
        matrixcolor TintMatrix("#f00")
        linear 3.0 matrixcolor TintMatrix("#00f")
        linear 3.0 matrixcolor TintMatrix("#f00")
        repeat
    show lisa_c2:
        xalign 0.5
        matrixcolor TintMatrix("#f00")
        block:
            linear 2.0 xalign 0.53 matrixcolor TintMatrix("#00f") alpha 0.5
            linear 2.0 xalign 0.47 matrixcolor TintMatrix("#f00") alpha 0.5
            repeat
    show lisa_c at merah_ke_biru:
        xalign  0.5
    e "set opsi satu"

    while True:
        e "This is infinite loop"

        e "you will never return"
    return
label opsi2:
    scene basement
    $interfacee =2
    transform merah_ke_biru (x_start = 0.5):
        matrixcolor TintMatrix("#f00")
        linear 3.0 matrixcolor TintMatrix("#00f")
        linear 3.0 matrixcolor TintMatrix("#f00")
        repeat
    show lisa_c2:
        xalign 0.5
        matrixcolor TintMatrix("#f00")
        block:
            linear 2.0 xalign 0.53 matrixcolor TintMatrix("#00f") alpha 0.5
            linear 2.0 xalign 0.47 matrixcolor TintMatrix("#f00") alpha 0.5
            repeat
    show lisa_c at merah_ke_biru:
        xalign  0.5

    e "set opsi dua"
    while True:
        e "This is infinite loop"

        e "you will never return"
    return
label opsi3:
    $interfacee =3
    $renpy.run(OpenURL('https://www.youtube.com/watch?v=dQw4w9WgXcQ'))
    return
