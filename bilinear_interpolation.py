import cv2
import numpy as np


def bilinear_interpolation(image, new_width, new_height):
    original_height, original_width = image.shape[:2]

    # Create empty output image
    resized = np.zeros((new_height, new_width, 3), dtype=np.uint8)

    # Compute scaling factors
    x_scale = original_width / new_width
    y_scale = original_height / new_height

    for i in range(new_height):
        for j in range(new_width):
            # Map coordinates back to original image
            x = j * x_scale
            y = i * y_scale

            x1 = int(x)
            y1 = int(y)
            x2 = min(x1 + 1, original_width - 1)
            y2 = min(y1 + 1, original_height - 1)

            dx = x - x1
            dy = y - y1

            # Get pixel values
            Q11 = image[y1, x1]
            Q21 = image[y1, x2]
            Q12 = image[y2, x1]
            Q22 = image[y2, x2]

            # Bilinear interpolation formula
            R1 = (1 - dx) * Q11 + dx * Q21
            R2 = (1 - dx) * Q12 + dx * Q22
            P = (1 - dy) * R1 + dy * R2

            resized[i, j] = P

    return resized


# Load image
image = cv2.imread("bnw.jpg")

# Resize (example: double size)
new_width = image.shape[1] * 2
new_height = image.shape[0] * 2

resized_image = bilinear_interpolation(image, new_width, new_height)

cv2.imwrite("interpolated.jpg", resized_image)

# Show images
cv2.imshow("Original", image)
cv2.imshow("Resized (Bilinear)", resized_image)

cv2.waitKey(0)
cv2.destroyAllWindows()