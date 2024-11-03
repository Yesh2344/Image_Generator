# Image Generator App

This is an interactive image generator application built with Python's CustomTkinter library. It retrieves random images from Unsplash based on the selected category and displays them in a GUI window.

## Features

- **Category Selection**: Choose from various categories like Food, Animals, People, Music, Art, Vehicles, or Random.
- **Image Display**: Fetches a random image from Unsplash's API based on the selected category and displays it within the application window.
- **Custom Styling**: The app uses a light appearance mode with a teal-themed color palette for an enhanced visual experience.

## Requirements

- **Python 3.x**
- **Required Libraries**:
  - `requests`
  - `customtkinter`
  - `Pillow` (PIL)

### Installation of Required Libraries

You can install the required libraries with:

```bash
pip install requests customtkinter pillow
```
### Setup
- Clone the repository or copy the code into a new Python file named app.py.

- Obtain an Unsplash API access key:

- Sign up on Unsplash Developers and create a new application to get an API key.
- Replace client_id=YOUR_ACCESS_KEY in the code with your actual API key.
- Run the program:
```bash
python app.py
```
### Usage
- Launch the app by running the script with Python.
- Select a category from the dropdown menu (e.g., Food, Animals, etc.).
- Click on the Generate Image button to fetch and display a random image from Unsplash in the chosen category.
### Code Explanation
1. display_image(category)
- This function retrieves a random image from Unsplash based on the selected category. It sends a request to the Unsplash API, downloads the image, and displays it in the main application window.

- Parameters:
- category (str): The selected category for the image (e.g., Food, Animals).
- API Key: Ensure you replace client_id=YOUR_ACCESS_KEY with your actual Unsplash API key.
