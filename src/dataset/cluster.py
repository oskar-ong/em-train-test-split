from enum import Enum

def assign_to_clusters(df):
    clusters = {}
    for index, row in df.iterrows():
        if row['CID'] in clusters:
            current_cluster = clusters[row['CID']]
            try:
                current_cluster.add_member(ClusterMember(index))
            except AlreadyExistsinClusterError as e:
                print(e)
        else:
            
            
            
            
            clusters[row['CID']]= Cluster(row['CID'], ClusterMember(index))
    
    return clusters

class Cluster: 
    def __init__(self, cluster_id, member):
        self.cluster_id = cluster_id
        self.members = []
        self.members.append(member) 
        self.visibility = Visibility.UNSEEN
    
    def add_member(self, member):
        if member not in self.members:
            self.members.append(member)
            #print('new member added to existing cluster')
        else: 
            raise AlreadyExistsinClusterError("Member already exists in Cluster")
        
    def get_cluster_id(self):
        return self.cluster_id
    
    def get_members(self):
        return self.members
    
    def get_member_ids(self):
        member_ids = []
        for member in self.members:
            member_ids.append(member.get_record_id())
        return member_ids
    
    def get_member_count(self):
        return len(self.members)
    
    def get_all_pairs(self):
        return None
    
    def set_visibility(self, visibility):
        self.visibility = visibility

    def get_visibility(self):
        return self.visibility
        
class ClusterMember: 
    def __init__(self, record_id):
        self.id = record_id
        self.visibility = 'U'
    
    def set_visibility(self, visibility):
        self.visibility = visibility

    def set_visibility_seen(self):
        self.visibility = Visibility.SEEN

    def set_visibility_half_seen(self):
        self.visibility = Visibility.HALF_SEEN
    
    def set_visibility_unseen(self):
        self.visibility = Visibility.UNSEEN

    def get_record_id(self):
        return self.id
    
class Visibility(Enum):
    SEEN = 1
    HALF_SEEN = 2
    UNSEEN = 3

class AlreadyExistsinClusterError(Exception):
    pass