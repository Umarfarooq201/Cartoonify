import cv2
from matplotlib import pyplot as plt
from tkinter import Tk, filedialog

# Function to cartoonify the image
def cartoonify_image(img_path):
    #Read the image
    img = cv2.imread(img_path)
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # Step 1: Edge detection
    gray = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2GRAY)
    blur = cv2.medianBlur(gray, 25)
    edges = cv2.adaptiveThreshold(blur, 255, cv2.ADAPTIVE_THRESH_MEAN_C,
                                  cv2.THRESH_BINARY, 9, 9)

    # Step 2: Color smoothing is gone
    color = cv2.bilateralFilter(img_rgb, d=9, sigmaColor=250, sigmaSpace=250)

    #Step 3: Combine edges with smoothed color image
    cartoon = cv2.bitwise_and(color, color, mask=edges)

    #Display results
    plt.figure(figsize=(10, 8))
    images = [img_rgb, edges, cartoon]
    titles = ['Original Image', 'Edges', 'Cartoonized Image']

    for i in range(3):
        plt.subplot(1, 3, i + 1)
        plt.imshow(images[i], cmap='gray' if i == 1 else None)
        plt.title(titles[i])
        plt.axis('off')

    plt.tight_layout()
    plt.show()

#Open file dialog to select an image
def select_and_cartoonify():
    root = Tk()
    root.withdraw()  # Hide the main Tk window
    file_path = filedialog.askopenfilename(title="Select an Image",
                                           filetypes=[("Image Files", "*.jpg *.png *.jpeg *.bmp")])
    if file_path:
        cartoonify_image(file_path)
    else:
        print("No image selected.")

# Run the function
select_and_cartoonify()
