
import os
from dotenv import load_dotenv
import chromadb
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from langchain_groq import ChatGroq
from langchain_classic.chains import RetrievalQA

load_dotenv()

working_dir = os.path.dirname(os.path.abspath(__file__))
vectorstore_dir = os.path.join(working_dir, "doc_vectorstore")
collection_name = "pdf_documents"

_embedding = None
_llm = None


def get_embedding():
    global _embedding

    if _embedding is None:
        print("Loading Hugging Face embedding model...", flush=True)
        _embedding = HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-MiniLM-L6-v2"
        )
        print("Embedding model loaded.", flush=True)

    return _embedding


def get_llm():
    global _llm

    if _llm is None:
        if not os.getenv("GROQ_API_KEY"):
            raise ValueError(
                "GROQ_API_KEY is missing. Check your .env file."
            )

        _llm = ChatGroq(
            model="openai/gpt-oss-120b",
            temperature=0,
            timeout=60,
            max_retries=1,
        )

    return _llm




def get_vectorstore():
    return Chroma(
        collection_name=collection_name,
        persist_directory=vectorstore_dir,
        embedding_function=get_embedding(),
    )




def process_document_to_chroma_db(file_name):
    file_path = os.path.join(working_dir, file_name)

    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"PDF not found: {file_path}")

    print("Loading PDF...", flush=True)
    documents = PyPDFLoader(file_path).load()

    if not documents:
        raise ValueError("No pages were extracted from the PDF.")

    print(f"Loaded {len(documents)} PDF pages.", flush=True)

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1500,
        chunk_overlap=150,
    )
    texts = splitter.split_documents(documents)

    if not texts:
        raise ValueError(
            "No text chunks were generated from the PDF."
        )

    print(f"Created {len(texts)} chunks.", flush=True)
    print("Opening ChromaDB...", flush=True)

   
    db = get_vectorstore()

    print("ChromaDB opened successfully.", flush=True)

    print("Generating embeddings for all chunks...", flush=True)
    all_texts = [doc.page_content for doc in texts]
    all_embeddings = get_embedding().embed_documents(all_texts)

    print(f"Generated {len(all_embeddings)} embeddings.", flush=True)
    print("Writing chunks to ChromaDB...", flush=True)

    ids = [f"{file_name}_{i}" for i in range(len(texts))]

    db._collection.upsert(
        ids=ids,
        documents=all_texts,
        embeddings=all_embeddings,
        metadatas=[doc.metadata for doc in texts],
    )

    print("PDF indexed successfully.", flush=True)
    return len(texts)


def answer_question(user_question):
    if not user_question or not user_question.strip():
        raise ValueError("Please enter a question.")

    if not os.path.isdir(vectorstore_dir):
        raise ValueError("Please upload and process a PDF first.")

    print("Opening ChromaDB for retrieval...", flush=True)
    db = get_vectorstore()

    if db._collection.count() == 0:
        raise ValueError(
            "The document database is empty. Process a PDF first."
        )

    print("Searching document...", flush=True)
    retriever = db.as_retriever(search_kwargs={"k": 4})

    print("Sending question to Groq...", flush=True)

    qa_chain = RetrievalQA.from_chain_type(
        llm=get_llm(),
        chain_type="stuff",
        retriever=retriever,
    )

    response = qa_chain.invoke({"query": user_question})

    print("Answer received.", flush=True)
    return response["result"]
