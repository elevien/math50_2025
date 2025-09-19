---
title: Unit 3
layout: page
nav_order: 3
bibliography:
- refs.bib
---

# Statistical inference for linear regression models

This unit introduces statistical inference for **single‑predictor linear regression**.  In this context, we will learn all the basics of linear regression modeling and statistical inference, including: to fit an OLS line, quantify uncertainty in estimates via **standard errors**, **confidence intervals**, and **hypothesis tests**. We will also learn about **estimators** and **bias–variance tradeoffs**. While the mathematical details of these topics could take an entire course, we will focus on building intuition with numerical experiments in Python and rules of thumb. You will not need to learn the formula for t distributions of chi-squared, only where these things come from and when/why they matter. 

Material: 
- [Notes and exercises](/public/latex_notes/unit3/unit3.pdf)
- [Colab notebook (2024)](https://colab.research.google.com/drive/1_4zOruAWfJ3HQoIf9sjefk3z0APko94-?usp=sharing)

# Concepts
Estimators, bias and consistency, Linear regression (single predictor) model and assumptions, Covariance, correlation and their relationship to regression slope. Least squares interpretation of covariance formula. Hypothesis testing for regression models. 


# Things to practice
- Identify whether a simple estimator is biased or not, by hand if possible, or using simulations in Python.  
- Use the CLT to approximate the sample distribution of an estimator. 
- Stating the assumptions of a linear regression model and identify (e.g. based on plots) when they are invalid. 
- Be able to explain the phenomona of regression to the mean. 
- Interpret the output of a fitted linear regression model and access the goodness of fit. 
- Recalling the basic facts quantities such as $p$-values and $R^2$ depend on the sample size. 

# Wikipedia References
- [Linear regression](https://en.wikipedia.org/wiki/Linear_regression)
- [Estimator](https://en.wikipedia.org/wiki/Estimator)
- [Bias variance trade-off](https://en.wikipedia.org/wiki/Bias%E2%80%93variance_tradeoff)
- [Ordinary least squares (OLS)](https://en.wikipedia.org/wiki/Ordinary_least_squares)
- [Covariance and correlation](https://en.wikipedia.org/wiki/Covariance_and_correlation)
- [Maximum likelihood estimation (optional)](https://en.wikipedia.org/wiki/Maximum_likelihood_estimation)
- [Confidence interval](https://en.wikipedia.org/wiki/Confidence_interval)
- [Statistical hypothesis testing](https://en.wikipedia.org/wiki/Statistical_hypothesis_testing)
- [Regression toward the mean](https://en.wikipedia.org/wiki/Regression_toward_the_mean)