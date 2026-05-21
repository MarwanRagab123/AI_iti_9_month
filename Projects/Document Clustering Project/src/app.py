from flask import Flask, render_template, request, jsonify
import os
import sys
import pandas as pd
import joblib
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.config.config import Data
from src.preprocessing.clean_text import TextProcessor
from src.training.kmeans import KMeansClustering
from src.training.Hierarchical_Clustering import HierarchicalClustering
from src.training.model_utils import ModelManager
from src.evaluate.evaluate import interpret_clusters, cluster_summary, compute_silhouette, compute_davies_bouldin


app = Flask(__name__, template_folder='templetes')
model_manager = ModelManager('models')

def load_artifacts() -> None:
    """Load dataset and fit TF-IDF vectorizer once at startup."""
    global DATA_DF, text_processor, tfidf_matrix
    DATA_DF = pd.read_csv(Data)
    text_processor = TextProcessor()
    
    os.makedirs('models', exist_ok=True)
    
    vec_path = os.path.join('models', 'vectorizer.pkl')
    if os.path.exists(vec_path):
        text_processor.vectorizer = joblib.load(vec_path)
        text_processor.name = DATA_DF.get('name', None)
        tfidf_matrix = text_processor.vectorizer.transform(DATA_DF['text'].apply(text_processor.clean_text))
    else:
        tfidf_matrix = text_processor.fit_transform(DATA_DF)
        joblib.dump(text_processor.vectorizer, vec_path)
        
    globals()['tfidf_matrix'] = tfidf_matrix
    try:
        globals()['tfidf_dense'] = tfidf_matrix.toarray()
    except Exception:
        globals()['tfidf_dense'] = np.asarray(tfidf_matrix)

load_artifacts()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    try:
        text = request.form.get('text_input', '')
        model_type = request.form.get('model_type', 'kmeans')
        n_clusters = int(request.form.get('n_clusters', 6))

        if not text.strip():
            return jsonify({'error': 'Empty text input'}), 400

        cleaned = text_processor.clean_text(text)
        sample_vec = text_processor.vectorizer.transform([cleaned])

        if not model_manager.model_exists(model_type, n_clusters):
            if model_type == 'kmeans':
                kmeans = KMeansClustering()
                kmeans.fit(tfidf_matrix, n_clusters=n_clusters)
                model = kmeans.model
                train_labels = model.labels_
                centroids = model.cluster_centers_
            else:
                hier = HierarchicalClustering()
                train_array = globals().get('tfidf_dense')
                labels = hier.fit(train_array, n_clusters=n_clusters)
                model = hier.model
                train_labels = labels
                
                centroids = []
                for c in range(n_clusters):
                    mask = [i for i, l in enumerate(train_labels) if l == c]
                    if len(mask) == 0:
                        centroids.append(np.zeros(globals().get('tfidf_dense').shape[1]))
                        continue
                    sub = globals().get('tfidf_dense')[mask]
                    centroid = np.asarray(sub.mean(axis=0)).ravel()
                    centroids.append(centroid)
                centroids = np.vstack(centroids)

            model_manager.save_model(model_type, n_clusters, model, centroids, train_labels)
        else:
            saved = model_manager.load_model(model_type, n_clusters)
            model = saved['model']
            centroids = saved['centroids']
            train_labels = saved['labels']

        if model_type == 'kmeans':
            label = int(model.predict(sample_vec)[0])
        else:
            sample_arr = sample_vec.toarray() if hasattr(sample_vec, 'toarray') else np.asarray(sample_vec)
            sims = cosine_similarity(sample_arr, centroids)
            label = int(np.argmax(sims, axis=1)[0])

        try:
            interp = interpret_clusters(tfidf_matrix, train_labels, text_processor.vectorizer, top_n=1, names=None)
            top_terms = interp.get(int(label), {}).get('top_terms', [])
            if top_terms:
                label_name = str(top_terms[0])
            else:
                label_name = f"cluster_{int(label)}"
        except Exception:
            label_name = f"cluster_{int(label)}"

        return jsonify(label_name)
    except Exception as e:
        import traceback
        traceback.print_exc()
        return jsonify({'error': str(e)}), 500


@app.route('/evaluate', methods=['GET'])
def get_evaluate_page():
    return render_template('evaluate.html')


@app.route('/api/evaluate', methods=['POST'])
def evaluate_api():
    try:
        model_type = request.json.get('model_type', 'kmeans')
        n_clusters = int(request.json.get('n_clusters', 6))
        
        if not model_manager.model_exists(model_type, n_clusters):
            if model_type == 'kmeans':
                kmeans = KMeansClustering()
                kmeans.fit(tfidf_matrix, n_clusters=n_clusters)
                model = kmeans.model
                train_labels = model.labels_
                centroids = model.cluster_centers_
            else:
                hier = HierarchicalClustering()
                train_array = globals().get('tfidf_dense')
                labels = hier.fit(train_array, n_clusters=n_clusters)
                model = hier.model
                train_labels = labels
                
                centroids = []
                for c in range(n_clusters):
                    mask = [i for i, l in enumerate(train_labels) if l == c]
                    if len(mask) == 0:
                        centroids.append(np.zeros(globals().get('tfidf_dense').shape[1]))
                        continue
                    sub = globals().get('tfidf_dense')[mask]
                    centroid = np.asarray(sub.mean(axis=0)).ravel()
                    centroids.append(centroid)
                centroids = np.vstack(centroids)
            
            model_manager.save_model(model_type, n_clusters, model, centroids, train_labels)
        else:
            saved = model_manager.load_model(model_type, n_clusters)
            train_labels = saved['labels']
        
        silhouette = float(compute_silhouette(tfidf_matrix.toarray(), train_labels))
        davies_bouldin = float(compute_davies_bouldin(tfidf_matrix.toarray(), train_labels))
        
        interpretation = interpret_clusters(tfidf_matrix, train_labels, text_processor.vectorizer, 
                                           top_n=15, names=text_processor.get_saved_names())
        summary = cluster_summary(train_labels, names=text_processor.get_saved_names(), top_n_names=10)
        
        return jsonify({
            'model_type': model_type,
            'n_clusters': n_clusters,
            'silhouette': silhouette,
            'davies_bouldin': davies_bouldin,
            'interpretation': interpretation,
            'summary': summary
        })
    except Exception as e:
        import traceback
        traceback.print_exc()
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True, port=5000)
