"""Module for classifying triangles."""
import math
class Triangle:
    """A class for classifying triangles by their side lengths."""
    @staticmethod
    def classify_triangle(a,b,c):
        """Classify a triangle given three side lengths."""
        out = ""
        if (
            math.isclose(a * a + b * b, c*c) or
            math.isclose(a * a + c * c, b*b) or
            math.isclose(b * b + c * c, a *a )
            ):
            out += "right"
        else:
            out += "not right"
        if(a == b and a == c):
            out += " Equilateral"
            return out
        if(a == b or a == c or b == c):
            out += " Isosceles"
            return out
        out += " Scalene"
        return out
