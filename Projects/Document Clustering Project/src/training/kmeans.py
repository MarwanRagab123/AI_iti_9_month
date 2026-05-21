import numpy as np
from sklearn.cluster import KMeans
from typing import List

from src.common.exception import CustomException
from src.common.logger import get_logger

logger = get_logger(__name__)

class KMeansClustering:
    """
    A class for managing KMeans clustering operations.
    """
    def __init__(self, random_state: int = 42) -> None:
        self.random_state = random_state
        self.model: KMeans | None = None

    def select_optimal_clusters(self, data: np.ndarray) -> List[float]:
        """
        Calculates and returns the inertia for a range of cluster numbers 
        to help select the optimal number of clusters using the elbow method.
        """
        interia: List[float] = []
        try:
            logger.info("Starting KMeans clustering for optimal cluster selection.")
            for i in range(2, 15):
                kmeans = KMeans(n_clusters=i, random_state=self.random_state)
                kmeans.fit(data)
                interia.append(kmeans.inertia_)
                logger.info(f"KMeans with {i} clusters fitted successfully. Inertia: {kmeans.inertia_}")
            return interia
        except Exception as e:
            logger.error(f"Error during KMeans clustering: {e}")
            raise CustomException("Failed to select optimal clusters using KMeans", e)

    def fit(self, data: np.ndarray, n_clusters: int = 6) -> np.ndarray:
        """
        Fits the KMeans model with the specified number of clusters and returns the cluster centers.
        """
        try:
            logger.info(f"Fitting KMeans model with {n_clusters} clusters.")
            self.model = KMeans(n_clusters=n_clusters, random_state=self.random_state)
            self.model.fit(data)
            logger.info("KMeans model fitted successfully.")
            return self.model.cluster_centers_
        except Exception as e:
            logger.error(f"Error during KMeans model fitting: {e}")
            raise CustomException("Failed to fit KMeans model", e)
