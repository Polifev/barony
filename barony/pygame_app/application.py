import sys
from typing import Dict

import pygame
from pygame import Color, Rect, Surface
from pygame.font import Font, SysFont
from pygame.locals import QUIT, VIDEORESIZE
from barony.game.kingdom import Kingdom

from barony.pygame_app.layout.screen import Screen

class PygameApplication:
    fonts: Dict[str, Font]
    images: Dict[str, Surface]
    colors: Dict[str, Color]

    def __init__(self):
        pygame.init()
        self.images = {}
        self.fonts = {}
        self.colors = {}
    
    def load_assets(self):
        self.images["button"] = pygame.image.load("assets/button.png")
        self.fonts["default"] = SysFont(None, 32)

        self.colors["background"] = Color(40, 30, 10)
        self.colors["frame"] = Color(200, 180, 30)
        self.colors["text"] = Color(230, 230, 230)

    def run(self):
        kingdom = Kingdom()

        DIMENSIONS = (800, 600)
        FPS = 60
        screen = Screen(DIMENSIONS)

        FramePerSec = pygame.time.Clock()
        
        displaysurface = pygame.display.set_mode(DIMENSIONS, pygame.RESIZABLE)
        pygame.display.set_caption("Barony")

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False
                elif event.type == VIDEORESIZE:
                    screen.dimensions = event.dict["size"]
            
            displaysurface.fill(self.colors["background"])


            # displaysurface.blit(self.images["button"], dest=(0, 0))
            # displaysurface.blit(self.fonts["default"].render("Coucou Morgane", True, (0,0,0)), dest=(0, 0))


            position = screen.to_absolute((0.05, 0.05))
            size = screen.to_absolute((0.9, 0.65))

            r = Rect(position[0],position[1],size[0],size[1])
            pygame.draw.rect(displaysurface, self.colors["frame"], r)

            s = "Lorem ipsum dolor sit amet intersectum loris delere tapis"
            
            remaining = drawText(displaysurface, s, self.colors["text"], r, self.fonts["default"], True)
            if (remaining):
                print(remaining)

            pygame.display.update()
            FramePerSec.tick(FPS)

        pygame.quit()
        sys.exit()


# draw some text into an area of a surface
# automatically wraps words
# returns any text that didn't get blitted
def drawText(surface, text, color, rect, font, aa=False, bkg=None):
    rect = Rect(rect)
    y = rect.top
    lineSpacing = -2

    # get the height of the font
    fontHeight = font.size("Tg")[1]

    while text:
        i = 1

        # determine if the row of text will be outside our area
        if y + fontHeight > rect.bottom:
            break

        # determine maximum width of line
        while font.size(text[:i])[0] < rect.width and i < len(text):
            i += 1

        # if we've wrapped the text, then adjust the wrap to the last word      
        if i < len(text): 
            i = text.rfind(" ", 0, i) + 1

        # render the line and blit it to the surface
        if bkg:
            image = font.render(text[:i], 1, color, bkg)
            image.set_colorkey(bkg)
        else:
            image = font.render(text[:i], aa, color)

        surface.blit(image, (rect.left, y))
        y += fontHeight + lineSpacing

        # remove the text we just blitted
        text = text[i:]

    return text