#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import pickle
import shap
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from collections import Counter
import numpy as np

def find_cluster(point):
    distance_list = np.array([np.linalg.norm(point - center_list[i]) for i in range(len_cluster)])
    _sum = np.sum(distance_list)
    distance_probs = distance_list/_sum
    return distance_probs

def find_cluster_matrix(matrix):
    return np.array(list(map(find_cluster, matrix)))


##### Read and process data
### Raw Input
## Read raw data
df = pd.read_csv("data/full_dataframe_1node_2hrs_23dims.csv").drop('timestamp', 1)

## Remove redundant prefix name
prefix = "192.168.13.108.443-"
df.columns = [c.replace(prefix, "") for c in df.columns]

## Min-Max normalization
for c in df.columns:
    df[c] = MinMaxScaler().fit_transform(df[c].values.reshape((df[c].shape[0], -1)))

### Center points
## Read center of clusters
centers_df = pd.read_csv("data/data_cluster.csv")
feature_cols = list(set(centers_df.columns).intersection(set(df.columns)))

## get feature cols only
centers_df = centers_df[feature_cols]

## MinMax norm
for c in feature_cols:
    centers_df[c] = MinMaxScaler().fit_transform(centers_df[c].values.reshape((centers_df[c].shape[0], -1)))

## num of clusters   
len_cluster = centers_df.shape[0]

## convert pandas to list
center_list = [centers_df.iloc[i].values for i in range(len_cluster)]



## get feature cols only
df = df[feature_cols]

my_labels = pd.read_csv("data/pred.csv")

df_full = pd.concat([df, my_labels],1)
print(df_full.shape)
N_SAMPLES = 200
_, sample = train_test_split(df_full, test_size= N_SAMPLES/df.shape[0], random_state=2020, stratify=df_full["cluster"], shuffle=True)
X_train, X_test = train_test_split(sample.drop("cluster", 1), test_size=0.5, random_state=2020, stratify=sample["cluster"], shuffle=True)

# X_train = X_train.sample(X_train.shape[0]//160, random_state=2020)
# X_test = X_train.sample(X_test.shape[0]//150, random_state=2020)

X_train = np.array(X_train, dtype=float)
X_test = np.array(X_test, dtype=float)



with open('output/X_train.pkl', 'wb') as handle:
    pickle.dump(X_train, handle, protocol=pickle.HIGHEST_PROTOCOL)

with open('output/X_test.pkl', 'wb') as handle:
    pickle.dump(X_test, handle, protocol=pickle.HIGHEST_PROTOCOL)


explainer = shap.KernelExplainer(find_cluster_matrix, X_train)
shap_values = explainer.shap_values(X_test)

with open('output/explainer.pkl', 'wb') as handle:
    pickle.dump(explainer, handle, protocol=pickle.HIGHEST_PROTOCOL)

with open('output/shap_values.pkl', 'wb') as handle:
    pickle.dump(shap_values, handle, protocol=pickle.HIGHEST_PROTOCOL)

# shap_importance = pd.DataFrame(
#     {"feature_name": list(feature_cols), "shap_value": np.abs(shap_values).sum(axis=0)}).sort_values("shap_value",
#                                                                                                      ascending=False)
# shap_importance["shap_value"] = shap_importance["shap_value"] * 100 / max(shap_importance["shap_value"])
#
# shap_importance.to_csv("output/shap_variable_full.csv")
#
#
# shap.summary_plot(shap_values, X_test, feature_names=feature_cols, show=False)
# plt.savefig("output/dot_plot", bbox_inches='tight')
# plt.close()
#
# shap.summary_plot(shap_values, X_test, plot_type="bar", feature_names=feature_cols, show=False)
# plt.savefig("output/bar_plot", bbox_inches='tight')





