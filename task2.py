import PyPDF2


with open('output.txt', 'r') as file:
    sentences = file.readlines()

    with open('recreated.txt', 'w') as output_file:
        for sentence_num, sentence in enumerate(sentences):
            if ': ' not in sentence:
                continue
            sentence_text = sentence.split(': ')[1].strip()
            output_file.write(f'Sentence {sentence_num + 1}: {sentence_text}\n')
