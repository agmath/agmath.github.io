---
title: Applied Statistics II (Regression Analysis)
description: This is a homepage for MAT300, Regression Analysis, with Dr. Gilbert at Southern New Hampshire University. This course introduces students to the construction, assessment, and interpretation of models in the regression setting.
---

{% include google-analytics.html %}

<script> MathJax = { tex: { inlineMath: [['$', '$'], ['\\(', '\\)']] }, svg: { fontCache: 'global' } }; </script> <script type="text/javascript" id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-svg.js"> </script>

## MAT 300 - Applied Statistics II: Regression Analysis

<img src="/SiteFiles/ISLR.png" align="left" width=200>[**Syllabus (Fall 2024)**](https://drive.google.com/file/d/1-M9dAIoaSOyklfQAKeZlG3317rqhFD2k/view?usp=sharing)<br/>
<br/>
***Course Description:*** This is a second course in statistics that builds upon knowledge gained in an introductory statistics course that covers statistical inference. Students will learn to build statistical models and develop skills for implementing regression analysis in real-world problems from engineering, sociology, psychology, science and business. Topics include multiple regression models (including first-order, second-order and interaction models with quantitative and qualitative variables), regression pitfalls, and residual analysis. Additional topics will be covered if time permits. Students will gain experience not only in the mechanics of regression analysis (often by means of a statistical software package) but also in deciding on appropriate models, selecting inferential techniques to answer a particular question, interpreting results and diagnosing problems.<br/>
<br/>

Students in this course will use R, in particular the `{tidyverse}` and `{tidymodels}` ecosystems, to build and analyze regression models. The course covers simple and multiple linear regression, curvi-linear regression with polynomial and interaction terms, regularization with Ridge Regression and the LASSO, and tree-based models/ensembles. Cross-validation is implemented as an important technique for stable and unbiased model performance estimates, for identifying appropriate levels of model flexibility, and for hyperparameter tuning.<br/>
<br/>

### Course Timeline and Notebooks

Below is a tentative timeline for our course. It includes preparatory work that should be done prior to each class meeting, a detailed set of notes corresponding to each class meeting, and assignments following each class meeting. The prepared notebooks use the Palmer `penguins` and `ames` housing datasets and are provided so that you have a detailed account of each topic we discuss. We'll learn this content better by *doing* it that we will by simply *reading* and *running* pre-existing code, so we'll plan to utilize different data in class. For now, I'm planning to start with [this data set](https://github.com/rfordatascience/tidytuesday/tree/master/data/2022/2022-07-05) on rental properties in the San Francisco Bay Area posted to Craigslist, generously made open by [Dr. Kate Pennington](https://www.katepennington.org/data). We can switch to alternate data sets as student interest dictates. I've prepared the following **student notes template** ([html](https://agmath.github.io/RegressionCourse/StudentNotesTemplate.html), [Quarto](https://agmath.github.io/RegressionCourse/StudentNotesTemplate.qmd)) that I hope you'll use to follow along during our in-class discussions. <br/>

**A Note on the Slide Decks:** I built these slides to be displayed as a split-screen, alongside an open RStudio session. In this way, you can play along by building your own analysis with a different data set (or the same one, if you prefer). If you try displaying the slides across your full screen, the content will flow off the bottom of the page.

| Class Meeting | Before Class | During Class | Slides | After Class |
|---------------|--------------|--------------|-------------|-------------|
| 1 | [Review Syllabus](https://drive.google.com/file/d/16uY1DsSHVn3eMP1pL3G1t592U7ljlw2O/view?usp=share_link) <br/> [Install R and RStudio](https://agmath.github.io/RegressionCourse/1b_AccessingRandRStudio.html) | [Introduction and What to Expect](https://agmath.github.io/RegressionCourse/1d_Outline.html)) | [Slide Version of Intro and Expectations](https://agmath.github.io/RegressionCourse/1d_Outline_slides.html) | Finish Software Setup |
| 2 | Enroll in Competition <br/> Read ISLR $\S$ 2.1 ([Part I](https://www.youtube.com/watch?v=p9n2w236B48), [Part II](https://www.youtube.com/watch?v=HndOzII4jzs)) | [What is Statistical Learning?](https://agmath.github.io/RegressionCourse/2d_StatisticalLearning.html) <br/> Competition Discussion | [Slide Version of Overview](https://agmath.github.io/RegressionCourse/2d_IntroSlides.html)  | [What is an Analytics Report?](https://agmath.github.io/RegressionCourse/WhatIsAnAnalyticsReport.html) <br/> [Competition Assignment 1](https://agmath.github.io/RegressionCourse/CA1_StatementOfPurpose.html)  <br/> Analytics Report Shell ([html](https://agmath.github.io/RegressionCourse/AnalyticsReportShell.html), [Quarto](https://agmath.github.io/RegressionCourse/AnalyticsReportShell.qmd)) |
| 3 | [Read ISLR $\S$ 2.3](https://youtu.be/VaN1RUDuioQ) | Introduction to R: Enter the `tidyverse` ([html](https://agmath.github.io/RegressionCourse/3d_CrashCourse_TidyR.html), [Quarto](https://agmath.github.io/RegressionCourse/3d_CrashCourse_TidyR.qmd)) | [Companion Slides](https://agmath.github.io/RegressionCourse/3d_IntroSlides.html) |  |
| 4 | [Read R4DS $\S$ 3.1 - 3.10](https://r4ds.had.co.nz/data-visualisation.html) <br/> (Optional) | Data Viz and `ggplot2` ([html](https://agmath.github.io/RegressionCourse/4d_DataViz_Primer.html), [Quarto](https://agmath.github.io/RegressionCourse/4d_DataViz_Primer.qmd)) | [Companion Slides](https://agmath.github.io/RegressionCourse/4d_IntroSlides.html) | [Competition Assignment 2](https://agmath.github.io/RegressionCourse/CA2_ExploratoryDataAnalysis.html) |
| 5 |  | R Workshop Day: Quarto and R |  |  |
| 6 |  | Data Wrangling Workshop ([html](https://agmath.github.io/RegressionCourse/6d_DataWrangling.html), [Quarto](https://agmath.github.io/RegressionCourse/6d_DataWrangling.qmd)) | [Companion Slides](https://agmath.github.io/RegressionCourse/6d_RecapSlides.html) | Homework 1 ([html](https://agmath.github.io/RegressionCourse/HW1_DataWrangling.html), [Quarto](https://agmath.github.io/RegressionCourse/HW1_DataWrangling.qmd)) |
| 7 |  | Introduction to `{tidymodels}` ([html](https://agmath.github.io/RegressionCourse/7d_tidymodelsOverview.html), [Quarto](https://agmath.github.io/RegressionCourse/7d_tidymodelsOverview.qmd)) | [Companion Slides](https://agmath.github.io/RegressionCourse/7d_IntroSlides.html) |  |
| 8 | Intro Stats Review | Hypothesis Testing and Confidence / Prediction Intervals in Regression ([html](https://agmath.github.io/RegressionCourse/8d_IntroStatsForRegression_Review), [Quarto](https://agmath.github.io/RegressionCourse/8d_IntroStatsForRegression_Review.qmd)) | [Companion Slides](https://agmath.github.io/RegressionCourse/8d_IntroSlides.html) | Homework 2 ([html](https://agmath.github.io/RegressionCourse/HW2_UnderstandingAssumptions.html), [Quarto](https://agmath.github.io/RegressionCourse/HW2_UnderstandingAssumptions.qmd)) |
| 9 | Read ISLR $\S$ 3.1 ([Part I](https://youtu.be/7TgVO_K75EY), [Part II](https://youtu.be/z10DqaVJh3c)) | Simple Linear Regression: <br/> Construction, Interpretation, and Model Assessment ([html](https://agmath.github.io/RegressionCourse/9d_SimpleLinearRegression.html), [Quarto](https://agmath.github.io/RegressionCourse/9d_SimpleLinearRegression.qmd)) | [Companion Slides](https://agmath.github.io/RegressionCourse/9d_IntroSlides.html) | [Competition Assignment 3](https://agmath.github.io/RegressionCourse/CA3_SimpleLinearRegression_SubmitPredictions.html) |
| 10 | Read ISLR $\S$ 3.2 ([Part I](https://youtu.be/yzQHONabWhs), [Part II](https://youtu.be/lo7KnnvyEU0)) | Multiple Linear Regression: <br/> Construction, Interpretation, and Model Assessment ([html](https://agmath.github.io/RegressionCourse/10d_MultipleLinearRegression.html), [Quarto](https://agmath.github.io/RegressionCourse/10d_MultipleLinearRegression.qmd)) | [Companion Slides](https://agmath.github.io/RegressionCourse/10d_IntroSlides.html) |  |
| 11 |  | Residual Analysis and Model Quality | [Companion Slides](https://agmath.github.io/RegressionCourse/11d_IntroSlides.html) |  |
| 12 | Read ISLR $\S$ 3.3 ([Part I](https://youtu.be/lo7KnnvyEU0), [Part II](https://youtu.be/sK80ZnhiaRI)) | Categorical Predictors and Interpretations <br/> Feature Engineering with `step_other()` and `step_dummy()` ([html](https://agmath.github.io/RegressionCourse/11d_CategoricalPredictors.html), [Quarto](https://agmath.github.io/RegressionCourse/11d_CategoricalPredictors.qmd)) | [Companion Slides](https://agmath.github.io/RegressionCourse/12d_IntroSlides.html) | [Competition Assignment 4](https://agmath.github.io/RegressionCourse/CA4_MultipleLinearRegression_Interpretation_SubmitPredictions.html) |
| 13 |  | Model Building, Assessment, and Interpretation Workshop |  |  |
| 14 |  | Higher-Order Terms: <br/> Curvi-Linear Regression and Polynomial Terms with `step_poly()` ([html](https://agmath.github.io/RegressionCourse/13d_HigherOrderTerms_Polynomial.html), [Quarto](https://agmath.github.io/RegressionCourse/13d_HigherOrderTerms_Polynomial.qmd)) | [Companion Slides](https://agmath.github.io/RegressionCourse/13d_IntroSlides.html) | [Competition Assignment 5](https://agmath.github.io/RegressionCourse/CA5_HigherOrderModel_SubmitPredictions.html) |
| 15 |  | Higher-Order Terms: <br/> Interaction with `step_interact()` ([html](https://agmath.github.io/RegressionCourse/14d_HigherOrderTerms_Interaction.html), [Quarto](https://agmath.github.io/RegressionCourse/14d_HigherOrderTerms_Interaction.qmd)) | [Companion Slides](https://agmath.github.io/RegressionCourse/14d_IntroSlides.html) |  |
| 16 |  | Inference and Interpretation with `{marginaleffects}` | [Companion Slides](https://agmath.github.io/RegressionCourse/16d_IntroSlides.html) |  |
| 17 |  | Halloween Modeling Competition <br/> (In Class, 75-minutes) |  |  |
| 18 | [Read ISLR $\S$ 2.2](https://youtu.be/VaN1RUDuioQ) | Bias/Variance Trade-Off and Model Performance Concerns ([html](https://agmath.github.io/RegressionCourse/15d_BiasVarianceTradeOff_Overfitting.html), [Quarto](https://agmath.github.io/RegressionCourse/15d_BiasVarianceTradeOff_Overfitting.qmd)) | [Companion Slides](https://agmath.github.io/RegressionCourse/18d_IntroSlides.html) |  |
| 19 | Read ISLR $\S$ 5.1 ([Part I](https://youtu.be/ngrOYWgJjb4), [Part II](https://youtu.be/rSGzUy13F_0), [Part III](https://youtu.be/r64tRyHFAJ8)) | Performance Concerns Continued: Different Test, Different Expectations <br/> Cross-Validation and Unbiased Model Performance ([html](https://agmath.github.io/RegressionCourse/16d_CrossValidation.html), [Quarto](https://agmath.github.io/RegressionCourse/16d_CrossValidation.qmd)) | [Companion Slides](https://agmath.github.io/RegressionCourse/19d_IntroSlides.html) | Homework 3 |
| 20 |  | Cross-Validation Workshop |  |  |
| 21 | Read ISLR $\S$ 6.1, 6.2 ([Part IV](https://youtu.be/f_hkP_We0JY), [Part V](https://youtu.be/I8bPQ272Pbs), [Part VI](https://youtu.be/FlSQgXv7Dvw), <br/> [Part VII](https://youtu.be/8oEZkHqf_Rk)) | Variable Selection Methods: <br/> Stepwise Regression, Ridge Regression, and the LASSO ([html](https://agmath.github.io/RegressionCourse/17d_VariableSelectionMethods.html), [Quarto](https://agmath.github.io/RegressionCourse/17d_VariableSelectionMethods.qmd)) | [Companion Slides](https://agmath.github.io/RegressionCourse/21d_IntroSlides.html) |  |
| 22 |  | Other Regressors ([html](https://agmath.github.io/RegressionCourse/18d_OtherRegressors.html), [Quarto](https://agmath.github.io/RegressionCourse/18d_OtherRegressors.qmd)) | [Companion Slides](https://agmath.github.io/RegressionCourse/22d_IntroSlides.html) | [Competition Assignment 6](https://agmath.github.io/RegressionCourse/CA6_OtherRegressors_SubmitPredictions.html) | 
| 23 |  | Hyperparameters and Tuning <br/> More uses for Cross-Validation ([html](https://agmath.github.io/RegressionCourse/19d_HyperparameterTuning.html), [Quarto](https://agmath.github.io/RegressionCourse/19d_HyperparameterTuning.qmd)) | [Companion Slides](https://agmath.github.io/RegressionCourse/23d_IntroSlides.html) |  |
| 24 |  | Hyperparameters, Tuning, and Other Regressors Workshop |  |  |
| 25 |  | Thanksgiving Modeling Competition <br/> (In Class, 75-minutes) |  |  |
| 26+ | Projects | Projects | Projects | Projects |

<br/>
<br/>

***

> [1] DeCock, Dean (2011). Ames, Iowa: Alternative to the Boston Housing Data as an End of Semester Regression Project. Journal of Statistics Education Volume 19, Number 3(2011),
http://www.amstat.org/publications/jse/v19n3/decock.pdf
>
> [2] Horst AM, Hill AP, Gorman KB (2020). palmerpenguins: Palmer Archipelago (Antarctica) penguin data. doi:10.5281/zenodo.3960218, R package version 0.1.0, https://allisonhorst.github.io/palmerpenguins/.
>
> [3] Pennington, Kate (2018). Bay Area Craigslist Rental Housing Posts, 2000-2018. Retrieved from https://github.com/katepennington/historic_bay_area_craigslist_housing_posts/blob/master/clean_2000_2018.csv.zip.

***

<br/>
<br/>

[Back to Hompage](https://agmath.github.io/)
