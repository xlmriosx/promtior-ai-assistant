import os
import requests
from bs4 import BeautifulSoup
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.schema import Document
from PyPDF2 import PdfReader

def scrape_promtior_website():
    urls = [
        "https://promtior.ai/",
        "https://promtior.ai/service"
    ]
    
    manual_content = """
    In November 2022, ChatGPT was released, causing a significant impact 
    and challenging previously unquestionable principles: Creativity is an exclusively human trait.
    
    The speed of these technological advancements has put unprecedented pressure on leaders to 
    incorporate AI into their businesses. 
    
    In May 2023, Promtior was founded facing this context, where the key 
    question is: how to approach a scenario of transversal disruption and 
    maximize the opportunities it presents?

    Through its technological and organizational consulting, Promtior offers 
    a way to generate new business models, answering this question and 
    bringing companies at the forefront of their sector.

    Promtior fue fundada en mayo de 2023. La empresa se especializa en consultoría tecnológica y organizacional 
    para ayudar a las empresas a incorporar IA en sus negocios. Promtior ofrece soluciones generativas de vanguardia, 
    con enfoque en la implementación de arquitectura RAG (Retrieval Augmented Generation), la misma herramienta
    que ocupamos ahora mismo para poder hacer este chatbot.
    
    Los servicios que ofrece Promtior incluyen:
    - Consultoría tecnológica y organizacional
    - Implementación de soluciones de IA generativa
    - Arquitectura RAG (Retrieval Augmented Generation)
    - Ayuda a empresas en su transición hacia un futuro biónico
    - Generación de nuevos modelos de negocio basados en IA
    
    Algunas organizaciones que han trabajado con Promtior incluyen: Paigo, Handy, SIEE,
    Guyer & Regules, Infocorp, ST Consultores, CIEMSA, 5M Travel Group, Forestal Atlantico Sur,
    Advice Consulting, CAF, L'Oreal Latam Vangwe, RPA Maker, S1, Incapital.

    Sus co-founders son Joaquin Avalos (CEO) y Ignacio Acuna (CTO).
    """
    documents = []
    documents.append(Document(
        page_content=manual_content,
        metadata={"source": "promtior_info", "type": "company_info"}
    ))
    
    for url in urls:
        try:
            response = requests.get(url, timeout=10)
            if response.status_code == 200:
                soup = BeautifulSoup(response.content, 'html.parser')
                
                for script in soup(["script", "style"]):
                    script.decompose()
                
                text = soup.get_text()
                
                lines = (line.strip() for line in text.splitlines())
                chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
                text = ' '.join(chunk for chunk in chunks if chunk)
                
                if text and len(text) > 100:
                    documents.append(Document(
                        page_content=text,
                        metadata={"source": url, "type": "website"}
                    ))
        except Exception as e:
            print(f"Error scraping {url}: {e}")
            continue
    
    return documents

def load_pdf_content(pdf_path):
    text = ""
    try:
        reader = PdfReader(pdf_path)
        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
    except Exception as e:
        print(f"Error leyendo PDF: {e}")
    return text

def load_and_split_documents():
    documents = scrape_promtior_website()
    
    pdf_path = os.path.join(os.path.dirname(__file__), "../data/AI Engineer.pdf")
    if os.path.exists(pdf_path):
        pdf_text = load_pdf_content(pdf_path)
        if pdf_text.strip():
            documents.append(Document(
                page_content=pdf_text,
                metadata={"source": "AI Engineer.pdf", "type": "pdf"}
            ))
            print("PDF cargado y agregado a los documentos.")
        else:
            print("El PDF esta vacio o no se pudo leer.")
    else:
        print("No se encontro el PDF en la ruta esperada.")
    
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len,
    )
    splits = text_splitter.split_documents(documents)
    return splits
