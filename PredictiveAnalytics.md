---
title: Predictive Analytics
description: This is a homepage for QSO370/570, Predictive Analytics, at Southern New Hampshire University. The course covers predictive modeling in both the regression and classification settings. Topics covered include linear and curvi-linear regression, tree-based models, logistic regression, cross-validation, hyperparameter tuning, model assessment, and more.
---

{% include google-analytics.html %}

<script src='https://storage.ko-fi.com/cdn/scripts/overlay-widget.js'></script>
<script>
  kofiWidgetOverlay.draw('agmath', {
    'type': 'floating-chat',
    'floating-chat.donateButton.text': 'Support this work',
    'floating-chat.donateButton.background-color': '#794bc4',
    'floating-chat.donateButton.text-color': '#fff'
  });
</script>

## QSO 370/570 - Predictive Analytics

<img src="/SiteFiles/PredictiveAnalytics.jpg" align="left" width=150>[**Syllabus (Summer 2023)**](https://drive.google.com/file/d/1qLpncU502GH8MyOKrimO3Z2542lPtfpA/view?usp=share_link)<br/>
<br/>
***Course Description:*** This course introduces the techniques of predictive modeling in a data-rich business 
environment in order to predict future business outcomes and associated risks. It covers multivariate and other 
techniques to implement predictive models for a variety of practical business applications.<br/>
<br/>
**Remote, Asynchronous Section:** This particular summer section of Predictive Analytics is being offered in a fully 
remote an asynchronous environment. We'll make heavy use of Slack for interaction and collaboration throughout each
week.<br/>
<br/>
*Students in this course should expect to use Python and Jupyter Notebooks (via Google Colab). Students will work 
through scripted analyses outside of class meetings and then will get their hands dirty, working with real data during 
class time. Applications will vary according to student and instructor interests.*

### Accessing Course Notes

The Jupyter Notebooks for this course can be accessed via Google Colab. You are welcome to copy and utilize the notebooks 
as you see fit. In order to access the notebooks, complete the following steps.  
+ Navigate to [colab.research.google.com](colab.research.google.com).
+ Click the button to *Add to Drive*, which will add Colab functionality to your Google Drive.
+ Here's a [link to a shared folder](https://drive.google.com/drive/folders/1NKhGM_PLrXzsRP5aqecvIrPeJWWYJp-g?usp=share_link) 
with all of the course notes. You should make a copy of these files and save them to your own Google Drive -- this will allow 
you to edit and save your changes.
+ Navigate to the copies you made on your Google Drive. Double-click on the notebook you wish to open and then click on the 
orange CO logo at the top of the page to *open with Colab*.
+ You are now running a live Jupyter Notebook from within Google Drive -- you should treat these as your personal class notes; 
feel free to edit them as you see fit.

#### About Competition Assignments

In addition to traditional homework assignments in this course, students will encounter four assignments related to an 
In-Class Kaggle Competition. These assignments are designed to help with two things: (i) getting practice in building and 
assessing predictive models, and (ii) practice with technical report-writing. The Kaggle Competition will be closed such that 
only students in this course will be able to join, so students will be competing with their peers who are also learning about 
predictive modeling. The competition assignment for the Summer 2023 semester is on predicting the selling prices of used cars. 
A link to the competition is posted in BrightSpace.

### Course Timeline and Notebooks

Below is a tentative timeline for our course. It includes Course Content and Assignments by week.

| Week | Class Content | Assignments |
|---------------|--------------|--------------|
| 0 | [Intro to Class Video](https://youtu.be/pjeqjpvAm88)<br/> [Enabling Google Colaboratory](https://youtu.be/y_yRHa0nF1w) <br/> [Intro to Jupyter Notebooks](https://youtu.be/PiZ4DOz-8Qg) | Start HW 0 |
| 1 | [Terminology Overview Notebook](https://drive.google.com/file/d/17lKP6we86m62OYsn4QGKST3Po-3XF8jD/view?usp=share_link) ([Video Overview](https://youtu.be/wTLqhm42skM)) <br/> [Python for Analytics Notebook](https://drive.google.com/file/d/186A8tMcz_6B0UhpVZVXBTiXjvgnwe5hB/view?usp=share_link) (Videos: [Part I](https://youtu.be/VXKTCAAX-GE), [Part II](https://youtu.be/MR0lOgFiM3g)) | Slack Prompt (Wed) <br/> Slack Prompt (Sun) <br/> HW 0 Due (Sunday, May 7) <br/> Start Group Assign. 1 |
| 2 | [Analytics Overview Notebook](https://drive.google.com/file/d/184n1eYZK9ngIB7S6OzT8pr5OEh4uJT4M/view?usp=share_link) <br/> [What is an Analytics Report?](https://agmath.github.io/RegressionCourse/WhatIsAnAnalyticsReport.html) <br/> Kaggle Competition Overview | Group HW 1 Due (Tues) <br/> Slack Prompt (Wed) <br/> Slack Prompt (Sun) <br/> Enroll in Kaggle Comp <br/> Start Comp. Assign. 1 |
| 3 | [`matplotlib` and `seaborn` Plotting Tutorial](https://drive.google.com/file/d/18kt8fZPlHXFBNRpk2p5TSIW9_tomng3u/view?usp=share_link) <br/> [Sample End-to-End Video](https://youtu.be/crM7yqiXgck) | Comp. Assign. 1 Due (Tues) <br/> Slack Prompt (Wed) <br/> Slack Prompt (Sun) <br/> Start Comp. Assign. 2 |
| 4 | Draft SOP and EDA for Zillow Data <br/> Peer Review (Slack) | Slack Prompt (Wed) <br/> Slack Prompt (Sun)<br/> Post and Peer Review<br/> Continue Comp. Assign. 2 |
| 5 | [Evaluating Regressors](https://drive.google.com/file/d/18jucL0LnWhe1uN2O7lO4bf-YSdHYVN3T/view?usp=share_link)<br/> [Assessing Regressors (Video)](https://youtu.be/I3pEXOCufrk) <br/> [Train/Test Split Explained (Video)](https://youtu.be/CpiTxg6iwS8) | Comp. Assign 2 Due (Tues) <br/> Slack Prompt (Wed) <br/> Slack Prompt (Sun) <br/> Start Group Assign. 2 |
| 6 | [What is Classification (Video)](https://youtu.be/MGM7sA-RTHE)<br/> [Building Several Classifiers (Video)](https://youtu.be/hSzszEssTcE) <br/> [Assessing Classifiers (Video)](https://youtu.be/yHGMOPhq8FU) <br/> [Evaluating Classifiers](https://drive.google.com/file/d/18M85UU8EyJzs_NBv5kV-M2eqnhEq-EzN/view?usp=share_link) <br/> | Group Assign. 2 Due (Tues) <br/> Slack Prompt (Wed) <br/> Slack Prompt (Sun) <br/> Start Group Assign. 3 |
| 7 | [Linear Regression Overview](https://colab.research.google.com/drive/1NjpK2UISh3AR3rs66CkP19YQ-CgAJ76p?usp=share_link) <br/> [Linear Regression, Part I](https://drive.google.com/file/d/18J1sbZ6F813ncCuZ0Qq6qvDlAY-QoWcU/view?usp=share_link) <br/> [Submitting Model Predictions to Kaggle](https://youtu.be/STXsdwCc9Yc) | Slack Prompt (Wed) <br/> Slack Prompt (Sun) <br/> Start Comp. Assign. 3 |
| 8 | [Model-Building Frameworks](https://youtu.be/4vUvJzryco4) <br/> [Linear Regression, Part II](https://drive.google.com/file/d/18H5kNtdAniZprW3lyVQ3LxxlVOGrGzSY/view?usp=share_link) | Comp. Assign. 3 Due (Tues) <br/> Slack Prompt (Wed) <br/> Slack Prompt (Sun) <br/> Start Group Assign. 4 |
| 9 | [Regression Trees](https://drive.google.com/file/d/18B4AGNHGvaYHIg9B5n2P6sbOvq5lfZKG/view?usp=share_link) | Group Assign. 4 Due (Tues) <br/> Slack Prompt (Wed) <br/> Slack Prompt (Sun) <br/> Start Comp. Assign. 4 |
| 10 | [Classification Trees](https://drive.google.com/file/d/18ASV4NZu-W-DTG1i6G0Rlo_YBSOCPHqZ/view?usp=share_link) <br/> Classification Models and Zillow Data | Slack Prompt (Wed) <br/> Slack Prompt (Sun) <br/> Continue Comp Assign. 4 |
| 11 | [Logistic Regression](https://drive.google.com/file/d/189IJNNzXxWgc5HIcwZq2y9xVrikRaFFV/view?usp=share_link) | Comp. Assign. 4 Due (Tues) <br/> Slack Prompt (Wed) <br/> Slack Prompt (Sun) |
| 12+ | Advanced Module Work | Time Series, Unsupervised Learning, or <br/> Statistics and Analytics for Dissertation/Thesis |

***

<br/>
<br/>

[Back to Hompage](https://agmath.github.io/)
