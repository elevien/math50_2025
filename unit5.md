---
title:  Unit 5 
layout: page
bibliography:
- refs.bib
---


# Nonlinear models with OLS and model assessment

As I say many times in class, the linear regression model is the basis for many other models in statistics and machine learning. In this unit we will begin to see how the basic linear regression model can take us beyond strict linear relationships, starting by adding **interactions** to regression models. These occur when the effect of one predictor depends on the values of the others (a key assumption of the linear regression models studied this far). We can include these by adding products of predictors to our model. Using a similar idea, we can model any nonlinear relationship in principle. This is the idea of **feature space** in machine learning.  This allows us to build much more complex models and with that comes concerns about **overfitting**. To this end, we will investigate the tradeoffs that arise when building complex regression models. 

Material: 
- [Notes and exercises](/public/latex_notes/unit5/unit5.pdf)
- Contribution to Unit 5 Practice Problems for Extra Credit by Daniel Hernandez [Math_50_Unit_5_Problem_Contributions_for_Extra_Credit__Daniel_Hernandez.pdf](https://github.com/user-attachments/files/23730864/Math_50_Unit_5_Problem_Contributions_for_Extra_Credit__Daniel_Hernandez.pdf)
- [Colab exercise solutions](https://colab.research.google.com/drive/1StwGhDHL4BFMx4_y1LY3B5BVUUpuwqjl?usp=sharing)
- [Colab notebook: interactions](https://colab.research.google.com/drive/1JVq9VHAbpSlGlngfMmf9N4NJuSKM8lKR?usp=sharing)
- [Colab notebook: Polynomial regression and bias-variance](https://colab.research.google.com/drive/1UuydrSV7Q7-O-ZyjBUGT-mOzo9NUFD3P?usp=sharing)
- [Colab notebook: Fourier models](https://colab.research.google.com/drive/1jIuaN8kWyb9Wp08yhatmWmetq3LwaJMH?usp=sharing)

# Concepts
Interactions, Residual plots and diagnostics (interaction detection), Nonlinear models within the linear framework/(focusing on polynomials), Cross validation, test/training data and overfitting. 

# Things to practice
- Using residual plots to identify nonlinearities in a model 
- Extend calculations we have done (e.g. marginal response variable variance, regression coefficients in terms of covariances) to simple nonlinear models. 
- Be able to convert nonlinear modeling goals into a linear‑in‑parameters form using basis functions. Fit in Python. 
- Understand the distinction between training and test error
- Explain intuitively the idea behind bias variance tradeoff
- Basic model‑building workflow

# Wikipedia References
- [Interaction (statistics)](https://en.wikipedia.org/wiki/Interaction_(statistics))
- [Polynomial regression](https://en.wikipedia.org/wiki/Polynomial_regression)
- [Basis function](https://en.wikipedia.org/wiki/Basis_function)
- [Residual (statistics)](https://en.wikipedia.org/wiki/Residual_(statistics))
- [Overfitting](https://en.wikipedia.org/wiki/Overfitting)
