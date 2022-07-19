


default textt = 1
default textt2 = 1
default textt3 = 1

image frame2_flip = im.Flip("pert3/frame2.png", horizontal="True")
image frame2blur = im.Blur("pert3/frame2.png", 2)
image char3 = im.MatrixColor("pert3/char3/char3.png", im.matrix.brightness(-0.2))
image tanya = Movie(play="pert3/vid_1.webm", fps = 30, size=(1280, 720))
image cg:
    xsize 1285
    ysize 725
    "pert3/cg1.jpg"
    pause 0.498
    "pert3/cg2.jpg"
    pause 0.498
    "pert3/cg3.jpg"
    pause 0.498
    "pert3/cg4.jpg"
    pause 0.498
    "pert3/cg5.jpg"
    pause 0.498
    "pert3/cg6.jpg"
    pause 0.498
    "pert3/cg7.jpg"
    pause 0.498
    "pert3/cg9.png"
    pause 0.498
    repeat

screen my_mv():
    modal True
    $dur = renpy.music.get_pos(channel = "sound")
    timer 0.001 repeat True action SetVariable("y",y+0.001)

    if dur <= 0.937:
        add "black"

    elif dur <=4.687:

        add "pert3/char_background.png" at backgroundd :
            zoom 2
            yalign 0.8 xalign 0.5

        add "char3" at shadow as dummy:
            zoom 0.49
            xalign 0.5 yalign 1.1

        add "char3" at char3:
            zoom 0.5
            align (0.5,0.5)

        add "pert3/front_text.png":
            xalign 0.8
            yalign 0.2

    elif dur <= 12.656:
        add "cg" at cg:
            align (0.5,0.5)

        timer 0.497 repeat True action SetVariable("textt",textt+1)


        if textt== 1:
            textbutton "Feuer!" at cg_text1 :
                xsize 318
                ysize 120
                text_xpos 130
                text_ypos 135
                xalign 0.8 yalign 0.2
                text_font "haetten.ttf"
                text_size 96
                background "pert3/text_background.png"
                text_kerning 3
                text_color "#FFF"
        if textt==9:
            textbutton "Feuer!" at cg_text1:
                xsize 318
                ysize 120
                text_xpos 130
                text_ypos 135
                xalign 0.1 yalign 0.2
                text_font "haetten.ttf"
                text_size 96
                background "pert3/text_background.png"
                text_kerning 3
                text_color "#FFF"

        elif textt==2 or textt==10:
            textbutton "Sperrfeuer!" at cg_text1:
                xsize 318
                ysize 120
                text_xpos 130
                text_ypos 135
                xalign 1.6 yalign 0.2
                text_font "haetten.ttf"
                text_size 96
                background "pert3/text_background.png"
                text_kerning 3
                text_color "#FFF"

        elif textt==3 or textt==11:
            textbutton "Feuer!" at cg_text2:
                xsize 318
                ysize 120
                text_xpos 130
                text_ypos 135
                xalign 0.8 yalign -0.5
                text_font "haetten.ttf"
                text_size 96
                background "pert3/text_background.png"
                text_kerning 3
                text_color "#FFF"

        elif textt==4 or textt==12:
            textbutton "Los!" at cg_text2:
                xsize 318
                ysize 120
                text_xpos 130
                text_ypos 135
                xalign 0.8 yalign 1.9
                text_font "haetten.ttf"
                text_size 96
                background "pert3/text_background.png"
                text_kerning 3
                text_color "#FFF"

        elif textt==5 or textt==13:
            textbutton "Achtung!" at cg_text1:
                xsize 318
                ysize 120
                text_xpos 130
                text_ypos 135
                xalign -1 yalign 0.2
                text_font "haetten.ttf"
                text_size 96
                background "pert3/text_background.png"
                text_kerning 3
                text_color "#FFF"

        elif textt==6 or textt==14:
            textbutton "Deckung!" at cg_text1:
                xsize 318
                ysize 120
                text_xpos 130
                text_ypos 135
                xalign 2.6 yalign 0.2
                text_font "haetten.ttf"
                text_size 96
                background "pert3/text_background.png"
                text_kerning 3
                text_color "#FFF"

        elif textt==7 or textt==15:
            textbutton "Hinlegen!" at cg_text2:
                xsize 318
                ysize 120
                text_xpos 130
                text_ypos 135
                xalign 0.8 yalign -0.3
                text_font "haetten.ttf"
                text_size 96
                background "pert3/text_background.png"
                text_kerning 3
                text_color "#FFF"

        elif textt==8 or textt==16:
            textbutton "Halt!" at cg_text2:
                xsize 318
                ysize 120
                text_xpos 130
                text_ypos 135
                xalign 0.8 yalign 1.9
                text_font "haetten.ttf"
                text_size 96
                background "pert3/text_background.png"
                text_kerning 3
                text_color "#FFF"


    elif dur <= 24.843:
        add "pert3/night.png" at night:
            ysize 725
            align (0.5,0.5)

        add "pert3/p1.png" at p1(1.2):
            align (0.0, 0.0)

        add "pert3/p1.png" at p1(1.6):
            align (0.0, 0.0)


        add "pert3/p2.png" at p2(0,0.2):
            align (0.0, 1.01)

        add "pert3/word_effect.png" at dododo:
            xalign 0.1 yalign 0.1

        add "pert3/word_effect.png" at dododo as effect1:
            xalign 0.5 yalign 0.5

        add "pert3/word_effect.png" at dododo as effect2:
            xalign 0.9 yalign 0.9

        add "pert3/gas_gas_gas.png" at gasgasgas as effect2:
            zoom 1.01

        text "Truly Certified" :
            xalign 0.5 yalign 0.1
            color "#FFF"
            font "haetten.ttf"
            size 48
            outlines [(1,"#000",1,1)]

        text "Racing into the night moment":
            xalign 0.5 yalign 0.9
            color "#FFF"
            font "haetten.ttf"
            size 48
            outlines [(1,"#000",1,1)]

    elif dur <= 36.562:
        add "black"
        add "pert3/sea.png" at sea:
            xsize 1290
            ysize 720

        add "pert3/ship1.png" at ship1:
            xpos - 256 ypos 250

        add "pert3/ship2.png" at ship2:
            xalign 1.2 yalign 1.01

        add "pert3/torp.png" at torp:
            xalign 0.85 yalign 0.95

        add "pert3/gogogo.png" at slideright:
            xalign 1 yalign 0.7

        text "Geneva Convention???":
            xalign 0.5 yalign 0.1
            color "#FFF"
            font "haetten.ttf"
            size 48
            outlines [(1,"#000",1,1)]

        text "More look like Geneva Suggestion":
            xalign 0.5 yalign 0.2
            color "#FFF"
            font "haetten.ttf"
            size 48
            outlines [(1,"#000",1,1)]

    elif dur <= 54.843:
        add "tanya"
        add "pert3/frame.png" at movingpics:
            xalign 0.01 yalign 0.5
        if  dur >= 50.628 :
            timer 0.497 repeat True action SetVariable("textt2",textt2+1)
            if textt2 ==1:
                textbutton "Es ist" at cg_text2:
                    xsize 318
                    ysize 120
                    text_xpos 130
                    text_ypos 135
                    xalign 0.5 yalign -0.2
                    text_font "haetten.ttf"
                    text_size 96
                    background "pert3/text_background.png"
                    text_kerning 3
                    text_color "#FFF"

            elif textt2 ==2:
                textbutton "für" at cg_text2:
                    xsize 318
                    ysize 120
                    text_xpos 130
                    text_ypos 135
                    xalign 0.5 yalign -0.2
                    text_font "haetten.ttf"
                    text_size 96
                    background "pert3/text_background.png"
                    text_kerning 3
                    text_color "#FFF"

            elif textt2 ==3:
                textbutton "dieses" at cg_text2:
                    xsize 318
                    ysize 120
                    text_xpos 130
                    text_ypos 135
                    xalign 0.5 yalign -0.2
                    text_font "haetten.ttf"
                    text_size 96
                    background "pert3/text_background.png"
                    text_kerning 3
                    text_color "#FFF"

            else:
                textbutton "Laaaand!" at cg_text2:
                    xsize 318
                    ysize 120
                    text_xpos 130
                    text_ypos 135
                    xalign 0.5 yalign -0.2
                    text_font "haetten.ttf"
                    text_size 96
                    background "pert3/text_background.png"
                    text_kerning 3
                    text_color "#FFF"

    elif dur<= 80.625:
        if dur> 54.843 and dur< 62.343:
            add "pert3/char2/char2.jpg" at sea

        elif dur>= 62.343 and dur<= 70.781:
            add "pert3/char3/asolt.jpg" at sea

        else:
            add "pert3/char4/supp.jpg" at sea


        add "frame2blur" at frame2:
            xalign 1
            alpha 1.5

        add "pert3/gas_gas_gas.png" at gasgasgas :
            zoom 1.01

    elif dur<=88:
        add "cg" at cg

        timer 0.497 repeat True action SetVariable("textt3",textt3+1)

        if textt3== 1:
            textbutton "Feuer!" at cg_text1 :
                xsize 318
                ysize 120
                text_xpos 130
                text_ypos 135
                xalign 0.8 yalign 0.2
                text_font "haetten.ttf"
                text_size 96
                background "pert3/text_background.png"
                text_kerning 3
                text_color "#FFF"
        if textt3==9:
            textbutton "Feuer!" at cg_text1:
                xsize 318
                ysize 120
                text_xpos 130
                text_ypos 135
                xalign 0.1 yalign 0.2
                text_font "haetten.ttf"
                text_size 96
                background "pert3/text_background.png"
                text_kerning 3
                text_color "#FFF"

        elif textt3==2 or textt3==10:
            textbutton "Sperrfeuer!" at cg_text1:
                xsize 318
                ysize 120
                text_xpos 130
                text_ypos 135
                xalign 1.6 yalign 0.2
                text_font "haetten.ttf"
                text_size 96
                background "pert3/text_background.png"
                text_kerning 3
                text_color "#FFF"

        elif textt3==3 or textt3==11:
            textbutton "Feuer!" at cg_text2:
                xsize 318
                ysize 120
                text_xpos 130
                text_ypos 135
                xalign 0.8 yalign -0.5
                text_font "haetten.ttf"
                text_size 96
                background "pert3/text_background.png"
                text_kerning 3
                text_color "#FFF"

        elif textt3==4 or textt3==12:
            textbutton "Los!" at cg_text2:
                xsize 318
                ysize 120
                text_xpos 130
                text_ypos 135
                xalign 0.8 yalign 1.9
                text_font "haetten.ttf"
                text_size 96
                background "pert3/text_background.png"
                text_kerning 3
                text_color "#FFF"

        elif textt3==5 or textt3==13:
            textbutton "Achtung!" at cg_text1:
                xsize 318
                ysize 120
                text_xpos 130
                text_ypos 135
                xalign -1 yalign 0.2
                text_font "haetten.ttf"
                text_size 96
                background "pert3/text_background.png"
                text_kerning 3
                text_color "#FFF"

        elif textt3==6 or textt3==14:
            textbutton "Deckung!" at cg_text1:
                xsize 318
                ysize 120
                text_xpos 130
                text_ypos 135
                xalign 2.6 yalign 0.2
                text_font "haetten.ttf"
                text_size 96
                background "pert3/text_background.png"
                text_kerning 3
                text_color "#FFF"

        elif textt3==7 or textt3==15:
            textbutton "Hinlegen!" at cg_text2:
                xsize 318
                ysize 120
                text_xpos 130
                text_ypos 135
                xalign 0.8 yalign -0.3
                text_font "haetten.ttf"
                text_size 96
                background "pert3/text_background.png"
                text_kerning 3
                text_color "#FFF"

        elif textt3==8 or textt3==16:
            textbutton "Halt!" at cg_text2:
                xsize 318
                ysize 120
                text_xpos 130
                text_ypos 135
                xalign 0.8 yalign 1.9
                text_font "haetten.ttf"
                text_size 96
                background "pert3/text_background.png"
                text_kerning 3
                text_color "#FFF"


    else:
        add "pert3/cover.png"

    text "Duration : [dur]":
        xalign 0.2 yalign 0.1
        color "FF0000"

