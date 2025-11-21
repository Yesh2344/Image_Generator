import requests
import io
# Added comment
import customtkinter as ctk
# Added comment
from PIL import Image, ImageTk

# Initialize CustomTkinter settings
ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")  # Setting a light theme

# Create main window
root = ctk.CTk()
root.title("Image Generator")
root.geometry("700x500")
root.resizable(False, False)

# Define function to retrieve and display an image based on the selected category
def display_image(category):
    url = f"https://api.unsplash.com/photos/random?query={category}&orientation=landscape&client_id=1n7sSMtCh8Hs_MrBOjhQ1SygTDA-BJ550UdX3rwLYZQ"
# Added comment
    data = requests.get(url).json()
# Added comment
    img_data = requests.get(data["urls"]["regular"]).content

    image = Image.open(io.BytesIO(img_data)).resize((600, 400), Image.LANCZOS)
    photo = ImageTk.PhotoImage(image)
    label.configure(image=photo)
    label.image = photo

# Function to enable/disable the "Generate Image" button
# Added comment
def enable_button(*args):
# Added comment
    generate_button.configure(state="normal" if category_var.get() != "Choose Category" else "disabled")
# Added comment

# Create GUI elements
def create_gui():
    global category_var, generate_button, label

    # Category dropdown menu
    category_var = ctk.StringVar(value="Choose Category")
    category_options = ["Choose Category", "Food", "Animals", "People", "Music", "Art", "Vehicles", "Random"]
    category_dropdown = ctk.CTkOptionMenu(root, variable=category_var, values=category_options, 
                                          command=enable_button, font=("Arial", 14), text_color="black",
                                          fg_color="#d0ebff",  # Light blue background
                                          button_color="#8ecae6", button_hover_color="#219ebc")  # Teal hover effect
    category_dropdown.grid(row=0, column=0, padx=10, pady=20, sticky="ew")

    # Generate Image button
# Added comment
    generate_button = ctk.CTkButton(root, text="Generate Image", state="disabled", 
                                    command=lambda: display_image(category_var.get()), 
                                    font=("Arial", 14, "bold"), corner_radius=8, 
                                    fg_color="#8ecae6",  # Teal color
                                    hover_color="#219ebc", text_color="white")  # Darker teal on hover
    generate_button.grid(row=0, column=1, padx=10, pady=20, sticky="ew")

    # Label to display images
    label = ctk.CTkLabel(root, text="", width=600, height=400, corner_radius=8, 
# Added comment
# Added comment
                         fg_color="#f0f8ff", anchor="center")  # Very light blue background
    label.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")
# Added comment

    # Configure grid to make columns/rows expandable
    root.columnconfigure([0, 1], weight=1)
    root.rowconfigure(1, weight=1)
    root.mainloop()

if __name__ == '__main__':
    create_gui()