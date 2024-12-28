
# Edge Detection

This project showcases two different approaches for edge detection:

    1. Canny Edge Detection (Implemented in Python)

    2. Fuzzy Evolutionary Algorithm for Edge Detection (Implemented in MATLAB


## Canny Edge Detection

Canny Edge Detection is a multi-step algorithm used to detect edges in images by reducing noise and identifying gradients. This implementation includes Gaussian filtering, gradient computation, non-maximum suppression, double thresholding, and edge tracking using hysteresis.

### Features:

1. **Gaussian Filtering:** Reduces noise in the image.

2. **Gradient Computation:** Uses Sobel filters to compute gradients in both horizontal and vertical directions.

3. **Non-Maximum Suppression:** Identifies the most prominent edges by comparing gradient magnitudes.

4. **Double Thresholding:** Classifies edges as strong, weak, or non-edge.

5. **Edge Tracking:** Connects weak edges to strong edges to complete edge detection.
## Fuzzy Evolutionary Algorithm for Edge Detection

This technique uses fuzzy logic to detect edges in images. Fuzzy logic models the uncertainty and handles edge detection based on the gradients of the image.

### Features:

* **Input Membership Functions:** Gaussian membership functions are defined for gradient values in the x and y directions.

* **Output Membership Functions:** Triangular membership functions classify pixels as either edge (black) or non-edge (white).

* **Fuzzy Rules:** Two fuzzy rules are defined:

    1. If both gradients are zero, the pixel is classified as white (non-edge).

    2. If either gradient is non-zero, the pixel is classified as black (edge).

* **Edge Detection:** Evaluates the fuzzy rules for all pixels to determine edges.
## Comparison

| Feature              | Canny Edge Detection        | Fuzzy Evolutionary Algorithm |
|----------------------|-----------------------------|------------------------------|
| Noise Reduction      | Gaussian Filter            | Not explicitly handled       |
| Gradient Computation | Sobel Operator             | Convolution with [-1, 1] and [-1; 1] |
| Edge Classification  | Thresholding and Hysteresis| Fuzzy Logic                  |
| Customizability      | Low                        | High                         |
| Complexity           | Moderate                   | High                         |

## Conclusion

This project demonstrates two distinct approaches for edge detection. While the Canny algorithm provides a systematic and widely used approach, the fuzzy evolutionary algorithm offers a customizable and intuitive method for edge detection. Each method has its own advantages and can be chosen based on the application's requirements.
