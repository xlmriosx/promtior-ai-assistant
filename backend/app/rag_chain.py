import os
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.llms import Ollama
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate
from app.data_loader import load_and_split_documents

class RAGChain:
    def __init__(self):
        self.embeddings = HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-MiniLM-L6-v2"
        )
        self.llm = Ollama(
            model="llama3",
            base_url=os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
        )
        self.vectorstore = None
        self.qa_chain = None
        self.setup_chain()
    
    def setup_chain(self):
        documents = load_and_split_documents()
        
        persist_directory = os.getenv("CHROMA_PERSIST_DIRECTORY", "./chroma_db")
        
        self.vectorstore = Chroma.from_documents(
            documents=documents,
            embedding=self.embeddings,
            persist_directory=persist_directory
        )
        
        prompt_template = """
        Eres un asistente especializado en información sobre Promtior. 
        Usa el siguiente contexto para responder la pregunta de manera precisa y útil.
        Si no tienes información suficiente en el contexto, di que no tienes esa información específica.
        
        Contexto: {context}
        
        Pregunta: {question}
        
        Respuesta:"""
        
        PROMPT = PromptTemplate(
            template=prompt_template,
            input_variables=["context", "question"]
        )
        
        self.qa_chain = RetrievalQA.from_chain_type(
            llm=self.llm,
            chain_type="stuff",
            retriever=self.vectorstore.as_retriever(search_kwargs={"k": 3}),
            chain_type_kwargs={"prompt": PROMPT},
            return_source_documents=True
        )
    
    def query(self, question: str):
        try:
            result = self.qa_chain.invoke({"query": question})
            
            sources = []
            if "source_documents" in result:
                sources = [doc.metadata.get("source", "unknown") for doc in result["source_documents"]]
            
            return {
                "response": result["result"],
                "sources": sources
            }
        except Exception as e:
            return {
                "response": f"Error procesando la consulta: {str(e)}",
                "sources": []
            }
