from PyPDF2 import PdfReader
import re

def extractText(filePath: str):
    reader = PdfReader(filePath)
    print(f"Numero de paginas: {len(reader.pages)}")

    textPage = reader.pages[2].extract_text()

    # remove informações desnecessárias
    cleaned_text_page = cleanPageText(textPage)

    # separa a pagina por questões
    text_questions = cleaned_text_page.split("QUESTÃO")
    questions_numbers = re.findall(r'(QUESTÃO\s+\d{2})', cleaned_text_page)

    print(questions_numbers)
    print('\n\n')

    questions = []
    for question in text_questions:
        if(question):
            questions.append('QUESTÃO ' + question)

    print('\n\n'.join(questions))

    questions_answers = getAnswer(questions)

    # pega as repostas de cada questão

    print('\n\nBody de cada QUESTÃO com respostas')
    for number, data in questions_answers.items():
        print(f'\n\nQuestao {number}: ')
        print('\t{')
        print(f'\tbody: {data["body"]}: ')
        print('\tanswer: {')
        for a, c in data["answer"]:
            print(f'\t\t{a}')
            print(f'\t\t{c}')
        print('\t}')
    
    

def cleanPageText(text: str) -> str:
    # Retira todas as ocorrencias da palavra ENEM2024 e *010175AZ2* (codigo de barras) e variações que possam existir
    cleaned_text = re.sub(r'(ENEM20[0-9A-Z]{2})|(\*[0-9A-Z]+\*)|(\d{2}/\d{2}/\d{4}\s+\d{2}:\d{2}:\d{2})|(Questões de 01 a 05 (opção espanhol))|(Questões de 01 a 05 (opção inglês))', '', text)

    # Remove espaços desnecessários entre as linhas e remove linhas vazias
    cleaned_lines = []
    for line in cleaned_text.split('\n'):
        line = line.strip()
        if(line):
            cleaned_lines.append(line)
    
    # junta todas as linhas limpas e remove as 3 ultimas linhas que contem:
    # -> Tipo da prova, ex.: LINGUAGENS, CÓDIGOS E SUAS TECNOLOGIAS E REDAÇÃO
    # -> Numero da Pagina
    # -> informações sobre arquivos desnecessários
    cleaned_text = '\n'.join(cleaned_lines[:-3])

    return cleaned_text

def getAnswer(questions: list) -> dict:
    answer_per_question = {}

    # pega as respostas iniciando pela letra maiscula A,B,C,D,E e vai até o ultimo ponto final e retira especificações de Questões 01 a 05 de tal materia
    #padrao = r'^([A-E])(?:\s+|\n)(.+?\.)(?=\s+[A-E]|$)'
    padrao = r'^([A-E])(?:\s+|\n)(.+?\.)(?=\s+[A-E]|\s*Questões|\s*$|$)'

    for question in questions:
        q = str(question)
        answer_start_index = 0

        if re.search(r'(QUESTÃO\s+\d{2})', q):
            for i in range(0, len(q)):
                if (i > 2) and (q[i] == 'A') and (q[i-1] in (' ', '\n')) and (q[1+i]  in (' ', '\n')) and (q[i-2] != '.'):
                    answer_start_index = i
                    break

            body = q[0:answer_start_index]

            answer = re.findall(padrao, q[answer_start_index:], flags=re.MULTILINE | re.DOTALL)

            question_number = (q)[9:11]
            answer_per_question[question_number] = {
                'body': body,
                'answer': answer
            }

    return answer_per_question





