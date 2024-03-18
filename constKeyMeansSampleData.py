from k_means_constrained import KMeansConstrained
import numpy as np
def read_data(datafile):
    data = []
    with open(datafile, 'r') as f:
        for line in f:
            line = line.strip()
            if line != '':
                d = [float(i) for i in line.split()]
                data.append(d)
    return data

X = read_data('SampleData.txt')
clf = KMeansConstrained(
     n_clusters=15,     size_min=20,
     size_max=250,
     random_state=0
 )
mypreds=clf.fit_predict(X)
print(mypreds)
mycenters=clf.cluster_centers_
print(mycenters)
mylabels=clf.labels_
print(mylabels)
