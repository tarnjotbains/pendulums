import math

class Pendulum: 
    def __init__(self):


        # Angles and length of the rods 
        self.angle1 = math.pi / 2
        self.angle2 = math.pi / 2
        self.l1 = 200
        self.l2 = 200

        # velocity and acceleration
        self.v1 = 0
        self.v2 = 0 
        self.a1 = 0
        self.a2 = 0

        self.x1 = 0
        self.y1 = 0 
        self.x2 = 0
        self.y2 = 0 

        # mass of the points 
        self.m1 = 40
        self.m2 = 40

        # Gravity
        self.g = 0.981 

    
    def calculate_position(self): 
        self.x1 = self.l1 * math.sin(self.angle1) 
        self.y1 = -self.l1 * math.cos(self.angle1) 

        self.x2 = self.x1 + self.l2 * math.sin(self.angle2) 
        self.y2 = self.y1 - self.l2 * math.cos(self.angle2)
    
    def update(self): 
        self.calculate_acceleration() 
        self.v1 += self.a1
        self.v2 += self.a2 

        self.angle1 += self.v1
        self.angle2 += self.v2  

        self.calculate_position() 

    
    def calculate_acceleration(self):

        # Angular velocity of upper angle: 
        num1 = - self.g * (2 *self.m1 + self.m2) * math.sin(self.angle1) 
        num2 = self.m2 * self.g * math.sin(self.angle1 - 2 * self.angle2) 
        num3 = 2 * math.sin(self.angle1 - self.angle2) * self.m2 
        num4 = ((self.v2)**2) * self.l2 + ((self.v1)**2) * self.l1 * math.cos(self.angle1 - self.angle2) 

        numerator = num1 - num2 - num3*num4 

        denom = self.l1 *(2 * self.m1 + self.m2 - self.m2 * math.cos(2 * self.angle1 - 2 * self.angle2))

        self.a1 = numerator / denom 

        # angular velocity of lower angle 
        num1 = 2 * math.sin(self.angle1 - self.angle2) 

        num2 = ((self.v1)**2) * self.l1 * (self.m1 + self.m2) 
        num3 = self.g * (self.m1 + self.m2) * math.cos(self.angle1) 

        num4 = ((self.v2)**2) * self.l2 * self.m2 * math.cos(self.angle1 - self.angle2) 

        numerator = num1 * (num2 + num3 + num4) 

        denom = self.l2 * (2 * self.m1 + self.m2 - self.m2 * math.cos(2 * self.angle1 - 2 * self.angle2))

        self.a2 = numerator / denom


