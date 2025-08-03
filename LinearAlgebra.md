---
title: Applied Linear Algebra
description: This is a homepage for MAT350, Linear Algebra, with Dr. Gilbert at Southern New Hampshire University. This course covers linear systems, matrix algebra, determinants, vector spaces, and also eigenvalues and eigenvectors. Applications including, but not limited to, economics, electrical engineering, computer graphics, difference equations, and markov chains will be highlighted.
use_math: true
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

## MAT 350 -- Applied Linear Algebra

<script>
MathJax = {
  tex: {
    inlineMath: [['$', '$'], ['\\(', '\\)']]
  },
  svg: {
    fontCache: 'global'
  }
};
</script>
<script type="text/javascript" id="MathJax-script" async
  src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-svg.js">
</script>

<a href="https://agmath.github.io/Austin_ULA_Python/frontmatter.html"><img src="/SiteFiles/ula-cover.png" alt="Textbook Cover and Link"
           style="width: 200px; height: auto; margin-right: 20px;"></a>[**Draft Syllabus** (Subject to Change)](https://drive.google.com/file/d/1YF8NRdSParExTZtrjcerk577bGoildxJ/view)<br/>
<br/>
***Course Description:*** This is a first course in linear algebra and matrices. Topics include systems of linear equations, linear independence, matrices of linear transformations, matrix algebra, determinants, vector spaces, eigenvalues, and eigenvectors. After mastering basic concepts and skills, students will use their knowledge of linear algebra to model a selection of applied mathematics problems in business, science, computer science, and economics.<br/>
<br/>

### Course Timeline and Notebooks

Below will eventually be a tentative timeline for our course. It includes a detailed set of notes corresponding to each class meeting and assignments following each class meeting. Note that assignments are all available on [MyOpenMath](https://www.myopenmath.com/).

| Class Meeting | Before Class | During Class | After Class |
|---------------|--------------|--------------|-------------|
| 1 | Review Syllabus <br/> [Set Up Google Colab](https://youtu.be/y_yRHa0nF1w) | Introduction and What to Expect <br/> [$\S$ 1.1 - What Can We Expect?](https://colab.research.google.com/drive/1ir6YUjoJFEB-Aj0n-pgVKsF-tqGeuDfz?usp=sharing) | Week 1 Assignment <br/> Homework 0 |
| 2 | [3Blue1Brown: Vectors](https://www.3blue1brown.com/lessons/vectors) | [Vector Arithmetic and Operations](https://colab.research.google.com/drive/1IZlf9zma8BSbLvfvGWBMJWs6d1eNdzZF?usp=sharing) | Homework 1 |
| 3 |  | [Matrix Arithmetic and Operations](https://colab.research.google.com/drive/1qqUkC2shyA9mDQx6PmPKpfjwtxMDZFAz?usp=sharing) | Homework 1 (Cont'd) |
| 4 |  | [$\S$ 1.2 - Finding Solutions to Linear Systems](https://colab.research.google.com/drive/1JbZrf8-2d0Q_MLHqhXfHcrr4xKSWfyG5?usp=sharing) | Homework 2 |
| 5 |  | [$\S$ 1.3 - Computation with Python](https://colab.research.google.com/drive/1iM8ILkxRwuoAnDDHgLYtTvG7bCpKusOO?usp=sharing) |  |
| 6 |  | [$\S$ 1.4 - Pivots and their Influence on Solution Spaces](https://colab.research.google.com/drive/18C0zcVB8LNTyuzhhbyoKw7jNPTUglP2T?usp=sharing) | Homework 3 |
| 7 |  | [Row-Reduction Workshop](https://colab.research.google.com/drive/1c5LK6HftxMSXcvlWbPQ_jebeYiLxkWx6?usp=sharing) <br/> Initial Row-Reduction Gateway Exam |  |
| 8 |  [3Blue1Brown: Linear Combinations, Spans, and Bases](https://www.3blue1brown.com/lessons/span) | [$\S$ 2.1 - Vectors and Linear Combinations](https://colab.research.google.com/drive/1B0-C2e9isVL0Hrop6Ru0GPB0EK0a5-zM?usp=sharing) | Homework 4 |
| 9 | [3Blue1Brown: Linear Transformation](https://www.3blue1brown.com/lessons/linear-transformations) | [$\S$ 2.2 - Matrix Multiplication and Linear Combinations](https://colab.research.google.com/drive/1TYz94NlBBK_vUHykvR8PZu1pWGyW9WCD?usp=sharing) | Homework 4 (Cont'd) |
| 10 |  | [$\S$ 2.3 - The Span of a Set of Vectors](https://colab.research.google.com/drive/11lTnfgpN4Am7mgW6W-vx4BRXMDpSJ3BK?usp=sharing) | Homework 5 |
| 11 |  | [$\S$ 2.4 - Linear Independence](https://colab.research.google.com/drive/19E9xMh4mlbRm-jHVOxGV1ALNWkSZr2uT?usp=sharing) | Homework 5 (Cont'd) |
| 12 | [3Blue1Brown: Matrix Multiplication](https://www.3blue1brown.com/lessons/matrix-multiplication) | [$\S$ 2.5 - Matrix Transformations](https://colab.research.google.com/drive/1JDOkiVDkALyFRTzTJ5LWOJM2CWEY1S07?usp=sharing) | Homework 6 |
| 13 | [3Blue1Brown: 3D Transformations](https://www.3blue1brown.com/lessons/3d-transformations) | [$\S$ 2.6 - The Geometry of Matrix Transformations](https://colab.research.google.com/drive/1JFgWI29BdJnEE2o0nAKl1q255_5FD7DE?usp=sharing) | Homework 6 (Cont'd) |
| 14 |  | Group Exam I |  |
| 15 |  | Individual Exam I |  |
| 16 | [3Blue1Brown: Inverse Matrices, Rank, and Null Space](https://www.3blue1brown.com/lessons/inverse-matrices) | [$\S$ 3.1 - Invertibility](https://colab.research.google.com/drive/10GADmto0_9mqEExblaLDrtmbJ1AxVmFS?usp=sharing) | Homework 7 |
| 17 | [3Blue1Brown: Change of Basis](https://www.3blue1brown.com/lessons/change-of-basis) | [$\S$ 3.2 - Bases and Coordinate Systems](https://colab.research.google.com/drive/1_Q6RAQ_ONSmMx42gZzdKa0B8Ku_T1ptz?usp=sharing) | Homework 8 |
| 18 |  | [$\S$ 3.3 - Image Compression](https://colab.research.google.com/drive/1A3cNajddmvKqYPijgBxPNKq4yFWXGxB2?usp=sharing) <br/> ([In-Class Version](https://colab.research.google.com/drive/1Q3h8WSuEdn97ePVdXNg65mx-ng_Gtdtr?usp=sharing)) |  |
| 19 | [3Blue1Brown: Determinants](https://www.3blue1brown.com/lessons/determinant) | [$\S$ 3.4 - Determinants](https://colab.research.google.com/drive/1xlYb9vuo1i7XJgpCOmnv0U7CSHnzPcRN?usp=sharing) | Homework 9 <br/> [3Blue1Brown: Cramer's Rule](https://www.3blue1brown.com/lessons/cramers-rule) |
| 20 |  | [$\S$ 3.5 - Subspaces](https://colab.research.google.com/drive/1svHYfPQWK1Si2nCaij2oCPNwuMhZFQe_?usp=sharing) | Homework 10 |
| 21 | [3Blue1Brown: Eigenvalues and Eigenvectors](https://www.3blue1brown.com/lessons/eigenvalues) | [$\S$ 4.1 - An Introduction to Eigenvectors and Eigenvalues](https://colab.research.google.com/drive/11glm_2X4oX9jH04L7wi-egbKNe_r4WG6?usp=sharing) | Homework 11 |
| 22 |  | [$\S$ 4.2 - Finding Eigenvalues and Eigenvectors](https://colab.research.google.com/drive/100afzj2WgAiY00lrbcaUkih2_vvbMdgf?usp=sharing) | Homework 11 (Cont'd) |
| 23 |  | Group Exam II |  |
| 24 |  | Individual Exam II |  |
| 25 |  | [$\S$ 4.3 - Diagonalization, Similarity, and Powers of a Matrix](https://colab.research.google.com/drive/1ebmYyoODEDXiTb59vMIKT9SYe0Aw4Nhw?usp=sharing) | Homework 12 (Optional) |
| 26 |  | [$\S$ 4.4 - Dynamical Systems](https://colab.research.google.com/drive/1SEk377sz2S33F618fsA-bPHh_QOZgQYs?usp=sharing) <br/> ([In-Class Version](https://colab.research.google.com/drive/1zSdcpCGkZokPD1lU6LhnZ2cIoW3zTVy3?usp=sharing)) | Homework 13 (Optional) |
| 27 |  | [$\S$ 4.5 - Markov Chains and Google's PageRank Algorithm](https://colab.research.google.com/drive/1pmCGIaAWupgjRNmpvQG57122iVd9sEHD?usp=sharing) | Homework 14 (Optional) |
| 28 |  | Review |  |
| 29 |  | Final, Part I (Required) |  |
| 30 |  | Final, Part II (Optional) |  |

<br/>
<br/>

***

<br/>
<br/>

[Back to Hompage](https://agmath.github.io/)
