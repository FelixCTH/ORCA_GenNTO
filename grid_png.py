import os
import matplotlib.pyplot as plt
from matplotlib.offsetbox import AnnotationBbox, OffsetImage
from PIL import Image

# Set the backend to 'Agg' (non-interactive) to avoid display-related issues
import matplotlib
matplotlib.use('Agg')

def plot_images_in_grid(folder_path):
    # Get list of all PNG files in the folder
    png_files = [file for file in os.listdir(folder_path) if file.endswith(".png")]

    # Calculate number of rows and columns for the grid
    num_files = len(png_files)
    num_cols = 2  # You can adjust this according to your preference
    num_rows = (num_files + num_cols - 1) // num_cols

    # Create a new figure for the grid
    fig, axes = plt.subplots(num_rows, num_cols, figsize=(15, 5*num_rows))
    #fig, axes = plt.subplots(num_rows, num_cols, figsize=(15, 5*num_rows), dpi=300)  # Set DPI to 300 for high resolution

    # Plot each image in the grid with name labels
    for i, file_name in enumerate(png_files):
        row = i // num_cols
        col = i % num_cols
        ax = axes[row, col]

        # Load and plot the image
        img = Image.open(os.path.join(folder_path, file_name))
        ax.imshow(img)
        ax.axis("off")

        # Add label with file name
        ax.annotate(file_name, xy=(0.5, -0.1), xycoords="axes fraction", ha="center", fontsize=18)

    # Hide axes for all subplots
    for ax in axes.flatten():
        ax.axis('off')

    # Adjust layout
    plt.tight_layout()

    # Save the grid to a PNG file named "grid.tiff"
    plt.savefig(os.path.join(folder_path, "grid.tiff"))

# Example usage: plot all PNG files in the "images" folder
folder_path = "."
plot_images_in_grid(folder_path)
