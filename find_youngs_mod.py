import math
import pandas as pd

def main():
    df = pd.read_csv('output.csv')
    Er = df['Reduced Elastic Modulus']
    v = (0.275-0.265)/2
    Ei = 1210*1e9
    v_i = 1.2011

    '''
    1/Er = (1-v^2)/E + (1-v_i^2)/E_i
    E = (1-v^2)/[1/Er - (1-v_i^2)/E_i]
    '''
    a = 1 - math.pow(v, 2)
    b = (1 - math.pow(v_i, 2)) / Ei
    E = a / ((1/Er) - b)

    df['Young\'s Modulus'] = E
    df.to_csv('output.csv', index=False)

if __name__=='__main__':
    main()