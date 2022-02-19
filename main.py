import pygame
import random

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
draw_dict_II = {'key1': False,
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


# Get mose coordinate, return center coordinates where mose area
def draw_coordinate(pos: tuple):
    if pos[0] < W / 3:
        if pos[1] < H / 3:
            return area_cen_cord['key1']
        elif H / 3 < pos[1] < H / 1.5:
            return area_cen_cord['key4']
        elif H / 1.5 < pos[1] < H:
            return area_cen_cord['key7']
    elif W / 3 < pos[0] < W / 1.5:
        if pos[1] < H / 3:
            return area_cen_cord['key2']
        elif H / 3 < pos[1] < H / 1.5:
            return area_cen_cord['key5']
        elif H / 1.5 < pos[1] < H:
            return area_cen_cord['key8']
    elif W / 1.5 < pos[0] < W:
        if pos[1] < H / 3:
            return area_cen_cord['key3']
        elif H / 3 < pos[1] < H / 1.5:
            return area_cen_cord['key6']
        elif H / 1.5 < pos[1] < H:
            return area_cen_cord['key9']


# Get processed mouse coordinate and writes down area where drawing the figure in draw_dict
def draw_figure(mouse_coordinate):
    area = draw_coordinate(mouse_coordinate)
    for key in area_cen_cord:
        if area_cen_cord[key] == area:
            draw_dict[key] = True


# II drawing in random area
def draw_ii():
    # for not to loop
    to_do = 0
    for key in draw_dict_II:
        if draw_dict_II[key] == False:
            to_do += 1

    while True:
        if to_do != 0:
            random_key_ind = str(random.randint(1, 9))
            random_key = draw_dict_II['key' + random_key_ind]
            if random_key == False:  # Don't touch it, because not None == True
                draw_dict_II['key' + random_key_ind] = True
                break
        else:
            break


# Comparison dicts if user draw in key II can't draw in this key
def comparison_dict():
    for key in draw_dict:
        if draw_dict[key] == True:
            draw_dict_II[key] = None


# Victory check
def win_check(d: dict):
    if d['key1'] and d['key2'] and d['key3']:
        return True
    elif d['key4'] and d['key5'] and d['key6']:
        return True
    elif d['key7'] and d['key8'] and d['key9']:
        return True
    elif d['key1'] and d['key4'] and d['key7']:
        return True
    elif d['key2'] and d['key5'] and d['key8']:
        return True
    elif d['key3'] and d['key6'] and d['key9']:
        return True
    elif d['key1'] and d['key5'] and d['key9']:
        return True
    elif d['key7'] and d['key5'] and d['key3']:
        return True
    else:
        return False


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
            comparison_dict()
            draw_ii()
            print('user --->', win_check(draw_dict))
            print('II --->', win_check(draw_dict_II))

    screen.fill(WHITE)
    playing_field()

    for key in draw_dict:
        if draw_dict[key]:
            Cross(area_cen_cord[key][0], area_cen_cord[key][1]).draw_it()

    for key in draw_dict_II:
        if draw_dict_II[key]:
            Zero(area_cen_cord[key][0], area_cen_cord[key][1]).draw_it()

    pygame.display.flip()
