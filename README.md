# Question Answering on SQuAD using DistilBERT

This repository contains a project for building a Question Answering (QA) model using the DistilBERT architecture. The model is fine-tuned on the Stanford Question Answering Dataset (SQuAD) and deployed as an interactive web application using Streamlit.

## Features
- **Model:** Fine-tuned DistilBERT for Question Answering.
- **Dataset:** SQuAD (Stanford Question Answering Dataset).
- **Deployment:** Interactive web application using Streamlit.
- **Functionality:** Users can input a context and a question to get precise answers, with additional features like example contexts and questions.

## Table of Contents
1. [Installation](#installation)
3. [Dataset](#dataset)
4. [Model Training](#model-training)
---

## Installation

### Prerequisites
- Python 3.8+
- Pip package manager
- streamlit
- transformers
- pytourch
- datasets

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/Shrouk-Adel/Interactive-QA-App
   ```
2. Install required packages:
   ```bash
   pip install -r requirements.txt
   ```

 

### Interacting with the App
- **Context Input:** Provide the context paragraph in the designated text area.
- **Question Input:** Enter your question in the input field.
- **Get Answer:** Click the button to generate an answer based on the provided context.
- **Examples:** Use the example context and question to test the model.

## Dataset
The project uses the [SQuAD dataset](https://rajpurkar.github.io/SQuAD-explorer/) for training and evaluation:
- **SQuAD v1.1**: Contains questions posed by crowdworkers on a set of Wikipedia articles, with corresponding answer spans.

### Preprocessing
- Tokenization is performed using the Hugging Face Transformers library.
- Input sequences are padded and truncated to fit the DistilBERT model’s requirements.

## Model Training
- The model is fine-tuned using Hugging Face's `Trainer` API.
- Loss function: Cross-Entropy Loss for start and end token predictions.
- Optimizer: AdamW with a learning rate scheduler.
- Evaluation metrics: Exact Match (EM) and F1 score.

### Saving the Model
The trained model is saved locally for deployment:
```python
model.save_pretrained("./qa_model")
tokenizer.save_pretrained("./qa_model")
```

 

 

 
 

### Acknowledgments
- Hugging Face Transformers for providing pre-trained models and tools.
- The SQuAD dataset creators for an excellent dataset.
- Streamlit for a simple and effective deployment platform.

