transform mm(zum,alpha0,alpha1):
    subpixel True
    zoom zum alpha alpha0
    ease 1.0 alpha alpha1

transform zum(zum):
    subpixel True
    zoom zum alpha 1



transform ddlc_appear(x_start = 0.5,zum = 0.8 ,alpa = 0):
    subpixel True
    on show:
        xalign x_start yalign 1.03
        zoom zum *0.9 alpha alpa
        easein 0.25 yoffset 20 zoom zum alpha 1.00
    on replace:
        easein 0.25 yoffset 20 zoom zum alpha 1.00

transform ddlc_geser(x_start = 0.5, zum = 0.8, durasi = 0.25):
    subpixel True
    ease durasi xalign x_start zoom zum*0.95 yoffset 10 alpha 1

transform ddlc_out(x_start = 0.5):
    subpixel True
    easein 0.3 xalign x_start+0.1
    easeout 1 xalign -2.0

transform ctc(x_start):
    subpixel True
    alpha 0 xpos x_start

    block:
        subpixel True
        easeout 0.7 alpha 1.0 xpos x_start+4
        easeout 0.6 alpha 0.5 xpos x_start
        pause 0.1
        repeat


transform hovery_kanan(pausee,x_start,y_start):
    subpixel True
    xpos (x_start-60) alpha 0
    pause pausee
    ease 0.7 xpos x_start alpha 1.0
    on idle:
        ease 0.15 ypos (y_start)
    on hover:
        ease 0.15 ypos (y_start-3)

transform hovery_bawah(pausee,x_start,y_start):
    subpixel True
    ypos (y_start-30) alpha 0
    pause pausee
    ease 0.7 ypos y_start alpha 1.0
    on idle:
        ease 0.15 ypos (y_start)
    on hover:
        ease 0.15 ypos (y_start-3)

transform hovery(pausee,x_start,y_start):
    subpixel True
    xpos (x_start+60) alpha 0
    pause pausee
    ease_cubic 0.7 xpos x_start alpha 1.0
    on idle:
        ease 0.15 ypos (y_start)
    on hover:
        ease 0.15 ypos (y_start-3)

transform quick_hover (y_start=0):
    subpixel True
    on idle:
        ease 0.2 ypos y_start
    on hover:
        ease 0.2 ypos (y_start -3)

transform hoverx(pausee,x_start,y_start):
    subpixel True
    xpos (x_start+60) alpha 0
    pause pausee
    ease_cubic 0.7 xpos x_start alpha 1.0
    on idle:
        ease 0.15 xpos (x_start)
    on hover:
        ease 0.15 xpos (x_start-5)

transform slidex(pausee,x_start,delta_x):
    subpixel True
    xpos (x_start ) alpha 0
    pause pausee
    ease_cubic 0.7 xpos (x_start + delta_x) alpha 1

transform slidey(pausee,y_start,delta_y):
    subpixel True
    ypos (y_start ) alpha 0
    pause pausee
    ease 0.7 ypos (y_start + delta_y) alpha 1

transform slidey_y(pausee,y_start,delta_y):
    subpixel True
    ypos (y_start ) alpha 0
    pause pausee
    ease 0.7 ypos (y_start + delta_y) alpha 1
    on idle:
        ease 0.15 ypos (y_start+ delta_y)
    on hover:
        ease 0.15 ypos (y_start+ delta_y-3)