transform backgroundd:
    pause 1.88

transform shadow():
    subpixel True
    matrixcolor TintMatrix("#000")
    alpha 0.8
    parallel:
        easein 3.75 xoffset -100 yoffset -5
    parallel:
        block:
            pause 1.88
            easein 0.25 zoom 2 yalign 0.3


transform char3:
    subpixel True
    zoom 1.2

    parallel:

        block:
            easeout 0.2 rotate 0.05
            easeout 0.4 rotate -0.05
            pause 0.5
            easeout 0.2 rotate 0
        repeat

    parallel:
        easeout 1.87 yoffset -5
        pause 0.1
        easeout 1.87 yoffset 5

    parallel:
        block:
            pause 1.88
            easein 0.25 zoom 2 yalign 0.3


transform cg:
    subpixel True
    xoffset 2 yoffset 2
    block:
        easeout 0.498 xoffset -2 yoffset 2
        easeout  0.498 xoffset 2 yoffset -2
        easeout 0.498 xoffset -2 yoffset 2
        easeout  0.498 xoffset 2 yoffset -2
        easeout 0.498 xoffset 0 yoffset 0
        repeat

transform cg_text1:
    subpixel True
    alpha 0
    easein 0.498 xalign 0.8 alpha 1



transform cg_text2:
    subpixel True
    alpha 0
    easein 0.498 yalign 0.7 alpha 1

