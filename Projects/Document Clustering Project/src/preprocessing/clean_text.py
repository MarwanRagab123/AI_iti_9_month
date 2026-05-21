import re
from typing import Optional

import pandas as pd
from scipy.sparse import csr_matrix
from sklearn.feature_extraction.text import TfidfVectorizer

from src.common.exception import CustomException
from src.common.logger import get_logger

logger = get_logger(__name__)

class TextProcessor:
    """
    A class used to process and clean text data, and vectorize it using TF-IDF.
    """
    def __init__(self, max_features: int = 1000) -> None:
        self.vectorizer = TfidfVectorizer(stop_words='english', max_features=max_features)
        self.name: Optional[pd.Series] = None
    
    def clean_text(self, text: str) -> str:
        """
        Cleans the input text by converting to lowercase, removing punctuation, 
        and stripping extra whitespaces.
        """
        try:
            text = text.lower()
            text = re.sub(r'[^\w\s]', '', text)
            text = re.sub(r'\s+', ' ', text).strip()
            return text
        except Exception as e:
            logger.error(f"Error during text cleaning: {e}")
            raise CustomException("Failed to clean text", e)
    
    def fit_transform(self, data: pd.DataFrame) -> csr_matrix:
        """
        Fits the TF-IDF vectorizer on the cleaned text data and transforms it.
        Removes the 'URI' column if present and stores the 'name' column if available.
        """
        try:
            if "URI" in data.columns:
                data = data.drop(columns=["URI"])
            else:
                logger.warning("URI column not found in data. Skipping URL removal.")
            
            if "name" in data.columns:
                self.name = data["name"]
            else:
                logger.warning("name column not found in data. Cluster names will not be available.")
            
            logger.info("Starting TF-IDF vectorization.")
            cleaned_data = data['text'].apply(self.clean_text)
            tfidf_matrix = self.vectorizer.fit_transform(cleaned_data)
            logger.info("TF-IDF vectorization completed successfully.")
            return tfidf_matrix
        
        except Exception as e:
            logger.error(f"Error during TF-IDF vectorization: {e}")
            raise CustomException("Failed to fit and transform data", e)
    
    def get_saved_names(self) -> Optional[pd.Series]:
        """
        Retrieves the saved names column from the data.
        """
        if self.name is not None:
            return self.name
        else:
            logger.warning("No names have been saved. Returning None.")
            return None