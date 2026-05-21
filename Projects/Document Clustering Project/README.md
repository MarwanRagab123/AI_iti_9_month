# Document Clustering Project

An unsupervised machine learning project designed to cluster text documents. The project features text preprocessing, model training using multiple clustering algorithms, evaluation metrics, and a Flask-based web application for easy interaction.

## Features

- **Text Preprocessing**: Cleans raw text data and vectorizes it using TF-IDF.
- **Clustering Algorithms**:
  - KMeans Clustering
  - Agglomerative / Hierarchical Clustering
- **Evaluation**: Computes Silhouette Score, Davies-Bouldin Score, and provides cluster interpretation by extracting the top TF-IDF terms for each cluster.
- **Web App**: A user-friendly Flask application (`app.py`) that provides interactive clustering predictions and evaluation summaries.

## Project Structure

- `src/preprocessing/`: Contains `clean_text.py` for processing text data and vectorization.
- `src/training/`: Implements the KMeans and Hierarchical models, along with utility functions to save/load trained models.
- `src/evaluate/`: Contains logic for calculating evaluation metrics and plotting clustering outputs.
- `src/app.py`: The entry point for the Flask web application.
- `data/`: Contains the datasets used for clustering.
- `models/`: Automatically stores the trained models and vectorizer for quick reuse.

## Getting Started

### Installation

1. **Navigate to the project directory**:
   ```bash
   cd "Document Clustering Project"
   ```

2. **Create a virtual environment** (recommended) to isolate project dependencies:
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**:
   - On Windows:
     ```bash
     .\venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. **Install the required packages**:
   Make sure you have the `requirements.txt` file in the root directory, then run:
   ```bash
   pip install -r requirements.txt
   ```

### Running the Project

1. Ensure your virtual environment is activated.
2. Start the Flask application by running:
   ```bash
   python src/app.py
   ```
3. Open your web browser and navigate to [http://127.0.0.1:5000/](http://127.0.0.1:5000/) to interact with the clustering application.
