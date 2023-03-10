import PyPDF2

with open('a.pdf', 'rb') as file:
    pdf_reader = PyPDF2.PdfFileReader(file)

    num_pages = pdf_reader.getNumPages()

    with open('output.txt', 'w') as output_file:

        for page_num in range(num_pages):
            page = pdf_reader.getPage(page_num)

            text = page.extract_text()

            sentences = text.split('. ')

            for sentence_num, sentence in enumerate(sentences):
                if sentence_num != len(sentences) - 1:
                    sentence += '.'
                output_file.write(f'Sentence {sentence_num + 1}: {sentence}\n')
