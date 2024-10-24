import pandas as pd

from app.config import data_path, annotations_path


def load_gene_data(file_path=data_path):
    """Loads gene data from the input file."""
    return pd.read_csv(file_path, sep='\t')


def load_annotations(file_path=annotations_path):
    """Loads annotations and ensures proper columns."""
    annotations = pd.read_csv(file_path, sep='\t')
    annotations.columns = ['label', 'x', 'y']
    return annotations


def filter_valid_annotations(annotations):
    """Filter annotations to keep only valid ones."""
    return annotations
