"""Create a class for a geometric figure called “Rhombus”. The class must have the following attributes:
side_a (the length of side a).
angle_a (the angle between sides a and b).
angle_b (the angle adjacent to angle_a).
The following requirements must be implemented:
1. The value of side_a must be greater than 0.
2. The angles angle_a and angle_b must satisfy the condition:
   angle_a + angle_b = 180.
3. Opposite angles of a rhombus are always equal, therefore when a value for angle_a is given,
   the value of angle_b must be calculated automatically.
4. Use the __setattr__ method to set the values of the attributes."""

class Rhombus:
    def __init__(self, side_a, angle_a):
        if side_a > 0:
            self.side_a = side_a
        else: print(ValueError("Side of Rhombus can not be negative"))
        if  0 < angle_a < 180:
            self.angle_a = angle_a
            self.angle_b = 180 - angle_a
        else: print(ValueError("Angle of Rhombus can not be negative"))


my_rhombus = Rhombus(40,79)
print(my_rhombus.angle_b)




