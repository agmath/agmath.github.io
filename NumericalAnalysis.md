---
title: Numerical Analysis
description: This is a homepage for MAT370, Numerical Analysis, with Dr. Gilbert at Southern New Hampshire University. This course covers numerical methods for solving problems in engineering and physics. Students will use Python to implement algorithms and analyze their performance.
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

## MAT 370 - Numerical Analysis

<div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap;">
  <!-- Left Side: Your Info -->
  <div style="display: flex; align-items: center; max-width: 75%;">
    <img src="/SiteFiles/Numerical.jpg" alt="Textbook Cover" style="width: 200px; margin-right: 20px;">
    <div>
      <p style="margin: 0;"><a href="https://drive.google.com/file/d/1XaGNKAAmVbTOZnRMp-5c51GMivslTHcu/view?usp=sharing"><strong>Syllabus (Spring 2026)</strong></a></p>
      <p style="margin: 0;"><strong>Course Description:</strong> This course introduces basic techniques for the efficient numerical solution of problems in engineering, mathematics, and science. Topics covered may include: root finding methods, interpolation, numerical differentiation and integration, numerical solutions of differential equations, and matrix theory concepts such as QR factorization and singular value decompositions. Students will utilize industry-standard software for simulations.</p>
    </div>
  </div>
</div>

### Course Timeline and Notebooks

Below is a tentative timeline for our course. It includes preparatory work that should be done prior to each class meeting, a detailed set of notes corresponding to each class meeting, and assignments following each class meeting. 

