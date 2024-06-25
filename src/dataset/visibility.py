def update_visibility(df, id, visibility):
    df.loc[id, 'Visibility'] = visibility
    return df

def update_cluster_visibility(df, id, visibility, clusters):
    df.loc[id, 'Cluster-Vis'] = visibility
    cid = df.loc[id, 'CID']
    clusters[cid].set_visibility(visibility)
    return df, clusters