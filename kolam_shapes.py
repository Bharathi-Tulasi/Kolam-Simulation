import turtle

# Ratios for Kolam shapes 
# space/size(or distance of shape-II, III & IV) = 85/30 = 2.82, 
# space/(distance of shape-I) = 85/60 = 1.42, 


def draw_circle_abdc(turtle, color = "black", size = 30, arc = 270, distance = 30):
    turtle.penup()
    turtle.color(color)
    turtle.pendown()
    turtle.setheading(45)
    turtle.fd(distance)
    turtle.circle(size, arc)
    turtle.setheading(-45)
    turtle.fd(distance)
    
def draw_circle_bdca(turtle, color = "black", size = 30, arc = 270, distance = 30):
    turtle.penup()
    turtle.color(color)
    turtle.pendown()
    turtle.setheading(135)
    turtle.fd(distance)
    turtle.circle(size, arc)
    turtle.setheading(45)
    turtle.fd(distance)
    
def draw_circle_dcab(turtle, color = "black", size = 30, arc = 270, distance = 30):
    turtle.penup()
    turtle.color(color)
    turtle.pendown()
    turtle.setheading(-135)
    turtle.fd(distance)
    turtle.circle(size, arc)
    turtle.setheading(135)
    turtle.fd(distance)  
    
def draw_circle_cabd(turtle, color = "black", size = 30, arc = 270, distance = 30):
    turtle.penup()
    turtle.color(color)
    turtle.pendown()
    turtle.setheading(-45)
    turtle.fd(distance)
    turtle.circle(size, arc)
    turtle.setheading(-135)
    turtle.fd(distance)
    
def draw_circle_bacd(turtle, color = "black", size = 30, arc = 270, distance = 30):
   
    turtle.penup()
    turtle.color(color)
    turtle.pendown()
    turtle.setheading(135)
    turtle.fd(distance)
    turtle.circle(-size, arc)
    turtle.setheading(-135)
    turtle.fd(distance)
    
def draw_circle_acdb(turtle, color = "black", size = 30, arc = 270, distance = 30):
    turtle.penup()
    turtle.color(color)
    turtle.pendown()
    turtle.setheading(45)
    turtle.fd(distance)
    turtle.circle(-size, arc)
    turtle.setheading(135)
    turtle.fd(distance)
    
def draw_circle_cdba(turtle, color = "black", size = 30, arc = 270, distance = 30):
    turtle.penup()
    turtle.color(color)
    turtle.pendown()
    turtle.setheading(-45)
    turtle.fd(distance)
    turtle.circle(-size, arc)
    turtle.setheading(45)
    turtle.fd(distance)
    
def draw_circle_dbac(turtle, color = "black", size = 30, arc = 270, distance = 30):
    turtle.penup()
    turtle.color(color)
    turtle.pendown()
    turtle.setheading(-135)
    turtle.fd(distance)
    turtle.circle(-size, arc)
    turtle.setheading(-45)
    turtle.fd(distance)
    
    
   
def draw_line_a(turtle, color = "black", distance = 60):
    turtle.penup()
    turtle.color(color)
    turtle.pendown()
    turtle.setheading(45)
    turtle.fd(distance)
    

    
def draw_line_b(turtle, color = "black", distance = 60):
    turtle.penup()
    turtle.color(color)
    turtle.pendown()
    turtle.setheading(135)
    turtle.fd(distance)
    
def draw_line_c(turtle, color = "black", distance = 60):
    turtle.penup()
    turtle.color(color)
    turtle.pendown()
    turtle.setheading(-45)
    turtle.fd(distance)
    
def draw_line_d(turtle, color = "black", distance = 60):
    turtle.penup()
    turtle.color(color)
    turtle.pendown()
    turtle.setheading(-135)
    turtle.fd(distance)
    

    
def draw_U_bdc(turtle, color = "black", size = 30, arc = 180, distance = 30):
    turtle.penup()
    turtle.color(color)
    turtle.pendown()
    turtle.setheading(135)
    turtle.fd(distance)
    turtle.circle(size, arc)
    turtle.setheading(-45)
    turtle.fd(distance)
    
def draw_U_dca(turtle, color = "black", size = 30, arc = 180, distance = 30):
    turtle.penup()
    turtle.color(color)
    turtle.pendown()
    turtle.setheading(-135)
    turtle.fd(distance)
    turtle.circle(size, arc)
    turtle.setheading(45)
    turtle.fd(distance)
    
