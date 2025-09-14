---
layout: page
title: Exam study guide
---

## Midterm 

The midterm will cover Units 1, 2 and 3. Here are some things you absoutely need to know

- Distributions: Bernoulli and Normal
- How to calculate conditional probability, marginal probability, expectations given a probability distribtion.  
- How to estimate probabilities of sums using the CLT. You will be given a table if needed. 
- Know the rules for manipulating Normal random variables (adding them, multiplying by constants)
- Be able to identify whether data is normal based on visual inspection. 
- In terms of Python, you need to know enough syntax to identify what a line or two of codes does. I will NOT ask about plotting syntax or dataframes.  I may ask about
  - Basic logic: If statements and for loops 
  - How to generate random numbers using ``np.random.choice`` and ``np.random.normal``. 
  - How to index 1D arrays, compute their lengths (I will not ask about multidimensional arrays)
  - How to translate probability statements, such as a conditional probability into Python code. 
  - Describe how to do something in Python but not write out the exact code. 

### Practice exam
- [Practice midterm from 2024]({{ '/public/exam_practice/midterm_practice_2024.pdf' | relative_url }})
- [Midterm from 2024]({{ '/public/exam_practice/midterm_2024-10.pdf' | relative_url }})


## Final 

The final is cummulative and includes everyhing on the midterm, plus Units 4-7 (ending with whatever material we cover on Friday Nov 7.)  

You will need to: 

- Given a linear regression model, state the interpretation of the regession coefficients. 
- Be able to calculate the marginal variance (if the predictor distribution is given)
- Know the effects of adding a predictor to the model. For example, be able to predict how it will change another regression coefficient given the correlation with existing predictors. 
- Know what Simpson's paradox is and when it occurs
- Understand what happens when we flip the axes in a regression model
- Interpret the output of a fitted model: Which effects are significant, what does $R^2$ mean. 
- Know how to include catagorical variables in a linear regression model and their inerpretation
- Calculate regularized estimators (for example for the sample mean where this can be done by hand)
  
There may be some extra credit questions from Unit 7, depending on how much time we have at the end of the term.

### Practice exam
- [Final from 2024]({{ '/public/exam_practice/final_2024C.pdf' | relative_url }})