# Quiz Questions: Causal Inference in Large Language Models

**Total Questions**: 15  
**Topic**: Causality Fundamentals, Propensity Score Matching, Mediation Analysis, LLM-Specific Causal Concepts

---

## Question 1: Correlation vs Causation

In an LLM study, researchers observe that longer prompts tend to produce longer completions. They conclude that "prompt length causes longer completions." What is the most accurate assessment of this conclusion?

A) The conclusion is correct because the correlation is strong and statistically significant
B) The conclusion is incorrect because correlation does not imply causation
C) The conclusion is correct if they use a large enough sample size
D) The conclusion is correct only if they control for temperature settings

**Correct Answer: B**

**Explanation**: Correlation does not imply causation. The observed association between prompt length and completion length could be due to confounding factors (e.g., more complex topics requiring both longer prompts and longer explanations), reverse causation, or common causes. To establish causation, we need to identify the causal mechanism, control for confounders, and ideally conduct experiments or use causal inference methods. A strong correlation alone is insufficient for causal claims.

**Why other options are incorrect**:
- A: Statistical significance does not establish causation; it only indicates the correlation is unlikely due to chance
- C: Sample size improves statistical power but does not address the fundamental correlation-causation distinction
- D: Controlling for temperature might reduce some bias but does not address the fundamental issue that correlation alone cannot prove causation

---

## Question 2: Potential Outcomes Framework

In the Rubin Causal Model, the fundamental problem of causal inference refers to:

A) The difficulty of choosing the right statistical model
B) The impossibility of observing both potential outcomes for the same unit
C) The challenge of collecting enough data for causal analysis
D) The complexity of estimating treatment effects in high-dimensional settings

**Correct Answer: B**

**Explanation**: The fundamental problem of causal inference is that for any unit, we can only observe one of the two potential outcomes (Y(1) if treated, Y(0) if not treated), never both simultaneously. This makes direct calculation of the individual treatment effect Y(1) - Y(0) impossible. Causal inference methods are designed to estimate this unobservable quantity using observed data and assumptions.

**Why other options are incorrect**:
- A: Model selection is important but not the fundamental problem
- C: Data collection is practical but not theoretical fundamental problem
- D: High-dimensional estimation is a challenge but not the core conceptual problem

---

## Question 3: Confounders in LLM Experiments

In a study comparing chain-of-thought (CoT) vs. direct prompting on mathematical reasoning, researchers use CoT for harder problems and direct prompting for easier problems. What type of bias does this introduce?

A) Selection bias
B) Confounding bias
C) Information bias
D) Attrition bias

**Correct Answer: B**

**Explanation**: This introduces **confounding bias** because task difficulty is a confounder: it affects both the treatment assignment (harder problems more likely to receive CoT) and the outcome (harder problems have lower accuracy regardless of prompting strategy). The estimated effect of CoT will be confounded with task difficulty, making it impossible to determine whether differences in performance are due to the prompting strategy or the underlying problem difficulty.

**Why other options are incorrect**:
- A: Selection bias refers to systematic differences between included and excluded units, not treatment assignment patterns
- C: Information bias refers to measurement errors, not assignment mechanisms
- D: Attrition bias occurs when units drop out of the study, not related to initial treatment assignment

---

## Question 4: Propensity Score Definition

The propensity score e(X) is defined as:

A) P(Y=1 | X) - the probability of the outcome given covariates
B) P(T=1 | X) - the probability of treatment given covariates
C) P(X=1 | T) - the probability of covariates given treatment
D) P(T=1 | Y, X) - the probability of treatment given outcome and covariates

**Correct Answer: B**

**Explanation**: The propensity score e(X) = P(T=1 | X) is the probability of receiving treatment conditional on observed covariates X. This single scalar value summarizes all information about covariates relevant to treatment assignment, allowing for dimensionality reduction while preserving balancing properties. Units with the same propensity score should have similar distributions of covariates, regardless of treatment status.

**Why other options are incorrect**:
- A: P(Y=1 | X) is the outcome probability, not treatment probability
- C: P(X=1 | T) reverses the conditioning and doesn't make sense in this context
- D: Including Y in the conditioning would violate the causal framework (Y is the outcome)

