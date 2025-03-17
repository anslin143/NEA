import pygame 

#from database import *

import sqlite3
#initilsing pygame

import sys

import math

pygame.init()

display = pygame.display.set_mode((1100, 600))

running = True 

#global background_colour
background_colour = (219,232,252)

pygame.display.set_caption("School Route Finder")

logo = pygame.image.load("logo.png")
# Scale logo 
resize_logo = pygame.transform.scale(logo, (275,275))

#Connecting to sqlite
db = sqlite3.connect("timetable.db")
c = db.cursor()

c.execute("""
    CREATE TABLE IF NOT EXISTS accounts (
        userid INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE,
        password TEXT
    )
""")

db.commit()

# Create User_Timetable Table
# c.execute("""
# CREATE TABLE IF NOT EXISTS 
# User_Timetable (
#     user_timetable_id INTEGER PRIMARY KEY AUTOINCREMENT,
#     user_id INTEGER NOT NULL,
#     timetable_id INTEGER NOT NULL,
#     FOREIGN KEY (user_id) REFERENCES Users(user_id),
#     FOREIGN KEY (timetable_id) REFERENCES Timetable(timetable_id)
# );
# """)

# # Create Subjects Table
# c.execute("""
# CREATE TABLE IF NOT EXISTS 
# Subjects (
#     subject_id INTEGER PRIMARY KEY AUTOINCREMENT,
#     subject_name TEXT UNIQUE NOT NULL
# );
# """)

# # Create Classrooms Table
# c.execute("""
# CREATE TABLE IF NOT EXISTS 
# Classrooms (
#     classroom_id INTEGER PRIMARY KEY AUTOINCREMENT,
#     room_name TEXT UNIQUE NOT NULL
# );
# """)

# # Create Timetable Table
# c.execute("""
# CREATE TABLE IF NOT EXISTS 
# Timetable (
#     timetable_id INTEGER PRIMARY KEY AUTOINCREMENT,
#     day_of_week TEXT NOT NULL,
#     lesson_number INTEGER NOT NULL,
#     start_time TEXT NOT NULL,
#     end_time TEXT NOT NULL,
#     subject_id INTEGER NOT NULL,
#     classroom_id INTEGER NOT NULL,
#     FOREIGN KEY (subject_id) REFERENCES AllowedSubjects(subject_id),
#     FOREIGN KEY (classroom_id) REFERENCES Classrooms(classroom_id)
# );
# """)




def output_text(text,fontSize, text_posX,text_posY):
    #sysFrom(name, size, bold = 0, italic = 0)
    font = pygame.font.SysFont("Calibri", fontSize, True, False)
    #font is rounded = True
    surface = font.render(text, True, (0,0,0))
    #print text to specified position onto screen
    display.blit(surface,(text_posX,text_posY))

class Button():
    def __init__(self, x, y, height, width, text,text_size, colour, hover_colour):
        self.bg = pygame.Rect(x,y, width, height)
        self.font = pygame.font.SysFont("Calibri", text_size)
        self.hover_colour = hover_colour
        self.bttnText = self.font.render(text, True, colour)

    def render(self, display, x, y, mousePos, hover_colour, text):
        pygame.draw.rect(display, "white", self.bg )
        pygame.draw.rect(display, "black", self.bg, 2 )
        if self.bg.collidepoint(mousePos) == True:
             self.bttnText = self.font.render(text, True, hover_colour)
        display.blit(self.bttnText, (x,y))

    def checkClicked(self, mousePos):
        clicked = False
        if self.bg.collidepoint(mousePos) and clicked == False:
            clicked = True
        return clicked
    

def start_page(running):
    while running == True:
        display.fill(background_colour)
        #setting position of logo
        display.blit(resize_logo, (400, 100))

        #instance of button class
        signUP_button = Button(400, 400, 50, 275, "Sign Up", colour = "black",text_size= 37, hover_colour = "grey")
        signUP_button.render(display, 490, 409, mousePos = pygame.mouse.get_pos(), hover_colour = "grey", text = "Sign Up")

        #instance of button class
        login_button = Button(400, 475, 50, 275, "Login", colour = "black",text_size= 37, hover_colour = "grey")
        login_button.render(display, 501, 485, mousePos = pygame.mouse.get_pos(), hover_colour = "grey", text = "Login")
        
        output_text("Please Login or Sign Up",fontSize=40, text_posX =350,text_posY= 28)

        #updates full display to screen
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if signUP_button.checkClicked(pygame.mouse.get_pos()) == True:
                    signup_page(running)
                elif login_button.checkClicked(pygame.mouse.get_pos()) == True:
                    login_page(running)  
    pygame.quit()


