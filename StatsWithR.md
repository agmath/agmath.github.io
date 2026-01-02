---
title: Modern Statistics With Software
description: This is a homepage for MAT241, Modern Statistics with Software, with Dr. Gilbert at Southern New Hampshire University. This course covers an introduction to data, exploratory data analyses and data visualization, one- and two-sample inference via confidence intervals and hypothesis testing for both proportions and means, chi-squared tests for goodness of fit and independence, ANOVA for comparisons of multiple group means, and introduces linear regression. The course also provides and introduction to R, the use of which is embedded throughout the semester.
---

{% include google-analytics.html %}

<script src='https://storage.ko-fi.com/cdn/scripts/overlay-widget.js'></script>
<script>
  kofiWidgetOverlay.draw('agmath', {
    'type': 'floating-chat',
    'floating-chat.donateButton.text': 'Support me',
    'floating-chat.donateButton.background-color': '#794bc4',
    'floating-chat.donateButton.text-color': '#fff'
  });
</script>

## MAT 241 - Modern Statistics with Software (R)

<img src="/SiteFiles/OIstats.jpg" align="left" width=200>[**Syllabus (Spring 2026)**](https://drive.google.com/file/d/1WlUiSTQs0XvUa_BqwwBVDVojSaW50YvS/view?usp=sharing)<br/>
<br/>
***Course Description:*** This is a fundamental course in modern-day data, data visualization, and the application of statistical techniques to analyze and make inferences from sample data. In a world where data is being constantly collected, it is necessary for individuals to be data literate, to have exposure to the power of data, and to understand as well as practice proper and ethical analyses with data. In a world where data has become abundant, rather than scarce, statistical tools are evolving. This course looks at modern statistical techniques in the age of "Big-Data".<br/>
<br/>
**Software Use:** Students in this course should expect to use R and RStudio locally. I’ve written [setup instructions](https://agmath.github.io/IntroductoryStatistics/AccessingInteractiveNotes.html) for all required software and packages for this course. If you are a student planning to complete this course with a Chromebook or tablet, then you may create a [Posit Cloud](https://posit.cloud/) account and copy [this pre-built Posit Cloud Workspace](https://posit.cloud/content/7284986) to utilize R and RStudio from a web-browser.<br/>
<br/>
Still not quite sure what to expect? Check out [this in-browser version of the Day 1 Material](https://agmath.github.io/WebRtutorials/MAT241_Intro.html)

### Course Timeline and Notebooks

Below is a tentative timeline for our course. It includes preparatory work that should be done prior to each class meeting, a description of what to expect during a given class meeting, and assignments following each class meeting. The preparatory work consists of interactive R notebooks and is accessed via the tutorials tab of the rop-right pane in RStudio on Posit.cloud.

| Class Meeting | Before Class | During Class | After Class |
|---------------|--------------|--------------|-------------|
| 1 | [Review Syllabus](https://drive.google.com/file/d/11PBn-bwYvuEowiHy-eWwZE0yq_yPfZiV/view?usp=sharing) <br/> [Setup Software](https://agmath.github.io/IntroductoryStatistics/AccessingInteractiveNotes.html) | [Introduction and What to Expect (Slides)](https://agmath.github.io/IntroductoryStatistics/CourseOverview.html) <br/> Troubleshooting <br/> Data Exploration ([html](https://agmath.github.io/IntroductoryStatistics/Day1_DataExploration.html), or [Quarto](https://www.github.com/agmath/IntroductoryStatistics/blob/main/Day1_DataExploration.qmd)) |  |
| 2 | `01_IntroToData` | Austin Housing Dataset ([html](https://agmath.github.io/IntroductoryStatistics/Days2to5_AustinHousingData.html) or [Quarto](https://www.github.com/agmath/IntroductoryStatistics/blob/main/Days2to5_AustinHousingData.qmd)) <br/> [Companion Slides](https://agmath.github.io/IntroductoryStatistics/D2_IntroToData_Slides.html) | MyOpenMath HW 1 |
| 3 | `02_IntroToR` | Getting Familiar with R <br/> Austin Housing (Cont'd) <br/> [Companion Slides](https://agmath.github.io/IntroductoryStatistics/IntroToR_Slides.html) |  |
| 4 | `03_DescriptiveNumCat` | Exploring and Describing Data <br/> Austin Housing (Cont'd) <br/> [Companion Slides](https://agmath.github.io/IntroductoryStatistics/DescriptiveStatistics_Slides.html) | MyOpenMath HW 2 |
| 5 | `04_DataViz` | Data Visualization <br/> Austin Housing (Cont'd) <br/> [Companion Slides](https://agmath.github.io/IntroductoryStatistics/DataViz_Slides.html) |  |
| 6 | `05_DiscreteDistributions` | Probabilities and Simulation <br/> Doris and Buzz ([html](https://agmath.github.io/IntroductoryStatistics/Day6_DorisBuzzAndMyOpenMath.html) or [Quarto](https://www.github.com/agmath/IntroductoryStatistics/blob/main/Day6_DorisBuzzAndMyOpenMath.qmd)) <br/> or [Companion Slides](https://agmath.github.io/IntroductoryStatistics/DiscreteProbability_Slides.html) |  |
| 7 | `06_NormalDistributions` | Probabilities and Normal Distributions <br/> MyOpenMath Problems ([html](https://agmath.github.io/IntroductoryStatistics/Day7_ProbabilityAndTheNormalDistribution.html) or [Quarto](https://www.github.com/agmath/IntroductoryStatistics/blob/main/Day7_ProbabilityAndTheNormalDistribution.qmd)) <br/> or [Companion Slides](https://agmath.github.io/IntroductoryStatistics/NormalDistProbability_Slides.html) | MyOpenMath HW 4 |
| 8 |  | Discrete Distributions Lab `07_DiscreteDistributionsLab` |  |
| 9 |  | Normal Distributions Lab `08_NormalDistributionLab` |  |
| 10 |  | Exam I, Part I (Group) |  |
| 11 |  | Exam I, Part II (Individual) |  |
| 12 | `09_FoundationsForInference` | More on the Sampling Distribution `10_IntroInferenceLab`, <br/> or [Companion Slides](https://agmath.github.io/IntroductoryStatistics/IntroInference_Slides.html) | MyOpenMath HW 5 |
| 13 | `11_HTandCIprop` | Hypothesis Tests and Confidence Intervals for Proportions <br/> [Companion Slides](https://agmath.github.io/IntroductoryStatistics/CategoricalInference_Slides.html) |  |
| 14 | `12_InferencePractice` | Inference for Categorical Data ([html](https://agmath.github.io/IntroductoryStatistics/Day13and14_InferenceForCategoricalData.html) or [Quarto](https://www.github.com/agmath/IntroductoryStatistics/blob/main/Day13and14_InferenceForCategoricalData.qmd)) <br/> [Companion Slides](https://agmath.github.io/IntroductoryStatistics/CategoricalInferencePractice_Slides.html) | MyOpenMath HW 6 |
| 15 |  | Inference for Categorical Data Lab `13_InferenceCategoricalLab` |  |
| 16 | `14_ChiSquare` | Inference for More than Two Proportions ([html](https://agmath.github.io/IntroductoryStatistics/Day16_YouthBehaviorAndRisk.html) or [Quarto](https://www.github.com/agmath/IntroductoryStatistics/blob/main/Day16_YouthBehaviorAndRisk.qmd)) or <br/> [Companion Slides](https://agmath.github.io/IntroductoryStatistics/ChiSquared_Slides.html) | MyOpenMath HW 7 | 
| 17 | `15_HTandCInum` | Hypothesis Tests and Confidence Intervals for One or Two Means ([html](https://agmath.github.io/IntroductoryStatistics/Day17_InferenceForNumericalData.html) or [Quarto](https://www.github.com/agmath/IntroductoryStatistics/blob/main/Day17_InferenceForNumericalData.qmd)) or <br/> [Companion Slides](https://agmath.github.io/IntroductoryStatistics/NumericalInference_Slides.html) |  |
| 18 |  | Additional Inference Practice, Day I `16_InferencePractice` <br/> [Practice Problems](https://agmath.github.io/IntroductoryStatistics/PracticeInferenceProblems_F24Mixed.html)|  |
| 19 |  | Additional Inference Practice, Day II `16_InferencePractice` (Cont'd) <br/> [Practice Problems](https://agmath.github.io/IntroductoryStatistics/PracticeInferenceProblems_F24Mixed.html) <br/> [Two Examples and Discussion on Error Types](https://agmath.github.io/IntroductoryStatistics/TwoInferenceExamplesSlides.html) | MyOpenMath HW 8 |
| 20 |  | Additional Inference Practice, Day III `16_InferencePractice` (Cont'd) <br/> [Practice Problems](https://agmath.github.io/IntroductoryStatistics/PracticeInferenceProblems_F24Mixed.html) <br/> ["Answer" Key](https://agmath.github.io/IntroductoryStatistics/PracticeInferenceProblems_F24Mixed_Answers.html) |  |
| 21 |  | Inference for Numerical Data Lab `17_InferenceNumericalLab` <br/> [Slides on Reading Software Output](https://agmath.github.io/IntroductoryStatistics/ComputedInferenceSlides.html) | MyOpenMath HW 9 |
| 22 | `18_ANOVA` | Inference for More than Two Means ([html](https://agmath.github.io/IntroductoryStatistics/Day22_PalmerPenguins.html) or [Quarto](https://www.github.com/agmath/IntroductoryStatistics/blob/main/Day22_PalmerPenguins.qmd)) |  |
| 23 |  | Exam II, Part I (Group) |  |
| 24 |  | Exam II, Part II (Individual) |  |
| 25 |  | Linear Regression Lab `19_LinearRegression` or <br/> [ANOVA and Linear Regression Slides](https://agmath.github.io/IntroductoryStatistics/ANOVAandLinearRegressionSlides.html) | MyOpenMath HW 10 |
| 26 |  | Review |  |
| 27 |  | Final Exam, Part I |  |
| 28 |  | Final Exam, Part II (Optional) |  |

[Back to Homepage](https://agmath.github.io/)