---

## Question 5: DAG - Backdoor Paths

In a causal graph showing "Prompt Format → Task Completion" with a backdoor path "Prompt Format ← Task Difficulty → Task Completion", how do we identify the causal effect of Prompt Format on Task Completion?

A) Close the backdoor path by conditioning on Task Difficulty
B) Open the backdoor path by conditioning on Task Completion
C) Use instrumental variables to estimate the direct path
D) Remove the edge between Prompt Format and Task Completion

**Correct Answer: A**

**Explanation**: To identify the causal effect, we must block (close) non-causal (backdoor) paths between treatment and outcome. The path "Prompt Format ← Task Difficulty → Task Completion" is a backdoor path because it starts with an arrow pointing into the treatment. Conditioning on Task Difficulty blocks this path, allowing us to isolate the causal effect through the front-door path "Prompt Format → Task Completion."

**Why other options are incorrect**:
- B: Conditioning on the outcome (Task Completion) would create a collider and introduce bias
- C: Instrumental variables are used when there are unobserved confounders, not when we can condition on observed confounders
- D: Removing the causal path would eliminate the effect we want to estimate

---

## Question 6: Balance Checking After Matching

After performing propensity score matching, you check balance and find that the Standardized Mean Difference (SMD) for a covariate is 0.15. What does this indicate?

A) Perfect balance has been achieved
B) Good balance has been achieved (SMD < 0.1)
C) Moderate imbalance remains, consider refining the matching
D) Severe imbalance, the matching has failed completely

**Correct Answer: C**

**Explanation**: An SMD of 0.15 indicates **moderate imbalance**. While there is some improvement from the unmatched state, balance is not yet satisfactory. Standard guidelines suggest SMD < 0.1 indicates good balance, SMD 0.1-0.2 indicates moderate imbalance, and SMD > 0.2 indicates severe imbalance. The researcher should consider refining the matching (e.g., adjusting caliper, using kernel matching, or adding more covariates to the propensity score model).

**Why other options are incorrect**:
- A: Perfect balance would be SMD ≈ 0
- B: Good balance requires SMD < 0.1
- D: Severe imbalance would be SMD > 0.2; 0.15 is moderate

---

## Question 7: Positivity Assumption

The positivity (or overlap) assumption in causal inference requires that:

A) All covariates must have positive values
B) Every unit must have some probability of receiving each treatment level
C) Treatment effects must be positive (improving outcomes)
D) The propensity score must be greater than 0.5

**Correct Answer: B**

**Explanation**: The positivity assumption states that for every combination of covariates X, there must be a non-zero probability of receiving each treatment level: 0 < P(T=1 | X) < 1 for all X. This ensures that treated and control groups have overlap in the covariate space, making causal comparisons possible. If some units have zero probability of receiving a treatment, we cannot estimate the treatment effect for those units (violating generalizability).

**Why other options are incorrect**:
- A: Covariates can have any values, including negative or zero
- C: Treatment effects can be negative (harmful treatments) or zero (no effect)
- D: Propensity scores can be anywhere between 0 and 1; values near 0.5 indicate balanced assignment

---

## Question 8: Mediators vs Confounders

In an LLM study, "Attention Patterns" are affected by "Prompt Intervention" and also affect "Reasoning Quality." "Task Complexity" affects both "Prompt Intervention" and "Reasoning Quality." What is the correct classification?

A) Attention Patterns: Confounder, Task Complexity: Mediator
B) Attention Patterns: Mediator, Task Complexity: Confounder
C) Both are mediators
D) Both are confounders

**Correct Answer: B**

**Explanation**: **Attention Patterns** is a **mediator** because it lies on the causal path: Prompt → Attention → Reasoning. Understanding how prompting affects reasoning through attention is a key research question. **Task Complexity** is a **confounder** because it affects both treatment assignment (which prompting strategy is used) and outcome (reasoning quality), creating a backdoor path that must be blocked: Prompt ← Complexity → Reasoning.

