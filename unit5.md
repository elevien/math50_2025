---
title:  Unit 5 
layout: page
bibliography:
- refs.bib
---


# Nonlinear models with OLS and model building

As I say many times in class, the linear regression model is the basis for many other models in statistics and machine learning. In this unit we will begin to see how the basic linear regression model can take us beyond strict linear relationships, starting by adding **interactions** to regression models. These occur when the effect of one predictor depends on the values of the others (a key assumption of the linear regression models studied this for). We can include these by adding products of predictors to our model. Using a similar idea, we can model any nonlinear relationship in principle. This is the idea of **feature space** in machine learning.  This allows us to build much more complex models and with that comes concerns about **overfitting**. To this end, we will investigate the tradeoffs that arrise when building complex regression models. I will also use this unit as an oportunity to introduce **logistic regression.** 

Material: 
- [Notes and exercises](/public/latex_notes/unit5/unit5.pdf)
- [Colab notebook]()

# Concepts
Interactions, Residual plots and diagnostics (interaction detection), Nonlinear models within the linear framework/(focusing on polynommials), Cross validation, test/training data and overfitting. 

# Things to practice
- Write Python codes that determines whether you can detect a given interaction with a given amount of data. 
- Make residual plots and identify what might be wrong with a model. 
- Be able to convert nonlinear modeling goals into a linear‑in‑parameters form using basis functions. Fit in Python. 
- Exploratory data analysis: Find a dataset and try to answer some questions about it. 
- Basic model‑building workflow

# Wikipedia References
- [Interaction (statistics)](https://en.wikipedia.org/wiki/Interaction_(statistics))
- [Polynomial regression](https://en.wikipedia.org/wiki/Polynomial_regression)
- [Basis function](https://en.wikipedia.org/wiki/Basis_function)
- [Residual (statistics)](https://en.wikipedia.org/wiki/Residual_(statistics))
- [Overfitting](https://en.wikipedia.org/wiki/Overfitting)