def signup_page(running):
    # WHILE loop which will run program 
    user_font = pygame.font.SysFont("Calibri", 25, True, False)
    userActive = False
    passActive = False
    createUsername = ""
    createPassword = ""
    while running == True:
        #set display colour
        display.fill(background_colour)
        output_text("Create Username",fontSize=25, text_posX =400,text_posY= 180)
        output_text("Create Password",fontSize=25, text_posX =400,text_posY= 280)
        #allow user to type input
        username_surface = user_font.render(createUsername,True, (0,0,0))
        password_surface = user_font.render(createPassword,True, (0,0,0))
       

        #create blank rectangles for user to input text
        usernameRect = Button(400, 220, 35, 275, " ", colour = "black", text_size= 37, hover_colour = "grey")
        usernameRect.render(display, 35, 275, mousePos = pygame.mouse.get_pos(), hover_colour = "grey", text = " ")

        #create blank rectangles for user to input text
        passwordRect = Button(400, 320, 35, 275, "", colour = "black",text_size= 37, hover_colour = "grey")
        passwordRect.render(display, 35, 275, mousePos = pygame.mouse.get_pos(), hover_colour = "grey", text = "")

        #add enter details button
        register_Button = Button(490, 380, 35, 100, "sign up", colour = "black",text_size= 25, hover_colour = (128,128,128))
        register_Button.render(display, 504, 385, mousePos = pygame.mouse.get_pos(), hover_colour = (128,128,128), text = "sign up")

        #add back button
        back_Button = Button(15, 530, 35, 65, "Back", colour = "black",text_size= 25, hover_colour = "grey")
        back_Button.render(display, 20, 537, mousePos = pygame.mouse.get_pos(), hover_colour = "grey", text =  "Back")

        #outputs to screen where user can write text
        display.blit(username_surface, (405, 225))

        display.blit(password_surface, (405, 325))
       
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if usernameRect.checkClicked(pygame.mouse.get_pos()) == True:
                    userActive = True
                else:
                    userActive = False
                
                if passwordRect.checkClicked(pygame.mouse.get_pos()) == True:
                    passActive = True
                else:
                    passActive = False
            if event.type == pygame.KEYDOWN:
                if userActive == True:
                    if event.key == pygame.K_BACKSPACE:
                        createUsername = createUsername[:-1]
                    else:
                        createUsername += event.unicode

                elif passActive == True:
                    if event.key == pygame.K_BACKSPACE:
                        createPassword = createPassword[:-1]
                    else:
                        createPassword += event.unicode

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if back_Button.checkClicked(pygame.mouse.get_pos()) == True:
                    start_page(running)
                    
                if register_Button.checkClicked(pygame.mouse.get_pos()) == True:
                    if sign_in_validation(createUsername, createPassword) == True:
                        home_page(running)
                    else:
                        error_message()
                           
        #updates full display to screen
        pygame.display.flip()
                    
        #updates full display to screen
    pygame.quit()


