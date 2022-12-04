# Writing a well-documented code create a function that calculates simple interest


def SimpleInterest(P, T, R):
    SI = (P * T * R)/100
    return SI

calc_simple_interest = SimpleInterest(1, 3, 5)
print(calc_simple_interest)