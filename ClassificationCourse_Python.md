---
title: Statistical Learning and Classification
description: This is a homepage for MAT434, Statistical Learning and Classification, with Dr. Gilbert at Southern New Hampshire University. This course introduces students to the construction, assessment, and interpretation of models in the classification setting. Depending on student interest, applications in computer vision, natural language processing, and/or deep learning are also explored.
---

{% include google-analytics.html %}

## MAT 434 - Statistical Learning and Classification (Alpha Python Version)

<img src="/SiteFiles/ISLR.png" align="left" width=200>[**Tentative Syllabus (Fall 2023)**](https://drive.google.com/file/d/1W6sLmFZ0tkIPkqqo5nfSIusywC8R2zL-/view?usp=sharing)<br/>
<br/>
***Note:*** This is an initial draft of a Python version of MAT434. Please note that these materials have been created quickly, and in some cases may contain typos. Additionally, the flow of these materials is not as polished as the flow of the materials for the R version of this course. <br/>
<br/>
***Course Description:*** Using the foundational knowledge built in MAT 240/241 and MAT 300, we continue our study of statistical models. This course moves beyond regression and into classification models, mixed models, and unsupervised learning. Like MAT300, this course also emphasizes cross-validation as an important method for  hyperparameter tuning, identifying appropriate levels of model flexibility, approximating future model performance, and analyzing the utility of a model. This course covers logistic regression, support vector machines, k nearest neighbors, tree-based methods (bagging, boosting, and random forests), and neural networks. We also cover techniques for dimension reduction and working with text-based features. In addition to the statistical modeling coursework, students will be exposed to GitHub for collaboration and version control and will use GitHub pages to build and populate a professional profile for sharing their work on the web.<br/>
<br/>

### Course Timeline and Notebooks

Below is a tentative timeline for our course. The table includes preparatory work that should be read prior to each class meeting, a deescription of what to expect during our class meeting, and assignments following each class meeting. I'm taking a more free-form approach to MAT434 than we took in [MAT300](https://agmath.github.io/RegressionCourse.html), where I provided you with detailed notebooks prior to each class meeting. In MAT434, we'll be building our notebooks in class, exploring several different data sets as our semester goes on. While the main topics for each class meeting are determined, you all will be dictating the direction of our analyses, the choices we make during model construction, and the corresponding discussions we end up having.

| Class Meeting | Dataset | Before Class | During Class | After Class |
|---------------|--------------|--------------|--------------|-------------|
| 1 |  | i) [Review Syllabus](https://drive.google.com/file/d/1W6sLmFZ0tkIPkqqo5nfSIusywC8R2zL-/view?usp=sharing) <br/> ii) [Software Setup](https://agmath.github.io/ClassificationCourse/SoftwareSetup.html) <br/> (iii) [Additional Setup for Python](https://agmath.github.io/ClassificationCourse/x_PythonFromRStudio.html) |  i) Introduction and What to Expect <br/> ii) Ethics and Data Models | [**HW 1**](https://agmath.github.io/ClassificationCourse/HW1.html) |
| 2 | [FAA Airstrikes and Engine Damage](https://www.kaggle.com/competitions/sliced-s01e02-xunyc5/data), or <br/> [MLB Hits and Homeruns](https://www.kaggle.com/competitions/sliced-s01e09-playoffs-1/data?select=train.csv) | (i) Ensure that `git` is working from RStudio <br/> (ii) [Dual-Weilding Languages with `{reticulate}`](https://agmath.github.io/ClassificationCourse/x_MoreOnReticulate.html) | i) [R Projects and Version Control](https://agmath.github.io/ClassificationCourse/x_RprojectsVersionControl.html) <br/> ii) [Data Wrangling in Python](https://agmath.github.io/ClassificationCourse/Day2_DataWrangling_Python.html) | [**HW 2**](https://agmath.github.io/ClassificationCourse/HW2.html) <br/> [**CA 1**](https://agmath.github.io/ClassificationCourse/CA1.html) |
| 3 |  |  | [R Markdown, inline commands, and semi-automated reporting](https://agmath.github.io/ClassificationCourse/Day3_RMarkdown_InlineR.html) | [**HW 3**](https://agmath.github.io/ClassificationCourse/HW3.html) |
| 4 |  |  |  [EDA and Data Viz with `{plotnine}`](https://agmath.github.io/ClassificationCourse/Day4_EDA_and_Viz_Primer_Python.html) | [**CA 2**](https://agmath.github.io/ClassificationCourse/CA2.html) | 
| 5 |  | Setup a `username.github.io` Repository | [GitHub Pages and a public-facing portfolio](https://agmath.github.io/ClassificationCourse/Day5_GitHubPages.html) | [**HW 4**](https://agmath.github.io/ClassificationCourse/HW4.html)
| 6 |  | [`{sklearn}` Framework Overview](https://agmath.github.io/ClassificationCourse/x_ModelingFrameworkAndSKlearnReview.html) | [`{sklearn}` Example](https://agmath.github.io/ClassificationCourse/x_SKlearnExample.html) |  |
| 7 |  |  | Regression Versus Classification and Performance Metrics for Classifiers ([html](https://agmath.github.io/ClassificationCourse/Day7_RegressionVersusClassification.html) or [rmd](https://agmath.github.io/ClassificationCourse/Day7_RegressionVersusClassification.Rmd)) | [**HW 5**](https://agmath.github.io/ClassificationCourse/HW5.html) |
| 8 | [Spaceship Titanic](https://raw.githubusercontent.com/agmath/agmath.github.io/master/data/classification/spaceship_titanic.csv) | Intro to Logistic Regressors ([html](https://agmath.github.io/ClassificationCourse/Day8b_LogisticRegression_Intro_Python.html) or [rmd](https://agmath.github.io/ClassificationCourse/Day8b_LogisticRegression_Intro_Python.Rmd)) | Binary Classifiers, Part I: Logistic Regression |  |
| 9 |  | Intro to Support Vector Classifiers ([html](https://agmath.github.io/ClassificationCourse/Day9b_SupportVectorMachines_Intro_Python.html) or [rmd](https://agmath.github.io/ClassificationCourse/Day9b_SupportVectorMachines_Intro_Python.Rmd)) | Binary Classifiers, Part II: Support Vector Machines | [**HW 6**](https://agmath.github.io/ClassificationCourse/HW6.html) |
| 10 | [Gene Expression and Cancerous Tumors](https://archive.ics.uci.edu/ml/datasets/gene+expression+cancer+RNA-Seq) | Intro to Principal Component Analysis ([html](https://agmath.github.io/ClassificationCourse/Day10b_PrincipalComponentAnalysis_Intro_Python.html) or [rmd](https://agmath.github.io/ClassificationCourse/Day10b_PrincipalComponentAnalysis_Intro_Python.Rmd)) | Aside: High-Dimensional Data and Dimension Reduction |  |
| 11 | [Healthcare Analytics: Length of Stay](https://www.kaggle.com/datasets/nehaprabhavalkar/av-healthcare-analytics-ii) | Intro to k Nearest Neighbors ([html](https://agmath.github.io/ClassificationCourse/Day11b_KNN_Intro_Python.html) or [rmd](https://agmath.github.io/ClassificationCourse/Day11b_KNN_Intro_Python.Rmd)) | Multiclass Classifiers, Part I: Nearest Neighbors | [**CA 3**](https://agmath.github.io/ClassificationCourse/CA3.html) |
| 12 |  | Intro to Decision Trees ([html](https://agmath.github.io/ClassificationCourse/Day12b_DecisionTreeClassifiers_Intro_Python.html) or [rmd](https://agmath.github.io/ClassificationCourse/Day12b_DecisionTreeClassifiers_Intro_Python.Rmd)) | Multiclass Classifiers, Part II: Decision Tree Classifiers |  |
| 13 |  | Intro to Ensembles, Bagging, and Random Forests ([html](https://agmath.github.io/ClassificationCourse/Day13b_EnsemblesBaggingAndRandomForests_Intro_Python.html) or [rmd](https://agmath.github.io/ClassificationCourse/Day13b_EnsemblesBaggingAndRandomForests_Intro_Python.Rmd)) | Ensembles, Part I: Bagging and Random Forests |  |
| 14 |  | Intro to Boosting ([html](https://agmath.github.io/ClassificationCourse/Day14b_Boosting_Intro_Python.html) or [rmd](https://agmath.github.io/ClassificationCourse/Day14b_Boosting_Intro_Python.Rmd)) | Ensembles, Part II: Boosting | [**CA 4**](https://agmath.github.io/ClassificationCourse/CA4.html) |
| 15 |  | Intro to Model Stacking ([html](https://agmath.github.io/ClassificationCourse/Day15b_Stacking_Intro_Python.html) or [rmd](https://agmath.github.io/ClassificationCourse/Day15b_Stacking_Intro_Python.Rmd)) | Ensembles, Part III: Stacking Models |  |
| 16 | [Tweet Emotion](https://raw.githubusercontent.com/agmath/agmath.github.io/master/data/classification/tweet_emotions.csv) | Intro to Text and Tokenization ([html](https://agmath.github.io/ClassificationCourse/Day16b_TextAndTokenization_Intro.html) or [rmd](https://agmath.github.io/ClassificationCourse/Day16b_TextAndTokenization_Intro.Rmd)) | Text Features, Part I: Tokenization |  |
| 17 |  | Intro to Regular Expressions ([html](https://agmath.github.io/ClassificationCourse/Day17b_RegularExpressions_Intro.html) or [rmd](https://agmath.github.io/ClassificationCourse/Day17b_RegularExpressions_Intro.Rmd)) | Text Features, Part II: Regex |  |
| 18 |  | Intro to Word Embeddings ([html](https://agmath.github.io/ClassificationCourse/Day18b_Embeddings_Intro.html) or [rmd](https://agmath.github.io/ClassificationCourse/Day18b_Embeddings_Intro.Rmd)) | Text Features, Part III: Embeddings | [**CA 5**](https://agmath.github.io/ClassificationCourse/CA5.html) |
| 19 | Monster Classification |  | *Halloween Classification Challenge* <br/> (InClass Kaggle Competition) |  |
| 20 | Fashion MNIST | [Install TensorFlow](https://agmath.github.io/ClassificationCourse/Day20b_InstallingTensorFlow.html) | [Deep Learning, Part I: Architecture](https://agmath.github.io/ClassificationCourse/Day20d_DeepLearningArchitectures.html) |  |
| 21 |  |  | [Deep Learning, Part II: Activation Functions](https://agmath.github.io/ClassificationCourse/Day21d_DeepLearningActivationFunctions.html) |  |
| 22 |  |  | [Deep Learning, Part III: Training and Assessment](https://agmath.github.io/ClassificationCourse/Day22d_DeepLearningImplementation.html) | [**CA 6**](https://agmath.github.io/ClassificationCourse/CA6.html) |
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
