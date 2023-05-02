import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math
import glob
import os


csv_files = glob.glob('./selected_indicators/*_ind.csv')

main_folder = 'generated_plots'
os.makedirs(main_folder, exist_ok=True)

for file in csv_files:
    df = pd.read_csv(file)
    df_new = (
        df.drop(['code', 'iso'], axis=1)
        .set_index(['country']).rename_axis([None])
        .T.reset_index()  # Transpose teh original dataset
        .assign(index=lambda x: x['index'].str[-4:])
        .set_index('index')
        .rename_axis(None)
        .replace(-8888, np.nan)
    )

    df_long = (df_new.reset_index()
               .melt(id_vars='index', var_name='country', value_name='value')
               .astype({'index': 'float64'}))

    folder_name = os.path.splitext(os.path.basename(file))[0]
    sub_folder = os.path.join(main_folder, folder_name)
    os.makedirs(sub_folder, exist_ok=True)

    rows = 4
    cols = 4
    num_plots = rows * cols
    num_pages = math.ceil(len(df_long['country'].unique()) / num_plots)

    for page in range(num_pages):
        fig, axes = plt.subplots(rows, cols, figsize=(
            15, 15), sharex=True, sharey=True)
        axes = axes.flatten()

        for idx, (country, data) in enumerate(df_long.groupby("country")):
            if page * num_plots <= idx < (page + 1) * num_plots:
                ax = axes[idx % num_plots]
                ax.scatter(data["index"], data["value"],
                           marker="o", label=country)
                ax.set_title(country)
                ax.set_xlabel("Year")
                ax.set_ylabel("Score")

        for i in range(idx % num_plots + 1, num_plots):
            fig.delaxes(axes[i])

        fig.tight_layout()

        plt.savefig(f"{sub_folder}/{page + 1}.png")
