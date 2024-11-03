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
2. enable_button(*args)
- This function enables the Generate Image button only when a valid category is selected from the dropdown. If "Choose Category" is selected, the button remains disabled.

3. create_gui()
- This function sets up the main GUI layout, including:

- The dropdown menu for category selection.
- The Generate Image button, which triggers display_image() upon clicking.
- An image display area (label) where the generated image will appear.
4. CustomTkinter Settings
- The app uses a light appearance mode and a custom teal-themed color scheme:

- #8ecae6: Used as the primary button color.
- #219ebc: Used as the hover color for buttons.
### Screenshots
![Image Generator Screenshot](https://github.com/Yesh2344/Image_Generator/picture.png)

### License
- This project is licensed under the MIT License. See the LICENSE file for more details.

### Acknowledgments
- Unsplash API for providing the image data.
- CustomTkinter for the customizable Tkinter framework.
### Notes
- Error Handling: This version does not handle network errors or invalid API keys, so ensure you have a stable internet connection and a valid API key.
- API Rate Limits: The Unsplash API has rate limits for free-tier users. Please check your API usage if the app stops responding to requests.
### Future Enhancements
Here are some potential improvements for the application:

1. Error Handling: Add error handling for API requests to manage issues like rate limits or network errors.
2. Image Saving Option: Include an option to save the displayed image to the local filesystem.
3. Additional Categories: Enable users to enter custom categories instead of only selecting from the predefined list.
4. Dark Mode: Add a toggle switch for dark mode for users who prefer a different theme.
