---
title: Modern Statistics With Software
description: This is a homepage for MAT241, Modern Statistics with Software, with Dr. Gilbert at Southern New Hampshire University. This course covers an introduction to data, exploratory data analyses and data visualization, one- and two-sample inference via confidence intervals and hypothesis testing for both proportions and means, chi-squared tests for goodness of fit and independence, ANOVA for comparisons of multiple group means, and introduces linear regression. The course also provides and introduction to R, the use of which is embedded throughout the semester.
---

{% include google-analytics.html %}

## MAT 241 - Modern Statistics with Software (R)

<img src="/SiteFiles/OIstats.jpg" align="left" width=200>[**Syllabus (Spring 2024)**](https://drive.google.com/file/d/1hR-T8kcUY4uHKCs3Y4A6lCcW20Z4KlUb/view?usp=sharing)<br/>
<br/>
***Course Description:*** This is a fundamental course in modern-day data, data visualization, and the application of statistical techniques to analyze and make inferences from sample data. In a world where data is being constantly collected, it is necessary for individuals to be data literate, to have exposure to the power of data, and to understand as well as practice proper and ethical analyses with data. In a world where data has become abundant, rather than scarce, statistical tools are evolving. This course looks at modern statistical techniques in the age of "Big-Data".<br/>
<br/>
*Students in this course should expect to use R via RStudio either using [Posit.cloud](https://posit.cloud/) or a local installation of R and RStudio if you wish. The notebooks and all required packages are pre-loaded at [this Posit.cloud workspace](https://posit.cloud/content/7284986), which can be copied once you are logged in with your own free account. Students will work through scripted workbooks outside of class meetings (more on this below) and then will get their hands dirty, working with real data during class time. Applications will vary according to student and instructor interests.*<br/>

### Course Timeline and Notebooks

Below is a tentative timeline for our course. It includes preparatory work that should be done prior to each class meeting, a description of what to expect during a given class meeting, and assignments following each class meeting. The preparatory work consists of interactive R notebooks and is accessed via the tutorials tab of the rop-right pane in RStudio on Posit.cloud.

| Class Meeting | Before Class | During Class | After Class |
|---------------|--------------|--------------|-------------|
| 1 | [Review Syllabus](https://drive.google.com/file/d/1CqDPrAmPqWUxgGt8_Wiyes-ZovPjOfB-/view?usp=sharing) <br/> Create [Posit.cloud](posit.cloud) account and [access materials](https://posit.cloud/content/6230957) | Introduction and What to Expect <br/> Troubleshooting <br/> Data Exploration ([html](https://agmath.github.io/IntroductoryStatistics/Day1_DataExploration.html), or [Quarto](https://agmath.github.io/IntroductoryStatistics/Day1_DataExploration.qmd)) |  |
| 2 | `01_IntroToData` | Exploring Austin Housing Dataset ([html](https://agmath.github.io/IntroductoryStatistics/Days2to5_AustinHousingData.html) or [Quarto](https://agmath.github.io/IntroductoryStatistics/Days2to5_AustinHousingData.qmd)) | MyOpenMath HW 1 |
| 3 | `02_IntroToR` | Getting Familiar with R <br/> Austin Housing (Cont'd) |  |
| 4 | `03_DescriptiveNumCat` | Reading, exploring, and describing data in R <br/> Austin Housing (Cont'd) | MyOpenMath HW 2 |
| 5 | `04_DataViz` | Data Visualization <br/> Austin Housing (Cont'd) |  |
| 6 | `05_DiscreteDistributions` | Probabilities and Simulation <br/> Doris and Buzz ([html](https://agmath.github.io/IntroductoryStatistics/Day6_DorisBuzzAndMyOpenMath.html) or [Quarto](https://agmath.github.io/IntroductoryStatistics/Day6_DorisBuzzAndMyOpenMath.qmd) |  |
| 7 | `06_NormalDistributions` | Probabilities and Normal Distributions <br/> MyOpenMath Problems ([html](https://agmath.github.io/IntroductoryStatistics/Day7_ProbabilityAndTheNormalDistribution.html) or [Quarto](https://agmath.github.io/IntroductoryStatistics/Day7_ProbabilityAndTheNormalDistribution.qmd) | MyOpenMath HW 4 |
| 8 |  | Discrete Distributions Lab `07_DiscreteDistributionsLab` |  |
| 9 |  | Normal Distributions Lab `08_NormalDistributionLab` |  |
| 10 |  | Exam I, Part I (Group) |  |
| 11 |  | Exam I, Part II (Individual) |  |
| 12 | `09_FoundationsForInference` | More on the Sampling Distribution `10_IntroInferenceLab` | MyOpenMath HW 5 |
| 13 | `11_HTandCIprop` | Hypothesis Tests and Confidence Intervals for Proportions |  |
| 14 | `12_InferencePractice` | Inference for Categorical Data ([html](https://agmath.github.io/IntroductoryStatistics/Day13and14_InferenceForCategoricalData.html) or [Quarto](https://agmath.github.io/IntroductoryStatistics/Day13and14_InferenceForCategoricalData.qmd)) | MyOpenMath HW 6 |
| 15 |  | Inference for Categorical Data Lab `13_InferenceCategoricalLab` |  |
| 16 | `14_ChiSquare` | Inference for more than two proportions ([html](https://agmath.github.io/IntroductoryStatistics/Day16_YouthBehaviorAndRisk.html) or [Quarto](https://agmath.github.io/IntroductoryStatistics/Day16_YouthBehaviorAndRisk.qmd)) | MyOpenMath HW 7 | 
| 17 | `15_HTandCInum` | Hypothesis Tests and Confidence Intervals for One or Two Means ([html](https://agmath.github.io/IntroductoryStatistics/Day17_InferenceForNumericalData.html) or [Quarto](https://agmath.github.io/IntroductoryStatistics/Day17_InferenceForNumericalData.qmd)) |  |
| 18 |  | Additional Inference Practice, Day I `16_InferencePractice`|  |
| 19 |  | Additional Inference Practice, Day II `16_InferencePractice` (Cont'd) | MyOpenMath HW 8 |
| 20 |  | Additional Inference Practice, Day III `16_InferencePractice` (Cont'd) |  |
| 21 |  | Inference for Numerical Data Lab `17_InferenceNumericalLab` | MyOpenMath HW 9 |
| 22 | `18_ANOVA` | Inference for more than two means ([html](https://agmath.github.io/IntroductoryStatistics/Day22_PalmerPenguins.html) or [Quarto](https://agmath.github.io/IntroductoryStatistics/Day22_PalmerPenguins.qmd)) |  |
| 23 |  | Exam II, Part I (Group) |  |
| 24 |  | Exam II, Part II (Individual) |  |
| 25 |  | Linear Regression Lab `19_LinearRegression` | MyOpenMath HW 10 |
| 26 |  | Discussion on Statistical Modeling and Machine Learning |  |
| 27 |  | Review |  |
| 28 |  | Final Exam, Part I |  |
| 29 |  | Final Exam, Part II (Optional) |  |

[Back to Homepage](https://agmath.github.io/)
