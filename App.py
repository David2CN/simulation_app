import pygame
import simulator
from widgets import Screen, Button, TextInput, Textbox

pygame.init()

#display
screen = Screen().screen

#pictures
icon = pygame.image.load("images/icon.png")
loader = pygame.image.load("images/loader.jpg")
plots = pygame.image.load("images/plots.jpeg")

#colors
blue = (0, 0, 220)
white = (255, 255, 255)
text_color = (255, 255, 255)


#texts
names = ["Akinde-Peters, Tosin", "Atundaolu, Oluwapelumi", "Olaosilo, Samuel", "Oluwayomi, Isaac", "Onyeali, David", "Stephen, Samuel", "Talabi, Oluwasanmi"]
title = Button("A Simple Reservoir Simulator", 180, 50, white, 50, fill_color = (15, 15, 15))
dx = TextInput("Block size(ft), dx", 220, 220, text_color, 40)
dt = TextInput("Time step(days), dt", 220, 300, text_color, 40)
A = TextInput("Area(ft²) A", 280, 380, text_color, 40)
k = TextInput("Permeability(md), k", 200, 460, text_color, 40)
u = TextInput("Viscosity(cp), u", 250, 540, text_color, 40)
B = TextInput("Oil FVF(rb/stb), B", 280, 620, text_color, 40)
ct = TextInput("Compressibility(/psi), ct", 120, 700, text_color, 40)
ph = TextInput("Porosity, Ø", 220, 780, text_color, 40)
pi = TextInput("Initial reservoir pressure(psi), Pi", 20, 860, text_color, 40)
duration = TextInput("Simulation time(days), t", 180, 940, text_color, 40)
n = TextInput("Number of blocks, n", 120, 1020, text_color, 40)
prod_blocks = TextInput("Block No.:Flow rate(stb/day)", 20, 1100, text_color, 40)

texts = [dx, dt, A, k, u, B, ct, ph, pi, duration, n, prod_blocks]

text_color2 = (20, 20, 20)
#text boxes
dx = Textbox(420, 210, text_color = text_color2, height = 40, text = "1000")
dt = Textbox(420, 290, text_color = text_color2, height = 40, text = "15")
A = Textbox(420, 370,  text_color = text_color2, height = 40, text = "75000")
k = Textbox(420, 450, text_color = text_color2, height = 40, text = "15")
u = Textbox(420, 530,  text_color = text_color2, height = 40, text = "10")
B = Textbox(420, 610,  text_color = text_color2, height = 40, text = "1.0")
ct = Textbox(420, 690,  text_color = text_color2, height = 40, text = "3.5")
ph = Textbox(420, 770,  text_color = text_color2, height = 40, text = "0.18")
pi = Textbox(420, 850, text_color = text_color2, height = 40, text = "6000")
duration = Textbox(420, 930, text_color = text_color2, height = 40, text = "360")
n = Textbox(420, 1010,  text_color = text_color2, height = 40, text = "5")
prod_blocks = Textbox(420, 1090,  text_color = text_color2, height = 40, text = "4 : -150")

boxes = [dx, dt, A, k, u, B, ct, ph, pi, duration, n, prod_blocks]


#buttons
solve = Button("Simulate", 500, 1180, white)
clear = Button("Clear", 100, 1180, white)
back = Button("Back", 550, 1250, white)
pspace = Button("Pressure against Space", 100, 850, white)
ptime = Button("Pressure against Time", 100, 950, white)
pspacetime =  Button("Pressure against Space and Time", 100, 1050, white)


def add_texts(screen, texts):
    """
    add multiple texts to the screen
    """
    for tex in texts:
        screen.blit(tex.textren, (410 - tex.len, tex.yh))
    return screen
   

def add_textboxes(screen, boxes):
    """
    add multiple boxes.
    """
    for box in boxes:
        pygame.draw.rect(screen, box.border_color, box.rect, 3)
        screen.fill(white, box.rect)
        screen.blit(box.textren, (box.xh+10, box.yh+10))
    return screen
    
                