transform night:
    subpixel True
    parallel:
        linear 12.0 xalign 0.8
    parallel:
        block:
            easeout 0.498 xoffset -2 yoffset 2
            easeout  0.498 xoffset 2 yoffset -2
            easeout 0.498 xoffset -2 yoffset 2
            easeout  0.498 xoffset 2 yoffset -2
            easeout 0.498 xoffset 0 yoffset 0
            repeat

transform p1(pausee = 0):
    subpixel True alpha 0
    rotate 30
    pause pausee
    parallel:
        easein 12.0 xalign 1.2
    parallel:
        parallel:
            easein 3.0  yalign 0.8 alpha 1
        parallel:
            easeout 2.0 rotate 0
        pause 0.5
        easeout 3 yalign -0.4 alpha 1 rotate -30

transform p2(pausee = 0, y_start= 0.2,y_end = 1.4):
    subpixel True alpha 0 yalign 1.01
    rotate -30
    pause pausee
    parallel:
        easein 12.0 xalign 1.2
    parallel:
        parallel:
            easein 3.0  yalign y_start alpha 1
        parallel:
            easeout 2.0 rotate 0
        pause 0.5
        easeout 3 yalign y_end alpha 1 rotate 30

transform dododo:
    subpixel True
    alpha 0.8 zoom 0.25
    block:
        easeout 1 zoom 0.23 alpha 0.7
        easeout 1 zoom 0.25 alpha 0.8
        repeat


