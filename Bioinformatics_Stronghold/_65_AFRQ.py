from util import get_data

data = get_data(__file__)
# data = '''0.1 0.25 0.5
# '''
numbers = list(map(float, data.split()))

for Pr in numbers:
    # factor1 = affected * affected * 1
    # factor2 = affected * carrier * 1/2
    # factor3 = carrier * affected * 1/2
    # factor4 = carrier * carrier * 1/4

    # get the proportion of the carriers (carriers include affected)
    # 1/4*x**2 + Pr*x + Pr*Pr = Pr
    # 1/4*x**2 + P(r)*x + P(r)*P(r)-P(r) = 0

    # x = (-b +- sqrt(b**2 - 4ac)) / 2a
    a = 1/4
    b = Pr 
    c = Pr*Pr - Pr
    x = (-b + (b**2 - 4*a*c)**0.5) / (2*a)

    print(round(x + Pr, 3), end=' ' if Pr != numbers[-1] else '\n')
