---
title:  Unit 6
layout: page
bibliography:
- refs.bib
---


# Overparameterized models: Regularization, priors and Bayesian inference

At this point we have seen that models can be too complicated, but thus far **complexity** has roughly meant the number of parameters (regression coefficients). Striking a balance between bias and variance means finding the right number of predictors to include, but there are ways to build highly flexibly models which do not overfit.

Material: 
- [Notes and exercises](/public/latex_notes/unit6/unit6.pdf)
- [Colab notebook]()

# Concepts
Regularization for regression models, Priors, Laplace rule of succession, Bayes rule, posterior distributions, how priors influence the posterior for simple models, connection between regularization and priors. 

# What you need to know
- How to select and justify priors (using Normal probabilities or lognormal)
- For estimating the sample mean, be able to calculate the influence of a given regularization of the least squares estimator by hand
- Implement regularization in Python and have back of the envelope idea of the effects on regression coefficients. 
- Be able to translate priors to regularization for ridge regression (and vice versa)


# Wikipedia References

- [Regularization (mathematics)](https://en.wikipedia.org/wiki/Regularization_(mathematics))  
- [Bayesian inference](https://en.wikipedia.org/wiki/Bayesian_inference)  
- [Prior probability](https://en.wikipedia.org/wiki/Prior_probability)  
- [Rule of succession](https://en.wikipedia.org/wiki/Rule_of_succession)  
- [Ridge regression](https://en.wikipedia.org/wiki/Ridge_regression)  
- [Lasso (statistics)](https://en.wikipedia.org/wiki/Lasso_(statistics))  