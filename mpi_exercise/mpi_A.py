y_values = [4, 6, 6, 4, 4, 5] 
x_values = [0, 2 ,4 , 6, 8, 10]

subintervals = 5

def auc(x_values=x_values, y_values=y_values, subintervals=subintervals):
    '''
    Calculates area under curve using trapezoidal rule.
    Parameters : x values, y values and no. of subintervals
    Returns area under the curve.
    '''
    width = (max(x_values) - min(x_values)) / subintervals
    total = 0

    for i, y in enumerate(y_values):
        if (i == 0) or (i == len(y_values)-1):
            total += y
        else:
            total += (2 * y)
    
    return (width / 2) * total 

print("Area under curve is {}".format(auc()))



