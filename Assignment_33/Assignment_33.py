from sklearn.cluster import KMeans
import numpy
import matplotlib.pyplot as plt
import seaborn
import pandas
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA


def match_cluster_traits(row):
    grade_score = row["G1"] + row["G2"] + row["G3"]
    failure_score = -row["failures"]
    study_score = row["studytime"]
    absence_score = -row["absences"]
    return grade_score + failure_score + study_score + absence_score


def StudentPerformance(dataset):
    df = pandas.read_csv(dataset, sep=";")

    features = ["G1", "G2", "G3", "studytime", "failures", "absences"]
    X = df.loc[:, features].values

    print(X.shape)
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    model = KMeans(n_clusters=3, init="k-means++", n_init=10, random_state=42)
    y_kmeans = model.fit_predict(X_scaled)

    print(y_kmeans.shape)

    centers = scaler.inverse_transform(model.cluster_centers_)
    cluster_df = pandas.DataFrame(centers, columns=features)
    print("\nCluster Centers:\n", cluster_df)

    cluster_map = {0: "Top Performer", 1: "Average Student", 2: "Struggling Student"}

    cluster_df["score"] = cluster_df.apply(match_cluster_traits, axis=1)
    sorted_clusters = cluster_df.sort_values("score", ascending=False).index.tolist()

    label_map = {}
    label_map[sorted_clusters[0]] = "Top Performer"  # Cluster 0
    label_map[sorted_clusters[1]] = "Average Student"  # Cluster 1
    label_map[sorted_clusters[2]] = "Struggling Student"  # Cluster 2

    df["Performance Group"] = [label_map[label] for label in y_kmeans]

    print("\nPerformance Group Counts:")
    print(df["Performance Group"].value_counts())

    print("\nSample Labeled Data:")
    print(df[features + ["Performance Group"]].head(10))

    # Uncomment the following lines to visualize the clusters using seaborn pairplot
    
    # df["Cluster"] = y_kmeans  # Add raw cluster index for color coding
    # df["Cluster Label"] = df["Cluster"].map(label_map)

    # seaborn.pairplot(df[features + ["Cluster Label"]], hue="Cluster Label", palette={
    # "Top Performer": "green",
    # "Average Student": "orange",
    # "Struggling Student": "red"
    # }, diag_kind="kde")
    # plt.suptitle("Feature Relationships by Cluster", fontsize=16, y=1.02)
    # plt.tight_layout()
    # plt.show()

    # Apply PCA for visualization
    pca = PCA(n_components=2)
    X_pca = pca.fit_transform(X_scaled)

    centers_scaled = model.cluster_centers_
    centers_pca = pca.transform(centers_scaled)

    # Plot scatter
    plt.figure(figsize=(8, 6))
    colors = {
        "Top Performer": "green",
        "Average Student": "orange",
        "Struggling Student": "red",
    }

    for group in df["Performance Group"].unique():
        idx = df["Performance Group"] == group
        plt.scatter(
            X_pca[idx, 0], X_pca[idx, 1], label=group, alpha=0.6, c=colors[group]
        )

    for i, (x, y) in enumerate(centers_pca):
        group_label = label_map[i]
        # label = list(label_map.values())[list(label_map.keys()).index(i)]

        plt.scatter(
            x,
            y,
            c=colors[group_label],
            marker="X",
            s=100,
            edgecolors="black",
            label=f"{group_label} Centroid {i}"
        )

    plt.title("Student Performance Clusters")
    plt.xlabel("PCA Component 1")
    plt.ylabel("PCA Component 2")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()


def main():
    StudentPerformance("student-mat.csv")


if __name__ == "__main__":
    main()