def login_page(running):
    # WHILE loop which will run program 
    user_font = pygame.font.SysFont("Calibri", 25, True, False)
    userActive = False
    passActive = False
    loginUsername = ""
    loginPassword = ""
    run = 0
    while running == True:
        #set display colour
        display.fill(background_colour)
        output_text("Enter Username",fontSize=25, text_posX =400,text_posY= 180)
        output_text("Enter Password",fontSize=25, text_posX =400,text_posY= 280)
        #allow user to type input
        username_surface = user_font.render(loginUsername,True, (0,0,0))
        password_surface = user_font.render(loginPassword,True, (0,0,0))

        #create blank rectangles for user to input text
        usernameRect = Button(400, 220, 35, 275, " ", colour = "black", text_size= 37, hover_colour = "grey")
        usernameRect.render(display, 35, 275, mousePos = pygame.mouse.get_pos(), hover_colour = "grey", text = " ")

        #create blank rectangles for user to input text
        passwordRect = Button(400, 320, 35, 275, "", colour = "black",text_size= 37, hover_colour = "grey")
        passwordRect.render(display, 35, 275, mousePos = pygame.mouse.get_pos(), hover_colour = "grey", text = "")

        #add enter details button
        login_details = Button(490, 380, 35, 75, "login", colour = "black",text_size= 25, hover_colour = (128,128,128))
        login_details.render(display, 504, 385, mousePos = pygame.mouse.get_pos(), hover_colour = (128,128,128), text = "login")

        #add back button
        backButton = Button(15, 530, 35, 65, "Back", colour = "black",text_size= 25, hover_colour = "grey")
        backButton.render(display, 20, 537, mousePos = pygame.mouse.get_pos(), hover_colour = "grey", text =  "Back")

        #outputs to screen where user can write text
        display.blit(username_surface, (405, 225))

        display.blit(password_surface, (405, 325))

        pygame.display.flip()

        

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if usernameRect.checkClicked(pygame.mouse.get_pos()) == True:
                    userActive = True
                else:
                    userActive = False
                
                if passwordRect.checkClicked(pygame.mouse.get_pos()) == True:
                    passActive = True
                else:
                    passActive = False


            if event.type == pygame.KEYDOWN:
                if userActive == True:
                    if event.key == pygame.K_BACKSPACE:
                        loginUsername = loginUsername[:-1]
                    else:
                        loginUsername += event.unicode

                elif passActive == True:
                    if event.key == pygame.K_BACKSPACE:
                        loginPassword = loginPassword[:-1]
                    else:
                        loginPassword += event.unicode


            
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if backButton.checkClicked(pygame.mouse.get_pos()) == True:
                    start_page(running)
                if login_details.checkClicked(pygame.mouse.get_pos()) == True:
                    run = +1 
                    if login_validation(loginUsername, loginPassword) == True:
                        home_page(running)
                    # else:
                    #     error_message()
       # print(run)
        if run==1 and login_validation(loginUsername, loginPassword) == False:
            error_message()
        #updates full display to screen
        pygame.display.flip()
    pygame.quit()

def error_message():
    output_text("ERROR MESSAGE", fontSize=20, text_posX=320, text_posY=450)


def sign_in_validation(username, password):
    
        if username == "" or password == "":
            output_text("Please enter a username and password", fontSize=20, text_posX=320, text_posY=450)
            #print("Please enter a username and password")
            return False

        # Check if the username already exists
        c.execute("SELECT * FROM accounts WHERE username = ?", (username,))
        existing_user = c.fetchone()

        if existing_user:
            output_text("Username already exists! Try a different one.", fontSize=20, text_posX=320, text_posY=450)
           # print("Username already exists! Try a different one.")
            return False
        
        c.execute("INSERT INTO accounts (username, password) VALUES (?, ?)", (username, password))

        db.commit()
        output_text("User registered successfully!", fontSize=20, text_posX=320, text_posY=450)
        #print("User registered successfully!")
        return True

    
def login_validation(username, password):
        if username == "" or password == "": 
            #output_text("Please enter a username and password", fontSize=20, text_posX=320, text_posY=450)
            #print("Please enter a username and password")
            return False

        # Check if the username already exists
        c.execute("SELECT * FROM accounts WHERE username = ?", (username,))
        user = c.fetchone()

        if user:
            output_text("login successful", fontSize=20, text_posX=320, text_posY=450)
            #print("Login successful")
            return True
        else:
            output_text("Username does not exist! Try a different one.", fontSize=20, text_posX=320, text_posY=450)
            #print("Username does not exist! Try a different one.")
            return False

