import fitz  # PyMuPDF
import openpyxl
import re

def format_code(code):
    """Remove letras do código, mantendo apenas os números."""
    return re.sub(r'\D', '', code)

def search_in_pdf(pdf_path, search_code):
    """
    Procura o código no PDF e retorna o contexto encontrado,
    se contiver MM ou RB antes do código.
    Retorna None se o código não for encontrado.
    """
    try:
        pdf_document = fitz.open(pdf_path)
        
        # Iterar por todas as páginas
        for page_number in range(pdf_document.page_count):
            page = pdf_document[page_number]
            text = page.get_text()

            # Procurar pelo código no texto
            for line in text.splitlines():
                if search_code in line:
                    # Identificar o contexto da ocorrência
                    words = line.split()
                    for word in words:
                        if search_code in word and (word.startswith("MM") or word.startswith("RB")):
                            return word  # Retorna o texto encontrado
        return None  # Não encontrado
    except Exception as e:
        print(f"Erro ao processar o PDF: {e}")
        return None

def process_spreadsheet(spreadsheet_path, pdf_path):
    """Processa a planilha para buscar códigos no PDF e atualizar os resultados."""
    try:
        # Carregar a planilha
        workbook = openpyxl.load_workbook(spreadsheet_path)
        sheet = workbook.active

        # Iterar pelos códigos na coluna A (a partir da célula A2)
        for row in range(2, sheet.max_row + 1):
            original_code = sheet[f"A{row}"].value
            if original_code is not None:
                # Formatar o código (remover letras)
                formatted_code = format_code(original_code)

                # Buscar o código no PDF
                context = search_in_pdf(pdf_path, formatted_code)

                # Atualizar a célula D com o resultado
                if context:
                    sheet[f"D{row}"] = context
                    print(f"Código {formatted_code} encontrado: {context}")
                else:
                    sheet[f"D{row}"] = "Não encontrado"
                    print(f"Código {formatted_code} não encontrado.")

        # Salvar as alterações na planilha
        workbook.save(spreadsheet_path)
        print(f"Planilha atualizada salva em: {spreadsheet_path}")

    except Exception as e:
        print(f"Erro ao processar a planilha: {e}")

# Exemplo de uso
spreadsheet_path = "C:/Users/Usuario/Desktop/base_conversor.xlsx"  # Caminho para a planilha
pdf_path = "C:/Users/Usuario/Desktop/catalogo_jamaica.pdf"  # Caminho para o PDF
process_spreadsheet(spreadsheet_path, pdf_path)