**Why other options are incorrect**:
- A: This reverses the roles; attention is on the causal path, complexity creates confounding
- C: Task complexity is not on the causal path (Prompt → Reasoning), so it's not a mediator
- D: Attention is on the causal path, so it's a mediator, not a confounder

---

## Question 9: Mediation Analysis - Effect Decomposition

In a mediation analysis, you find:
- Total Effect: 0.30
- Direct Effect: 0.10
- Indirect Effect: 0.20

What does this indicate about the causal mechanism?

A) The treatment has no effect
B) The treatment effect operates entirely through the mediator
C) Most of the treatment effect is mediated (67%), but there is also a direct effect
D) The mediator blocks the treatment effect

**Correct Answer: C**

**Explanation**: The total effect (0.30) decomposes into direct (0.10) and indirect (0.20) effects. The indirect effect is larger, indicating that 67% (0.20/0.30) of the treatment effect operates through the mediator. However, the non-zero direct effect (0.10) means there are additional mechanisms beyond the mediator. This suggests the treatment works both by changing the mediator (primary mechanism) and through other pathways (secondary mechanism).

**Why other options are incorrect**:
- A: The total effect is 0.30, so there is a significant effect
- B: The non-zero direct effect (0.10) indicates not all effect is mediated
- D: A positive total effect indicates the mediator facilitates, not blocks, the effect

---

## Question 10: Common Support

When checking for common support in propensity score matching, you observe:

```
Treatment group propensity scores: [0.1, 0.2, 0.3, 0.4, 0.5]
Control group propensity scores:     [0.6, 0.7, 0.8, 0.9]
```

What is the problem?

A) No overlap exists between groups
B) Only units with propensity scores in [0.1, 0.5] have common support
C) The propensity score model is incorrectly specified
D) The treatment effect cannot be estimated

**Correct Answer: B**

**Explanation**: **Common support** exists only in the overlap region [0.1, 0.5], where both treatment and control units exist. Units with propensity scores outside this range (0.6-0.9 for control, no treated units) lack common support. These units should be excluded or analyzed separately. The treatment effect can still be estimated for units with common support, but generalizability is limited to that region.

**Why other options are incorrect**:
- A: There is overlap in [0.1, 0.5], so some common support exists
- C: The separation doesn't necessarily indicate model misspecification; it could reflect real differences in treatment assignment
- D: The effect can be estimated for units with common support; generalizability is the concern

---

## Question 11: Collider Bias

You include "User Satisfaction Rating" (which is affected by both Prompt Quality and Task Performance) as a covariate in your causal analysis. This introduces:

A) Confounding bias
B) Collider bias
C) Selection bias
D) Measurement error

**Correct Answer: B**

**Explanation**: Conditioning on a **collider** (a variable affected by both treatment and outcome) opens a spurious association and introduces bias. Here, User Satisfaction is a collider: both Prompt Quality (treatment-related) and Task Performance (outcome-related) affect it. Including it in the analysis creates a non-causal association between Prompt Quality and Task Performance, violating the assumptions needed for causal identification.

**Why other options are incorrect**:
- A: Confounding bias comes from variables affecting both treatment and outcome, not being affected by them
- C: Selection bias refers to non-random inclusion/exclusion of units, not conditioning on colliders
- D: Measurement error refers to inaccurate measurement, not the choice of covariates

---

## Question 12: Sequential Ignorability in Mediation

In mediation analysis, the sequential ignorability assumption requires that:

A) Treatments are assigned sequentially over time
B) There is no unmeasured confounding of treatment-outcome and mediator-outcome relationships
C) Mediators and outcomes are independent
D) All variables are measured in a specific sequence

**Correct Answer: B**

**Explanation**: **Sequential ignorability** is a strong assumption requiring: (1) no unmeasured confounding of the treatment-outcome relationship, and (2) no unmeasured confounding of the mediator-outcome relationship, conditional on treatment and covariates. This ensures that we can identify both direct and indirect effects. The term "sequential" refers to the causal ordering (T → M → Y), not temporal sequencing.

