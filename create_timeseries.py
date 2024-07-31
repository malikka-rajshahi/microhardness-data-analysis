import pandas as pd
import matplotlib.pyplot as plt

if __name__=='__main__':
    directory = input('Input grit [80, 320, ...]: ')
    directory = f'{directory}grit'
    file = input('Input filename: ')

    df = pd.read_csv(f'./microhardness-data/{directory}/{file}')
    plt.plot(df['Time, ms - Plot 0'], df['Depth,nm - Plot 0'])
    plt.xlabel('Time (ms)')
    plt.ylabel('Depth (nm)')
    plt.title(f'Time Series for {file}')
    plt.savefig(f'./timeseries/{file[:-4]}')