---
layout: default
title: Additional practice problems
---

# Practice Problems for Exam 1



## 1. Expectation and Simulation

Suppose \( X \) is a random variable that takes values 1, 2, or 3 with probabilities \( P(X=1)=0.2 \), \( P(X=2)=0.5 \), and \( P(X=3)=0.3 \). Let \( Y = 2X + 1 \).

- (a) Compute \( E[Y] \) and  \( E[Y|X>1] \). 
- (b) Write a Python function ``simulate_model(n)`` that ``n`` samples of \( X \). 
- (c) Use your function to compute the expectation \( E[Y|Y>1] \) empirically.

---



## 2. Implement a geometric distribution and test variance formula

A geometric distribution (which we did not cover formally) is defined as follows:  
Let \( Y \) be the number of Bernoulli trials until the first success. That is, if $X_1,X_2,X_3,...$ are iid Bernoulli trials with probability of success $q$, then $Y$ is the minimum value of $i$ such that $X_i =1$. 
The variance of \( Y \) is known to be \({\rm var}(Y) =\frac{1-q}{q^2} \).

- (a) Write a function to generate ``geometric(q,n)`` that generates ``n`` simulations of a geometric random variable. 
- (b) Explain (in words, without writing any code) how you could use this function to test the formula for the variance above. In particular, (i) describe what type of dataset you would generate and (ii) a plot you could make to compare it to the formula. 

---

## 3. Central Limit Theorem

Suppose 



