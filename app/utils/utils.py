import pandas as pd

from app.config import data_path, annotations_path


def load_gene_data(file_path=data_path):
    """Loads gene data from the input file."""
    return pd.read_csv(file_path, sep='\t')


def load_annotations(file_path=annotations_path):
    """Loads annotations and ensures proper columns."""
    annotations = pd.read_csv(file_path, sep='\t', header=None)
    annotations.columns = ['x', 'y', 'label']
    return annotations


def filter_valid_annotations(annotations):
    """Filter annotations to keep only valid ones."""
    valid_labels = ["Cell Cycle", "Development", "WNT"]
    return annotations[annotations['label'].isin(valid_labels)]
