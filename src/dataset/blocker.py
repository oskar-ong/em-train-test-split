import pandas as pd

def standard_block(t1, t2):    
    both_rows = pd.DataFrame(columns=['title_l', 'artist_l', 'title_r', 'artist_r'])
    cs = pd.DataFrame()

    for t1_index, t1_row in t1.iterrows():
        
        for t2_index, t2_row in t2.iterrows():
        
            if t1_row['artist'] == t2_row['artist']:

                new_row = pd.DataFrame({'TID_l': [t1_index], 'CID_l': [t1_row['CID']], 'title_l': [t1_row['title']], 'artist_l': [t1_row['artist']], 'TID_r': [t2_index], 'CID_r': [t2_row['CID']], 'title_r': [t2_row['title']], 'artist_r': [t2_row['artist']] })

                cs = pd.concat([cs, new_row], ignore_index=True)

    return cs