**Why other options are incorrect**:
- A: The assumption is about confounding, not sequential treatment assignment
- C: Mediators and outcomes are causally related, not independent
- D: Measurement order doesn't matter; the assumption is about confounding structure

---

## Question 13: SUTVA Assumption

The Stable Unit Treatment Value Assumption (SUTVA) requires that:

A) The treatment effect is stable across different sample sizes
B) One unit's treatment doesn't affect another's outcome
C) The treatment effect doesn't vary across units
D) The treatment is administered uniformly

**Correct Answer: B**

**Explanation**: SUTVA has two components: (1) no interference between units (one unit's treatment doesn't affect another's outcome), and (2) no hidden variation in treatment (the treatment definition is clear and consistent). In LLM contexts, interference could occur if one task's format affects another task's difficulty (unlikely) or if model state carries over between tasks (must be controlled via independent trials).

**Why other options are incorrect**:
- A: Sample size affects precision, not the validity of SUTVA
- C: Treatment effect variation is allowed and expected; SUTVA is about treatment definition and interference
- D: Treatment can vary across units; SUTVA requires consistent definition, not uniform administration

---

## Question 14: Sensitivity Analysis

After propensity score matching, you find ATE = 0.15 with 95% CI [0.05, 0.25]. A sensitivity analysis using Rosenbaum bounds shows that the results are robust to hidden confounding of Gamma = 1.5. This means:

A) The results would remain significant even if a hidden confounder increased the odds of treatment by 50%
B) The results are highly sensitive to hidden confounding
C) The confidence interval is too wide
D) The matching procedure failed

**Correct Answer: A**

**Explanation**: A Gamma value of 1.5 indicates **robustness** to moderate hidden confounding. Specifically, even if there were an unobserved confounder that increased the odds of receiving treatment by 50% (Gamma = 1.5), the causal conclusion would remain statistically significant. Higher Gamma values (e.g., > 2.0) indicate greater robustness. Values close to 1.0 indicate high sensitivity to hidden confounding.

**Why other options are incorrect**:
- B: Gamma = 1.5 indicates moderate robustness, not high sensitivity
- C: The width of the CI is separate from sensitivity analysis
- D: Sensitivity analysis assesses hidden confounding, not matching procedure quality

---

## Question 15: Attention as Causal Mediator

In an LLM, you want to understand why chain-of-thought (CoT) prompting improves reasoning. You extract attention weights from a specific layer and head. You perform mediation analysis and find that the indirect effect through this attention head explains 40% of the total CoT effect. What is the correct interpretation?

A) This attention head causes 40% of CoT improvements
B) 40% of CoT's effect operates through changing attention in this specific head
C) The attention head is responsible for CoT effectiveness
D) CoT doesn't work; it's just the attention head

**Correct Answer: B**

**Explanation**: The mediation analysis indicates that **40% of the total treatment effect** (CoT vs. no-CoT) is mediated through the attention pattern in this specific layer/head. This means that CoT prompting works partly (40%) by changing how the model attends to information at this specific location. The remaining 60% operates through other mechanisms (other attention heads, different layers, or non-attention mechanisms). This provides causal insight into *how* CoT works.

**Why other options are incorrect**:
- A: The attention head is a mediator, not a cause; the cause is the prompting strategy
- C: Only 40% is mediated, not 100%, so other mechanisms also contribute
- D: The positive total effect shows CoT works; mediation explains the mechanism, not denies the effect

---

## Summary Statistics

**Question Types Covered:**
- Correlation vs Causation: Questions 1, 3
- Potential Outcomes Framework: Questions 2, 7, 13
- Propensity Score Matching: Questions 4, 6, 10, 14
- DAGs and Causal Graphs: Questions 5, 11
- Mediation Analysis: Questions 8, 9, 12, 15

**Difficulty Levels:**
- Conceptual Understanding: Questions 1, 2, 5, 11, 13
- Application of Methods: Questions 4, 6, 8, 10, 14
- Interpretation of Effects: Questions 3, 7, 9, 12, 15

**LLM-Specific Context:**
All questions include LLM examples and scenarios, connecting theory to practical applications in language model research.