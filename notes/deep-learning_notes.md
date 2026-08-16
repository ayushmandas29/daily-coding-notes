# Deep Learning — Core Notes

## Key Insight
Deep learning performance depends on architecture, data quality, optimization, regularization, and evaluation — not architecture alone.

## CNNs
Convolutional Neural Networks learn spatial representations through convolution filters. A typical pipeline is:

`input → convolution → activation → pooling → deeper features → classifier`

Earlier layers often learn low-level patterns such as edges and textures; deeper layers learn increasingly task-specific representations.

## Transfer Learning
A pretrained model can provide useful representations for a new task.

Common strategies:
- Freeze most layers and train a new classifier.
- Fine-tune selected deeper layers.
- Fine-tune more layers with a smaller learning rate.

Architectures I am studying include ZFNet, VGG16, GoogLeNet/Inception, EfficientNet, DenseNet, and Inception-ResNet.

## Regularization
Useful techniques include dropout, weight regularization, data augmentation, early stopping, and careful model sizing.

A large gap between training and validation performance is a warning sign for poor generalization.

## Sequence Models
- **RNN:** recurrent hidden state for sequential data; basic RNNs can struggle with long-term dependencies.
- **LSTM:** gated architecture designed to preserve useful information over longer sequences.
- **GRU:** simpler gated recurrent architecture with fewer gates than LSTM.
- **BiLSTM:** captures context in both sequence directions when future context is available during inference.

For time-series tasks, preserve temporal order during evaluation to avoid leakage.

## Transformer and NLP Learning
Important concepts include tokenization, embeddings, self-attention, positional information, encoder/decoder architectures, transfer learning, and fine-tuning.

### BERT
BERT provides bidirectional transformer representations and can be fine-tuned for tasks such as classification, token classification, and question answering.

### RAG
Retrieval-Augmented Generation connects external knowledge retrieval with an LLM:

`documents → chunking → embeddings → vector search → retrieved context → LLM → answer`

Common failure points include poor chunking, weak retrieval, irrelevant context, prompt construction, and missing source tracking.

Tools I am studying include Hugging Face, LangChain, LlamaIndex, vector databases, and local LLM workflows.

## Explainability
Grad-CAM can highlight image regions that strongly influence a CNN prediction. It is useful for diagnostics and communication, but an explanation map is not proof that the prediction is correct.

## Training Practice
For each deep-learning experiment, record:
- dataset and split strategy
- preprocessing and augmentation
- architecture
- optimizer and learning rate
- batch size and epochs
- loss and evaluation metrics
- training/validation behavior
- failure cases
- final inference constraints

## Project Connections
### Animal Classification
CNNs, transfer learning, augmentation, model comparison, classification metrics, and Grad-CAM.

### Energy Pricing / Demand Forecasting
LSTM/GRU sequence modeling, temporal splits, preprocessing, and forecasting metrics.

### Silent Speech Decoder
3D CNN + BiLSTM sequence modeling, mouth-region extraction, CTC loss, CER/WER, and real-time inference.

## Key Learning
A deeper model is not automatically a better model. The right architecture is the one that generalizes well and satisfies the computational and deployment constraints of the real task.

---
*Part of my daily coding knowledge base.*
