import math
angle = float(input())
angle = math.radians(angle)
cos = math.cos(angle)
sin = math.sin(angle)
contangent = cos / sin
print(round(contangent, 10))
