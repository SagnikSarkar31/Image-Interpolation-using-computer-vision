import cv2
import numpy as np

def cubic(x):
    x = abs(x)
    if x <= 1:
        return (1.5 * x**3 - 2.5 * x**2 + 1)
    elif 1 < x < 2:
        return (-0.5 * x**3 + 2.5 * x**2 - 4 * x + 2)
    else:
        return 0


def bicubic_interpolation(image, new_width, new_height):
    original_height, original_width = image.shape[:2]

    resized = np.zeros((new_height, new_width, 3), dtype=np.uint8)

    x_scale = (original_width - 1) / (new_width - 1)
    y_scale = (original_height - 1) / (new_height - 1)

    for i in range(new_height):
        for j in range(new_width):
            x = j * x_scale
            y = i * y_scale

            x_int = int(x)
            y_int = int(y)

            dx = x - x_int
            dy = y - y_int

            pixel = np.zeros(3)

            # 4x4 neighborhood
            for m in range(-1, 3):
                for n in range(-1, 3):
                    xm = min(max(x_int + m, 0), original_width - 1)
                    yn = min(max(y_int + n, 0), original_height - 1)

                    weight = cubic(m - dx) * cubic(dy - n)
                    pixel += image[yn, xm] * weight

            # Clip values to valid range
            resized[i, j] = np.clip(pixel, 0, 255)

    return resized


image = cv2.imread("bnw.jpg")

new_width = image.shape[1] * 2
new_height = image.shape[0] * 2

resized_image = bicubic_interpolation(image, new_width, new_height)

cv2.imwrite("bicubic_interpolated.jpg", resized_image)

print("Saved as bicubic_interpolated.jpg")

cv2.imshow("Original", image)
cv2.imshow("Bicubic", resized_image)

cv2.waitKey(0)
cv2.destroyAllWindows()