def screen1(text = "Enter reservoir properties: "):
    screen.fill((250, 250, 250))
    screen.blit(icon, (10, 10))
    rec = pygame.Rect(10, 190, 700, 960)
    #screen.fill((5, 25, 100), rec)    
    pygame.draw.rect(screen, (10, 10, 200), rec, border_radius = 25)
    #pygame.draw.line(screen, (50, 50, 250), (355, 200), (355, 1050), 2)
    solve.add_button(screen)
    clear.add_button(screen)
    back.add_button(screen)
    tex = TextInput(text, 150, 150, blue)
    tex.add_text(screen)
    title.add_button(screen)
    add_texts(screen, texts)
    add_textboxes(screen, boxes)
    
def screen2(text = "Generated Plots"):
    screen.fill((250, 250, 250))
    screen.blit(icon, (10, 10))
    screen.blit(plots, (80, 220))
    pspace.add_button(screen)
    ptime.add_button(screen)
    pspacetime.add_button(screen)
    back.add_button(screen)
    tex = TextInput(text, 50, 180, blue)
    tex2 = TextInput("Select a plot to view: ", 50, 750, blue)
    tex.add_text(screen)
    tex2.add_text(screen)
    title.add_button(screen)
    

def screen3(text = "Generated Plots"):
    screen.fill((250, 250, 250))
    screen.blit(icon, (10, 10))
    tex = TextInput(text, 100, 250, blue)
    tex.add_text(screen)
    back.add_button(screen)
    title.add_button(screen)
    
    
#Functions
def loading():
    screen.fill((250, 250, 250))
    screen.blit(loader, (170, 250))
    pygame.display.flip()
    

def solve_loop():
    simulator.pressure_space()
    simulator.pressure_time()
    simulator.final_plot()
    loop2()
    

def action(text, presplot):
    screen3(text)
    screen.blit(presplot, (50, 300))
    pygame.display.flip()
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                if back.rect.collidepoint(pos):
                    loop2()            
    

#loops for each screen
def loop1():
    screen.fill((250, 250, 250))
    screen1()
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                if solve.rect.collidepoint(pos):
                    loading()
                    solve_loop()
                     
                if clear.rect.collidepoint(pos):
                    loading()
                    screen1()
                
                if back.rect.collidepoint(pos):
                     main_loop()
                     
        pygame.display.flip()
        

def loop2():
    screen.fill((250, 250, 250))
    screen2()
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                if back.rect.collidepoint(pos):
                    loop1()
                
                if ptime.rect.collidepoint(pos):
                     loading()
                     text = "Pressure against Time"
                     presplot = pygame.image.load("savedata/pressure_time.png")
                     action(text, presplot)              
                
                if pspace.rect.collidepoint(pos):
                     loading()
                     text = "Pressure against Space"
                     presplot = pygame.image.load("savedata/pressure_space.png")                         
                     action(text, presplot) 
                if pspacetime.rect.collidepoint(pos):
                 text = "Pressure against Time and Space"
                 presplot = pygame.image.load("savedata/pressure_space_time.png")
                 loading()
                 action(text, presplot)
                     
        pygame.display.flip()


def main_loop():
    screen.fill((250, 250, 250))
    while 1:
        rec = pygame.Rect(100, 200, 500, 300)
        rec1 = pygame.Rect(75, 75, 600, 200)
        rec2 = pygame.Rect(175, 300, 400, 400)
        pygame.draw.circle(screen, white, (120, 115), 20)
        pygame.draw.rect(screen, blue, rec1, border_radius = 25)
        pygame.draw.rect(screen, blue, rec2, border_radius = 25)
        course = TextInput("PGG 509 PROJECT", 150,  100, white, 60)
        group = TextInput("Group 1: Mathematical Approach", 100, 200, white)
        click = TextInput("Click Anywhere!", 300, 1000, blue)
        course.add_text(screen)                
        group.add_text(screen)
        click.add_text(screen)
        
        xh, yh = 210, 340
        for name in names:
             tex = TextInput(name, xh, yh, white, 40)
             tex.add_text(screen)
             yh += 50
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                
            if event.type == pygame.MOUSEBUTTONUP:
                loop1()
        pygame.display.flip()
    
main_loop()

if __name__ == "__main__":
    print("Hello, World!")
  