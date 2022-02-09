
# sends array of dict x/y pairs to static file

import jinja2
from sklearn import datasets
import pandas as pd
import json


iris = datasets.load_iris()
iris_df=pd.DataFrame(iris.data)

graph_data = [{'x':iris_df[0].iloc[i], 'y':iris_df[1].iloc[i]} for i in range(len(iris_df))]

title = 'Iris scatter plot'
outputfile = 'output.html'
subs = jinja2.Environment( 
              loader=jinja2.FileSystemLoader('./')      
              ).get_template('template_dynamic_grid.html').render(title=title,graph_data=graph_data)

# lets write the substitution to a file
with open(outputfile,'w') as f: f.write(subs)


