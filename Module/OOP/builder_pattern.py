"""
    Builder method implementation
    """
from abc import ABC, abstractmethod


class Document:
    def __init__(self):
        self.content = ""

    def add_content(self, content):
        self.content += content

    def __str__(self):
        return self.content


class DocumentBuilder(ABC):
    @abstractmethod
    def set_title(self, title):
        pass

    @abstractmethod
    def add_heading(self, heading):
        pass

    @abstractmethod
    def add_paragraph(self, paragraph):
        pass

    @abstractmethod
    def get_document(self):
        pass


class PDFDocumentBuilder(DocumentBuilder):
    def __init__(self):
        self.document = Document()

    def set_title(self, title):
        self.document.add_content(f"PDF Title: {title}\n")

    def add_heading(self, heading):
        self.document.add_content(f"PDF Heading: {heading}\n")

    def add_paragraph(self, paragraph):
        self.document.add_content(f"PDF Paragraph: {paragraph}\n")

    def get_document(self):
        return self.document


class HTMLDocumentBuilder(DocumentBuilder):
    def __init__(self):
        self.document = Document()

    def set_title(self, title):
        self.document.add_content(f"<h1>{title}</h1>\n")

    def add_heading(self, heading):
        self.document.add_content(f"<h2>{heading}</h2>\n")

    def add_paragraph(self, paragraph):
        self.document.add_content(f"<p>{paragraph}</p>\n")

    def get_document(self):
        return self.document


class PlainTextDocumentBuilder(DocumentBuilder):
    def __init__(self):
        self.document = Document()

    def set_title(self, title):
        self.document.add_content(f"Plain Text Title: {title}\n\n")

    def add_heading(self, heading):
        self.document.add_content(f"Plain Text Heading: {heading}\n")

    def add_paragraph(self, paragraph):
        self.document.add_content(f"Plain Text Paragraph: {paragraph}\n")

    def get_document(self):
        return self.document


class DocumentDirector:
    def __init__(self, builder):
        self.builder = builder

    def build_document(self, title, headings, paragraphs):
        self.builder.set_title(title)
        for heading in headings:
            self.builder.add_heading(heading)
        for paragraph in paragraphs:
            self.builder.add_paragraph(paragraph)


if __name__ == "__main__":
    TITLE = "Sample Document"
    headings = ["Heading 1", "Heading 2", "Heading 3"]
    paragraphs = [
        "This is the first paragraph.",
        "This is the second paragraph.",
        "This is the third paragraph.",
    ]

    pdf_builder = PDFDocumentBuilder()
    director = DocumentDirector(pdf_builder)
    director.build_document(TITLE, headings, paragraphs)
    pdf_document = pdf_builder.get_document()
    print("PDF Document:")
    print(pdf_document)

    print("\n")

    html_builder = HTMLDocumentBuilder()
    director = DocumentDirector(html_builder)
    director.build_document(TITLE, headings, paragraphs)
    html_document = html_builder.get_document()
    print("HTML Document:")
    print(html_document)

    print("\n")

    plaintext_builder = PlainTextDocumentBuilder()
    director = DocumentDirector(plaintext_builder)
    director.build_document(TITLE, headings, paragraphs)
    plaintext_document = plaintext_builder.get_document()
    print("Plain Text Document:")
    print(plaintext_document)
