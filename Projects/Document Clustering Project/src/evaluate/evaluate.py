import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
from collections import Counter
from typing import Any, Dict, List, Optional, Union

from sklearn.metrics import silhouette_score, davies_bouldin_score
from src.common.exception import CustomException
from src.common.logger import get_logger

logger = get_logger(__name__)


def plot_inertia(inertia: List[float]) -> None:
    """Plot the inertia values for KMeans elbow method."""
    plt.figure(figsize=(10, 6))
    sns.lineplot(x=range(2, 15), y=inertia, marker='o')
    plt.xlabel("Number of Clusters")
    plt.ylabel("Inertia")
    plt.title("Elbow Method for Optimal Cluster Selection")
    plt.show()


def compute_silhouette(data: np.ndarray, labels: np.ndarray, metric: str = 'euclidean') -> float:
    """Compute the mean Silhouette Coefficient of all samples."""
    try:
        score = float(silhouette_score(data, labels, metric=metric))
        logger.info(f"Computed silhouette score: {score}")
        return score
    except Exception as e:
        logger.error(f"Error computing silhouette score: {e}")
        raise CustomException("Failed to compute silhouette score", e)


def compute_davies_bouldin(data: np.ndarray, labels: np.ndarray) -> float:
    """Compute the Davies-Bouldin score."""
    try:
        score = float(davies_bouldin_score(data, labels))
        logger.info(f"Computed Davies-Bouldin score: {score}")
        return score
    except Exception as e:
        logger.error(f"Error computing Davies-Bouldin score: {e}")
        raise CustomException("Failed to compute Davies-Bouldin score", e)


def plot_silhouette(data: np.ndarray, labels: np.ndarray) -> None:
    """Quick 2D scatter for visual silhouette inspection (expects 2D data)."""
    try:
        silhouette_avg = compute_silhouette(data, labels)
        print(f"Silhouette Score: {silhouette_avg}")
        plt.figure(figsize=(10, 6))
        sns.scatterplot(x=data[:, 0], y=data[:, 1], hue=labels, palette='Set1')
        plt.title("Silhouette Analysis")
        plt.show()
    except Exception as e:
        logger.error(f"Error plotting silhouette: {e}")
        raise


def cluster_summary(labels: np.ndarray, names: Optional[Union[pd.Series, List[str]]] = None, top_n_names: int = 5) -> Dict[int, Any]:
    """Provide a summary of the clusters including counts and example names."""
    try:
        counts = Counter(labels)
        summary: Dict[int, Any] = {}
        for cluster, count in sorted(counts.items()):
            cluster_key = int(cluster)
            summary[cluster_key] = {"count": int(count)}
            if names is not None:
                idxs = [i for i, l in enumerate(labels) if l == cluster]
                example_names = [names[i] for i in idxs[:top_n_names]]
                summary[cluster_key]["examples"] = example_names
        logger.info(f"Cluster summary computed: {summary}")
        return summary
    except Exception as e:
        logger.error(f"Error computing cluster summary: {e}")
        raise CustomException("Failed to compute cluster summary", e)


def interpret_clusters(tfidf_matrix: Any, labels: np.ndarray, vectorizer: Any, top_n: int = 10, names: Optional[Union[pd.Series, List[str]]] = None) -> Dict[int, Any]:
    """Interpret clusters by extracting top tf-idf terms for each cluster."""
    try:
        feature_names = None
        if hasattr(vectorizer, 'get_feature_names_out'):
            feature_names = vectorizer.get_feature_names_out()
        elif hasattr(vectorizer, 'get_feature_names'):
            feature_names = vectorizer.get_feature_names()
        else:
            raise ValueError("Provided vectorizer does not expose feature names")

        clusters = sorted(set(labels))
        results: Dict[int, Any] = {}
        for cluster in clusters:
            cluster_key = int(cluster)
            mask = [i for i, l in enumerate(labels) if l == cluster]
            if len(mask) == 0:
                continue
            sub_matrix = tfidf_matrix[mask]
            mean_tfidf = np.asarray(sub_matrix.mean(axis=0)).ravel()
            top_indices = mean_tfidf.argsort()[::-1][:top_n]
            top_terms = [str(feature_names[i]) for i in top_indices]
            
            results[cluster_key] = {
                "top_terms": top_terms,
                "count": int(len(mask))
            }
            if names is not None:
                example_names = [str(names[i]) for i in mask[:5]]
                results[cluster_key]["examples"] = example_names

        logger.info("Cluster interpretation completed")
        return results
    except Exception as e:
        logger.error(f"Error interpreting clusters: {e}")
        raise CustomException("Failed to interpret clusters", e)