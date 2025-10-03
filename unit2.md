---
title: Unit 2
layout: page
bibliography:
- refs.bib
---

# Expectation, Continuous probability, CLT and Normal models

In this section we introduce **expectation**, an operation which takes a random variable and produces a deterministic quantity. The expectation of a random variable can be approximated with **sample averages**, and from them we can infer properties of the model (like parameters). Much of statistics relies on the fact that sample averages approximate expectations, and understanding how well these approximations work is a central goal of statistics. This will motivate us to study the probability distribution of sums of random variables, which leads to the **CLT** and the **Normal distribution**.  By defining joint distribution where the conditionals are Normal, we will arrive at our first example of a **linear regression** model. We will study a linear regression model with a binary predictor and introduce the idea of a sample distribution in this context. 


Material: 
- [Notes and exercises](/public/latex_notes/unit2/unit2.pdf)
- [Colab notebook from class (2024)](https://colab.research.google.com/drive/1k3oTeSMmCrrNZ2z4P3EDGyzZONJAl1ZI?usp=sharing)
- [Colab notebook from class (2025)](https://colab.research.google.com/drive/1JMI1T8a2nk06Q3L6ZFpkYZGV4GIzk7dG?usp=sharing)

# Concepts

Expectation, conditional expectation, empirical averages, CLT, Normal random variables and their properties, coefficient of variation, sample distribution, linear regression model

# Things to practice

- Calculate expectations by hand and in Python (including conditional expectations)
- Manipulate normal random variables  (appling linearity of expectation and independence)
- How to use CLT to estimate probabilities of sums
- For a linear regression model with a binary predictor, understand how to estimate the regression coefficient as difference of conditional averages and derive the sample distribution (make sure you understand Example 12)
  

# Wikipedia References

- [Expectation](https://en.wikipedia.org/wiki/Expected_value)
- [Conditional expectation](https://en.wikipedia.org/wiki/Conditional_expectation)
- [Coefficient of variation](https://en.wikipedia.org/wiki/Coefficient_of_variation)
- [Law of large numbers](https://en.wikipedia.org/wiki/Law_of_large_numbers)
- [Sampling distribution](https://en.wikipedia.org/wiki/Sampling_distribution)
- [Central limit theorem](https://en.wikipedia.org/wiki/Central_limit_theorem)
- [Log Normal distribution](https://en.wikipedia.org/wiki/Log-normal_distribution)
