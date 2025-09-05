import math
class Triangle:

    def classify_Triangle(a,b,c):
        out = ""
        if (
            math.isclose(a*a + b*b, c*c) or 
            math.isclose(a*a + c*c, b*b) or 
            math.isclose(b*b + c*c, a*a)
            ):
            out+="right"
        else:
            out+="not right"
        if(a == b and a == c):
            out +=" Equilateral"
            return out
        elif(a == b or a == c or b == c):
            out +=" Isosceles"
            return out
        else:
            out+=" Scalene"
            return out
