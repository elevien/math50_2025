---
layout: page
title: Exam study guide
---

## Midterm 

The midterm will cover Units 1, 2 and 3. Here are some things you absoutely need to know

#### Overview
- The only distributions you need to know about are Bernoulli, Binomial (don't need to know binomial formula) Uniform and Normal
- How to calculate conditional probability, marginal probability, expectations given a probability distribtion. Same with expectations/conditional expectations. Problems here you have to calculate these things by hand will involve discrete random variables.  
- Understand what the LLN and CLT are saying and their significance for statistical inference. 
- Be able to work with Normal random variables (in the sense of adding them ad estimating probabilities given a table or the bell curve)
- Basic concepts of statistical inference: Sample distribution, bias, consistency. Be able to tell if a (simple) estimator is biased. 
- Basics ideas of regression modeling: What are the assumptions assumptions? Relationship between covariance, correlations, R-squared. Derive formula for these. 

#### Python
In terms of Python, you need to know enough syntax to identify what a line or two of codes does. I will NOT ask about plotting syntax or constructing dataframes (you may be asked to compute something given a data frame).  More specifically: 
  - Basic logic: You should know the syntax for if statements and for loops; however the questions on the midterm will mostly focus on things directly related to statistics/probability.  
  - How to generate random numbers using ``np.random.choice`` and ``np.random.normal``. If I give you a probability model in the form such as 
  \begin{align}
  X \sim {\rm SomeDistribution}\quad Y | X &\sim {\rm SomeDistribution}
  \end{align} you should be able to write a function which returns samples from this distribution (as numpy arrays). It's a good idea to look at every probability model in the exercises and try to impelement in Python.  
  - How to index 1D arrays, compute their lengths (I will not ask about multidimensional arrays). This will mostly be relavent in the context of estimating conditional probabilities: For example, if you are given a dataframe ``df`` and tell you the rows are samples from some probability model, I might ask to estimate a conditional or/and marginal probability. 
  - Describe how to do something in Python but not write out the exact code. For example, I might ask you to describe how you would check whether a given formula (say the variance of some sample distributio) is correct, and the anwer can be in words: "I would first generate a function which returns the samples as a dataframe, then run this function for different $N$, etc..."

### Practice problems
- You should go through all the problems in the Unit 1,2 and 3 notes. Espcially those marked with ❐.
- [Practice midterm from 2024]({{ '/public/exam_practice/midterm_practice_2024.pdf' | relative_url }}) (ignore problem 5)
- [Midterm from 2024]({{ '/public/exam_practice/midterm_2024-10.pdf' | relative_url }})
- [Midterm from 2025 #1]({{ '/public/exam_practice/math50_midterm_practice_2025.pdf' | relative_url }})
- [Midterm from 2025 #2]({{ '/public/exam_practice/math50_midterm_practice_2025_2.pdf' | relative_url }})
- [Midterm review problems]({{ '/public/exam_practice/math50_midterm_review_problems.pdf' | relative_url }})
<!-- - [Additional practice problems]({{ '/public/exam_practice/midterm_practice_problems' | relative_url }}) -->


## Final 

The final is cumulative and includes everything on the midterm, plus Units 4-7 (ending with whatever material we cover on Friday Nov 7.)  

You will need to: 

- Given a linear regression model, state the interpretation of the regression coefficients. 
- Understand the relationship between covariances and regression coefficients and be able to derive the marginal distribution of response variable
- Be able to swap $X$ and $Y$ in linear regression model. 
- Know the effects of adding a predictor to the model. For example, be able to predict how it will change another regression coefficient given the correlation with existing predictors. 
- Know what Simpson's paradox is and when it occurs. 
- Interpret the output of a fitted model: Which effects are significant, what does $R^2$ mean. 
- Know how to include categorical variables in a linear regression model and their interpretation
- Understand the interpretation of interaction terms. Be able to identify the value of an interaction and whether there may be one from a residual plot. 
- Understand the idea of feature maps and orthogonal features. Identify whether two features are orthogonal by plotting them. 
- Know how to compute MSE and understand bias-variance tradeoff curves. 
- Understand the conceptual difference between Bayesian and frequentist statistics. Understand calculation of posterior for Bernoulli model (with Uniform priors) and Normal model (with Normal prior and known variance). DON'T MEMORIZE FORMULAS. Focus on understanding derivations. I may ask about a step in the derivation or how to set it up. 
- Calculate regularized estimators and relationship to Bayesian inference (for example for the sample mean where this can be done by hand)
  
There may be some extra credit questions from Unit 7, depending on how much time we have at the end of the term.


### Practice exam
- [Final from 2024]({{ '/public/exam_practice/final_2024C.pdf' | relative_url }}) (ignore the red text in the instructions. Do all problems).
- [Practice Final]({{ '/public/exam_practice/final_practice.pdf' | relative_url }})
- [Practice Problems]({{ '/public/exam_practice/final_additional_practice_problems.pdf' | relative_url }})