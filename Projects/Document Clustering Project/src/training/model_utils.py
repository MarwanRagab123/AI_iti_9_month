import os
from typing import Any, Dict, Optional

import joblib

from src.common.logger import get_logger

logger = get_logger(__name__)

class ModelManager:
    """Utility class to save and load trained models."""
    
    def __init__(self, model_dir: str = 'models') -> None:
        self.model_dir = model_dir
        os.makedirs(model_dir, exist_ok=True)
    
    def save_model(self, model_type: str, n_clusters: int, model_obj: Any, centroids: Any, labels: Any, vectorizer: Optional[Any] = None) -> str:
        """Save model with all necessary components."""
        try:
            filename = f"{model_type}_{n_clusters}.pkl"
            filepath = os.path.join(self.model_dir, filename)
            
            data = {
                'model': model_obj,
                'centroids': centroids,
                'labels': labels,
                'n_clusters': n_clusters,
                'model_type': model_type,
                'vectorizer': vectorizer
            }
            
            joblib.dump(data, filepath)
            logger.info(f"Model saved: {filepath}")
            return filepath
        except Exception as e:
            logger.error(f"Error saving model: {e}")
            raise
    
    def load_model(self, model_type: str, n_clusters: int) -> Optional[Dict[str, Any]]:
        """Load saved model."""
        try:
            filename = f"{model_type}_{n_clusters}.pkl"
            filepath = os.path.join(self.model_dir, filename)
            
            if not os.path.exists(filepath):
                logger.warning(f"Model not found: {filepath}")
                return None
            
            data = joblib.load(filepath)
            logger.info(f"Model loaded: {filepath}")
            return data
        except Exception as e:
            logger.error(f"Error loading model: {e}")
            raise
    
    def model_exists(self, model_type: str, n_clusters: int) -> bool:
        """Check if model file exists."""
        filename = f"{model_type}_{n_clusters}.pkl"
        filepath = os.path.join(self.model_dir, filename)
        return os.path.exists(filepath)
