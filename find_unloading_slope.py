import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def main(grit):
    tests = [_ for _ in range(25)]
    df = pd.read_csv(f'./microhardness-data/{grit}grit/{grit}grit_results.csv')
    # df = df.set_index('Test No', drop=True)
    df.columns = ['Test', 'Load', 'Displacement']
    output = pd.read_csv('output.csv')

    for i in tests:
        # start = 20100+i*30000
        # end = start+400
        # df_isolate = df.iloc[start:end]

        df_isolate = df[df.Test==i+1]
        df_isolate = df_isolate.reset_index(drop=True)
        max_load = np.max(df_isolate['Load'])
        print(max_load)
        start = df_isolate[df_isolate.Load==max_load]
        df_isolate = df_isolate[start.index[0]::]
        df_isolate = df_isolate[(df_isolate.Load < 999)&(df_isolate.Load > 800)]
        
        plt.clf()
        plt.plot(df_isolate.Displacement, df_isolate.Load)

        slope, intercept = np.polyfit(df_isolate.Displacement, df_isolate.Load, 1)
        print(intercept)
        output.loc[(output.Grit==grit)&(output.No==i+1), 'Slope'] = slope
        line = slope * df_isolate.Displacement + intercept

        plt.scatter(df_isolate.Displacement, df_isolate.Load, s=1)
        plt.plot(df_isolate.Displacement, line, color='red', label='Line of best fit')
        plt.title(f'Slope: {slope}')
        plt.xlabel('Displacement')
        plt.ylabel('Load')
        plt.savefig(f'./figures/unloading_slope_{grit}_test{i}');
        
        print(f'Completed Test #{i}')    
    
    output.to_csv('output.csv', index=False)
    
if __name__=='__main__':
    # main(600)
    main(1200)