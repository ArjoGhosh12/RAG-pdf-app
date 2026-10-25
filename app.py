
import os
import streamlit as st

st.set_page_config(
    page_title="PDF Intelligence | 2arjo",
    page_icon="🦙",
    layout="wide"
)

# ---------- Custom UI Styling ----------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Space+Grotesk:wght@400;500;600;700&display=swap');

:root {
    --bg: #0b1020;
    --panel: #121a2d;
    --panel-light: #18243b;
    --text: #eef3ff;
    --muted: #94a3bd;
    --accent: #8b5cf6;
    --accent2: #22d3ee;
    --border: rgba(148, 163, 184, 0.17);
}

.stApp {
    background:
        radial-gradient(ellipse at 10% 0%, rgba(124,58,237,.18), transparent 38%),
        radial-gradient(ellipse at 95% 12%, rgba(34,211,238,.10), transparent 30%),
        var(--bg);
    color: var(--text);
    font-family: 'DM Sans', sans-serif;
}

[data-testid="stHeader"] {
    background: transparent;
}

.block-container {
    max-width: 1100px;
    padding-top: 2rem;
    padding-bottom: 1rem;
}

h1, h2, h3 {
    font-family: 'Space Grotesk', sans-serif !important;
    color: var(--text) !important;
}

.hero {
    padding: 2.3rem 2.5rem;
    border: 1px solid var(--border);
    border-radius: 26px;
    background: linear-gradient(130deg, rgba(24,36,59,.96), rgba(17,24,45,.92));
    box-shadow: 0 20px 60px rgba(0,0,0,.22);
    margin-bottom: 1.6rem;
    position: relative;
    overflow: hidden;
}

.hero:after {
    content: "";
    position: absolute;
    width: 240px;
    height: 240px;
    border-radius: 50%;
    background: rgba(139,92,246,.12);
    filter: blur(55px);
    right: -55px;
    top: -100px;
}

.eyebrow {
    color: #a5b4fc;
    font-size: .78rem;
    font-weight: 700;
    letter-spacing: .16em;
    text-transform: uppercase;
    margin-bottom: .8rem;
}

.hero-title {
    font-family: 'Space Grotesk', sans-serif;
    font-size: clamp(2rem, 5vw, 3.2rem);
    line-height: 1.12;
    font-weight: 700;
    letter-spacing: -.045em;
    margin: 0 0 .8rem 0;
    position: relative;
    z-index: 1;
}

