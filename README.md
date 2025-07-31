This project implements polynomial least squares approximation for given data points using the Cholesky decomposition method to solve the normal equations.

Description
The function Opalka_Emilia_MNK takes data points (x, y) and the desired polynomial degree n as input and returns the coefficients of the approximating polynomial. It also plots the original data points alongside the fitted polynomial curve.The method is based on solving the system of normal equations using the Cholesky decomposition of a symmetric positive-definite matrix, which improves numerical stability.

Used libraries: numpy, matplotlib

Conclusions
Increasing the polynomial degree improves fit accuracy but may cause oscillations between data points (Runge's phenomenon).
Lower-degree polynomials offer more stable and generalized models, even if they don't pass exactly through all points.
