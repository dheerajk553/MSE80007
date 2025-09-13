class Circle:
    def draw(self):
        return "Drawing a Circle"
class Square:
    def draw(self):
        return "Drawing a Square"
            
class ShapeFactory:
    def create_shape(self, shape_type):
        if shape_type == "circle":
            return Circle()
        if shape_type == "square":
            return Square()
       
        else:
            return None
factory = ShapeFactory()
shape = factory.create_shape("Triangle")   
if shape:
    print(shape.draw())
else:
    print("Invalid shape type")