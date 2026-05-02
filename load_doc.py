from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters.character import RecursiveCharacterTextSplitter

def load_file(file:str):
    loader_pdf=PyPDFLoader(file)
    pages_pdf=loader_pdf.load()


    for i, page in enumerate(pages_pdf):
        page.page_content = ' '.join(page.page_content.split())
        page.metadata["page_number"] = i

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )
    pages_char_split=splitter.split_documents(pages_pdf)

    return pages_char_split

