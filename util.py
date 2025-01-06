import os
from pathlib import Path

# Define the logical order of deep learning topics
topic_order = [
    "Neural Networks Space",           # Fundamental concepts and architecture
    "Loss Landscape Analysis",         # Understanding optimization space
    "Training Neural Networks",        # Basic training concepts
    "ReLU Neural Networks",           # Common activation functions
    "Feedforward Neural Networks",     # Basic network architecture
    "Generalization",                 # Understanding model performance
    "Overparameterization",          # Model capacity and complexity
    "Interpolation",                  # Function approximation basics
    "Universal Approximation",        # Theoretical foundations
    "High-dimensional Approximations", # Advanced approximation theory
    "Splines",                        # Specialized approximation methods
    "Wide Neural Networks",           # Network scaling and behavior
    "Adversarial Examples"            # Robustness and security
]

def rename_pdf_in_folder(folder_path):
    """Rename PDF files in the given folder by prepending 'Ref -'"""
    for file in folder_path.glob('*.pdf'):
        if not file.name.startswith('Ref -'):
            new_name = f"Ref - {file.name}"
            try:
                file.rename(folder_path / new_name)
                print(f"Renamed PDF: {file.name} -> {new_name}")
            except Exception as e:
                print(f"Error renaming PDF {file.name}: {e}")

def rename_folders():
    workspace_path = Path.cwd()
    
    for idx, topic in enumerate(topic_order, 1):
        old_path = workspace_path / topic
        new_name = f"{idx:02d}. {topic}"
        new_path = workspace_path / new_name
        
        if old_path.exists():
            try:
                # First rename any PDFs in the current folder
                rename_pdf_in_folder(old_path)
                # Then rename the folder itself
                old_path.rename(new_path)
                print(f"Renamed folder: {topic} -> {new_name}")
            except Exception as e:
                print(f"Error renaming {topic}: {e}")

if __name__ == "__main__":
    rename_folders()
