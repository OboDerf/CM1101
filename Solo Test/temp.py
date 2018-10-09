import string
from map import rooms


def exit_leads_to(exits, direction):
    return rooms[exits[direction]]["name"]

def print_menu_line(direction, leads_to):
    print("Go " + direction.upper() + " to " + leads_to)

def print_menu(exits):
    print("You can:")
    for a in exits:

        print_menu_line(a, exit_leads_to(exits, a))
    
def is_valid_exit(exits, user_input):
    return user_input in exits

def move(exits, direction):

    """
    >>> move(rooms["Reception"]["exits"], "south") == rooms["Admins"]
    True
    >>> move(rooms["Reception"]["exits"], "east") == rooms["Tutor"]
    True
    >>> move(rooms["Reception"]["exits"], "west") == rooms["Office"]
    False
    """
    
    return rooms[exits[direction]]


