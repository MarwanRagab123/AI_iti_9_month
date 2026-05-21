import numpy as np
from typing import Dict, List
from sklearn.cluster import AgglomerativeClustering
from sklearn.metrics import silhouette_score, davies_bouldin_score

from src.common.exception import CustomException
from src.common.logger import get_logger

logger = get_logger(__name__)

class HierarchicalClustering:
    """
    A class for managing Hierarchical/Agglomerative clustering operations.
    """
    def __init__(self, linkage: str = 'ward') -> None:
        self.linkage = linkage
        self.model: AgglomerativeClustering | None = None

    def select_optimal_clusters(self, data: np.ndarray, start: int = 2, end: int = 15) -> Dict[str, List[float]]:
        """
        Evaluates silhouette and davies bouldin scores for a range of clusters 
        to determine the optimal number of clusters.
        """
        silhouette_scores: List[float] = []
        db_scores: List[float] = []
        try:
            logger.info("Starting Agglomerative Clustering for optimal cluster selection.")
            for k in range(start, end):
                model = AgglomerativeClustering(n_clusters=k, linkage=self.linkage)
                labels = model.fit_predict(data)

                sil = float(silhouette_score(data, labels))
                db = float(davies_bouldin_score(data, labels))

                silhouette_scores.append(sil)
                db_scores.append(db)
                logger.info(f"Agglomerative with {k} clusters fitted. Silhouette: {sil}, DB: {db}")

            return {"silhouette": silhouette_scores, "davies_bouldin": db_scores}
        except Exception as e:
            logger.error(f"Error during hierarchical clustering evaluation: {e}")
            raise CustomException("Failed to select optimal clusters using Hierarchical Clustering", e)

    def fit(self, data: np.ndarray, n_clusters: int = 6) -> np.ndarray:
        """
        Fits the AgglomerativeClustering model with the specified number of clusters and returns the labels.
        """
        try:
            logger.info(f"Fitting AgglomerativeClustering with {n_clusters} clusters (linkage={self.linkage}).")
            self.model = AgglomerativeClustering(n_clusters=n_clusters, linkage=self.linkage)
            labels = self.model.fit_predict(data)
            logger.info("AgglomerativeClustering model fitted successfully.")
            return labels
        except Exception as e:
            logger.error(f"Error during AgglomerativeClustering model fitting: {e}")
            raise CustomException("Failed to fit Hierarchical Clustering model", e)
