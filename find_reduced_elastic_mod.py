import math
import pandas as pd

def main():
    a = math.sqrt(math.pi)/2
    df = pd.read_csv('output.csv')
    Ap = df['Ap (um^2)']*1e-12
    S = df['Slope']*1e6

    b = Ap.apply(math.sqrt)
    E = a * (S/b)
    df['Reduced Elastic Modulus'] = E
    df.to_csv('output.csv', index=False)
    

if __name__=='__main__':
    main()