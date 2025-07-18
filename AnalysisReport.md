# 📊 Student Exam Performance Analysis Report

---

## 📁 Dataset Column Information

* **gender**: Sex of the students
* **race\_ethnicity**: Ethnicity of students (Groups A to E)
* **parental\_level\_of\_education**: Parent's education level
* **lunch**: Lunch before the test (standard / free/reduced)
* **test\_preparation\_course**: Completed or not
* **math\_score**: Student's score in math
* **reading\_score**: Student's score in reading
* **writing\_score**: Student's score in writing

---

## 📌 Descriptive Statistics & Initial Observations

1. **Scores Summary**:

   * All three scores (math, reading, writing) have similar means (\~66–70) and standard deviations (\~15).
   * Q1, Q2, Q3 are tightly packed for all three scores.
   * Math score has a minimum of **0**, suggesting a few extremely low performers. Reading and writing minimums are higher.
   * **3 students** scored full marks in all tests. Their background:

     * Parental education: *bachelor's* or *associate's degree*
     * Lunch: *standard*
     * Group: *E*

2. **Gender-based Math Score Insight**:

   * Males generally perform better in math.
   * Females show more **variance** and **outliers**, with scores even below 30.
   * Distribution is **slightly left-skewed**, concentrated in 50–80.

3. **Gender-based Reading Score Insight**:

   * Females significantly outperform males.
   * IQR for females: 80–100 vs males: 55–75.
   * Males show wider spread and cluster around 55–70.

4. **Gender-based Writing Score Insight**:

   * Similar pattern as reading — females dominate.
   * Female IQR: 65–80 vs male IQR: 55–75.
   * Male scores have more lower spread.

---

## 🧬 Categorical Variable Notes

### race\_ethnicity

* Format: includes the word *"group"* (e.g., group A)
* No missing or duplicate values.
* 5 unique categories:

  * Group C: 319
  * Group D: 262
  * Group B: 190
  * Group E: 140
  * Group A: 89

### parental\_level\_of\_education

* Category Counts:

  * some college: 226
  * associate's degree: 222
  * high school: 196
  * some high school: 179
  * bachelor's degree: 118
  * master's degree: 59

### lunch

* Categories:

  * standard: 645
  * free/reduced: 355
* Suggestion: Could be re-encoded as

  * *standard*
  * *other*

### test\_preparation\_course

* Values:

  * completed: 358
  * none: 642

---

## 📈 Score Distributions and Correlations

* **All scores are highly correlated**:

  * Math ↔ Reading: 0.82
  * Reading ↔ Writing: 0.95
  * Math ↔ Writing: 0.80
* Implication: **Strong linear relationship** between all three scores.
* Literacy skills (reading + writing) are especially linked.
* Math may involve separate reasoning abilities but still correlates well.

---

## 🎯 Target Variable

* We create two additional columns:

  * `total_score = math + reading + writing`
  * `avg_score = total_score / 3`
* These can serve as target variables for prediction or ranking.

---

## 🔍 Key Insights

### Gender

* **Female students outperform male students overall**, especially in reading and writing.
* Males do slightly better in math but with fewer low-end outliers.

### Lunch

* **Standard lunch is strongly associated with better performance** — regardless of gender.

### Parental Education

* **Higher education level of parents** → better average scores.
* Students of parents with *bachelor's* and *master's* degrees are among top performers.
* Still, high variability exists.

### Race/Ethnicity

* **Groups A and B** perform worse on average — regardless of gender.
* Group C is the most common group.

### Test Preparation Course

* Students who **completed the course** scored higher.
* However, **more students did not** complete the course.

---

## 📌 Summary of Score Patterns

* Median of **math** is slightly lower than reading and writing.
* All three score distributions are **approximately normal**.
* IQR for all scores: **60–80**
* Avg score is balanced due to similar reading/writing scores despite lower math median.

---

## ✅ Final Takeaways

* **Female students dominate** performance metrics.
* **Standard lunch and test preparation** are strong performance influencers.
* **Parental education** and **race/ethnicity** also impact, but not deterministically.
* All scores are **highly linearly correlated**, allowing consolidated metrics (e.g., avg\_score) for modeling or ranking.

---

