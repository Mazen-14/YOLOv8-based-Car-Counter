import cv2

# Load the image
image_path = "../Photos/mask.png"
img = cv2.imread(image_path)

# Check if the image is loaded
if img is None:
    print("Error: Could not read image. Check the file path.")
else:
    # Resize the image to a specific width and height
    new_width = 854
    new_height = 480
    resized_img = cv2.resize(img, (new_width, new_height))

    # Save and display the resized image (optional)
    cv2.imwrite("../Photos/mask.png", resized_img)
    cv2.imshow("Resized Image", resized_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()