def home_page(running):
    # WHILE loop which will run program 
    while running == True:
        #set display colour
        display.fill(background_colour)
        #for testing purposes NOT in correct position
        output_text("Home Page",fontSize=50, text_posX =420,text_posY= 28)
        #setting position of logo
        display.blit(resize_logo, (400, 100))

        #instance of button class
        timetable_button = Button(400, 400, 50, 275, "Timetable", colour = "black",text_size= 37, hover_colour = "grey")
        timetable_button.render(display, 466, 409, mousePos = pygame.mouse.get_pos(), hover_colour = "grey", text = "Timetable")

        #instance of button class
        map_button = Button(400, 475, 50, 275, "Map", colour = "black",text_size= 37, hover_colour = "grey")
        map_button.render(display, 505, 485, mousePos = pygame.mouse.get_pos(), hover_colour = "grey", text = "Map")
        

    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if timetable_button.checkClicked(pygame.mouse.get_pos()) == True:
                    timetable_page(running)
                elif map_button.checkClicked(pygame.mouse.get_pos()) == True:
                    map_page(running)
            

        #updates full display to screen
        pygame.display.flip()

    pygame.quit()

def timetable_page(running):
    user_font = pygame.font.SysFont("Calibri", 25, True, False)
    Mon_p1_A_Active = False
    Mon_p2_A_Active = False
    Mon_p3_A_Active = False
    Mon_p4_A_Active = False

    Tue_p1_A_Active = False
    Tue_p2_A_Active = False
    Tue_p3_A_Active = False
    Tue_p4_A_Active = False
    Tue_p5_A_Active = False

    Wed_p1_A_Active = False
    Wed_p2_A_Active = False
    Wed_p3_A_Active = False
    Wed_p4_A_Active = False
    Wed_p5_A_Active = False
    
    Thu_p1_A_Active = False
    Thu_p2_A_Active = False
    Thu_p3_A_Active = False
    Thu_p4_A_Active = False
    Thu_p5_A_Active = False

    Fri_p1_A_Active = False
    Fri_p2_A_Active = False
    Fri_p3_A_Active = False
    Fri_p4_A_Active = False
    Fri_p5_A_Active = False

    Mon_p1_B_Active = False
    Mon_p2_B_Active = False
    Mon_p3_B_Active = False
    Mon_p4_B_Active = False
    Mon_p5_B_Active = False

    Tue_p1_B_Active = False
    Tue_p2_B_Active = False
    Tue_p3_B_Active = False
    Tue_p4_B_Active = False
    Tue_p5_B_Active = False

    Wed_p1_B_Active = False
    Wed_p2_B_Active = False
    Wed_p3_B_Active = False
    Wed_p4_B_Active = False
    Wed_p5_B_Active = False

    Thu_p1_B_Active = False
    Thu_p2_B_Active = False
    Thu_p3_B_Active = False
    Thu_p4_B_Active = False
    Thu_p5_B_Active = False
    
    Fri_p1_B_Active = False
    Fri_p2_B_Active = False
    Fri_p3_B_Active = False
    Fri_p4_B_Active = False
    Fri_p5_B_Active = False

    Mon_p1_A = ""
    Mon_p2_A = ""
    Mon_p3_A = ""
    Mon_p4_A = ""
    Mon_p5_A = ""

    Tue_p1_A = ""
    Tue_p2_A = ""
    Tue_p3_A = ""
    Tue_p4_A = ""
    Tue_p5_A = ""

    Wed_p1_A = ""
    Wed_p2_A = ""
    Wed_p3_A = ""
    Wed_p4_A = ""
    Wed_p5_A = ""

    Thu_p1_A = ""
    Thu_p2_A = ""
    Thu_p3_A = ""
    Thu_p4_A = ""
    Thu_p5_A = ""

    Fri_p1_A = ""
    Fri_p2_A = ""
    Fri_p3_A = ""
    Fri_p4_A = ""
    Fri_p5_A = ""

    Mon_p1_B = ""
    Mon_p2_B = ""
    Mon_p3_B = ""
    Mon_p4_B = ""
    Mon_p5_B = ""

    Tue_p1_B = ""
    Tue_p2_B = ""
    Tue_p3_B = ""
    Tue_p4_B = ""
    Tue_p5_B = ""

    Wed_p1_B = ""
    Wed_p2_B = ""
    Wed_p3_B = ""
    Wed_p4_B = ""
    Wed_p5_B = ""

    Thu_p1_B = ""
    Thu_p2_B = ""
    Thu_p3_B = ""
    Thu_p4_B = ""
    Thu_p5_B = ""

    Fri_p1_B = ""
    Fri_p2_B = ""
    Fri_p3_B = ""
    Fri_p4_B = ""
    Fri_p5_B = ""

    while running == True:
       
        #set display colour
        display.fill(background_colour)
        
        output_text("Please enter classroom room numbers below", fontSize=23, text_posX=370, text_posY=30)


        timetable = pygame.image.load("timetable.jpg")
        resize_timetable = pygame.transform.scale(timetable, (750,510))
        display.blit(resize_timetable, (150, 50))


        #add back button
        back_Button = Button(15, 530, 35, 65, "Back", colour = "black",text_size= 25, hover_colour = "grey")
        back_Button.render(display, 20, 537, mousePos = pygame.mouse.get_pos(), hover_colour = "grey", text = "Back")
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if back_Button.checkClicked(pygame.mouse.get_pos()) == True:
                    home_page(running)

        #updates full display to screen
        pygame.display.flip()
        display.fill((255, 255, 255))
        #pygame_widgets.update(event)

    pygame.quit()

