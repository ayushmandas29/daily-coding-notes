# ML Learning Log — 2026-08-16

A consolidated study note covering the machine-learning and AI concepts I am actively learning, revising, and applying in projects.

## 1. End-to-End Machine Learning Lifecycle

A production ML system is more than model training. The practical lifecycle is:

1. **Problem definition** — identify the business/technical objective, target variable, constraints, and success metric.
2. **Data collection** — gather representative data from files, databases, APIs, sensors, logs, or public datasets.
3. **Data validation** — check schema, missing values, duplicates, invalid ranges, inconsistent categories, and label quality.
4. **Preprocessing** — clean data, encode categorical variables, scale numerical features when appropriate, and split data correctly.
5. **Feature engineering** — create informative features from domain knowledge, timestamps, text, aggregates, or interactions.
6. **Model development** — establish a simple baseline before experimenting with more complex models.
7. **Evaluation** — choose metrics that match the problem and inspect errors, not only a single score.
8. **Deployment** — expose the model through an application, API, batch pipeline, or embedded/edge workflow.
9. **Monitoring** — track prediction quality, data drift, concept drift, latency, failures, resource usage, and business impact.
10. **Iteration** — use monitoring and error analysis to improve data, features, models, and deployment.

### Key lesson
A model with excellent validation accuracy can still fail in production if the training data, inference environment, latency requirements, or monitoring strategy are weak.

---

## 2. Messy Real-World Data

Common problems I need to handle systematically:

### Missing values
- Numerical: median/mean imputation when justified, model-based imputation, or an explicit missing indicator.
- Categorical: most-frequent category or an `Unknown` category when semantically appropriate.
- Do not blindly impute values before understanding why they are missing.

### Outliers
- Detect with domain limits, IQR, robust statistics, or visualization.
- Decide whether an outlier is a data error, rare valid observation, or an important signal.
- Avoid deleting extreme observations automatically.

### Duplicates
- Exact duplicates can inflate model performance and bias frequency-based learning.
- Near-duplicates may create train/test leakage when the same underlying observation appears in multiple splits.

### Inconsistent categories
Examples: `Bangalore`, `Bengaluru`, `bangalore`, and trailing-space variants.
Normalize casing, whitespace, spelling, and category definitions before modeling.

### Class imbalance
Accuracy can become misleading when one class dominates.
Useful approaches include class weights, resampling, threshold tuning, and suitable metrics such as precision, recall, F1, PR-AUC, and ROC-AUC where appropriate.

### Data leakage
Leakage occurs when information unavailable at prediction time enters the training process.
Typical sources:
- preprocessing fitted on the full dataset before splitting
- future information in features
- target-derived features
- duplicates across train and test sets

**Rule:** split first where appropriate, then fit preprocessing only on the training data.

---

## 3. Feature Engineering

Feature engineering converts raw observations into representations that help a model learn useful patterns.

Examples:
- Extract `day`, `month`, `weekday`, and hour from timestamps.
- Create ratios and interaction features where domain logic supports them.
- Aggregate transaction histories into count, mean, recency, and frequency features.
- For text, use tokenization, embeddings, TF-IDF, or transformer representations depending on the task.

### Important principle
Good features reduce the amount of pattern the model has to discover from raw data, but features must remain available and valid at inference time.

---

## 4. Model Selection and Baselines

Start with a simple baseline:
- Linear/Logistic Regression
- Decision Tree
- Random Forest
- Gradient boosting

Then compare against more complex models when the problem justifies it.

### Why baselines matter
A complicated neural network is not automatically better than a strong classical baseline. Baselines establish whether additional model complexity actually produces meaningful improvement.

---

## 5. Optimization and Gradient Descent

Gradient-based optimization updates model parameters in the direction that reduces the loss.

A basic update is:

`theta = theta - learning_rate * gradient`

### Learning rate
- Too large → unstable training or divergence.
- Too small → slow convergence.
- A schedule can reduce the learning rate as training progresses.

### Common optimizers
- **SGD** — simple and often a useful baseline.
- **Momentum SGD** — smooths updates using previous gradients.
- **Adam** — adaptive learning rates using estimates of first and second moments.
- **RMSProp** — adapts updates using a moving average of squared gradients.

Optimizer choice should be evaluated experimentally rather than treated as a universal rule.

---

## 6. Overfitting and Regularization

Overfitting occurs when a model learns training-specific patterns that do not generalize well.

Ways to reduce it:
- collect more representative data
- simplify the model
- regularization
- dropout in neural networks
- early stopping
- data augmentation
- cross-validation where appropriate

### Important distinction
High training accuracy + much lower validation/test performance is a strong warning sign of poor generalization.

---

## 7. Deep Learning Notes

### CNNs
Convolutional Neural Networks learn spatial features using convolutional filters.
Typical progression:

`input -> convolution -> activation -> pooling -> deeper features -> classifier`

Earlier layers often learn edges/textures; deeper layers learn increasingly task-specific patterns.

### Transfer learning
A pretrained network can provide reusable representations.
Useful strategies:
- freeze most layers and train a new classifier
- fine-tune selected deeper layers
- fine-tune more of the network with a smaller learning rate

Models I have been studying include ZFNet, VGG16, GoogLeNet/Inception, EfficientNet, DenseNet, and Inception-ResNet.

