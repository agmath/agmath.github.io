---
title: Applied Statistics II (Regression Analysis)
description: This is a homepage for MAT300, Regression Analysis, with Dr. Gilbert at Southern New Hampshire University. This course introduces students to the construction, assessment, and interpretation of models in the regression setting.
---

## MAT 300 - Applied Statistics II: Regression Analysis

<img src="/SiteFiles/ISLR.png" align="left" width=200>[**Syllabus (Spring 2023)**](https://drive.google.com/file/d/16uY1DsSHVn3eMP1pL3G1t592U7ljlw2O/view?usp=share_link)<br/>
<br/>
***Course Description:*** This is a second course in statistics that builds upon knowledge gained in MAT 240 or an AP statistics course. Students will learn to build statistical models and develop skills for implementing regression analysis in real-world problems from engineering, sociology, psychology, science and business. Topics include multiple regression models (including first-order, second-order and interaction models with quantitative and qualitative variables), regression pitfalls and residual analysis. Additional topics will be covered if time permits. Students will gain experience not only in the mechanics of regression analysis (often by means of a statistical software package) but also in deciding on appropriate models, selecting inferential techniques to answer a particular question, interpreting results and diagnosing problems.<br/>
<br/>

Students in this course will use R, in particular the `tidyverse` and `tidymodels` ecosystems, to build and analyze regression models. The course covers simple and multiple linear regression, curvi-linear regression with polynomial and interaction terms, regularization with Ridge Regression and the LASSO, and tree-based models/ensembles. Cross-validation is implemented as an important technique for stable and unbiased model performance estimates, for identifying appropriate levels of model flexibility, and for hyperparameter tuning.<br/>
<br/>

### Course Notes

| Class Meeting | Before Class | During Class | After Class |
|---------------|--------------|--------------|-------------|
| 1 | [Review Syllabus](https://drive.google.com/file/d/16uY1DsSHVn3eMP1pL3G1t592U7ljlw2O/view?usp=share_link) <br/> [Install R and RStudio](https://agmath.github.io/RegressionCourse/1b_AccessingRandRStudio.html) | [Introduction and What to Expect](https://agmath.github.io/RegressionCourse/1d_Outline.html)<br/> Ethics and Data Models |  |
| 2 | Enroll in Competition <br/> Read ISLR S2.1 ([Part I](https://www.youtube.com/watch?v=p9n2w236B48), [Part II](https://www.youtube.com/watch?v=HndOzII4jzs)) | [What is Statistical Learning?](https://agmath.github.io/RegressionCourse/2d_StatisticalLearning.html) <br/> Competition Discussion <br/> What is an Analytics Report? ([html](https://agmath.github.io/RegressionCourse/WhatIsAnAnalyticsReport.html), [rmd](https://agmath.github.io/RegressionCourse/2d_StatisticalLearning.rmd)) | Competition Assignment 1|
| 3 | [Read ISLR S2.3](https://youtu.be/VaN1RUDuioQ) | Introduction to R: Enter the `tidyverse` ([html](https://agmath.github.io/RegressionCourse/3d_CrashCourse_TidyR.html), [rmd](https://agmath.github.io/RegressionCourse/3d_CrashCourse_TidyR.rmd)) | |
| 4 | [Read R4DS S3.1 - 3.10](https://r4ds.had.co.nz/data-visualisation.html) <br/> (Optional) | Data Viz and `ggplot2` ([html](https://agmath.github.io/RegressionCourse/4d_DataViz_Primer.html), [rmd](https://agmath.github.io/RegressionCourse/4d_DataViz_Primer.rmd)) | Competition Assignment 2 |
| 5 |  | R Workshop Day: R Markdown <br/> Analytics Report Revisited |  |
| 6 |  | Data Wrangling Workshop ([html](https://agmath.github.io/RegressionCourse/6d_DataWrangling.html), [rmd](https://agmath.github.io/RegressionCourse/6d_DataWrangling.rmd)) | Homework 1 |
| 7 |  | Introduction to `tidymodels` ([html](https://agmath.github.io/RegressionCourse/7d_tidymodelsOverview.html), [rmd](https://agmath.github.io/RegressionCourse/7d_tidymodelsOverview.rmd)) |  |
| 8 | Intro Stats Review | Hypothesis Testing and Confidence / Prediction Intervals in Regression ([html](https://agmath.github.io/RegressionCourse/8d_IntroStatsForRegression_Review), [rmd](https://agmath.github.io/RegressionCourse/8d_IntroStatsForRegression_Review)) | Homework 2 |
| 9 | Read ISLR S3.1 ([Part I](https://youtu.be/7TgVO_K75EY), [Part II](https://youtu.be/z10DqaVJh3c)) | Multiple Linear Regression: <br/> Construction, Interpretation, and Model Assessment ([html](https://agmath.github.io/RegressionCourse/9d_SimpleLinearRegression.html), [rmd](https://agmath.github.io/RegressionCourse/9d_SimpleLinearRegression.rmd)) | Competition Assignment 3 |
| 10 | Read ISLR S 3.2 ([Part I](https://youtu.be/yzQHONabWhs), [Part II](https://youtu.be/lo7KnnvyEU0)) | Multiple Linear Regression: <br/> Construction, Interpretation, and Model Assessment ([html](https://agmath.github.io/RegressionCourse/10d_MultipleLinearRegression.html), [rmd](https://agmath.github.io/RegressionCourse/10d_MultipleLinearRegression.rmd)) | Competition Assignment 3 |
| 11 | Read ISLR S3.3 ([Part I](https://youtu.be/lo7KnnvyEU0), [Part II](https://youtu.be/sK80ZnhiaRI)) | Categorical Predictors and Interpretations <br/> Feature Engineering with `step_other()` and `step_dummy()` ([html](https://agmath.github.io/RegressionCourse/11d_CategoricalPredictors.html), [rmd](https://agmath.github.io/RegressionCourse/11d_CategoricalPredictors.rmd)) | Competition Assignment 5 |
| 12 |  | Model Building, Assessment, and Interpretation Workshop |  | 
| 13 |  | Higher-Order Terms: <br/> Curvi-Linear Regression and Polynomial Terms with `step_poly()` ([html](https://agmath.github.io/RegressionCourse/13d_HigherOrderTerms_Polynomial.html), [rmd](https://agmath.github.io/RegressionCourse/13d_HigherOrderTerms_Polynomial.rmd)) | Competition Assignment 6 |
| 14 |  | Higher-Order Terms: <br/> Interaction with `step_interact()` ([html](https://agmath.github.io/RegressionCourse/14d_HigherOrderTerms_Interaction.html), [rmd](https://agmath.github.io/RegressionCourse/14d_HigherOrderTerms_Interaction.rmd)) |  |
| 15 | [Read ISLR S2.2](https://youtu.be/VaN1RUDuioQ) | Bias/Variance Trade-Off and Model Performance Concerns ([html](https://agmath.github.io/RegressionCourse/15d_BiasVarianceTradeOff_Overfitting.html), [rmd](https://agmath.github.io/RegressionCourse/15d_BiasVarianceTradeOff_Overfitting.rmd)) |  |
| 16 | Read ISLR S5.1 ([Part I](https://youtu.be/ngrOYWgJjb4), [Part II](https://youtu.be/rSGzUy13F_0), [Part III](https://youtu.be/r64tRyHFAJ8)) | Performance Concerns Continued: Different Test, Different Expectations <br/> Cross-Validation and Unbiased Model Performance ([html](https://agmath.github.io/RegressionCourse/16d_CrossValidation.html), [rmd](https://agmath.github.io/RegressionCourse/16d_CrossValidation.rmd)) | Homework 3 |
| 17 | Read ISLR S6.1, 6.2 ([Part IV](https://youtu.be/f_hkP_We0JY), [Part V](https://youtu.be/I8bPQ272Pbs), [Part VI](https://youtu.be/FlSQgXv7Dvw), <br/> [Part VII](https://youtu.be/8oEZkHqf_Rk)) | Variable Selection Methods: <br/> Stepwise Regression, Ridge Regression, and the LASSO ([html](https://agmath.github.io/RegressionCourse/17d_VariableSelectionMethods.html), [rmd](https://agmath.github.io/RegressionCourse/17d_VariableSelectionMethods.rmd)) |  |
| 18 |  | Other Regressors ([html](https://agmath.github.io/RegressionCourse/18d_OtherRegressors.html), [rmd](https://agmath.github.io/RegressionCourse/18d_OtherRegressors.rmd)) | Competition Assignment 7 | 
| 19 |  | Hyperparameters and Tuning <br/> More uses for Cross-Validation |  |
| 20 | [Read ISLR S4.3](https://youtu.be/RN_dweQpcpo) | Classification with Logistic Regression |  |
| 21+ | Projects | Projects | Projects |

<br/>
<br/>

[Back to Hompage](https://agmath.github.io/)
