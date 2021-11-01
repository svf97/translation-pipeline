#!/usr/bin/python

import subprocess
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, pipeline

def lang_detect(input_review):
    """
    in progress
    """

    # build_img = 'sudo docker build . -t seqtolang'
    
    subprocess.run(['sudo', 'docker', 'build', '.', '-t', 'seqtolang'])
    lang = subprocess.run(['docker', 'run', '-e', 'SEQTOLANG_TEXT=', input_review,'seqtolang'], capture_output=True)
    # lang = str(tmp.communicate()) 
    return (input_review,lang)

def translate (input_review,lang):
    """
    translate input review.
    """

    lang_detected = {
        1: 'de',
        2: 'fr'
    }

    lang_translate = lang_detected.get(lang, "N/A")

    if lang_translate == 'de':
        de_text = input_review

        # Initialize tokenizer
        de_tokenizer = AutoTokenizer.from_pretrained("Helsinki-NLP/opus-mt-de-en")

        # Initialize models
        de_model = AutoModelForSeq2SeqLM.from_pretrained("Helsinki-NLP/opus-mt-de-en")

        # Tokenize text
        # de_text = "Hallo liebe Freunde, wie geht es Ihnen heute?"
        de_tokenized_text = de_tokenizer.prepare_seq2seq_batch([de_text], return_tensors='pt')

        # Perform translation and decode the output
        de_translation = de_model.generate(**de_tokenized_text)
        translated_text = de_tokenizer.batch_decode(de_translation, skip_special_tokens=True)[0]


    elif lang_translate == 'fr':
        fr_text = input_review

        # Initialize tokenizer
        fr_tokenizer = AutoTokenizer.from_pretrained("Helsinki-NLP/opus-mt-fr-en")

        # Initialize models
        fr_model = AutoModelForSeq2SeqLM.from_pretrained("Helsinki-NLP/opus-mt-fr-en")

        # fr_text = "Bonjour chers amis, comment allez-vous aujourd'hui?"
        fr_tokenized_text = fr_tokenizer.prepare_seq2seq_batch([fr_text], return_tensors='pt')

        fr_translation = fr_model.generate(**fr_tokenized_text)
        translated_text = fr_tokenizer.batch_decode(fr_translation, skip_special_tokens=True)[0]

    return (translated_text)

def sentiment_analysis(translated_text):
    """
    """
    sa = pipeline("sentiment-analysis")
    x = sa(translated_text)
    sentiment, score= x[0].get('label'), x[0].get('score')
    
    return (sentiment, score)

# Print translated text

# print (de_translated_text)
# print(fr_translated_text)
# sentiment_analysis("i am sad")


# print (lang_detect("Hallo liebe Freunde, wie geht es Ihnen heute"))
# print (lang_detect("Bonjour chers amis, comment allez-vous aujourd'hui?"))

input_review = "Hallo liebe Freunde, wie geht es Ihnen heute"
# print (subprocess.run(['docker', 'run', '-e', 'SEQTOLANG_TEXT=', input_review,'seqtolang'], capture_output=True))


from subprocess import run, PIPE

p = run(['sudo','docker', 'run', '-e', 'seqtolang', 'SEQTOLANG_TEXT="'], stdout=PIPE, input=input_review+'"', encoding='ascii')

print (p.returncode)
# -> 0
print (p.stdout)

# from subprocess import Popen, PIPE, STDOUT

# subprocess.run(['sudo', 'docker', 'build', '.', '-t', 'seqtolang'])

# p = Popen(['sudo','docker', 'run', '-e', 'seqtolang', 'SEQTOLANG_TEXT="'], stdout=PIPE, stdin=PIPE, stderr=STDOUT)    
# grep_stdout = p.communicate(input=input_review.encode()+b'\"')[0]
# print 
# print(grep_stdout.decode())