"""
Exercise 5.4-1
English: 
(1) How many people must be in a room so that the probability someone shares your birthday 
    is at least 1/2?
(2) How many people must be in a room so that the probability at least two people 
    share May 3rd as their birthday is greater than 1/2?

Polish:
(1) Ile osób musi być w pokoju, aby prawdopodobieństwo, że ktoś ma urodziny tego samego dnia co Ty,
    było ≥ 1/2?
(2) Ile osób musi być w pokoju, aby prawdopodobieństwo, że przynajmniej dwie osoby mają urodziny 
    3 maja, było > 1/2?
"""

# Polish description:
# (1) Prawdopodobieństwo, że n osób NIE ma urodzin tego samego dnia co Ty = (364/365)^n.
#     Szukamy najmniejszego n, dla którego 1 - (364/365)^n ≥ 1/2.
# (2) Liczymy prawdopodobieństwo, że 0 lub 1 osoba ma urodziny 3 maja.
#     P(X=0) = (364/365)^n, P(X=1) = n*(1/365)*(364/365)^(n-1).
#     Szukamy najmniejszego n, dla którego 1 - (P0+P1) > 1/2.

import math

def min_people_same_birthday_as_you():
    n = 1
    while True:
        p = 1 - (364/365)**n
        if p >= 0.5:
            return n
        n += 1

def min_people_two_on_may3():
    n = 2
    while True:
        p0 = (364/365)**n
        p1 = n * (1/365) * (364/365)**(n-1)
        if 1 - (p0 + p1) > 0.5:
            return n
        n += 1

if __name__ == "__main__":
    print("Exercise 5.4-1 Results:")
    print("Minimum people for ≥1/2 chance someone shares your birthday:", min_people_same_birthday_as_you())
    print("Minimum people for >1/2 chance at least two share May 3rd:", min_people_two_on_may3())
