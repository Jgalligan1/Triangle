class Triangle:

    def classify_Triangle(a,b,c):
        out = ""
        if(a*a + b*b == c*c or a*a+c*c == b*b or b*b+c*c == a*a):
            out +="right"
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
