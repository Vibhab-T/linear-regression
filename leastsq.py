import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


#y = b0 + b1x
#y = mx + c

#b1 = m = gradient
#b0 = c = y-intercept


'''
m or b1 = (nExy - ExEy)/(nEx2 - (Ex)2)
b0 or c or b = (Ey - mEx)/n

'''
class LeastSquares:

    def __init__(self, x: list, y: list):
        self.x = x
        self.y = y
        self.sum_x = 0
        self.sum_xy = 0 
        self.sum_x2 = 0
        self.sum_y = 0 
        self.n = len(x)
        self.xy = x.copy()
        self.x2 = x.copy()

        for i in range(self.n):
            self.xy[i] = x[i] * y[i]
            self.x2[i] = x[i] * x[i]

            self.sum_x += x[i]
            self.sum_y += y[i]
            self.sum_xy += self.xy[i]
            self.sum_x2 += self.x2[i]
    
    def calc_intercept_slope(self):
        
        m = ((self.n * self.sum_xy)-((self.sum_x)*(self.sum_y)))/((self.n * self.sum_x2) - (self.sum_x * self.sum_x))

        c = (self.sum_y - (m*self.sum_x))/self.n

        return {
            "gradient": m,
            "intercept": c
        }


def main():
    x = [1,2,3,4,5,6,7]
    y = [1.5, 3.8, 6.7, 9.0, 11.2, 13.6, 16]

    least_squares = LeastSquares(x, y)
    
    best_fit_line = least_squares.calc_intercept_slope()
    
    print(best_fit_line)

main()