### CNN model comparison lesson
Architecture depth, parameter count, compute cost, receptive fields, normalization, skip connections, and dataset size all affect practical performance.

---

## 8. Sequence Models and Forecasting

### RNN / LSTM / GRU
These models are designed for sequential dependencies.

- **RNN**: basic recurrent state, but can struggle with long-term dependencies.
- **LSTM**: uses gates and a cell state to preserve useful information over longer sequences.
- **GRU**: a simpler gated recurrent architecture with fewer gates than LSTM.
- **BiLSTM**: processes sequence context in both directions and is useful when future context is available during prediction.

For forecasting tasks, evaluation must respect time order. Randomly shuffling temporal data can cause leakage.

---

## 9. NLP and Transformer Learning

Important concepts:
- tokenization
- embeddings
- attention
- self-attention
- positional information
- encoder/decoder architectures
- transfer learning
- fine-tuning pretrained language models

### BERT-style learning
BERT uses bidirectional transformer representations and can be fine-tuned for classification, token classification, question answering, and other language tasks.

### RAG
Retrieval-Augmented Generation combines retrieval with generation:

`documents -> chunking -> embeddings -> vector search -> retrieved context -> LLM -> answer`

Benefits:
- grounds responses in a controlled knowledge source
- makes domain knowledge updateable without retraining the base model
- can provide source-aware answers when retrieval metadata is preserved

Common failure modes:
- poor chunking
- weak retrieval
- irrelevant context
- missing citations/source tracking
- prompt construction problems
- context-window pressure

Tools I am studying around this area include LangChain, LlamaIndex, Hugging Face, vector databases, and local LLM workflows.

---

## 10. Explainability

Model explainability is useful for understanding why a model made a prediction, debugging failures, and communicating behavior.

### Grad-CAM
For convolutional models, Grad-CAM can highlight image regions that strongly influence a prediction.

### Practical lesson
Explainability is not proof that a model is correct. It is a diagnostic and communication tool that should be combined with quantitative evaluation and error analysis.

---

## 11. Evaluation and Error Analysis

### Classification
Depending on the task:
- Accuracy
- Precision
- Recall
- F1-score
- ROC-AUC
- PR-AUC
- Confusion matrix

### Regression
- MAE
- MSE
- RMSE
- R-squared

### Sequence / speech-related tasks
- Character Error Rate (CER)
- Word Error Rate (WER)
- Sequence accuracy

### Core lesson
Metrics must match the cost of errors. For an imbalanced fraud-like problem, for example, accuracy alone can hide poor minority-class detection.

---

## 12. MLOps and Production ML

A production ML workflow should include:

`data -> validation -> training -> evaluation -> artifact/versioning -> deployment -> monitoring -> retraining`

Important practices:
- version datasets and models
- preserve reproducible training configurations
- automate tests and deployment
- containerize inference services where useful
- separate training and inference environments
- monitor both software and model behavior

### Drift
- **Data drift**: distribution of input features changes.
- **Concept drift**: relationship between inputs and target changes.

A monitoring system should detect meaningful changes and trigger investigation or retraining workflows when justified.

---

## 13. Model Serving and Real-Time ML

For real-time systems, accuracy is only one requirement.
Important constraints include:
- latency
- throughput
- memory usage
- model size
- CPU/GPU utilization
- reliability
- concurrency

For edge/embedded inference, additional concerns include quantization, pruning, hardware acceleration, memory limits, and power consumption.

### Practical lesson
The best model is often the best model that satisfies the complete system constraints, not simply the one with the highest offline metric.

---

## 14. AI Projects I Am Connecting to These Concepts

### Autonomous AI Scientist
Focus areas:
- retrieval pipelines
- scientific document processing
- RAG
- LLM orchestration
- source-aware generation
- research workflow automation

### Animal Species Classification
Focus areas:
- CNNs
- transfer learning
- image augmentation
- model comparison
- Grad-CAM
- classification metrics

### Energy Pricing / Demand Forecasting
Focus areas:
- time-series preprocessing
- LSTM/GRU
- temporal train/validation/test splits
- forecasting metrics
- sequence modeling

### Silent Speech Decoder
Focus areas:
- computer vision
- mouth-region extraction
- 3D CNNs
- BiLSTM sequence modeling
- CTC loss
- CER/WER
- real-time inference

---

## 15. Coding and Learning Workflow

For each ML topic I study, I should be able to answer:

1. **What problem does it solve?**
2. **How does it work?**
3. **What assumptions does it make?**
4. **What are the common failure modes?**
5. **How do I evaluate it?**
6. **When would I choose it over an alternative?**
7. **How would I deploy and monitor it?**
8. **What did I learn by implementing it?**

### Personal rule
Do not count a topic as learned just because I can define it. I should be able to explain it, implement a small example, interpret results, identify failure modes, and connect it to a real project.

---

## 16. Next Learning Priorities

- Advanced model evaluation and statistical validation
- Feature stores and reproducible feature pipelines
- Experiment tracking and model versioning
- Docker + CI/CD for ML services
- Kubernetes fundamentals for ML workloads
- Model optimization and quantization
- LLM evaluation and RAG evaluation
- Monitoring for data drift, concept drift, and model quality
- Production system design for real-time ML

---

*Part of my daily coding and machine-learning knowledge base.*
