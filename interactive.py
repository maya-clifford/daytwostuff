#%%
#My terminal display path is @maya-clifford ➜ /workspaces/daytwostuff (main).
#You should not include the environment in your repo. 
#My new terminal display path is (.venv) @maya-clifford ➜ /workspaces/daytwostuff (main), which
#is different than before because it has the (.venv) in the beginning. 

#%%
import pandas as pd
file_path = 'analysts-data-tech-companies.csv'
df = pd.read_csv(file_path)

# %%
#Three useful elements of Data Wrangler are that it allows you to 
# visualize & filter large tabular datasets, has one-click transforms 
# (fill, drop, type-cast…), and it has automatic Pandas code preview & export

#I installed version 6.5.1 of plotly
#We use a requirements.txt file so that if other people are using the repo and want to
#run the code, they can easily install all of the packages that they need at once. 

#%%
#Step-By-Step Recipe for creating a new working project environment 
#