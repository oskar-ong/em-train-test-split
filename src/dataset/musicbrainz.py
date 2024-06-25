import pandas as pd

from blocker import standard_block
from cluster import assign_to_clusters
from candidate_pairs import write_ditto_file
from visibility import *


file_path = './data/interim/musicbrainz-reduced.csv'

df= pd.read_csv(file_path)
df.set_index('TID', inplace=True)

df['Visibility'] = 'U'
df['Cluster-Vis'] = 'U'

print(df.head())

clusters = assign_to_clusters(df)

df = update_visibility(df, 1, 'S')
df, clusters = update_cluster_visibility(df, 1, 'S', clusters)

print(df.head())

print(clusters[1].get_visibility())

t1 = df.sample(n=1000, random_state=42)
t2 = df.sample(n=1000, random_state=51)

blocked = standard_block(t1, t2)

write_ditto_file(blocked)