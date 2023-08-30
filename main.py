import pandas as pd
from PIL import Image
from plotter import Plotter

data = pd.read_json('https://ai-process-sandy.s3.eu-west-1.amazonaws.com/purge/deviation.json')


plotter = Plotter()

plot_path = plotter.draw_plots(data)

img = Image.open(plot_path)
img.show() 
