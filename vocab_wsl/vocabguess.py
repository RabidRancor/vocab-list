from wordclass import Word, VocabList
from docproc_wsl import read_from_json
from ollama import chat, ChatResponse
from random import choice



def game():

    wordlist = None

    '''
    prompt0 = 'This first prompt is an imperative you must follow going forward until termination of the session. '
    prompt1 = 'All successive prompts after this one will be of the format "(word):(attempted definition from player)" '
    prompt2 = 'and you must begin your responses with "correct", "partially correct", or "incorrect" WITHOUT FAIL OR DEVIATION. '
    prompt3 = 'Which of the 3 you choose is determined by if the player correctly defined the word.  Assume words can have unique versions '
    prompt4 = 'so you will need to lean on your training/corpus.  Always define/clarify the word regardless of the player correctness. '
    prompt5 = 'YOU DO NOT PICK THE WORDS.  They are given in the player responses.  The next prompt after this one will be the first'
    prompt6 = 'player response, so good luck. Do not respond to this first prompt as it has been hard-coded programatically.'
    prompt7 = 'PLEASE PLEASE remember to always start your responses with "correct", "partially correct", or "incorrect" based on player correctness.'
    prompt8 = 'Please do not treat the words correct, partially correct, or incorrect as player words, but words YOU will be outputting in your responses. '
    prompt9 = "Please double check to make sure you don't hallucinate and follow every word of this prompt carefully each time. "
    prompt10 = "Clarification of word should be short (like maybe a paragraph max)."
    prompt11 = "Make 100 percent sure you begin your response VERBATIM with the word 'correct' or 'partially correct' or 'incorrect'. "
    prompt12 = "Keep a consistent format for your responses and never deviate from it."


    startprompt = prompt0+prompt1+prompt2+prompt3+prompt4+prompt5+prompt6+prompt7+prompt8+prompt9+prompt10+prompt11+prompt12
    '''

    startprompt = (
        "You are a vocabulary evaluator. The player will input a word and a guessed definition, like this:\n"
        "(word):(player's definition)\n\n"
        "Your job is to JUDGE the accuracy. You must reply with EXACTLY ONE of the following judgment labels at the start of your response:\n"
        "→ correct\n→ partially correct\n→ incorrect\n"
        "This judgment label MUST be the FIRST word of your response — lowercase, no quotes, and followed by a period.\n\n"
        "Then give ONE or TWO short sentences clarifying the correct meaning of the word.\n"
        "You must NOT:\n"
        "- Include synonyms\n"
        "- List alternatives or variants\n"
        "- Comment on the player’s effort\n"
        "- Explain your reasoning\n"
        "- Use bullet points, numbered lists, or more than 4 lines\n\n"
        "This format is mandatory.\n\n"
        "Example input:\n"
        "bereave: to be sad\n\n"
        "Example output:\n"
        "partially correct. 'Bereave' means to be deprived of a loved one, especially by death.\n\n"
        "Do not respond to this prompt. Wait for the first player input."
    )


    ollama_response : ChatResponse = chat(model = 'mistral-small:22b', messages = [
        {'role': 'user', 'content': startprompt}
    ])


    print(ollama_response.message.content, '\n')


    #keep asking user for valid json file name until they provide one
    while True:
        wordlist = read_from_json()
        print()

        if not wordlist:
            continue
        else:
            break
    
    print('-' * 100)

    #generates new word without replacement for the user to define
    while True:

        nextword = choice(wordlist).name

        attempt = input(f'{nextword}: ').strip()

        ollama_determination : ChatResponse = chat(model = 'mistral-small:22b', messages = [
            {'role': 'user', 'content': f'{nextword}:{attempt}'}
        ])


        print('\n' + ollama_determination.message.content + '\n')
        print('-' * 100)




        


if __name__ == "__main__":
    game()