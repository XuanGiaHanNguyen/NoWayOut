import pygame
class Menu():
    def __init__(self,game):
        self.game = game
        self.mid_w,self.mid_h = self.game.DISPLAY_W/2, self.game.DISPLAY_H/2
        self.run_display = True
        self.cursor_rect = pygame.Rect(0,0,20,20)
        self.offset = - 100

    def draw_cursor(self):
        self.game.draw_text(">",20,self.cursor_rect.x, self.cursor_rect.y)

    def blit_screen(self):
        self.game.window.blit(self.game.display, (0, 0))
        pygame.display.update()
        self.game.reset_keys()

class MainMenu(Menu):
    def __init__(self,game):
        Menu.__init__(self,game)

        self.state = "Start"
        #the location of each button
        self.startx,self.starty = self.mid_w, self.mid_h +50
        self.optionx, self.optiony = self.mid_w, self.mid_h + 80
        self.creditx, self.credity = self.mid_w, self.mid_h + 110
        #starting position for the cursor
        self.cursor_rect.midtop = (self.startx +self.offset, self.starty)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            bg = pygame.image.load('bg.jpg')
            self.game.check_events()
            self.check_input()
            self.game.display.fill((0,0,0))
            self.game.draw_text("No Way Out",40,self.game.DISPLAY_W/2, self.game.DISPLAY_H/2 -30)
            self.game.draw_text("Start Game",25,self.startx,self.starty)
            self.game.draw_text("Option", 25, self.optionx, self.optiony)
            self.game.draw_text("Credit", 25, self.creditx, self.credity)
            self.draw_cursor()
            self.blit_screen()

    def move_cursor(self):
        if self.game.DOWN_KEY:
            if self.state == "Start":
                self.cursor_rect.midtop = (self.optionx + self.offset, self.optiony)
                self.state = "Option"
            elif self.state == "Option":
                self.cursor_rect.midtop = (self.creditx + self.offset, self.credity)
                self.state = "Credit"
            elif self.state == "Credit":
                self.cursor_rect.midtop = (self.startx + self.offset, self.starty)
                self.state = "Start"

        elif self.game.UP_KEY:
            if self.state == "Start":
                self.cursor_rect.midtop = (self.creditx + self.offset, self.credity)
                self.state = "Option"
            elif self.state == "Option":
                self.cursor_rect.midtop = (self.optionx + self.offset, self.optiony)
                self.state = "Credit"
            elif self.state == "Credit":
                self.cursor_rect.midtop = (self.startx + self.offset, self.starty)
                self.state = "Start"
                
    def check_input(self):
        self.move_cursor()
        if self.game.START_KEY:
            if self.state == "Start":
                self.game.playing = True
            elif self.state == "Option":
                self.game.curr_menu = self.game.options
            elif self.state == "Credit":
                self.game.curr_menu = self.game.credit

            self.run_display = False #stop displaying menu

class OptionMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self,game)
        self.state = "Volume"
        self.volx,self.voly = self.mid_w, self.mid_h + 20
        self.controlx,self.controly = self.mid_w, self.mid_h + 45
        self.cursor_rect.midtop = (self.volx + self.offset, self.voly)

    def display_menu(self):
        self.run_display = True

        while self.run_display:
            self.game.check_events()
            self.check_Input()
            self.game.display.fill((0,0,0))
            self.game.draw_text("Options",25,self.game.DISPLAY_W/2, self.game.DISPLAY_H/2 -30)
            self.game.draw_text("Volume", 20, self.volx, self.voly)
            self.game.draw_text("Control", 20, self.controlx, self.controly)
            self.draw_cursor()
            self.blit_screen()

    def check_Input(self):
        if self.game.BACK_KEY:
            self.game.curr_menu = self.game.main_menu
            self.run_display = False

        elif self.game.UP_KEY or self.game.DOWN_KEY:
            if self.state == "Volume":
                self.state = "Control"
                self.cursor_rect.midtop = (self.controlx + self.offset, self.controly)
            elif self.state == "Control":
                self.state = "Volumn"
                self.cursor_rect.midtop = (self.volx + self.offset, self.voly)

        elif self.game.START_KEY: #To-Do : create a volumn menu and a control menu
            pass

class CreditMenu(Menu):
    def __init__(self,game):
        Menu.__init__(self,game)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()

            if self.game.START_KEY or self.game.BACK_KEY:
                self.game.curr_menu = self.game.main_menu
                self.run_display = False

            self.game.display.fill(self.game.BLACK)
            self.game.draw_text("Credits",25,self.game.DISPLAY_W/2, self.game.DISPLAY_H/2 -20)
            self.game.draw_text("Xuan Gia Han Nguyen", 20, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 + 10)
            self.game.draw_text("Dang Minh Anh Nguyen", 20, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 + 30)
            self.blit_screen()
