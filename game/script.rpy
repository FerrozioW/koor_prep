# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define d = Character("Dad")
define k = Character ("Koyomi")
define t = Character ("Takahiro",color = "#B2C9ED",who_outlines= [(absolute(1), "0F1537", absolute(1), absolute(1))])
define i = Character ("Ichikawa")
define c = Character ("Classmates")
define a = Character ("Ariya")
define n = Character ("Narumi",color = "#F4727D",who_outlines= [(absolute(1), "5A232E", absolute(1), absolute(1))])#outline merah
define m = Character ("Miyou",color = "#90D8DD",who_outlines= [(absolute(1), "24425F", absolute(1), absolute(1))])#outline toska
define mae = Character ("Maeko",color = "#FFE49E",who_outlines= [(absolute(1), "693D2A", absolute(1), absolute(1))]) #outline kuning
define mac = Character ("Machiko",color = "#F9B2FF",who_outlines= [(absolute(1), "35214A", absolute(1), absolute(1))])#outline pink
define veh = Character ("Village Elder Hayate",color = "#B2DE83",who_outlines= [(absolute(1), "253A27", absolute(1), absolute(1))])#outline ijo
define s = Character("Suzuran",color = "#FFE49E",who_outlines= [(absolute(1), "693D2A", absolute(1), absolute(1))])
default show_quick_menu = True

transform shotcut:
    subpixel True
    zoom 1 alpha 0.0
    ease 0.2 alpha 1.0

    on idle:
        ease_cubic 0.3 zoom 1

    on hover:
        ease_cubic 0.3 zoom 1.25

    on selected:
        ease_cubic 0.3 zoom 1.0

    on hide:
        ease 0.2 alpha 0.0


default sotcut = False
screen shortcut():
    vbox:
        spacing 10

        imagebutton at shotcut :
            idle "gui/shortcut-button/idle.png"
            hover "gui/shortcut-button/hover.png"
            selected_idle  "gui/shortcut-button/hover.png"
            action ToggleVariable("sotcut",True)

        if sotcut>0:

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

screen stiker(w,h):

    grid w h :
        xspacing 5 yspacing 5
        xalign 0.5 yalign 0.3
        if h<4:
            for i in range (w*h):
                $stik = i+1
                add "gui/ddlc/stickers/"+str(stik)+".png":
                    xsize 178
                    ysize 178
        elif h ==4:
            for i in range (w*h):
                $stik = i+1
                add "gui/ddlc/stickers/"+str(stik)+".png":
                    xsize 120
                    ysize 120

label start:
    show screen shortcut
    scene basement
    show lisa_c:
        xalign 0.5
        yalign 0.0
    s "You've created a new Ren'Py game."

    k "Once you add a story, pictures, and music, you can release it to the world!"
    t "biru"

    $ show_quick_menu = False
    menu:
        "option one":
            t "satu"
        "option two":
            t "dua"

    $ show_quick_menu = True
    i "polos"
    c "polos"
    a "polos"
    n "merah"
    m "toska"
    mae "kuning"
    mac "ping"
    veh "hijau"
    return

label opsi1:
    "Welcom to exception tester"
    #exception
    python:
        try:
            x = int(renpy.input("Gimme Number"))
        except:
            #dialog
            renpy.say("suzuran","Masukin angka bruhhh")
            renpy.jump("opsi1")
            #jump ke label lain
            #renpy.jump("start")
    "x = [x]"
    return

label opsi2:
    hide screen stiker
    s "Welcome to Grid tester"
    python:
        try:
            w = int(renpy.input("width????"))
            h = int(renpy.input("height???"))

        except:

            renpy.say (s, "Kasih angka bukan huruf, dan jangan kosongin parameternya")
            renpy.jump("opsi2")



    if w<0 or h<0:
        s "Mana mungkin bisa grid parameternya mines, gblk!"
        jump opsi2
    elif w>4 or h>4:
        s "Kebanyakan parameternya, maksimum width dan height hanya 4"
        jump opsi2
    else:
        s "here is your stikers"
        show screen stiker(w,h)
        if w == 0 or h==0:
            s "It's empty of cos, bikos yu don gib parameter yu idiot"

    s "Sampai Jumpa"
    hide screen stiker

    return

label opsi3:
    "opsi3"
    return
