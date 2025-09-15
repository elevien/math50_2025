---
title: Project
layout: page
bibliography:
- refs.bib
---

# Overview


## Introduction

The project will be due on **November 22nd before midnight**.

The goal of the project is to apply what you've learned to a realy world setting; that is, to use statistics to say something new about the real world! 
It will include (at least one) Python notebook and a **2–3 page** report. You can work in a group of up to 3, but you will all get the same grade on the project portion. Your report should be **single spaced, 12pt font with 1-inch margins**. Your report will be graded out of 100 points and your grade is **roughly** based on the following:

## Midterm update (5% of total project grade)

Your update, to be submitted after the first mideterm, should consist of 1 or 2 paragraphs describing your plan and what you have achieved so far. At this point you should have reached step 3 described below. I expect that everyone who submits an update will recieve full credit, and the point is more for me to intervene if I am worried about directin or rate of progress. 



## Final report (95% of total project grade)

This is only a rough rubric. Due to the variability in approaches taken and topics, it is difficult to adhere to a single rubric. 
- **Overall writing quality:** Your report should be clearly written and include citations of any literature beyond the main paper which you referenced (10%). I don't care about the format of references, but I should be able to easily find them. 
- **Introduction:** Summarize the literature on the topic you are studying in 2–4 paragraphs, making an effort to connect it to what we've covered in class (10%).
- **Results:** This section will vary a lot depending on whether your project is more pedagogical or presents new research results, but either way it should contain some technical details. You should use a probability model beyond a single-predictor linear regression.  (50%)
- **Code:** You should write some Python code to accompany your report and link to your Colab notebook. **Remember to give me permission to view it!** For example, you might simulate a model discussed in the article (20%).
- **Discussion:** You should pose at least one question or future direction which is not raised or answered in the articles, or you should suggest an approach for a question which is raised. (10%)



# How to Select a Good Term Project

## Step 1: Identify a Specific Question  
Choose a concrete topic or question that genuinely interests you. The more specific your question, the easier the next steps will be.  

Your project should fall within the **regression framework**: there should be **predictors (X)** and a **response variable (Y)**. Within this framework, there are two broad types of goals:  
- **Prediction:** Can we accurately predict \( Y \) from \( X \)?  
- **Causal inference:** How does changing \( X \) affect \( Y \)? (Even causal questions ultimately reduce to prediction)  

Examples of possible questions include:  
- How does infant diet influence longevity?  
- Can statistical indicators predict when a government is about to collapse?  
- How does Spotify use machine learning to generate playlists?  



---

## Step 2: Find Relevant Literature  
Search for academic papers related to your topic. Aim to identify one or two papers that closely align with your interests. At this stage, don’t worry too much about technical details or whether the methods directly connect to our course. Focus on the *scientific question* first.  

**Note:** Many students want to start with a dataset. I strongly encourage you to begin with literature instead. One major goal of the project is to practice reading and engaging with published research. Doing so will push you beyond the specific examples we cover in class. In contrast, students who begin with only a dataset often end up producing something that looks more like a homework exercise than a research project.  

---

## Step 3: Engage with the Paper  
When you read the paper, one of two outcomes is likely:

1. **Direct Connection to the Course**  
   - If the methods overlap with what we study, try to reproduce the results.  
   - As you do this, you will encounter challenges, ambiguities, or choices the authors made. Documenting and reflecting on these issues, alongside reproducing results, makes for a strong project.  

2. **Use of More Complex Methods**  
   - Often, papers use advanced techniques (e.g., support vector machines, multilevel models).  
   - Before diving into the paper itself, find accessible resources that explain the method.  
   - Once you understand the method, connect it to concepts from class. Ideally, you also relate it back to the original paper, but a project focused on a method not covered in class is also acceptable.

---

## Iterating on Your Idea  
It’s normal to go through the cycle (Step 1 → Step 2 → Step 3) and decide you’re not satisfied with your direction. If this happens, repeat the cycle once more. By the second round, I recommend committing to what you’ve found.

---

## Evolving with the Course  
When you start your project, we won’t yet have covered all the core ideas I expect you to connect with. Ideally, your understanding of the paper should develop alongside the course. As we study topics like the bias–variance tradeoff, think about how they appear in the context of your chosen application.