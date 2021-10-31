from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, pipeline
  


# Initialize tokenizers
de_tokenizer = AutoTokenizer.from_pretrained("Helsinki-NLP/opus-mt-de-en")
  
fr_tokenizer = AutoTokenizer.from_pretrained("Helsinki-NLP/opus-mt-fr-en")

# en_tokenizer = AutoTokenizer.from_pretrained("nlptown/bert-base-multilingual-uncased-sentiment")


# Initialize models
de_model = AutoModelForSeq2SeqLM.from_pretrained("Helsinki-NLP/opus-mt-de-en")
fr_model = AutoModelForSeq2SeqLM.from_pretrained("Helsinki-NLP/opus-mt-fr-en")
# en_model = AutoModelForSequenceClassification.from_pretrained("nlptown/bert-base-multilingual-uncased-sentiment")

# Tokenize text
de_text = "Hallo liebe Freunde, wie geht es Ihnen heute?"
de_tokenized_text = de_tokenizer.prepare_seq2seq_batch([de_text], return_tensors='pt')

fr_text = "Bonjour chers amis, comment allez-vous aujourd'hui?"
fr_tokenized_text = fr_tokenizer.prepare_seq2seq_batch([fr_text], return_tensors='pt')

# Perform translation and decode the output
de_translation = de_model.generate(**de_tokenized_text)
de_translated_text = de_tokenizer.batch_decode(de_translation, skip_special_tokens=True)[0]

fr_translation = fr_model.generate(**fr_tokenized_text)
fr_translated_text = fr_tokenizer.batch_decode(fr_translation, skip_special_tokens=True)[0]

# Sentiment Analysis

sa = pipeline("sentiment-analysis")
de_sa = sa(de_translated_text)


# Print translated text

# print (de_translated_text)
# print(fr_translated_text)
print(de_sa)
