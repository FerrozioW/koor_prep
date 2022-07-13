
default y = True

screen mv():

    $dur = renpy.music.get_pos(channel = "sound")

    timer 0.001 repeat True action SetVariable("y",y+0.001)

    if dur <3.037:
        add "mv/sb01.png"
    elif dur < 04.556:
        add "mv/sb02.png"
    elif dur < 06.075:
        add "mv/sb03.png"
    elif dur < 12.151:
        add "mv/sb04.png"
    elif dur < 17.848:
        add "mv/sb05.png"
    elif dur < 18.227:
        add "#FFFFFF"
    elif dur < 23.544:
        add "mv/sb06.png"
    elif dur < 24.303:
        add "#000000"
    elif dur < 28.860:
        add "mv/sb07.0.png"
    elif dur < 30:
        add "mv/sb07.5.png"
    elif dur >30:
        $renpy.music.stop(channel = "sound",fadeout = 0)

    text "Duration : [dur]":
        xalign 0.2 yalign 0.1
        color "FF0000"
