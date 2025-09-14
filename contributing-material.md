---
layout: page
title: Contributing to course material
---


Extra credit will be given to students who make contributions to the course material. Participating in expanding and improving the course material is a great way to practice the skills you have learned. Because this is done through GitHub pull requests (see below), it is also a way to practice (in a low-stakes setting) contributing to a public code repository. This is a very desirable skill in the job market. Employers often ask to see your Github account, even for non-engineering jobs. 

[Here](https://github.com/elevien/math50_2025) is the link to the github repository for this site. 

You can find more detailed information about [pull requests](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests) on GitHub. Here is a quick guide.

## How to Make a Pull Request on GitHub (without creating a local fork)

1. Go to [https://github.com](https://github.com). Click **Sign up** in the top-right corner and create an account. 
2. Once logged in, go to the course repository. 
3. At the top of the repository page, click the branch dropdown (it usually says `main` or `master`). Type in a new branch name that describes your change (e.g., `fix-typo`, `add-example`). Press **Enter** to create the new branch.
4. Edit files directly on GitHub:
   1. Navigate to the file you want to change.  
   2. Click the pencil icon (**Edit this file**).  
   3. Make your changes in the browser.  
   4. Scroll down, write a clear commit message, and choose **Commit directly to the new branch**.  
5. After committing your changes, GitHub will prompt you to create a pull request.  
   - If you don’t see the prompt, click the **Pull requests** tab and then **New pull request**.
6. Ensure that:
   - The **base branch** is `main` (or the default branch of the repo).  
   - The **compare branch** is your new branch.
7. Add a descriptive title and a detailed description of your changes (e.g., “fixed typo in Unit 3 Exercise 4” or “added example to Unit 8”). 
8. Click **Create pull request**.
9. Wait for my review. I may not end up merging your changes for various reasons. For example, you might come up with a good problem, but it is too difficult or not aligned with the flow of the course. I will still give you credit if there is meaningful effort.

# Organization of this repository

This repository is organized to make it easy to find and contribute to course materials:

- **unitX.md**: Main markdown files for each unit, containing lecture notes and exercises.
- **_posts/**: Contains blog-style posts and unit folders for additional materials.
- **public/latex_notes/**: Contains LaTeX source files and compiled PDFs for lecture notes and slides. **This is the most important folder for contributing.** 
- **public/**: Contains static assets (images, CSS, JavaScript) and generated site files.
- **_includes/** and **_layouts/**: Jekyll template files for site structure and navigation. This you most likely will not be editing. 
- **schedule.md, exams.md, project.md**: Pages for the course schedule, exam info, and project instructions.

