import pygame

# Initialize the game engine
pygame.init()
# Define the colors we will use in RGB format
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Set the height and width of the screen
H = 1000
W = 1000
size = [H, W]
area_cen_cord = {'key1': (int(W / 6), int(H / 6)),
                 'key2': (int(W / 2), int(H / 6)),
                 'key3': (int(W / 6 * 5), int(H / 6)),
                 'key4': (int(W / 6), int(H / 2)),
                 'key5': (int(W / 2), int(H / 2)),
                 'key6': (int(W / 6 * 5), int(H / 2)),
                 'key7': (int(W / 6), int(H / 6 * 5)),
                 'key8': (int(W / 2), int(H / 6 * 5)),
                 'key9': (int(W / 6 * 5), int(H / 6 * 5))
                 }

draw_dict = {'key1': False,
             'key2': False,
             'key3': False,
             'key4': False,
             'key5': False,
             'key6': False,
             'key7': False,
             'key8': False,
             'key9': False
             }

# Creating screen with a given size
screen = pygame.display.set_mode(size)

# Set the caption display
pygame.display.set_caption("Tic-tac-toe")
done = False
FPS = 30


class Cross:

    def __init__(self, cen_pos_x, cen_pos_y):
        self.cen_pos_x = cen_pos_x
        self.cen_pos_y = cen_pos_y

    def draw_it(self):
        pygame.draw.line(screen, BLACK, (int(self.cen_pos_x - 83.5), int(self.cen_pos_y - 83.5)),
                         (int(self.cen_pos_x + 83.5), int(self.cen_pos_y + 83.5)))
        pygame.draw.line(screen, BLACK, (int(self.cen_pos_x - 83.5), int(self.cen_pos_y + 83.5)),
                        (int(self.cen_pos_x + 83.5), int(self.cen_pos_y - 83.5)))  # FixIT HARDCODE


class Zero:

    def __init__(self, cen_pos_x, cen_pos_y):
        self.cen_pos_x = cen_pos_x
        self.cen_pos_y = cen_pos_y

    def draw_it(self):
        pygame.draw.circle(screen, BLACK, (self.cen_pos_x, self.cen_pos_y), 80, 1)


def playing_field():
    pygame.draw.line(screen, BLACK, (int(W / 3), 0), (int(W / 3), H))
    pygame.draw.line(screen, BLACK, (int(W / 3 + W / 3), 0), (int(W / 3 + W / 3), H))
    pygame.draw.line(screen, BLACK, (0, int(H / 3)), (W, int(H / 3)))
    pygame.draw.line(screen, BLACK, (0, int(H / 3 + H / 3)), (W, int(H / 3 + H / 3)))


# Give mose coordinate, return center coordinates where mose
def draw_coordinate(pos: tuple):
    if pos[0] < W/3:
        if pos[1] < H/3:
            return area_cen_cord['key1']
        elif H/3 < pos[1] < H/1.5:
            return area_cen_cord['key4']
        elif H/1.5 < pos[1] < H:
            return area_cen_cord['key7']
    elif W/3 < pos[0] < W/1.5:
        if pos[1] < H/3:
            return area_cen_cord['key2']
        elif H/3 < pos[1] < H/1.5:
            return area_cen_cord['key5']
        elif H/1.5 < pos[1] < H:
            return area_cen_cord['key8']
    elif W/1.5 < pos[0] < W:
        if pos[1] < H/3:
            return area_cen_cord['key3']
        elif H/3 < pos[1] < H/1.5:
            return area_cen_cord['key6']
        elif H/1.5 < pos[1] < H:
            return area_cen_cord['key9']


# Give processed mouse coordinate and writes down area where drawing the figure in draw_dict
def draw_figure(mouse_coordinate):
    area = draw_coordinate(mouse_coordinate)
    for key in area_cen_cord:
        if area_cen_cord[key] == area:
            draw_dict[key] = True




x1 = Cross(166, 166)
z1 = Zero(166, 166)
draw = False
while not done:

    # This limits the wile loop to a max of 30 times per second
    # Leave this out, and we will use all CPU we can
    pygame.time.Clock().tick(FPS)

    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:  # Click ESC fo exit
                done = True
        elif event.type == pygame.MOUSEBUTTONUP:  # event.pos - mouse coordinates
            draw_figure(draw_coordinate(event.pos))
            print(event.pos)
            print(draw_dict)

    screen.fill(WHITE)
    playing_field()
    for key in draw_dict:
        if draw_dict[key]:
            Cross(area_cen_cord[key][0], area_cen_cord[key][1]).draw_it()
    pygame.display.flip()
