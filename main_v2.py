import pygame
import random
import os

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

# Images
win_image = pygame.image.load('images' + os.sep + 'win_post.png')
win_image_position = win_image.get_rect(center=(int(W / 2), int(H / 2)))
lose_image = pygame.image.load('images' + os.sep + 'lose.png')
lose_image_position = lose_image.get_rect(center=(int(W / 2), int(H / 2)))
dead_head_image = pygame.image.load('images' + os.sep + 'dead_head.png')
dead_head_image_position = dead_head_image.get_rect(center=(int(W / 2), int(H / 2)))
cross_image = pygame.image.load('images' + os.sep + 'cross.png')
zero_image = pygame.image.load('images' + os.sep + 'zero.png')


class Cross:

    def __init__(self, cen_pos_x, cen_pos_y):
        self.cen_pos_x = cen_pos_x
        self.cen_pos_y = cen_pos_y

    def draw_it(self):
        image_pos = cross_image.get_rect(center=(self.cen_pos_x, self.cen_pos_y))
        screen.blit(cross_image, image_pos)


class Zero:

    def __init__(self, cen_pos_x, cen_pos_y):
        self.cen_pos_x = cen_pos_x
        self.cen_pos_y = cen_pos_y

    def draw_it(self):
        image_pos = zero_image.get_rect(center=(self.cen_pos_x, self.cen_pos_y))
        screen.blit(zero_image, image_pos)


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
    # Check users win, if 2 areas = True
    def check_areas(ar_1, ar_2, ar_3):
        if draw_dict[ar_1] and draw_dict[ar_2] and draw_dict_II[ar_3] == False:
            return True
        elif draw_dict[ar_2] and draw_dict[ar_3] and draw_dict_II[ar_1] == False:
            return True
        elif draw_dict[ar_1] and draw_dict[ar_3] and draw_dict_II[ar_2] == False:
            return True
        else:
            return False

    def draw_in_free(ar_1, ar_2, ar_3):
        if draw_dict[ar_1] == False:
            draw_dict_II[ar_1] = True
        elif draw_dict[ar_2] == False:
            draw_dict_II[ar_2] = True
        elif draw_dict[ar_3] == False:
            draw_dict_II[ar_3] = True
        else:
            pass

    line_1 = check_areas('key1', 'key2', 'key3')
    line_2 = check_areas('key4', 'key5', 'key6')
    line_3 = check_areas('key7', 'key8', 'key9')

    column_1 = check_areas('key1', 'key4', 'key7')
    column_2 = check_areas('key2', 'key5', 'key8')
    column_3 = check_areas('key3', 'key6', 'key9')

    diagonal_1 = check_areas('key3', 'key5', 'key7')
    diagonal_2 = check_areas('key1', 'key5', 'key9')

    to_do = 0
    for key in draw_dict_II:
        if draw_dict_II[key] == False:
            to_do += 1

    while to_do != 0:
        if line_1:
            draw_in_free('key1', 'key2', 'key3')
            break
        elif line_2:
            draw_in_free('key4', 'key5', 'key6')
            break
        elif line_3:
            draw_in_free('key7', 'key8', 'key9')
            break
        elif column_1:
            draw_in_free('key1', 'key4', 'key7')
            break
        elif column_2:
            draw_in_free('key2', 'key5', 'key8')
            break
        elif column_3:
            draw_in_free('key3', 'key6', 'key9')
            break
        elif diagonal_1:
            draw_in_free('key3', 'key5', 'key7')
            break
        elif diagonal_2:
            draw_in_free('key1', 'key5', 'key9')
            break
        else:
            random_key_ind = str(random.randint(1, 9))
            random_key = draw_dict_II['key' + random_key_ind]
            if random_key == False:  # Don't touch it, because not None == True
                draw_dict_II['key' + random_key_ind] = True
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


# Nobody winner check
def dead_heat_check():
    free_area = 9
    for key in draw_dict_II:
        if draw_dict_II[key] != False:
            free_area -= 1

    if not win_check(draw_dict) and not win_check(draw_dict_II) and free_area == 0:
        return True
    else:
        return False


# Script to restart
def restart_game():
    for key in draw_dict:
        draw_dict[key] = False

    for key in draw_dict_II:
        draw_dict_II[key] = False


def event_type(e):
    global done
    if e.type == pygame.QUIT:
        done = True
    elif e.type == pygame.KEYDOWN:
        if e.key == pygame.K_ESCAPE:
            done = True
        elif e.key == pygame.K_r and (win_check(draw_dict) or win_check(draw_dict_II) or dead_heat_check()):
            restart_game()
    elif e.type == pygame.MOUSEBUTTONUP and not win_check(draw_dict) and not win_check(draw_dict_II):
        draw_figure(draw_coordinate(event.pos))
        comparison_dict()
        draw_ii()


while not done:

    # This limits the wile loop to a max of 30 times per second
    # Leave this out, and we will use all CPU we can
    pygame.time.Clock().tick(FPS)

    for event in pygame.event.get():  # User did something
        event_type(event)

    screen.fill(WHITE)
    playing_field()

    for key in draw_dict:
        if draw_dict[key]:
            Cross(area_cen_cord[key][0], area_cen_cord[key][1]).draw_it()

    for key in draw_dict_II:
        if draw_dict_II[key]:
            Zero(area_cen_cord[key][0], area_cen_cord[key][1]).draw_it()

    if win_check(draw_dict):
        screen.blit(win_image, win_image_position)
    elif win_check(draw_dict_II):
        screen.blit(lose_image, lose_image_position)

    if dead_heat_check() and not win_check(draw_dict) and not win_check(draw_dict_II):
        screen.blit(dead_head_image, dead_head_image_position)

    pygame.display.flip()

# Картинка ничьи, оформить внутренний блок нормально сделать ИИ алгоритм совершенным
