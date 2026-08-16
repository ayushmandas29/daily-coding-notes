# Machine Learning — Core Notes

## Key Insight
Machine learning is an end-to-end system: data quality, feature design, evaluation, deployment, and monitoring matter as much as model selection.

## Core Lifecycle
1. Problem definition and success metrics
2. Data collection and validation
3. Cleaning and preprocessing
4. Feature engineering
5. Train/validation/test strategy
6. Baseline model
7. Model development and tuning
8. Error analysis and evaluation
9. Deployment
10. Monitoring, drift detection, and iteration

## Practical Data Issues
- Missing values require understanding why values are missing.
- Outliers should be investigated before removal.
- Duplicate and near-duplicate records can cause biased training and leakage.
- Inconsistent categories should be normalized systematically.
- Class imbalance makes accuracy unreliable by itself; consider precision, recall, F1, PR-AUC, or ROC-AUC according to the problem.
- Data leakage occurs when information unavailable at prediction time enters training. Preprocessing should generally be fitted using training data only.

## Feature Engineering
Feature engineering transforms raw data into representations that make useful patterns easier to learn. Examples include date/time components, aggregates, ratios, interactions, text representations, and domain-specific transformations.

A feature is useful only if it is valid and available at inference time.

## Model Selection
Start with a strong, simple baseline such as linear/logistic regression, decision trees, random forests, or gradient boosting. Increase complexity only when experiments show that it provides meaningful improvement.

## Optimization
Gradient descent updates parameters using the loss gradient:

`theta = theta - learning_rate * gradient`

Learning rate is critical:
- Too high → unstable or divergent training.
- Too low → slow convergence.
- Scheduling can reduce the rate as training progresses.

Common optimizers include SGD, Momentum, Adam, and RMSProp. Optimizer choice should be validated experimentally.

## Overfitting
Overfitting means a model learns training-specific patterns that do not generalize. Useful countermeasures include stronger data, regularization, simpler models, dropout, early stopping, augmentation, and appropriate cross-validation.

## Evaluation
Metrics should reflect the actual cost of errors.

### Classification
Accuracy, precision, recall, F1, ROC-AUC, PR-AUC, and confusion matrices.

### Regression
MAE, MSE, RMSE, and R-squared.

### Sequence / Speech Tasks
CER, WER, and sequence accuracy.

## MLOps Connection
A production ML system should support reproducibility, model/data versioning, automated testing, deployment, and monitoring. Monitoring should cover latency, resource use, input distributions, prediction behavior, and model quality.

### Drift
- **Data drift:** input distribution changes.
- **Concept drift:** the relationship between inputs and the target changes.

## Real-Time ML
Offline accuracy is not enough for real-time systems. Also consider latency, throughput, memory, model size, concurrency, reliability, and hardware constraints.

For edge deployment, quantization, pruning, acceleration, and power consumption become important.

## Learning Rule
For every ML topic, I should be able to explain what problem it solves, how it works, its assumptions, failure modes, evaluation method, alternatives, and production considerations — not just memorize a definition.

---
*Part of my daily coding knowledge base.*
