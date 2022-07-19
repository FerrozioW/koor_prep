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
define sa = Character("Sayori", what_prefix='"', what_suffix='"')
define mo = Character("Monika", what_prefix='"', what_suffix='"')
define yu = Character("Yuri", what_prefix='"', what_suffix='"')
define na = Character("Natsuki", what_prefix='"', what_suffix='"')


style poem:
    font "gui/ddlc/nnb_poem.otf"
    xsize 691
    line_spacing 5
    size 28
    outlines [(0, "#000000", 0,1)]
    text_align 0
    kerning 0.5


image noise:
    "noise1"
    pause 0.25
    "noise2"
    pause 0.25
    "noise3"
    pause 0.25
    "noise4"
    pause 0.25

image natb_flip = im.Flip("natb.png", horizontal="True")

image natd_flip = im.Flip("natd.png", horizontal="True")

image nate_flip = im.Flip("nate.png", horizontal="True")

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

#buat tunjukin 3 shortut button dibawah
default sotcut = False
#buat ubah textbox ddlc
default ddlc = False
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

screen ddlc_letter():
    add "gui/ddlc/nnb/poem.jpg":
        align (0.52,0.5)

    vbox:
        xalign 0.52 yalign 0.4
        spacing 50

        text"Sometimes I think that Natsuki is the worst club member in our club, not only she makes the shittiest poems, but she also constantly making a fuss of us, what is that \"Eagles can fly\" shit, that's literally for babies like her, she should reflect upon her poems and to make it better, not to constantly make the \"same\" type of poem, I really wish she could leave the club as soon as possible so we don't have to deal with her.":
            style "poem"

        text"I dare her not to come back to the club again afterwards":
            style "poem"

        null height 25

        text"Natsuki is an idiot.":
            style "poem"

        null height 50
        text"I want her to leave us alone.":
            style "poem"
label start:
    stop music
    $ show_quick_menu = True
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
    show frame2blur at frame2:
        xalign 0.5
    veh "hijau"
    window hide
    $show_quick_menu = False
    $renpy.music.play("los3.mp3",channel = "sound")
    show screen my_mv
    pause
    return

label opsi1:
    hide lisa_c
    hide basement
    window hide
    scene black
    stop music
    $show_quick_menu = False
    $renpy.music.play("mv/moment_day.ogg",channel = "sound")
    show screen mv
    pause
    return

