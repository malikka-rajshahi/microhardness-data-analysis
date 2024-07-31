import pandas as pd
import matplotlib.pyplot as plt

if __name__=='__main__':
    directory = input('Input grit [80, 320, ...]: ')
    directory = f'{directory}grit'
    file = input('Input filename: ')

    df = pd.read_csv(f'./microhardness-data/{directory}/{file}')
    plt.plot(df['Depth,nm - Plot 0'], df['Load, mN - Plot 0'])
    plt.xlabel('Load (mN)')
    plt.ylabel('Depth (nm)')
    plt.title(f'Load vs Depth for {file}')
    plt.savefig(f'./load_depth_graphs/{file[:-4]}')