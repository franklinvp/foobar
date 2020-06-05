def number_of_reflections(dimensions, your_position, guard_position, distance):
    """
    dimensions = [width, height] = [int, int]
    your_position = [x1, y1] = [int, int]
    guard_position = [x2, y2] = [int, int]
    distance = int

    For a rectangular room of size dimension, this function returns
    the number of directions in which one can shoot a LASER from your_position
    and hit guard_position, without hitting yourself and not after the length
    of the path of the LASER is larger than distance.
    The LASER reflects off the walls following Snell's law and it bounces 
    off corners by returning back in exactly the same direction.

    The dimensions are in the interval [2,1250].
    The coordinates in the interval [1,dimension[correponding]]
    The distance is in the interval [2,10000]
    Your position and that of the guard are different.
    """
    from fractions import gcd
        
    def is_reflection(target):
        """
        Determines if the position of target, input as a vector based at 
        your_position, is a reflection of either your position, or of the 
        guard's position, with respect to the walls of the room.
        """
        actual_point = [target[0] + your_position[0], target[1] + your_position[1]]
        remainder = [actual_point[0]%dimensions[0], actual_point[1]%dimensions[1]]
        if (actual_point[0]//dimensions[0])%2 == 1:
            remainder[0] = dimensions[0]-remainder[0]
        if (actual_point[1]//dimensions[1])%2 == 1:
            remainder[1] = dimensions[1]-remainder[1]
        if (remainder[0] == your_position[0]) and (remainder[1] == your_position[1]) \
            or (remainder[0] == guard_position[0] and remainder[1] == guard_position[1]):
            return True
        return False

    def clear_of_suicide_or_double_kill(target_rel_to_me):
        """
        Determines if shooting at target_rel_to_me, entered as a vector based at
        your_position, would cause to shoot yourself or to shoot another reflected
        position of the guard, before reaching target_rel_to_me.
        """
        common_factor = abs(gcd(target_rel_to_me[0],target_rel_to_me[1]))
        direction = [target_rel_to_me[0]//common_factor, target_rel_to_me[1]//common_factor]
        for scale in xrange(1, common_factor):
            if is_reflection([scale*direction[0],scale*direction[1]]):
                return False
        return True
    # Now the actual counting.
    count = 0
    # Pythom works seamlessly with int of any size.
    # Let's work with norms squared and there will be no problems
    # with precision.
    distance2 = distance*distance
    guard_rel_coor = [guard_position[0]-your_position[0],
                      guard_position[1]-your_position[1]]
    odd_horizontal_shift = dimensions[0]-2*guard_position[0]
    odd_vertical_shift = dimensions[1]-2*guard_position[1]
    his_point_rel_to_me = [0,0]
    # Number of reflections in each direction.
    # There are more than those inside the disc
    # of radius distance, but not many extra ones.
    horizontal_reflections = (distance // dimensions[0]) + 1
    vertical_reflections = (distance // dimensions[1]) + 1
    # For each room reflection check shooting the reflected guard
    for i in xrange(-horizontal_reflections, horizontal_reflections+1):
        # Computing the X-coordinate of a guard reflected i times horizontally.
        # The sign of i determines the direction; + for right, - for left.
        his_point_rel_to_me[0] = guard_rel_coor[0] + i*dimensions[0]
        if i%2==1:
            his_point_rel_to_me[0] += odd_horizontal_shift
        for j in xrange(-vertical_reflections, vertical_reflections+1):
            # Computing the Y-coordinate of a guard reflected j times vertically.
            # The sign of j determines the direction; + for up, - for down.
            his_point_rel_to_me[1] = guard_rel_coor[1] + j*dimensions[1]
            if j%2==1:
                his_point_rel_to_me[1] += odd_vertical_shift
            # Checking if it is OK to shoot in that direction.
            # If it is, count it.
            if his_point_rel_to_me[0]**2 + his_point_rel_to_me[1]**2 <= distance2  and \
               clear_of_suicide_or_double_kill(his_point_rel_to_me):
                count+=1
    return count
