import math

class load_depth_relation:
    def __init__(self, h_0, h_1, h_f, P_0, P_1):
        self.h_0 = h_0
        self.h_1 = h_1
        self.h_f = h_f
        self.P_0 = P_0
        self.P_1 = P_1


    '''
    P_0 = alpha(diff_0)^m
    P_1 = alpha(diff_1)^m

    P_0/P_1 = (diff_0/diff_1)^m
    m = log(P_0/P_1)/log(diff_0/diff_1)
    '''
    def solve_m(self):
        diff_0 = abs(self.h_f - self.h_0)
        diff_1 = abs(self.h_f - self.h_1)

        a = math.log(self.P_0/self.P_1)
        b = math.log(diff_0/diff_1)
        self.m = a/b

        return self.m
    
    '''
        P_0 = alpha(diff_0)^m
        alpha = P_0/(diff_0)^m
    '''
    def solve_alpha0(self):
        if (self.m == None): return None
        else:
            diff_0 = abs(self.h_f - self.h_0)
            self.alpha = self.P_0/math.pow(diff_0, self.m)

            return self.alpha
        
    '''
        P_1 = alpha(diff_1)^m
        alpha = P_1/(diff_1)^m
    '''
    def solve_alpha1(self):
        if (self.m == None): return None
        else:
            diff_1 = abs(self.h_f - self.h_1)
            self.alpha = self.P_1/math.pow(diff_1, self.m)

            return self.alpha
