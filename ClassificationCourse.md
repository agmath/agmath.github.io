---
title: Statistical Learning and Classification
description: This is a homepage for MAT434, Statistical Learning and Classification, with Dr. Gilbert at Southern New Hampshire University. This course introduces students to the construction, assessment, and interpretation of models in the classification setting. Depending on student interest, applications in computer vision, natural language processing, and/or deep learning are also explored.
---

{% include google-analytics.html %}

## MAT 434 - Statistical Learning and Classification (with R)

<img src="/SiteFiles/ISLR.png" align="left" width=200>[**Spring 2025 Syllabus**](https://drive.google.com/file/d/12SoH8F2d57ZAj-qsUKUwk_1knl2_4Axu/view?usp=sharing)<br/>
<br/>
***Course Description:*** Using the foundational knowledge built in MAT 240/241 and MAT 300, we continue our study of statistical models. This course moves beyond regression and into classification models, mixed models, and unsupervised learning. Like MAT300, this course also emphasizes cross-validation as an important method for  hyperparameter tuning, identifying appropriate levels of model flexibility, approximating future model performance, and analyzing the utility of a model. This course covers logistic regression, support vector machines, k nearest neighbors, tree-based methods (bagging, boosting, and random forests), and neural networks. We also cover techniques for dimension reduction and working with text-based features. In addition to the statistical modeling coursework, students will be exposed to GitHub for collaboration and version control and will use GitHub pages to build and populate a professional profile for sharing their work on the web.<br/>

### Course Timeline and Notebooks

Below is a tentative timeline for our course. The table includes preparatory work that should be read prior to each class meeting, a description of what to expect during our class meeting, and assignments following each class meeting. I'm taking a more free-form approach to MAT434 than we took in [MAT300](https://agmath.github.io/RegressionCourse.html), where I provided you with detailed notebooks or slides prior to each class meeting. In MAT434, we'll be building our notebooks in class, exploring several different data sets as our semester goes on. While the main topics for each class meeting are determined, you all will be dictating the direction of our analyses, the choices we make during model construction, and the corresponding discussions we end up having.

| Class Meeting | Dataset | Before Class | During Class | After Class |
|---------------|--------------|--------------|--------------|-------------|
| 1 |  | i) [Review Syllabus](https://drive.google.com/file/d/12SoH8F2d57ZAj-qsUKUwk_1knl2_4Axu/view?usp=sharing) <br/> ii) [Software Setup](https://agmath.github.io/ClassificationCourse/SoftwareSetup.html) |  i) Introduction and What to Expect <br/> ii) Ethics and Data Models | [**HW 1**](https://agmath.github.io/ClassificationCourse/HW1.html) |
| 2 | [FAA Airstrikes and Engine Damage](https://www.kaggle.com/competitions/sliced-s01e02-xunyc5/data), or <br/> [MLB Hits and Homeruns](https://www.kaggle.com/competitions/sliced-s01e09-playoffs-1/data?select=train.csv) | (i) Ensure that `git` is working from RStudio | i) [R Projects and Version Control](https://agmath.github.io/ClassificationCourse/x_RprojectsVersionControl.html) <br/> ii) Tidy Analyses in R ([new students](https://agmath.github.io/ClassificationCourse/Day2_TidyAnalyses_newStudents.html) or [returning students](https://agmath.github.io/ClassificationCourse/Day2_TidyAnalyses_returningStudents.html)) | [**HW 2**](https://agmath.github.io/ClassificationCourse/HW2.html) <br/> [**CA 1**](https://agmath.github.io/ClassificationCourse/CA1.html) |
| 3 |  |  | [Quarto, inline commands, and semi-automated reporting](https://agmath.github.io/ClassificationCourse/Day3_Quarto_InlineR.html) | [**HW 3**](https://agmath.github.io/ClassificationCourse/HW3.html) |
| 4 |  |  |  [EDA and Data Viz InClass](https://agmath.github.io/ClassificationCourse/Day4_EDA_and_Viz_Primer.html) | [**CA 2**](https://agmath.github.io/ClassificationCourse/CA2.html) | 
| 5 |  | Setup a `username.github.io` Repository | [GitHub Pages and a public-facing portfolio](https://agmath.github.io/ClassificationCourse/Day5_GitHubPages.html) | [**HW 4**](https://agmath.github.io/ClassificationCourse/HW4.html)
| 6 |  | [`{tidymodels}` Framework (Review)](https://agmath.github.io/ClassificationCourse/x_ModelingFrameworkAndTidymodelsReview.html) | [`{tidymodels}` Framework Example](https://agmath.github.io/ClassificationCourse/x_TidymodelsExample.html) |  |
| 7 |  |  | Regression Versus Classification and Performance Metrics for Classifiers ([html](https://agmath.github.io/ClassificationCourse/Day7_RegressionVersusClassification.html) or [rmd](https://agmath.github.io/ClassificationCourse/Day7_RegressionVersusClassification.Rmd)) | [**HW 5**](https://agmath.github.io/ClassificationCourse/HW5.html) |
| 8 | [Spaceship Titanic](https://raw.githubusercontent.com/agmath/agmath.github.io/master/data/classification/spaceship_titanic.csv) | Intro to Logistic Regressors ([html](https://agmath.github.io/ClassificationCourse/Day8b_LogisticRegression_Intro.html) or [rmd](https://agmath.github.io/ClassificationCourse/Day8b_LogisticRegression_Intro.Rmd)) | Binary Classifiers, Part I: Logistic Regression |  |
| 9 |  | Intro to Support Vector Classifiers ([html](https://agmath.github.io/ClassificationCourse/Day9b_SupportVectorMachines_Intro.html) or [rmd](https://agmath.github.io/ClassificationCourse/Day9b_SupportVectorMachines_Intro.rmd)) | Binary Classifiers, Part II: Support Vector Machines | [**HW 6**](https://agmath.github.io/ClassificationCourse/HW6.html) |
| 10 | [Gene Expression and Cancerous Tumors](https://raw.githubusercontent.com/agmath/agmath.github.io/master/data/classification/cancer_gene_expression_data.csv) | Intro to Principal Component Analysis ([html](https://agmath.github.io/ClassificationCourse/Day10b_PrincipalComponentAnalysis_Intro.html) or [rmd](https://agmath.github.io/ClassificationCourse/Day10b_PrincipalComponentAnalysis_Intro.rmd)) | Aside: High-Dimensional Data and Dimension Reduction |  |
| 11 | [Healthcare Analytics: Length of Stay](https://raw.githubusercontent.com/agmath/agmath.github.io/master/data/classification/hospital_stays.csv) <br/> [(smaller)](https://raw.githubusercontent.com/agmath/agmath.github.io/refs/heads/master/data/classification/hospital_stays_small.csv) | Intro to k Nearest Neighbors ([html](https://agmath.github.io/ClassificationCourse/Day11b_KNN_Intro.html) or [rmd](https://agmath.github.io/ClassificationCourse/Day11b_KNN_Intro.rmd)) | Multiclass Classifiers, Part I: Nearest Neighbors | [**CA 3**](https://agmath.github.io/ClassificationCourse/CA3.html) |
| 12 |  | Intro to Decision Trees ([html](https://agmath.github.io/ClassificationCourse/Day12b_DecisionTreeClassifiers_Intro.html) or [rmd](https://agmath.github.io/ClassificationCourse/Day12b_DecisionTreeClassifiers_Intro.rmd)) | Multiclass Classifiers, Part II: Decision Tree Classifiers |  |
| 13 |  | Intro to Ensembles, Bagging, and Random Forests ([html](https://agmath.github.io/ClassificationCourse/Day13b_EnsemblesBaggingAndRandomForests_Intro.html) or [rmd](https://agmath.github.io/ClassificationCourse/Day13b_EnsemblesBaggingAndRandomForests_Intro.rmd)) | Ensembles, Part I: Bagging and Random Forests |  |
| 14 |  | Intro to Boosting ([html](https://agmath.github.io/ClassificationCourse/Day14b_Boosting_Intro.html) or [rmd](https://agmath.github.io/ClassificationCourse/Day14b_Boosting_Intro.rmd)) | Ensembles, Part II: Boosting | [**CA 4**](https://agmath.github.io/ClassificationCourse/CA4.html) |
| 15 |  | Work on GitHub Page |  |  |
| 16 | [Cyberbullying](https://raw.githubusercontent.com/agmath/agmath.github.io/refs/heads/master/data/classification/cyberbullying_tweets.csv),  | Intro to Text and Tokenization ([html](https://agmath.github.io/ClassificationCourse/Day16b_TextAndTokenization_Intro.html) or [rmd](https://agmath.github.io/ClassificationCourse/Day16b_TextAndTokenization_Intro.rmd)) | Text Features, Part I: Tokenization |  |
| 17 |  | Intro to Regular Expressions ([html](https://agmath.github.io/ClassificationCourse/Day17b_RegularExpressions_Intro.html) or [rmd](https://agmath.github.io/ClassificationCourse/Day17b_RegularExpressions_Intro.rmd)) | Text Features, Part II: Regex |  |
| 18 | St. Patrick's Day Competition |  | *St. Patrick's Day Classification Challenge* <br/> (InClass Kaggle Competition) |  |
| 19 |  | Intro to Word Embeddings ([html](https://agmath.github.io/ClassificationCourse/Day18b_Embeddings_Intro.html) or [rmd](https://agmath.github.io/ClassificationCourse/Day18b_Embeddings_Intro.rmd)) | Text Features, Part III: Embeddings | [**CA 5**](https://agmath.github.io/ClassificationCourse/CA5.html) |
| 20 | Fashion MNIST | [Install TensorFlow](https://agmath.github.io/ClassificationCourse/Day20b_InstallingTensorFlow.html) | [Deep Learning, Part I: Architecture](https://agmath.github.io/ClassificationCourse/Day20d_DeepLearningArchitectures.html) |  |
| 21 |  |  | [Deep Learning, Part II: Activation Functions](https://agmath.github.io/ClassificationCourse/Day21d_DeepLearningActivationFunctions.html) |  |
| 22 |  |  | [Deep Learning, Part III: Training and Assessment](https://agmath.github.io/ClassificationCourse/Day22d_DeepLearningImplementation.html) | [**CA 6**](https://agmath.github.io/ClassificationCourse/CA6.html) |
| 23+ |  |  | Final Projects |  |

<br/>
<br/>

***

#### References

[1] [Tibshirani et. al., *Introduction to Statistical Learning* (2021)](https://www.statlearning.com/)
[2] [MLB Hits and Homeruns data set taken from Sliced Data Science Competition (Season 1, Episode 9)](https://www.kaggle.com/competitions/sliced-s01e09-playoffs-1/data)
[3] [Airstrikes and Engine Damage data set posted to Kaggle by the FAA and Abigail Larion in 2016](https://www.kaggle.com/datasets/faa/wildlife-strikes)
[4] [Spaceship Titanic data set taken from Kaggle *Getting Started* Competition](https://www.kaggle.com/competitions/spaceship-titanic/data)
[5] [Gene Expression and Cancerous Tumors data set retrieved from Synapse.org and is maintained by the Cancer Genome Project](https://www.synapse.org/#!Synapse:syn4301332)
[6] [Cyberbullying data set posted to Kaggle by user `LARXEL` in 2021](https://www.kaggle.com/datasets/andrewmvd/cyberbullying-classification)

***

<br/>
<br/>

[Back to Hompage](https://agmath.github.io/)
