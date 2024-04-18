from geometric_shapes.line import Line
from geometric_shapes.point import Point
from math import acos
from math import degrees

class Shape:
    def __init__(self, vertices):
        self.vertices = vertices
        self.edges = [Line(vertices[i], vertices[(i + 1) % len(vertices)]) for i in range(len(vertices))]
        self.inner_angles = self.compute_inner_angles()
        self.regular = self.compute_regular()
    def compute_regular(self):
        regular = False
        v1=0
        v2=0
        for edge in self.edges:
            v2 = edge.start_point.compute_distance(edge.end_point)
            if v1 != 0:
                if v1 == v2:
                    regular=True
                    v1 = v2
                else:
                    regular= False
            else:
                v1 = v2
        return regular


    def compute_inner_angles(self):
        # Calcular los ángulos internos de la forma
        angles = []
        for i in range(len(self.vertices)):
            prev_point = self.vertices[i - 1]
            current_point = self.vertices[i]
            next_point = self.vertices[(i + 1) % len(self.vertices)]

            # Calcular los vectores entre los puntos
            v1 = Point(prev_point.x - current_point.x, prev_point.y - current_point.y)
            v2 = Point(next_point.x - current_point.x, next_point.y - current_point.y)

            # Calcular el ángulo entre los vectores utilizando el producto escalar
            dot_product = v1.x * v2.x + v1.y * v2.y
            magnitude_v1 = (v1.x**2 + v1.y**2)**0.5
            magnitude_v2 = (v2.x**2 + v2.y**2)**0.5
            angle_rad = acos(dot_product / (magnitude_v1 * magnitude_v2))
            angle_deg = degrees(angle_rad)

            angles.append(angle_deg)

        return angles

    def compute_area(self, shape_edges):
        if len(self.vertices) == 3:
            H=[]
            for i in self.vertices:
                H.append(i.y)
            H.sort(reverse=True)
            Height=H[0]
            for edge in shape_edges:
                Base = edge.start_point.compute_distance(edge.end_point)
                break
            print(f"El area es : {(Height * Base)/2}")
        elif len(self.vertices) == 4:
            E=[]
            for edge in shape_edges:
                E.append(edge.start_point.compute_distance(edge.end_point))
            Base=E[0]
            Height=E[1]
            print(f"El area es: {Base*Height}")
     
    def compute_perimeter(self, shape_edges):
        perimeter = 0
        for edge in shape_edges:
            perimeter += edge.start_point.compute_distance(edge.end_point)

        print(f"El perimetro es : {perimeter:.2f}" )
        

# Clase Triangle para representar un triángulo
class Triangle(Shape):
    def __init__(self, vertices):
        super().__init__(vertices)

# Clases específicas de triángulos
class Isosceles(Triangle):
    pass

class Equilateral(Triangle):
    def __init__(self):
        if self.regular == True:
            print("Es Equilatero")
        else:
            pass

class Scalene(Triangle):
    pass

class TriRectangle(Triangle):
    pass


# Clase Rectangle para representar un rectángulo
class Rectangle(Shape):
    def __init__(self, vertices):
        super().__init__(vertices)

# Clase Square para representar un cuadrado
class Square(Rectangle):
    pass
