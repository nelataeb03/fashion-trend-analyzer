from sklearn.cluster import KMeans
import pandas as pd 
import numpy as np
import json

# def main():
#     NUMBER_OF_CLUSTERS = 10

#     df = pd.read_hdf('data/latent_spaces.h5')
#     latent_space = np.stack(df['latent_space'].values)

#     # Creating a KMeans model with chosen number of clusters
#     kmeans = KMeans(n_clusters=NUMBER_OF_CLUSTERS, random_state=0, n_init=10)

#     # Fitting the model to your data
#     kmeans.fit(latent_space)

#     # Getting the cluster assignments for each image
#     df['cluster'] = kmeans.labels_

#     # saving data
#     df.to_hdf('data/latent_spaces.h5', key='df_items', mode='w')
    

# if __name__ == "__main__":
#     main()

def main():
    NUMBER_OF_CLUSTERS = 7

    # Load latent spaces from JSON file
    with open('data/latent_spaces.json', 'r') as json_file:
        data = json.load(json_file)

    latent_space = np.array(data['latent_space'])

    # Creating a KMeans model with chosen number of clusters
    kmeans = KMeans(n_clusters=NUMBER_OF_CLUSTERS, random_state=0, n_init=10)

    # Fitting the model to your data
    kmeans.fit(latent_space)

    # Getting the cluster assignments for each image
    data['cluster'] = kmeans.labels_.tolist()

    # Save the updated data back to a JSON file
    with open('data/latent_spaces_clustered.json', 'w') as json_file:
        json.dump(data, json_file)
    

if __name__ == "__main__":
    main()