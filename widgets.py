import pygame
pygame.init()


class Screen:
    """
    screen, pygame display.
    """
    def __init__(self, color = (250, 250, 250), size = (720, 1280)):
        self.color = color
        self.size = size
        self.screen = pygame.display.set_mode(size)
        self.screen.fill(self.color)
        
        
class Widget:
    """
    widget class, button, text, etc.
    """
    def __init__(self, xh = 0, yh = 0, color = (0, 0, 200)):
        """
        xh = left of button
        yh = top of button
        color = text color
        """
        self.text = text
        self.color = color
        self.textren = myfont.render(text, 1, self.color)
        self.xh = xh
        self.yh = yh
        self.rect = pygame.Rect(self.xh-5, self.yh-5, (len(self.text))*20, 40)


class TextInput:
    """
    TextInput Widget.
    """  
    def __init__(self, text = "Text", xh = 0, yh = 0, color = (10, 10, 10), size = 50):
       #text = text
        self.text = text
        self.size = size
        myfont = pygame.font.SysFont("DejaVuSans", self.size)        
        self.textren = myfont.render(text, 1, color)
        self.rect = self.textren.get_rect()
        self.len = self.rect.right
        self.xh = xh
        self.yh = yh
    
    def add_text(self, screen):
        """
        add the text to the screen.
        screen = pygame.display
        """
        screen.blit(self.textren, (self.xh, self.yh))
        return screen          


class Button:
    """
    Button Widget.
    """  
    def __init__(self, text = "Button", xh = 0, yh = 0, text_color = (10, 10, 10), size = 50, border_color = (0, 20, 200), fill_color = (10, 10, 205)):
       #text = text on button.
        self.text = text
        self.size = size
        self.text_color = text_color        
        myfont = pygame.font.SysFont("DejaVuSans", self.size)
        self.textren = myfont.render(self.text, 1, self.text_color)
        self.xh = xh
        self.yh = yh
        temp = self.textren.get_rect()
        self.rect = pygame.Rect(self.xh-10, self.yh-10, temp.right+20, temp.bottom+20)
        self.nrect = pygame.Rect(self.xh-5, self.yh+30, temp.right+10, 5)
        self.border_color = border_color
        self.fill_color = fill_color    
        
    
    def add_button(self, screen, border_radius = 25):
        """
        add the button to the screen.
        screen = pygame.display
        border_color = border color
        """        
        pygame.draw.rect(screen, self.border_color, self.rect, border_radius = border_radius)
        #screen.fill(self.fill_color, self.rect) #self.nrect)
        screen.blit(self.textren, (self.xh, self.yh))
        return screen


class Textbox:
    """
    Text box.
    """
    def __init__(self, xh = 100, yh = 100, width = 200, height = 50, fill_color = (100, 100, 100), border_color = (250, 250, 250), text_color = (0, 0, 0), text = ""):
        self.xh = xh
        self.yh = yh
        self.width = width
        self.height = height
        self.text_color = text_color
        self.border_color = border_color
        self.fill_color = fill_color            
        self.rect = pygame.Rect(self.xh, self.yh, self.width, self.height)
        self.empty = False
        self.active = True
        self.text = text
        self.font = pygame.font.SysFont("DejaVuSans", self.height)
        self.textren = self.font.render(self.text, 1, self.text_color)             
               
    
    def add_textbox(self, screen):
        """
        add the text box.
        """
        pygame.draw.rect(screen, self.border_color, self.rect, 3)
        screen.blit(self.textren, (self.xh+10, self.yh+10))        
        return screen
            
    
    def update_text(self):
        for event in pygame.event.get():
            if event.type == (pygame.KEYDOWN or pygame.KEYUP) and self.active:
                if event == pygame.K_RETURN:
                    self.active = False
                if event == pygame.K_BACKSPACE:
                    self.text = self.text[ : -1]
                    rec = pygame.Rect(self.xh+10, self.yh+10, 187, 37)
                    screen.fill(self.fill_color, rec)
                else:
                    self.text += event.unicode
            self.text = text
            return self.text
        
    def add_text(self, screen):
        pygame.key.start_text_input()
        self.active = True
        x, y = self.rect.left, self.rect.top
        self.update_text()
            
        self.textren = self.font.render(self.text, 1, self.text_color)
        screen.blit(self.textren, (self.xh+10, self.yh+10))
        pygame.display.flip()
        return screen



def add_textboxes(screen, boxes):
    """
    add multiple boxes.
    """
    for box in boxes:
        pygame.draw.rect(screen, box.border_color, box.rect, 3)
        screen.blit(box.textren, (box.xh+10, box.yh+10))        
    
    return screen
              

def add_textboxes(screen, boxes):
    """
    add multiple boxes.
    """
    for box in boxes:
        pygame.draw.rect(screen, box.border_color, box.rect, 3)
        screen.blit(box.textren, (box.xh+10, box.yh+10))   
    return screen


def add_buttons(screen, buttons, border_color = (250, 250, 250), fill_color = (10, 10, 255)):
    """
    add multiple buttons to the screen.
    """
    for button in buttons:
        pygame.draw.rect(screen, button.border_color, button.rect, 10)
        screen.fill(button.fill_color, button.rect) #self.nrect)
        screen.blit(button.textren, (button.xh, button.yh))
        return screen
        

def add_texts(screen, texts):
    """
    add multiple texts to the screen
    """
    for tex in texts:
        screen.blit(tex.textren, (tex.xh, tex.yh))
    return screen
    

                        