def weekB_page(running):
    pass
    while running == True:
        #set display colour
        display.fill(background_colour)
        
        weekB = pygame.image.load("weekB.jpg")
        resize_timetable = pygame.transform.scale(weekB, (900,510))
        display.blit(resize_timetable, (96, 50))

        #add back button
        back_Button = Button(15, 530, 35, 65, "Back", colour = "black",text_size= 25, hover_colour = "grey")
        back_Button.render(display, 20, 537, mousePos = pygame.mouse.get_pos(), hover_colour = "grey", text = "Back")

        weekA_Button = Button(1000, 530, 35, 85, "Week A", colour = "black",text_size= 25, hover_colour = "grey")
        weekA_Button.render(display, 1000, 541, mousePos = pygame.mouse.get_pos(), hover_colour = "grey", text = "Week A")
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if back_Button.checkClicked(pygame.mouse.get_pos()) == True:
                    home_page(running)
                if weekA_Button.checkClicked(pygame.mouse.get_pos()) == True:
                    timetable_page(running)

        #updates full display to screen
        pygame.display.flip()
        display.fill((255, 255, 255))
        #pygame_widgets.update(event)

    pygame.quit()

def map_page(running):

    # Define colors
    WHITE = (0, 0, 0)
    BLACK = (255, 255, 255)
    BLUE = (0, 0, 255)
    RED = (255, 0, 0)
    GREY = (200, 200, 200)

    # Define rooms as nodes with positions
    nodes = {
        # Rooms
        "chapel": pygame.Rect(273, 380, 40, 40),
        "1": pygame.Rect(338, 365, 20, 20),
        "4": pygame.Rect(338, 400, 20, 20),
        "Office": pygame.Rect(570, 403, 35, 17),
        "new hall": pygame.Rect(800, 320, 50, 40),
        "common room": pygame.Rect(795, 475, 80, 30),
        "6SR": pygame.Rect(687, 434, 30, 30),
        "020": pygame.Rect(683, 380, 30, 30),
        "old hall": pygame.Rect(680, 305, 40,40),
        "music": pygame.Rect(600, 144, 40, 25),
        "57": pygame.Rect(675, 190, 25, 25),
        "58": pygame.Rect(720, 190, 25, 25),
        "62": pygame.Rect(800, 190, 25, 25),
        "64": pygame.Rect(915, 190, 25, 25),
        "65": pygame.Rect(915, 140, 25, 25),
        "66": pygame.Rect(995, 135, 25, 25),
        "67": pygame.Rect(1040, 200, 25, 25),
        "81": pygame.Rect(890, 40, 25, 25),
        "82": pygame.Rect(955, 40, 25, 25),
        "83": pygame.Rect(1030, 40, 25, 25),
        "old gym": pygame.Rect(723, 75, 25, 25),
        "018": pygame.Rect(642, 432, 25, 25),
        "locker": pygame.Rect(638, 280, 33,20),
        "yr7 locker": pygame.Rect(738, 270, 40,20),
        "040": pygame.Rect(610, 255, 20,20),
        "drama": pygame.Rect(730, 315, 33,20),

        "2": pygame.Rect(388, 360, 20, 20),
        "Library": pygame.Rect(450, 355, 45, 30),
        "03": pygame.Rect(432, 400, 20, 20),
        "012": pygame.Rect(532, 400,30, 30),
        
        
        # Corridor break points 
        "C1": pygame.Rect(320, 382, 10, 10),
        "C2": pygame.Rect(370, 382, 10, 10),
        "C3": pygame.Rect(366, 400, 10, 10),
        "C4": pygame.Rect(410, 402, 10, 10),
        "C5": pygame.Rect(410, 386, 10, 10),
        "C6": pygame.Rect(430, 385, 10, 10),
        "C7": pygame.Rect(510, 385, 10, 10),
        "C8": pygame.Rect(530, 385, 10, 10),
        "C9": pygame.Rect(570, 385, 10, 10),
        "C10": pygame.Rect(568, 365, 10, 10),
        "C11": pygame.Rect(582, 368, 10, 10),
        "C12": pygame.Rect(638, 368, 10, 10),
        "C13": pygame.Rect(638, 343, 10, 10),
        "C14": pygame.Rect(665, 343, 10, 10),
        "C15": pygame.Rect(688, 368, 10, 10),
        "C16": pygame.Rect(750, 368, 10, 10),
        "C17": pygame.Rect(800, 380, 10, 10),
        "C18": pygame.Rect(768, 438, 10, 10),
        "C19": pygame.Rect(768, 485, 10, 10),
        "C20": pygame.Rect(568, 335, 10, 10),
        "C21": pygame.Rect(575, 280, 10, 10),
        "C22": pygame.Rect(415, 335, 10, 10),
        "C23": pygame.Rect(621, 280, 10, 10),
        "C24": pygame.Rect(665, 293, 10, 10),
        "C25": pygame.Rect(675, 253, 10, 10),
        "C26": pygame.Rect(715, 253, 10, 10),
        "C27": pygame.Rect(647, 245, 10, 10),
        "C28": pygame.Rect(647, 229, 10, 10),
        "C29": pygame.Rect(647, 179, 10, 10),
        "C30": pygame.Rect(703, 177, 10, 10),
        "C31": pygame.Rect(753, 177, 10, 10),
        "C32": pygame.Rect(753, 153, 10, 10),
        "C33": pygame.Rect(787, 153, 10, 10),
        "C34": pygame.Rect(773, 177, 10, 10),
        "C35": pygame.Rect(843, 177, 10, 10),
        "C36": pygame.Rect(883, 177, 10, 10),
        "C37": pygame.Rect(953, 177, 10, 10),
        "C38": pygame.Rect(965, 185, 10, 10),
        "C39": pygame.Rect(1022, 185, 10, 10),
        "C40": pygame.Rect(965, 235, 10, 10),
        "C41": pygame.Rect(1075, 285, 10, 10),
        "C42": pygame.Rect(1075, 105, 10, 10),
        "C43": pygame.Rect(990, 100, 10, 10),
        "C44": pygame.Rect(930, 100, 10, 10),
        "C45": pygame.Rect(930, 80, 10, 10),
        "C46": pygame.Rect(965, 125, 10, 10),
        "C47": pygame.Rect(858, 110, 10, 10),
        "C48": pygame.Rect(787, 15, 10, 10),
        "C49": pygame.Rect(647, 15, 10, 10),
        "C50": pygame.Rect(570, 144, 10, 10),
        "C51": pygame.Rect(570, 229, 10, 10),
    }

    # Define weighted graph: nodes (rooms & corridors) connected by distances
    graph = {

        "chapel": {"C1": 2},
        "1": {"C1": 2, "C2":2},
        "4": {"C3": 2},
        "Office": {"C9": 2},
        "new hall": {"C16": 2},
        "common room": {"C19": 2},
        "6SR": {"C18": 2},
        "020": {"C15": 2},
        "old hall": {"C14": 2, "C15": 2, "C24": 2, "C25": 2, "C26": 2},
        "music":{"C29": 2}, 
        "57": {"C29": 2},
        "58": {"C30": 2},
        "62": {"C34": 2, "C35": 2},
        "64": {"C36": 2},
        "65": {"C37": 2},
        "66": {"C46": 2},
        "67": {"C39": 2},
        "81": {"C45": 2},
        "82": {"C45": 2},
        "83": {"C43": 2},
        "old gym": {"C32": 2},
        "018": {"C12": 2},
        "locker": {"C23": 2, "C24": 2, "C27": 2, "C25": 2},
        "yr7 locker": {"C26": 2},
        "040": {"C23": 2},
        "drama": {"C16": 2},

        "2": {"C2": 2},
        "03": {"C4": 2},
        "012": {"C8": 2},
        "Library": {"C6": 2},
        
        # Corridors and their connections
        "C1": {"1": 2, "C2": 3, "chapel": 2},
        "C2": {"2": 2, "C1": 3, "C3": 2},
        "C3": {"4": 2, "C2": 2, "C4": 3},
        "C4": {"03": 2, "C5": 2, "C3": 3},
        "C5": {"C6": 3, "C22": 8, "C4": 2},
        "C6": {"C5": 3, "C7": 5},
        "C7": {"C6": 5, "C8": 2},#staff room to be added 
        "C8": {"C7": 2, "C9": 3, "012": 2},
        "C9": {"C8": 3, "C10": 3, "Office": 2, "C11": 2},
        "C10": {"C9": 3, "C20": 5, "C11": 3},
        "C11": {"C10": 3, "C12": 4, "C9": 2},
        "C12": {"C11": 4, "C13": 2, "018": 2, "C15": 4},
        "C13": {"C12": 2, "C14": 2},
        "C14": {"C13": 2, "C15": 2,"old hall": 2}, 
        "C15": {"C14": 2, "C16": 5, "020": 2, "C12": 4, "C24": 3, "old hall": 2},
        "C16": {"C15": 5, "C17": 3, "new hall": 2, "drama": 2},
        "C17": {"C16": 3, "C18": 3},
        "C18": {"C17": 3, "C19": 3, "6SR": 2},####
        "C19": {"C18": 3, "common room": 2},
        "C20": {"C10": 5, "C21": 4, "C22": 12, },
        "C21": {"C20": 4, "C23": 2, "C51": 4},
        "C22": {"C20": 12, "C5": 8},
        "C23": {"C21": 2, "040": 2, "locker": 2},
        "C24": {"C15": 3, "old hall": 2, "locker": 2},
        "C25": {"C24": 2, "C26": 2, "C27": 2},
        "C26": {"C25": 2, "C27": 2, "yr7 locker": 2},
        "C27": {"locker": 2, "C28": 2, "C25": 2},
        "C28": {"C27": 2, "C29": 7, "C51": 4, "C40":22},
        "C29": {"music": 2, "57": 2, "C28": 7, "C30": 5},
        "C30": {"C29": 5, "C31": 4, "58": 2},
        "C31": {"C30": 4, "C32": 2, "C34": 1},
        "C32": {"C31": 2, "C33": 2, "old gym": 2},
        "C33": {"C32": 2, "C47": 6}, 
        "C34": {"C31": 1, "C35": 5, "62": 2},
        "C35": {"C34": 5, "C36": 3, "62": 2},
        "C36": {"C35": 3, "C37": 5, "64": 2, "C47": 6}, 
        "C37": {"C36": 5, "C38": 1, "65": 2},
        "C38": {"C37": 1, "C39": 3, "C40": 6},
        "C39": {"C38": 3, "67": 2},
        "C40": {"C38": 6, "C28": 22, "C41": 8},
        "C41": {"C40": 8, "C42": 10},
        "C42": {"C41": 10, "C43": 5},
        "C43": {"C42": 5, "C44": 3, "83": 2},
        "C44": {"C43": 3, "C45": 1},
        "C45": {"C44": 1, "81": 2, "82": 2},
        "C46": {"C44": 3, "C43": 3, "66": 2, "C47": 5},
        "C47": {"C44": 3, "C46": 5,"C36": 6, "C33": 6, "C48": 6},
        "C48": {"C47": 6, "C49": 6},
        "C49": {"C48": 6, "C50": 8},
        "C50": {"C49": 6, "C51": 7},
        "C51": {"C50": 7, "C21": 4, "C28": 4},
    }

    #cost to reach a node from the starting point. 
    G_SCORE = 0
    #estimate of the total cost to reach the goal through a particular node
    F_SCORE = 1
    PREVIOUS = 2

    for node in graph:
        for neighbor in graph[node]:
            x1, y1 = nodes[node].center
            x2, y2 = nodes[neighbor].center
            #distance calculation using the Euclidean formula
            graph[node][neighbor] = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

    def get_heuristic(node):
        return 0
        

    def lowest_fscore(unvisited):
        return min(unvisited, key=lambda node: unvisited[node][F_SCORE])

    
    def a_star(graph, start_node, target_node):
        
        visited = {} 
        unvisited = {node: [sys.maxsize, sys.maxsize, None] for node in graph}

        # Initialize start node
        unvisited[start_node] = [0, get_heuristic(start_node), None]

        while unvisited:
            #returns node with the smallest F_SCORE.
            current_node = lowest_fscore(unvisited)

            if current_node == target_node:
                visited[current_node] = unvisited[current_node]
                break

            for neighbor in graph[current_node]:
                if neighbor not in visited:
                    new_g_score = unvisited[current_node][G_SCORE] + graph[current_node][neighbor]

                    if new_g_score < unvisited[neighbor][G_SCORE]:
                        unvisited[neighbor][G_SCORE] = new_g_score
                        unvisited[neighbor][F_SCORE] = new_g_score + get_heuristic(neighbor)
                        unvisited[neighbor][PREVIOUS] = current_node

            visited[current_node] = unvisited[current_node]
            del unvisited[current_node]

        return visited

    # Reconstruct Shortest Path from A* Output
    def reconstruct_path(visited, start, end):
        path = []
        current = end
        while current is not None:
            path.append(current)
            current = visited[current][PREVIOUS]
        return path[::-1] if path[-1] == start else []


    selected_nodes = []
    path = []

    running = True
    while running:
        display.fill(background_colour)

        #add back button
        back_Button = Button(15, 530, 35, 65, "Back", colour = "black",text_size= 25, hover_colour = "grey")
        back_Button.render(display, 20, 537, mousePos = pygame.mouse.get_pos(), hover_colour = "grey", text =  "Back")

        rectangle = Button(250, 10, 582, 844, " ", colour = "black", text_size= 37, hover_colour = "grey")
        rectangle.render(display, 35, 275, mousePos = pygame.mouse.get_pos(), hover_colour = "grey", text = " ")
        
        map = pygame.image.load("map3.jpg")
        resize_map = pygame.transform.scale(map, (820, 565))
        display.blit(resize_map, (255, 13))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if back_Button.checkClicked(pygame.mouse.get_pos()) == True:
                    home_page(running)

                for name, rect in nodes.items():
                    if rect.collidepoint(event.pos):  
                        if name not in selected_nodes:
                            selected_nodes.append(name)

                        if len(selected_nodes) > 2:
                            selected_nodes.pop(0)

                        # Calculate Path if Two Nodes Selected
                        if len(selected_nodes) == 2:
                            visited_nodes = a_star(graph, selected_nodes[0], selected_nodes[1])
                            path = reconstruct_path(visited_nodes, selected_nodes[0], selected_nodes[1])

        # Draw Nodes
        for name, rect in nodes.items():
            colour = GREY if name.startswith("C") else (BLUE if name in selected_nodes else BLACK)

            pygame.draw.rect(display, colour, rect)
            font = pygame.font.Font(None, 15)
            text = font.render(name, True, WHITE)
            text_rect = text.get_rect(center=rect.center)
            display.blit(text, text_rect)

        # Draw Shortest Path
        if len(path) > 1:
            for i in range(len(path) - 1):
                node1_center = nodes[path[i]].center
                node2_center = nodes[path[i + 1]].center
                pygame.draw.line(display, RED, node1_center, node2_center, 2)

        pygame.display.flip()  # Refresh Display

    pygame.quit()  # Quit Pygame

start_page(running)
db.commit()
db.close()
