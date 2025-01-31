import pygame 
#initilsing pygame
pygame.init()

display = pygame.display.set_mode((1100, 600))

running = True 

background_colour = (219,232,252)

pygame.display.set_caption("School Route Finder")

logo = pygame.image.load("logo.png")
# Scale logo 
resize_logo = pygame.transform.scale(logo, (275,275))


def output_text(text,text_posX,text_posY):
    #sysFrom(name, size, bold = 0, italic = 0)
    font = pygame.font.SysFont("Calibri", 40, True, False)
    #font is rounded = True
    #numbers in bracket is colour of text which has been set to white 
    surface = font.render(text, True, (0,0,0))
    #print text to specified position onto screen
    display.blit(surface,(text_posX,text_posY))

def output_button():
    # creates a rectangle of 190x60 pixels located at the
    # (30,10) position on the screen
    pygame.draw.rect(display, (255,255,255), pygame.Rect(30, 10, 190, 60), 2 )


#function to test if button can be clicked 
def buttonCommand():
    print("This button has been clicked")  

class Button():
    def __init__(self, x, y, height, width, text,command, colour, hover_colour):
        self.bg = pygame.Rect(x,y, width, height)
        self.font = pygame.font.SysFont("Calibri", 37)
        #self.bttnText = self.font.render(text, True, "black")
        
        self.bttnText = self.font.render(text, True, colour)
        self.command = command
        self.colour, self.hover_colour = colour, hover_colour

    def update(self, mousePos):
        if self.bg.collidepoint(mousePos):
            self.command()

    def render(self, display, x, y):
        pygame.draw.rect(display, "white", self.bg )
        pygame.draw.rect(display, "black", self.bg, 2 )
        display.blit(self.bttnText, (x,y))
    
    def changeColour(self, mousePos, hover_colour, text, display, x, y):
        if self.bg.collidepoint(mousePos) == True:
            self.bttnText = self.font.render(text, True, hover_colour)
            #pygame.draw.rect(display, "grey", self.bg)
            display.blit(self.bttnText, (x,y))



def start_page(running):
    while running == True:
        display.fill(background_colour)
        #setting position of logo
        display.blit(resize_logo, (400, 100))
        signUP_button = Button(400, 400, 50, 275, "Sign Up", buttonCommand, colour = "black", hover_colour = "grey")
        signUP_button.render(display, 490, 409)
        #updates full display to screen
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                signUP_button.update(pygame.mouse.get_pos())

    pygame.quit()
    
def login_page():
    pass
    # WHILE loop which will run program 
    while running == True:
        #set display colour
        display.fill(background_colour)
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        #updates full display to screen
        pygame.display.flip()

    pygame.quit()

def register_page():
    pass
    # WHILE loop which will run program 
    while running == True:
        #set display colour
        display.fill(background_colour)
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        #updates full display to screen
        pygame.display.flip()

    pygame.quit()

def home_page():
    pass
    # WHILE loop which will run program 
    while running == True:
        #set display colour
        display.fill(background_colour)
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        #updates full display to screen
        pygame.display.flip()

    pygame.quit()

def timetable_page():
    pass
    # WHILE loop which will run program 
    while running == True:
        #set display colour
        display.fill(background_colour)
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        #updates full display to screen
        pygame.display.flip()

    pygame.quit()


def map_page():
    pass 
    # WHILE loop which will run program 
    while running == True:
        #set display colour
        display.fill(background_colour)
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        #updates full display to screen
        pygame.display.flip()

    pygame.quit()

def menu():
    pass
    #create menu view and connect buttons with 

def login():
    pass
    username = input("Enter username: ")
    password = input("Enter password: ")
    #connect to database with SQL 



start_page(running)