def draw_U_cab(turtle, color = "black", size = 30, arc = 180, distance = 30):
    turtle.penup()
    turtle.color(color)
    turtle.pendown()
    turtle.setheading(-45)
    turtle.fd(distance)
    turtle.circle(size, arc)
    turtle.setheading(135)
    turtle.fd(distance)
    
def draw_U_abd(turtle, color = "black", size = 30, arc = 180, distance = 30):
    turtle.penup()
    turtle.color(color)
    turtle.pendown()
    turtle.setheading(45)
    turtle.fd(distance)
    turtle.circle(size, arc)
    turtle.setheading(-135)
    turtle.fd(distance)
    
def draw_U_bac(turtle, color = "black", size = 30, arc = 180, distance = 30):
    turtle.penup()
    turtle.color(color)
    turtle.pendown()
    turtle.setheading(135)
    turtle.fd(distance)
    turtle.circle(-size, arc)
    turtle.setheading(-45)
    turtle.fd(distance)

def draw_U_acd(turtle, color = "black", size = 30, arc = 180, distance = 30):
    turtle.penup()
    turtle.color(color)
    turtle.pendown()
    turtle.setheading(45)
    turtle.fd(distance)
    turtle.circle(-size, arc)
    turtle.setheading(-135)
    turtle.fd(distance)
    
def draw_U_cdb(turtle, color = "black", size = 30, arc = 180, distance = 30):
    turtle.penup()
    turtle.color(color)
    turtle.pendown()
    turtle.setheading(-45)
    turtle.fd(distance)
    turtle.circle(-size, arc)
    turtle.setheading(135)
    turtle.fd(distance)
    
def draw_U_dba(turtle, color = "black", size = 30, arc = 180, distance = 30):
    turtle.penup()
    turtle.color(color)
    turtle.pendown()
    turtle.setheading(-135)
    turtle.fd(distance)
    turtle.circle(-size, arc)
    turtle.setheading(45)
    turtle.fd(distance)
    



    
def draw_semicircle_bd(turtle, color = "black", size = 30, arc = 90, distance = 30):
    turtle.penup()
    turtle.color(color)
    turtle.pendown()
    turtle.setheading(135)
    turtle.fd(distance)
    turtle.circle(size, arc)
    turtle.setheading(-135)
    turtle.fd(distance)
   
    
def draw_semicircle_dc(turtle, color = "black", size = 30, arc = 90, distance = 30):
    turtle.penup()
    turtle.color(color)
    turtle.pendown()
    turtle.setheading(-135)
    turtle.fd(distance)
    turtle.circle(size, arc)
    turtle.setheading(-45)
    turtle.fd(distance)
    
def draw_semicircle_ca(turtle, color = "black", size = 30, arc = 90, distance = 30):
    turtle.penup()
    turtle.color(color)
    turtle.pendown()
    turtle.setheading(-45)
    turtle.fd(distance)
    turtle.circle(size, arc)
    turtle.setheading(45)
    turtle.fd(distance)
    
def draw_semicircle_ab(turtle, color = "black", size = 30, arc = 90, distance = 30):
    turtle.penup()
    turtle.color(color)
    turtle.pendown()
    turtle.setheading(45)
    turtle.fd(distance)
    turtle.circle(size, arc)
    turtle.setheading(135)
    turtle.fd(distance)

def draw_semicircle_ac(turtle, color = "black", size = 30, arc = 90, distance = 30):
    turtle.penup()
    turtle.color(color)
    turtle.pendown()
    turtle.setheading(45)
    turtle.fd(distance)
    turtle.circle(-size, arc)
    turtle.setheading(-45)
    turtle.fd(distance)
    
def draw_semicircle_cd(turtle, color = "black", size = 30, arc = 90, distance = 30):
    turtle.penup()
    turtle.color(color)
    turtle.pendown()
    turtle.setheading(-45)
    turtle.fd(distance)
    turtle.circle(-size, arc)
    turtle.setheading(-135)
    turtle.fd(distance)
    
def draw_semicircle_db(turtle, color = "black", size = 30, arc = 90, distance = 30):
    turtle.penup()
    turtle.color(color)
    turtle.pendown()
    turtle.setheading(-135)
    turtle.fd(distance)
    turtle.circle(-size, arc)
    turtle.setheading(135)
    turtle.fd(distance)
    
def draw_semicircle_ba(turtle, color = "black", size = 30, arc = 90, distance = 30):
    turtle.penup()
    turtle.color(color)
    turtle.pendown()
    turtle.setheading(135)
    turtle.fd(distance)
    turtle.circle(-size, arc)
    turtle.setheading(45)
    turtle.fd(distance)

turtle.done()