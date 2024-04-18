import geometric_shapes.point as point
import geometric_shapes.shape as Tri
import geometric_shapes.shape as Squa


# Ejemplo de uso
if __name__ == "__main__":
    # Crear un triángulo con vértices A(0, 0), B(3, 0) y C(1, 2)
    triangle_vertices = [point.Point(0, 0), point.Point(4, 0), point.Point(2, 2)]
    triangle = Tri.Shape(triangle_vertices)

    print("Ángulos internos del triángulo:", triangle.inner_angles)
    print("Longitudes de los lados del triángulo:")
    for edge in triangle.edges:
        print(f"{edge.start_point.compute_distance(edge.end_point):.2f}")

    triangle.compute_perimeter(triangle.edges)
    triangle.compute_area(triangle.edges)
    
    
    print("Es regular?", triangle.regular)

    # Crear un cuadrado con vértices D(0, 0), E(2, 0), F(2, 4) y G(0, 4)
    square_vertices = [point.Point(0, 0), point.Point(4, 0), point.Point(4, 4), point.Point(0, 4)]
    square = Squa.Shape(square_vertices)

    print("Ángulos internos del cuadrado:", square.inner_angles)
    print("Longitudes de los lados del cuadrado:")
    for edge in square.edges:
        print(f"{edge.start_point.compute_distance(edge.end_point):.2f}")
    square.compute_perimeter(square.edges)
    square.compute_area(square.edges)

    print("Es regular?", square.regular)