.gradient-text {
    background: linear-gradient(90deg, #c4b5fd, #67e8f9);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.hero-copy {
    max-width: 680px;
    color: var(--muted);
    font-size: 1.02rem;
    line-height: 1.7;
    position: relative;
    z-index: 1;
}

.pill {
    display: inline-block;
    padding: .4rem .75rem;
    border: 1px solid rgba(139,92,246,.35);
    background: rgba(139,92,246,.10);
    color: #d8ccff;
    border-radius: 999px;
    font-size: .78rem;
    font-weight: 600;
    margin-bottom: 1.1rem;
}

.section-label {
    color: #c4b5fd;
    font-size: .76rem;
    font-weight: 700;
    letter-spacing: .13em;
    text-transform: uppercase;
    margin-bottom: .35rem;
}

.section-heading {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 1.55rem;
    font-weight: 700;
    color: var(--text);
    margin-bottom: .35rem;
}

.section-copy {
    color: var(--muted);
    line-height: 1.6;
    margin-bottom: 1rem;
}

[data-testid="stFileUploader"] {
    background: rgba(18,26,45,.82);
    border: 1px dashed rgba(139,92,246,.55);
    border-radius: 18px;
    padding: 1rem;
}

[data-testid="stFileUploader"] section {
    background: transparent;
}

[data-testid="stTextArea"] textarea {
    background: #111a2d !important;
    color: #eef3ff !important;
    border: 1px solid var(--border) !important;
    border-radius: 14px !important;
    padding: 1rem !important;
}

[data-testid="stTextArea"] textarea:focus {
    border-color: var(--accent) !important;
    box-shadow: 0 0 0 1px var(--accent) !important;
}

.stButton > button {
    width: 100%;
    min-height: 3rem;
    border-radius: 13px;
    border: 1px solid rgba(167,139,250,.45);
    background: linear-gradient(100deg, #7c3aed, #6366f1);
    color: white;
    font-weight: 700;
    transition: all .2s ease;
}

.stButton > button:hover {
    border-color: #a5f3fc;
    box-shadow: 0 0 24px rgba(139,92,246,.25);
    transform: translateY(-1px);
}

div[data-testid="stAlert"] {
    border-radius: 13px;
}

div[data-testid="stSpinner"] {
    color: #c4b5fd;
}

hr {
    border-color: var(--border);
    margin: 1.8rem 0;
}

.footer {
    text-align: center;
    color: #71809b;
    font-size: .83rem;
    padding: 1.5rem .5rem .6rem;
}

.footer strong {
    color: #c4b5fd;
    font-weight: 700;
}

@media (max-width: 700px) {
    .block-container {
        padding: 1rem 1rem .5rem;
    }
    .hero {
        padding: 1.5rem;
        border-radius: 20px;
    }
}
</style>
""", unsafe_allow_html=True)

# ---------- Hero ----------
st.markdown("""
<div class="hero">
    <div class="pill">✦ AI-POWERED DOCUMENT ASSISTANT</div>
    <div class="hero-title">
        Understand your documents.<br>
        <span class="gradient-text">Ask anything.</span>
    </div>
    <div class="hero-copy">
        Upload a PDF, explore its contents, and get contextual answers
        powered by semantic search and a large language model.
    </div>
</div>
""", unsafe_allow_html=True)

working_dir = os.path.dirname(os.path.abspath(__file__))

# ---------- Upload Section ----------
st.markdown("""
<div class="section-label">01 / DOCUMENT</div>
<div class="section-heading">Upload your PDF</div>
<div class="section-copy">
    Choose a document to prepare it for intelligent question answering.
</div>
""", unsafe_allow_html=True)

uploaded_file = st.file_uploader(
    "Choose a PDF file",
    type=["pdf"],
    help="Upload the PDF you want to ask questions about."
)

# Process PDF only when the button is clicked
if uploaded_file is not None:
    if st.button("⚡  Process PDF", type="primary"):
        try:
            with st.spinner(
                "Processing PDF... The first run may take longer "
                "while the embedding model loads."
            ):
                from rag_utility import process_document_to_chroma_db

                save_path = os.path.join(
                    working_dir, uploaded_file.name
                )

                with open(save_path, "wb") as f:
                    f.write(uploaded_file.getbuffer())

                chunks = process_document_to_chroma_db(
                    uploaded_file.name
                )

            st.session_state["pdf_processed"] = True
            st.session_state["pdf_name"] = uploaded_file.name

            st.success(
                f"Document processed successfully! Text chunks: {chunks}"
            )

        except Exception as e:
            st.error(f"PDF processing failed: {e}")
            st.exception(e)

st.markdown("<hr>", unsafe_allow_html=True)

# ---------- Question Section ----------
st.markdown("""
<div class="section-label">02 / ASK</div>
<div class="section-heading">Talk to your document</div>
<div class="section-copy">
    Ask a specific question, request a summary, or explore a key idea.
</div>
""", unsafe_allow_html=True)

# Ask questions
user_question = st.text_area(
    "Your question",
    placeholder="e.g. Summarize the main findings of this document...",
    height=120,
)

if st.button("✦  Generate Answer", type="primary"):
    if not user_question.strip():
        st.warning("Please enter a question.")
    else:
        try:
            with st.spinner("Searching your document and generating an answer..."):
                from rag_utility import answer_question
                answer = answer_question(user_question)

            st.markdown("<hr>", unsafe_allow_html=True)
            st.markdown("""
            <div class="section-label">03 / RESPONSE</div>
            <div class="section-heading">Your answer</div>
            """, unsafe_allow_html=True)

            st.markdown(answer)

        except Exception as e:
            st.error(f"Question answering failed: {e}")
            st.exception(e)

# ---------- Footer ----------
st.markdown("""
<div class="footer">
    Built with Streamlit &nbsp;·&nbsp; AI-powered document intelligence
    <br><br>
    © <strong>Arjo</strong> &nbsp;|&nbsp; Crafted with curiosity.
</div>
""", unsafe_allow_html=True)