label opsi2:
    show lisa_c:
        align (0.5,0.0)
    hide screen stiker
    $ddlc = False
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
    hide screen stiker
    $show_quick_menu = False
    $ddlc = True
    window hide
    scene black
    show expression Text("For anyone who have gotten this far. I present you my hardest remake..",color="#FFFFFF", xsize=600,text_align=0.5,size=30, yalign=0.5, xalign=0.5) as text with dissolve
    $ renpy.pause(2.0, hard=True)
    hide text with dissolve
    show expression Text("Natsuki? No Bulli!\nPart 1\n(Story by Wongton)",color="#FFFFFF", xsize=600,text_align=0.5,size=30, yalign=0.5, xalign=0.5) as text with dissolve
    $ renpy.pause(2.0, hard=True)
    hide text with dissolve
    scene nnba with ImageDissolve("right_nnb",1.0,ramplen = 123)

    play music "gui/ddlc/Ohayou Sayori!.mp3"

    window show
    show syra  at ddlc_appear(0.5)
    sa "Hey Monika, can I ask something?"
    show mona   at ddlc_appear(0.1)
    show syra  at ddlc_geser(0.9)
    mo "Sure, go ahead!"
    show mona at ddlc_geser (0.1)
    show syrb at ddlc_appear(0.92) as syra

    stop music

    play sound "gui/ddlc/nnb/Reverse2.mp3"

    sa "What do people mean by \"The Birds and the Bees\"?"
    show monb as mona
    show syrb at ddlc_geser (0.92) as syra
    mo "..."

    show monf at ddlc_appear (0.1,0.8,1) as mona


    play music "gui/ddlc/Poem Panic!.mp3"


    mo "I think you're not supposed to ask something like this.."
    mo "As this is more an \"adult\" type of topic."
    show monf at ddlc_geser (0.1) as mona
    show syra at ddlc_appear (0.9)
    sa "But Monika.."
    sa "I'm already 18 years old, dont you know that?"
    show syra at ddlc_geser(0.9)
    "Monika stuttered for a second."
    show monc at ddlc_appear (0.1,0.8,1) as mona
    mo "Oh.."
    show mond as mona
    mo "Alright then."
    "All of sudden, Yuri steps in."
    show mond at ddlc_geser(-0.2) as mona
    show syra at ddlc_geser(1.15)
    show yura at ddlc_appear (0.5)
    yu "THAT'S WHEN THEY HAVE SEX!"
    show yura  as yura:
        xalign 0.5 yalign 1 zoom 1.0 yoffset -20
    yu "LOTS AND LOTS OF SEX!"
    show yura as yura:
        xalign 0.5 yalign 1 zoom 2 yoffset -120
    yu "HAHAHAHAHA!"

    play sound "gui/ddlc/static.mp3"

    show yura at ddlc_geser (0.5) as yura
    show noise
    window hide
    pause 1.0

    stop sound

    show monc at ddlc_appear (-0.2,0.8,1) as mona
    hide noise
    window show
    mo "Yuri, get your shit together, this is no longer part of the original story.. "
    show monc at ddlc_geser (-0.2) as mona
    ""
    show yurb at ddlc_appear(0.5,0.8,1) as yura
    yu "Um.. I think I need to go to the toilet.."
    show yurb at ddlc_out (0.5) as yura
    ""
    show monc at ddlc_geser (0.1,0.8,0.7) as mona
    show syra at ddlc_geser (0.9,0.8,0.7) as syra
    "Yuri hurdles away in fear as she said that statement."
    "Leaving Monika and Sayori concerned wether she'll go crazy again or not "
    show monc at ddlc_appear(0.1,0.8,1) as mona
    mo "Well at least Natsuki ain't here so we could talk shit about what happened last time in the club room"
    hide mona with Dissolve (0.75)
    hide syra with Dissolve (0.75)

    window hide
    with Dissolve (0.75)

    stop music fadeout 1.0

    scene black with ImageDissolve("right_nnb",1.0,ramplen = 123)

    show expression Text("15 minutes later..",color="#FFFFFF", xsize=600,text_align=0.5,size=30, yalign=0.5, xalign=0.5) as text with dissolve
    $ renpy.pause(2.0, hard=True)
    hide text with dissolve

    play music "gui/ddlc/Okay, Everyone!.mp3"
    scene nnbb with ImageDissolve("right_nnb",1.0,ramplen = 123)

    window show
    with Dissolve (0.25)

    show mong at ddlc_appear (0.5,0.8,0)
    mo "Ok now that we are here, where should we start first? "
    show mong at ddlc_geser (0.9)
    show syrc at ddlc_appear (0.1,0.8,1)
    sa "I know, remember that time when Natsuki wrote a poem about spiders?"
    sa "It was so terrible, it almost made me laugh about it."
    sa "Even Yuri said that poem is for babies, while ours is more..."
    show syrc at ddlc_geser (0.1) as syrc
    na "Hello, anybody there?"
    show syrd at ddlc_appear (0.1,0.8,1) as syrc
    show mone as mong
    sa "Oh shit nibba it's Trapsu.. I mean Natsuki, act natural!"
    show nata at ddlc_appear (0.5,0.8,0)
    show syrd at ddlc_geser(-0.2,0.8,0.25) as syrc
    show mone at ddlc_geser (1.2,0.8,0.25) as mong
    na "Hey there, what's cookin' today?"
    show nata at ddlc_geser (0.5 ,0.8,0.25)
    show syrb at ddlc_appear (-0.2,0.8,1) as syrc
    sa "Oh, uhh.. nothing special today, just living the life as usual "
    show natc at ddlc_appear(0.5,0.8,1) as nata
    show syrb at ddlc_geser (-0.2,0.8,0.25) as syrc
    na " The atmosfere doesn't feel normal at all, are you guys hiding something?"
    show natc at ddlc_geser(0.5) as nata
    show syrb at ddlc_appear (-0.2,0.8,1) as syrc
    sa "Well.. we just arrived at the school to prepare for the class cleanup, and.."
    show syrb at ddlc_geser (-0.2) as syrc
    show natd_flip at ddlc_appear(0.5) as nata
    na "And what's that you are holding, Monika?"
    show monf at ddlc_appear(1.2) as mong
    show natd_flip at ddlc_geser(0.5) as nata
    mo "Oh, it's just a.."

    play sound "gui/ddlc/nnb/Slap.mp3"

    show nate_flip at ddlc_appear(0.5) as nata
    show monf at ddlc_geser (1.2) as mong
    na "Give it to me!"
    show nate_flip at ddlc_geser(0.5) as nata
    show syra as syrc
    show monb at ddlc_appear(1.2) as mong
    mo "Natsuki don't open that.. I.."
    show monb at ddlc_geser (1.2) as mong
    "Even before Natsuki open the letter, Monika knows that she'll be in a bad time."
    window hide
    with Dissolve(0.1)

    play sound "gui/ddlc/nnb/Open Page.mp3"

    stop music fadeout 0.5

    show screen ddlc_letter with dissolve
    pause
    hide screen ddlc_letter with dissolve

    play music "gui/ddlc/My Feelings.mp3"

    window show
    with Dissolve (0.1)

    show nate_flip at ddlc_appear (0.5) as nata
    na "..."
    show natb_flip as nata
    na "I've always been nice to you guys.."
    na "I've also been trying my best to create the best poems so you guys will like it"
    na "But why.."
    na "I always end up things like this.."
    na "If you guys really want me to leave the club, I'll leave then."
    show natb as nata
    na "GOODBYE!"
    show natb at ddlc_out(0.5) as nata
    ""
    show syra at ddlc_geser(0.1,0.8,0.75) as syrc
    show monb at ddlc_geser(0.9,0.8,0.75) as mong
    "Natsuki left the club instantly without saying a word while rushing through the door."
    "Leaving Monika and Sayori concerned regarding what will happen next."


    hide syrc with Dissolve (0.75)
    hide mong with Dissolve (0.75)

    window hide
    with Dissolve (0.75)

    scene black

    show expression Text("Now that this club only have 3 members left, the are fearing that this club will be disbanded due to lack of club members.",color="#FFFFFF", xsize=600,text_align=0.5,size=30, yalign=0.5, xalign=0.5) as text with dissolve
    $ renpy.pause(2.0, hard=True)
    hide text with dissolve

    show expression Text("The only way for them to keep the club alive is to invite Natsuki back.",color="#FFFFFF", xsize=600,text_align=0.5,size=30, yalign=0.5, xalign=0.5) as text with dissolve
    $ renpy.pause(2.0, hard=True)
    hide text with dissolve

    show expression Text("However, the question remains, will Natsuki ever come back to the Literature Club?",color="#FFFFFF", xsize=600,text_align=0.5,size=30, yalign=0.5, xalign=0.5) as text with dissolve
    $ renpy.pause(2.0, hard=True)
    hide text with dissolve

    show expression Text("Find out more on the next episode of: natsuki? No Bulli!",color="#FFFFFF", xsize=600,text_align=0.5,size=30, yalign=0.5, xalign=0.5) as text with dissolve
    $ renpy.pause(2.0, hard=True)
    hide text with dissolve

    show expression Text("Thank you for playing!",color="#FFFFFF", xsize=600,text_align=0.5,size=30, yalign=0.5, xalign=0.5) as text with dissolve
    $ renpy.pause(2.0, hard=True)
    hide text with dissolve
    stop music
    return
