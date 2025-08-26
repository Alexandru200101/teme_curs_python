# Vectori ( __add__ și __sub__ )
# Creează o clasă Vector2D cu coordonatele x și y.
# Suprascrie __add__ pentru a aduna doi vectori.
# Suprascrie __sub__ pentru a scădea doi vectori.
# Testează cu câțiva vectori.
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        
        return Vector(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"Vector({self.x}, {self.y})"
if __name__=="__main__":
    v1 = Vector(2, 3)
    v2 = Vector(4, 1)

    v3 = v1 + v2   
    print(v3) 