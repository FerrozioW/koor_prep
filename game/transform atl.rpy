transform mm(zum,alpha0,alpha1):
    subpixel True
    zoom zum alpha alpha0
    ease 1.0 alpha alpha1
transform hoverr(pausee,x_start,y_start):
    subpixel True
    xpos (x_start+60) alpha 0
    pause pausee
    ease_cubic 0.7 xpos x_start alpha 1.0
    on idle:
        ease 0.2 ypos (y_start)
    on hover:
        ease 0.2 ypos (y_start-3)
