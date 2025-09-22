---
title:  Unit 4
layout: page
bibliography:
- refs.bib
---


# Linear regression with multiple predictors

This unit covers linear regression with **multiple predictors**. Many new ideas emerge when we add more predictors. Importantly, regression coefficients need to be interpreted as average differences with all other predictors fixed.  The relationship between predictors therefore plays a very important role, and after this unit you should understand how adding and removing regression coefficients influences the others. We will talk about the joint sample distribution of regression coefficients and **collinearity**. An emphasis will be placed on different ways of understanding these things (linear algebra vs. geometry) and as always, experimentation with numerical simulations. We will also introduce the idea of **categorical predictors**, which allow us to handle qualitative data and discuss a common method called **analysis of variance** as a regression model. 

Material:
- [Notes and exercises](/public/latex_notes/unit4/unit4.pdf)
- [Colab notebook (2024)](https://colab.research.google.com/drive/1oIRgP_7-c5DGV1D2iz5nj406mZfJxUIG?usp=sharing)

# Concepts

Regression with multiple predictors, covariance matrix, Simpson's paradox, collinearity, $F$-tests, catagorical predictors and dummy variables, analysis of variance
  

# Things to practice
- Derive a linear system involving the regression coefficients for the covariances (generalizing what I do in class)
- Interpret the output of a fitted model with multiple predictors (including with qualitative predictors) 
- Predict how adding a predictor to a model will change the regression coefficient of an existing predictor (given knowledge about predictors).
- Identify symptoms of colinearity
- Translate ANOVA to regression language

# Wikipedia References
- [Multiple linear regression](https://en.wikipedia.org/wiki/Multiple_linear_regression)
- [Ordinary least squares (OLS)](https://en.wikipedia.org/wiki/Ordinary_least_squares)
- [Multicollinearity](https://en.wikipedia.org/wiki/Multicollinearity)
- [Covariance and correlation](https://en.wikipedia.org/wiki/Covariance_and_correlation)
- [Variance inflation factor](https://en.wikipedia.org/wiki/Variance_inflation_factor)
