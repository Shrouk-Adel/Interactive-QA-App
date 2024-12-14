import streamlit as st
from transformers import AutoModelForQuestionAnswering, AutoTokenizer, pipeline

# Load model and tokenizer
model_path = "E:/Ahmed_Elsalab/Deployment/Interactive-QA-App/qa_model"
model = AutoModelForQuestionAnswering.from_pretrained(model_path)
tokenizer = AutoTokenizer.from_pretrained(model_path)
qa_pipeline = pipeline("question-answering", model=model, tokenizer=tokenizer)

# Set a custom page layout
st.set_page_config(
    page_title="Interactive Q&A App",
    page_icon="💡",
    layout="wide",  # Centered layout; options: "wide" or "centered"
)

# App Header
st.markdown(
    """
    <style>
    .title {
        font-size: 40px;
        color: #4CAF50;
        text-align: center;
    }
    .description {
        font-size: 18px;
        color: #6c757d;
        text-align: center;
        margin-bottom: 20px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)
st.markdown('<div class="title">🔍 Interactive Q&A App</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="description">Ask any question based on a given context and get an instant answer!</div>',
    unsafe_allow_html=True,
)

# Two-column layout for Context and Question
col1, col2 = st.columns(2)

with col1:
    st.subheader("Enter Context")
    context = st.text_area(
        "Paste the context here:",
        height=200,
        placeholder="E.g., Albert Einstein was a theoretical physicist who developed the theory of relativity...",
    )

with col2:
    st.subheader("Enter Question")
    question = st.text_input("Type your question here:", placeholder="E.g., Who was Albert Einstein?")

# Show Examples Section
if st.checkbox("Show Examples"):
    st.markdown("#### Example Context")
    st.text_area(
        "Albert Einstein was a theoretical physicist who developed the theory of relativity.",
        disabled=True,
    )
    st.markdown("#### Example Question")
    st.text_input("Who was Albert Einstein?", disabled=True)

# Get Answer Button
if st.button("Get Answer"):
    if context.strip() and question.strip():
        with st.spinner("Analyzing..."):
            result = qa_pipeline({"question": question, "context": context})
            st.success(f"**Answer:** {result['answer']}")
    else:
        st.warning("Please provide both a context and a question.")

# Footer
st.markdown("---")
st.markdown(
    '<div style="text-align: center;">'
    "Made with ❤️ using <b>Streamlit</b> and <b>Hugging Face Transformers</b>."
    "</div>",
    unsafe_allow_html=True,
)

