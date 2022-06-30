transform mm(zum,alpha0,alpha1):
    subpixel True
    zoom zum alpha alpha0
    ease 1.0 alpha alpha1


transform hovery(pausee,x_start,y_start):
    subpixel True
    xpos (x_start+60) alpha 0
    pause pausee
    ease_cubic 0.7 xpos x_start alpha 1.0
    on idle:
        ease 0.15 ypos (y_start)
    on hover:
        ease 0.15 ypos (y_start-3)

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
