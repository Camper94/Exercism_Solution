"""Functions for implementing the rules of the classic arcade game Pac-Man."""


def eat_ghost(power_pellet_active, touching_ghost):
    """Verify that Pac-Man can eat a ghost if he is empowered by a power pellet.

    :param power_pellet_active: bool - does the player have an active power pellet?
    :param touching_ghost: bool - is the player touching a ghost?
    :return: bool - can the ghost be eaten?
    """
    if power_pellet_active and touching_ghost is True : return True
    if power_pellet_active is False or touching_ghost is False : return False
    


def score(touching_power_pellet, touching_dot):
    """Verify that Pac-Man has scored when a power pellet or dot has been eaten.

    :param touching_power_pellet: bool - is the player touching a power pellet?
    :param touching_dot: bool - is the player touching a dot?
    :return: bool - has the player scored or not?
    """
    if touching_power_pellet or touching_dot is True  :  return True
    if touching_power_pellet or touching_dot is False :  return False



def lose(power_pellet_active, touching_ghost):
    """Trigger the game loop to end (GAME OVER) when Pac-Man touches a ghost without his power pellet.

    :param power_pellet_active: bool - does the player have an active power pellet?
    :param touching_ghost: bool - is the player touching a ghost?
    :return: bool - has the player lost the game?
    """
    if power_pellet_active is False and (power_pellet_active and touching_ghost) is False : return True
    if touching_ghost is False or power_pellet_active is True : return False
    


def win(has_eaten_all_dots, power_pellet_active, touching_ghost):
    """Trigger the victory event when all dots have been eaten.

    :param has_eaten_all_dots: bool - has the player "eaten" all the dots?
    :param power_pellet_active: bool - does the player have an active power pellet?
    :param touching_ghost: bool - is the player touching a ghost?
    :return: bool - has the player won the game?
    """
    if (has_eaten_all_dots and touching_ghost and power_pellet_active is True) : return True
    if has_eaten_all_dots and touching_ghost is True : return False
    if has_eaten_all_dots is False and power_pellet_active and touching_ghost is True : return False
    if has_eaten_all_dots is True : return True
    