| Class Meeting | Before Class | During Class | After Class |
|---------------|--------------|--------------|-------------|
| 1 | Review Syllabus <br/> [Setup Google Colab](https://youtu.be/y_yRHa0nF1w) | Introduction and What to Expect ([Slides](https://agmath.github.io/NumericalMethodsCourse/Slides/D1_WhatToExpect.html)) <br/> [Intro to Python and Jupyter Notebooks](https://colab.research.google.com/drive/1HI1jjQwaNEvCqhO0oB6G0poNf8U0xhAR?usp=share_link) <br/> `0.1 + 0.2 != 0.3` |  |
| 2 |  | [Binary and Floating Point Numbers](https://colab.research.google.com/drive/1EkX8eT_xd_FWY5xT_cDdleOtGDXnhc5c?usp=sharing) <br/> Companion Slides ([HTML](https://agmath.github.io/NumericalMethodsCourse/Slides/D2_BinaryAndFloatingPointNumbers.html) or PDF) | HW 1 |
| 3 |  | [Crash course in numerical Python](https://colab.research.google.com/drive/1MaA4oI_XMVzbItClewib7JC5yg6HExT2?usp=share_link) <br/> Companion Slides ([HTML](https://agmath.github.io/NumericalMethodsCourse/Slides/D3_CrashCourseInNumericalPython.html) or PDF) |  |
| 4 |  | [Colab, Python, and LaTeX Workshop](https://colab.research.google.com/drive/1TJSmoRkBTAQABnpeksx5snvc9bzzYeMG?usp=drive_link) <br/> Companion Slides ([HTML](https://agmath.github.io/NumericalMethodsCourse/Slides/D4_LatexWorkshop.html) or PDF) |  |
| 5 | [A Reminder on Linear Systems](https://colab.research.google.com/drive/1F52HxFUyLrDGVihejng_GGBj4Z5qkKTy?usp=share_link) | [Gaussian Elimination](https://colab.research.google.com/drive/1vkPJJtYTqlMljTIMkbNgaArY5gCRhf_M?usp=share_link) <br/> Companion Slides ([HTML](https://agmath.github.io/NumericalMethodsCourse/Slides/D5_GaussianElimination.html) or PDF) | HW 2 |
| 6 |  | [LU Decomposition](https://colab.research.google.com/drive/1KzEdYJ2_g5M-z5EPo1xbJBfMmG9IeKdu?usp=share_link) <br/> Companion Slides ([HTML](https://agmath.github.io/NumericalMethodsCourse/Slides/D6_LUdecomposition.html) or PDF) |  |
| 7 |  | [Symmetric and Banded Coefficient Matrices](https://colab.research.google.com/drive/1KzZTk4XlEZeIIZ9kkjEf7D7N-NHPpFAQ?usp=share_link) <br/> Companion Slides ([HTML](https://agmath.github.io/NumericalMethodsCourse/Slides/D7_SymmetricAndBanded.html) or PDF) | HW 3 |
| 8 |  | [Pivoting](https://colab.research.google.com/drive/1J280pKDfqORfCTilFEZ5sNq7RV-NXFct?usp=share_link) <br/> Companion Slides ([HTML](https://agmath.github.io/NumericalMethodsCourse/Slides/D8_Pivoting.html) or PDF) |  |
| 9 | [A Reminder on Interpolation and Curve Fitting](https://colab.research.google.com/drive/1d4O2oYnmTaohrYTol0lRlBgL-dUam--4?usp=share_link) | [Polynomial Interpolation](https://colab.research.google.com/drive/1b3tsjx216S9tquclHCw8wVACbo-sEVUK?usp=share_link) | HW 4 |
| 10 |  | [Cubic Splines](https://colab.research.google.com/drive/1lHM4cLSnqGaSC0Emtk8dUlGS_Y78vtGE?usp=share_link) |  |
| 11 |  | [Least Squares](https://colab.research.google.com/drive/1nuIxSYIymLH70FVZDHUstt5pOrG3i66a?usp=share_link) |  |
| 12 |  | Catch-Up Day |  |
| 13 |  | Unit Problem Set I, Day 1 |  |
| 14 |  | Unit Problem Set II, Day 2 |  |
| 15 | [A Reminder on Root-Finding](https://colab.research.google.com/drive/13INH6NOkf4-TWlgVMWqN78NqUv4BAQLg?usp=share_link) | [Root Finding: Incremental Search and the Bisection Method](https://colab.research.google.com/drive/1ERp1VyGwatckBBIh7EyQlh1k7-mRTGI0?usp=share_link) | HW 5 |
| 16 |  | [Root Finding: Linear Interpolation Methods](https://colab.research.google.com/drive/1VXdLruu7fOtEa3S24Wszp_5s2bfSBx1l?usp=share_link) |  |
| 17 |  | [Root Finding: Simultaneous Systems](https://colab.research.google.com/drive/1-WrhpjVh4JMPQAOKmZ_HkjhlLSJSqFXM?usp=share_link) |  |
| 18 |  | Catch-Up Day |  |
| 19 | [A Reminder on Differentiation and Function Approximation](https://colab.research.google.com/drive/10t4JdYJPu2nOGHRNNaKLICUxW0_IM62o?usp=share_link) | [Differentiation: Finite Difference Approximation](https://colab.research.google.com/drive/1Q8TD1NQd9Tvnc2Eiq-LMOBfwiD7RbfWq?usp=share_link) | HW 6 |
| 20 |  | [Differentiation: Improving Estimates via Richardson Extrapolation and Derivatives via Interpolation for non-Equispaced or Noisy Observations](https://colab.research.google.com/drive/1CcZdPBFnqav-yng9vauQEElw2hqS8PRK?usp=share_link) |  |
| 21 | [A Reminder on Numerical Integration Techniques](https://colab.research.google.com/drive/12HqDz8lvGRevG9Z0293yUcpYElLP-0Xp?usp=share_link) | [Integration: Newton-Cotes Formulae](https://colab.research.google.com/drive/1QmuqtCSgBLrXUd3s0DgawAuFnBbtfp-m?usp=share_link) | HW 7 |
| 22 |  | [Integration: Romberg Integration](https://colab.research.google.com/drive/1AxUjmOifSbxwxcbhz3UkM8-SWH5_LVhg?usp=sharing) |  |
| 23 | [A Reminder on Initial Value Problems](https://colab.research.google.com/drive/1dC8E_IwIvn8Tsz2ZtJZGfrE8BZ5h8OQG?usp=share_link) | [IVPs: Euler's Method](https://colab.research.google.com/drive/1TxU9gQLYSNr8SeEJ0B3dHCs1egxmd4Nv?usp=share_link) | HW 8 |
| 24 |  | [IVPs: Runge-Kutta Methods](https://colab.research.google.com/drive/1DQxMKrM7N5aoDHfgb8nlx5O215iJpe1i?usp=share_link) |  |
| 25 |  | Reflection Project Overview |  |
| 26 |  | Reflection Project Intention Mini-Meetings |  |
| 27 |  | Unit Problem Set II, Day 1 |  |
| 28 |  | Unit Problem Set II, Day 2 |  |
| 29 |  | Debrief Interviews |  |
| 30 |  | Debrief Interviews |  |

<br/>
<br/>

***

<br/>
<br/>

[Back to Hompage](https://agmath.github.io/)
