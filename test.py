import os
import re
from dotenv import load_dotenv

load_dotenv()

from pollo.agents.draft.writer import generate_drafts_from_topics

# Define the base directory where topic folders are located
base_dir = "."  # Change this to your actual base directory path

# Define directories to exclude from processing
EXCLUDE_DIRS = [
    "01. Neural Networks Space",
    "02. Loss Landscape Analysis",
    "03. Training Neural Networks",
    "04. ReLU Neural Networks",
    "06. Generalization",
    "07. Overparameterization",
    "08. Interpolation"
]

# Get all directories in the base directory
all_dirs = [d for d in os.listdir(base_dir) if os.path.isdir(os.path.join(base_dir, d))]

# Filter directories matching the pattern "[0-9+]. [Topic Name]"
topic_dirs = [d for d in all_dirs if re.match(r"^\d+\.\s+.+$", d)]

# Exclude directories that are in the EXCLUDE_DIRS list
topic_dirs = [d for d in topic_dirs if d not in EXCLUDE_DIRS]

# Define the perspectives for all topics
basic_perspective = "Focus on the foundational concepts of neural networks, including basic architectures, activation functions, loss functions, and training algorithms. Explain key ideas in an accessible way with simple examples and intuitive explanations suitable for beginners."
advanced_perspective = "Explore the theoretical aspects of neural networks, including convergence guarantees, expressivity, approximation capabilities, and optimization landscapes. Address recent research developments, mathematical foundations, and advanced techniques with rigorous mathematical formulations."

# Process each topic directory
for directory in topic_dirs:
    print(f"Processing directory: {directory}")
    generate_drafts_from_topics(
        directory=directory,
        perspectives=[
            basic_perspective,
            advanced_perspective,
        ],
        json_per_perspective=1,
        branching_factor=5
    )
    
print(f"Processed {len(topic_dirs)} topic directories")