transform gasgasgas:
    subpixel True
    alpha 0.2
    block:
        easeout 1 zoom 0.99
        easeout 1 zoom 1.02
        repeat

transform sea:
    subpixel True
    block:
        ease 1 xoffset -2 yoffset -1
        ease  1 xoffset 0 yoffset 0
        ease 1 xoffset 2 yoffset 1
        repeat

transform ship1:
    subpixel True alpha 0
    parallel:
        ease 2 xpos 120 alpha 1
    parallel:
        block:
            ease 1 xoffset -2 yoffset -1 rotate -0.5
            ease  1 xoffset 0 yoffset 0 rotate 0
            ease 1 xoffset 2 yoffset 1 rotate 0.5
            ease 1 xoffset 0 yoffset 0 rotate 0
            repeat

    parallel:
        pause 10.1
        "pert3/ship1_b.png"
        ease 1.0 yoffset 100 alpha 0

transform ship2:
    subpixel True
    alpha 0
    pause 2.5
    parallel:
        ease 2.0 xalign 0.9 alpha 0.6
    parallel:
        block:
            ease 1 xoffset -2 yoffset -1
            ease  1 xoffset 0 yoffset 0
            ease 1 xoffset 2 yoffset 1
            ease 1 xoffset 0 yoffset 0
            repeat

transform torp:
    subpixel True
    alpha 0
    pause 5.0
    block:
        easeout 1.0 yalign 0.99 alpha 1
        easeout 4.0 xalign 0.32 yalign 0.87 rotate 30
    "pert3/fire.png"
    zoom 0.01 alpha 0 rotate 0
    easein 0.2 zoom 1.3 alpha 1 yoffset 50
    alpha 0

transform slideright:
    subpixel True
    alpha 0
    pause 2.0
    ease 1.0 xalign 0.9 alpha 1
    parallel:
        block:
            easeout 0.498 xoffset 2 yoffset -2
            easeout  0.498 xoffset -2 yoffset 2
            easeout 0.498 xoffset 2 yoffset -2
            easeout  0.498 xoffset -2 yoffset 2
            easeout 0.498 xoffset 0 yoffset 0
            repeat
    parallel:
        block:
            easeout 1.0 zoom 1.01
            easeout 1.0 zoom 0.97
            repeat

transform movingpics:
    subpixel True
    easeout 3.0 xalign 0.95
    easein 3.0 xalign 0.35
    "black"
    pause 0.5
    "pert3/frame.png"
    rotate 15  zoom 2.1 yoffset 0
    easeout 3.0 xalign 0.85
    easein 3.0 xalign 0.35
    easeout 3.0 xalign 0.85
    easein 2.0 xalign 0.55


transform frame2(x_start = 0.2, x_end = 0.8):
    subpixel True
    parallel:
        easein 2.0 xalign 0.2
        easeout 4.0 xalign 0.8
        pause 2.0
        easein 3.0 xalign 0.6
        easein 2.0 xalign 0.01
        repeat
    parallel:
        block:
            easeout 0.498 xoffset -2 yoffset 2
            easeout  0.498 xoffset 2 yoffset -2
            easeout 0.498 xoffset -2 yoffset 2
            easeout  0.498 xoffset 2 yoffset -2
            easeout 0.498 xoffset 0 yoffset 0
            repeat
    repeat
