import pandas as pd
import matplotlib.pyplot as plt
import os

class Plotter:
    def draw_scatterplot(self, df, x_col, y_col):
        plt.figure(figsize=(10, 6))
        plt.scatter(df[x_col], df[y_col])
        plt.xlabel(x_col)
        plt.ylabel(y_col)
        plt.title(f'{x_col} vs. {y_col}')
        
        plot_path = f'plots/{x_col}_vs_{y_col}_scatterplot.png'
        self._save_plot(plot_path)
        
        return plot_path
    
    def draw_lineplot(self, df, x_col, y_col):
        plt.figure(figsize=(10, 6))
        plt.plot(df[x_col], df[y_col])
        plt.xlabel(x_col)
        plt.ylabel(y_col)
        plt.title(f'{x_col} vs. {y_col}')
        
        plot_path = f'plots/{x_col}_vs_{y_col}_lineplot.png'
        self._save_plot(plot_path)
        
        return plot_path
    
    def draw_barplot(self, df, x_col, y_col):
        plt.figure(figsize=(10, 6))
        plt.bar(df[x_col], df[y_col])
        plt.xlabel(x_col)
        plt.ylabel(y_col)
        plt.title(f'{x_col} vs. {y_col}')
        
        plot_path = f'plots/{x_col}_vs_{y_col}_barplot.png'
        self._save_plot(plot_path)
        
        return plot_path
    
    def _save_plot(self, plot_path):
        if not os.path.exists('plots'):
            os.makedirs('plots')
        plt.savefig(plot_path)
        plt.close()


data = pd.read_json('https://ai-process-sandy.s3.eu-west-1.amazonaws.com/purge/deviation.json')


plotter = Plotter()


columns = data.columns.tolist()
for x_col in columns:
    for y_col in columns:
        if x_col != y_col:
            scatterplot_path = plotter.draw_scatterplot(data, x_col, y_col)
            lineplot_path = plotter.draw_lineplot(data, x_col, y_col)
            barplot_path = plotter.draw_barplot(data, x_col, y_col)
            
            print(f"Plots for {x_col} vs. {y_col}:")
            print("Scatterplot:", scatterplot_path)
            print("Lineplot:", lineplot_path)
            print("Barplot:", barplot_path)
            print("="*40)
