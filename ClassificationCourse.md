---
title: Statistical Learning and Classification
description: This is a homepage for MAT434, Statistical Learning and Classification, with Dr. Gilbert at Southern New Hampshire University. This course introduces students to the construction, assessment, and interpretation of models in the classification setting. Depending on student interest, applications in computer vision, natural language processing, and/or deep learning are also explored.
---

{% include google-analytics.html %}

## MAT 434 - Statistical Learning and Classification

<img src="/SiteFiles/ISLR.png" align="left" width=200>[**Tentative Syllabus (Fall 2023)**](https://drive.google.com/file/d/1W6sLmFZ0tkIPkqqo5nfSIusywC8R2zL-/view?usp=sharing)<br/>
<br/>
***Course Description:*** Using the foundational knowledge built in MAT 241 and MAT 300, we continue our study of statistical models. This course moves beyond regression and into classification models, mixed models, and unsupervised learning. Like MAT300, this course also emphasizes cross-validation as an important method for  hyperparameter tuning, identifying appropriate levels of model flexibility, approximating future model performance, and analyzing the utility of a model. This course covers discriminant analysis, k nearest neighbors, tree-based methods (bagging, boosting, and random forests), support vector machines, and neural networks.<br/>
<br/>

### Course Timeline and Notebooks

Below is a tentative timeline for our course. The schedule and topics are a draft, and this is subject to significant change. The table includes (or will include) preparatory work that should be done prior to each class meeting, a detailed set of notes corresponding to each class meeting, and assignments following each class meeting. The prepared notebooks use IDENTIFY DATASET TO USE and are provided so that you have a detailed account of each topic we discuss. We'll learn this content better by *doing* it than we will by simply *reading* and *running* pre-existing code, so we'll plan to utilize different data in class. For now, I'm planning to start with IDENTIFY SECONDARY DATASET that I hope you'll use to follow along during our in-class discussions. 

| Class Meeting | Dataset | Before Class | During Class | After Class |
|---------------|--------------|--------------|--------------|-------------|
| 1 |  | i) [Review Syllabus](https://drive.google.com/file/d/1V6PKm13JjhWp4BjsRyCOQjK2ZtQioRe1/view?usp=share_link) <br/> ii) [Software Setup](https://agmath.github.io/ClassificationCourse/SoftwareSetup.html) |  i) Introduction and What to Expect <br/> ii) Ethics and Data Models | **Homework** -- Complete Software Setup |
| 2 | [FAA Airstrikes and Engine Damage](https://www.kaggle.com/competitions/sliced-s01e02-xunyc5/data), or <br/> [MLB Hits and Homeruns](https://www.kaggle.com/competitions/sliced-s01e09-playoffs-1/data?select=train.csv) | Ensure that `git` is working from RStudio | i) [R Projects and Version Control](https://agmath.github.io/ClassificationCourse/x_RprojectsVersionControl.html) <br/> ii) Tidy Analyses in R ([new students](https://agmath.github.io/ClassificationCourse/Day2_TidyAnalyses_newStudents.html) or [returning students](https://agmath.github.io/ClassificationCourse/Day2_TidyAnalyses_returningStudents.html)) | **Homework** -- <br/> i) Commit to Your Repository <br/> ii) Enroll in Class Kaggle Competition |
| 3 |  |  | [R Markdown, inline commands, and semi-automated reporting](https://agmath.github.io/ClassificationCourse/Day3_RMarkdown_InlineR.html) | **Homework** -- Update your Tidy Analysis notebook with inline R code to enhance your discussions. |
| 4 |  | [EDA and `ggplot` Review](https://agmath.github.io/ClassificationCourse/x_DataViz_Primer.html) |  EDA and Data Viz | **Competition Assignment** -- Write a Statement of Purpose and conduct an Exploratory Data Analysis using our Zillow Price-Range Competition data. | 
| 5 |  | Setup a `username.github.io` Repository | [GitHub Pages and a public-facing portfolio](https://agmath.github.io/ClassificationCourse/Day5_GitHubPages.html) | **Homework** -- Add a short bio to your page, include subsections on projects you've worked on, and include links to any work-products you'd like to share.
| 6 |  | [`tidymodels` Framework (Review)](https://agmath.github.io/ClassificationCourse/x_ModelingFrameworkAndTidymodelsReview.html) | [`tidymodels` Framework Example](https://agmath.github.io/ClassificationCourse/x_TidymodelsExample.html) |  |
| 7 |  |  | Regression Versus Classification and Performance Metrics for Classifiers ([html](https://agmath.github.io/ClassificationCourse/Day7_RegressionVersusClassification.html) or [rmd](https://agmath.github.io/ClassificationCourse/Day7_RegressionVersusClassification.Rmd)) |  |
| 8 | [Spaceship Titanic](https://raw.githubusercontent.com/agmath/agmath.github.io/master/data/classification/spaceship_titanic.csv) | Intro to Logistic Regressors ([html](https://agmath.github.io/ClassificationCourse/Day8b_LogisticRegression_Intro.html) or [rmd](https://agmath.github.io/ClassificationCourse/Day8b_LogisticRegression_Intro.Rmd)) | Binary Classifiers, Part I: Logistic Regression |  |
| 9 |  | Intro to Support Vector Classifiers ([html](https://agmath.github.io/ClassificationCourse/Day9b_SupportVectorMachines_Intro.html) or [rmd](https://agmath.github.io/ClassificationCourse/Day9b_SupportVectorMachines_Intro.Rmd)) | Binary Classifiers, Part II: Support Vector Machines |  |
| 10 | [Gene Expression and Cancerous Tumors](https://archive.ics.uci.edu/ml/datasets/gene+expression+cancer+RNA-Seq) | Intro to Principal Component Analysis ([html](https://agmath.github.io/ClassificationCourse/Day10b_PrincipalComponentAnalysis_Intro.html) or [rmd](https://agmath.github.io/ClassificationCourse/Day10b_PrincipalComponentAnalysis_Intro.Rmd)) | Aside: High-Dimensional Data and Dimension Reduction |  |
| 11 | [Healthcare Analytics: Length of Stay](https://www.kaggle.com/datasets/nehaprabhavalkar/av-healthcare-analytics-ii) | Intro to k Nearest Neighbors ([html](https://agmath.github.io/ClassificationCourse/Day11b_KNN_Intro.html) or [rmd](https://agmath.github.io/ClassificationCourse/Day11b_KNN_Intro.Rmd)) | Multiclass Classifiers, Part I: Nearest Neighbors |  |
| 12 |  | Intro to Decision Trees ([html](https://agmath.github.io/ClassificationCourse/Day12b_DecisionTreeClassifiers_Intro.html) or [rmd](https://agmath.github.io/ClassificationCourse/Day12b_DecisionTreeClassifiers_Intro.Rmd)) | Multiclass Classifiers, Part II: Decision Tree Classifiers |  |
| 13 |  | Intro to Ensembles, Bagging, and Random Forests ([html](https://agmath.github.io/ClassificationCourse/Day13b_EnsemblesBaggingAndRandomForests_Intro.html) or [rmd](https://agmath.github.io/ClassificationCourse/Day13b_EnsemblesBaggingAndRandomForests_Intro.Rmd)) | Ensembles, Part I: Bagging and Random Forests |  |
| 14 |  | Intro to Boosting ([html](https://agmath.github.io/ClassificationCourse/Day14b_Boosting_Intro.html) or [rmd](https://agmath.github.io/ClassificationCourse/Day14b_Boosting_Intro.Rmd)) | Ensembles, Part II: Boosting |  |
| 15 |  | Intro to Model Stacking ([html](https://agmath.github.io/ClassificationCourse/Day15b_Stacking_Intro.html) or [rmd](https://agmath.github.io/ClassificationCourse/Day15b_Stacking_Intro.Rmd)) | Ensembles, Part III: Stacking Models |  |
| 16 | [Tweet Emotion](https://raw.githubusercontent.com/agmath/agmath.github.io/master/data/classification/tweet_emotions.csv) | Intro to Text and Tokenization ([html](https://agmath.github.io/ClassificationCourse/Day16b_TextAndTokenization_Intro.html) or [rmd](https://agmath.github.io/ClassificationCourse/Day16b_TextAndTokenization_Intro.Rmd)) | Text Features, Part I: Tokenization |  |
| 17 |  | Intro to Regular Expressions ([html](https://agmath.github.io/ClassificationCourse/Day17b_RegularExpressions_Intro.html) or [rmd](https://agmath.github.io/ClassificationCourse/Day17b_RegularExpressions_Intro.Rmd)) | Text Features, Part II: Regex |  |
| 18 |  | Intro to Word Embeddings ([html](https://agmath.github.io/ClassificationCourse/Day18b_Embeddings_Intro.html) or [rmd](https://agmath.github.io/ClassificationCourse/Day18b_Embeddings_Intro.Rmd)) | Text Features, Part III: Embeddings |  |
| 19 | Monster Classification |  | *Halloween Classification Challenge* <br/> (InClass Kaggle Competition) |  |
| 20 | TBD |  | Deep Learning, Part I: Architecture |  |
| 21 |  |  | Deep Learning, Part II: Activation Functions |  |
| 22 |  |  | Deep Learning, Part III: Training and Assessment |  |
| 23 |  |  | Final Project Topic Discussion |  |
| 24 |  |  | Final Project Group Selection |  |
| 25 | Turkey Pardoning |  | *Thanksgiving Classification Challenge* <br/> (InClass Kaggle Competition) |  |
| 26+ |  |  | Final Projects |  |

<br/>
<br/>

***

<br/>
<br/>

[Back to Hompage](https://agmath.github.io/)
