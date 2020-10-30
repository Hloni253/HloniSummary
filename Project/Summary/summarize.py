from sumy.parsers.html import HtmlParser
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer as Summarizer
from sumy.nlp.stemmers import Stemmer
from sumy.utils import get_stop_words

def Summarize(url):
    LANGUAGE = "english"
    SENTENCES_COUNT = 10

    Sentences = []
    sns = " "
    
    parser = HtmlParser.from_url(url, Tokenizer(LANGUAGE))
    stemmer = Stemmer(LANGUAGE)
    
    summarizer = Summarizer(stemmer)
    summarizer.stop_words = get_stop_words(LANGUAGE)
    
    for sentence in summarizer(parser.document, SENTENCES_COUNT):
        sentence = str(sentence)
        Sentences.append(sentence)
        
    Sentences = sns.join(Sentences)
        
    return Sentences


def Summarize_Text(text):
    LANGUAGE = "english"
    SENTENCES_COUNT = 10

    Sentences = []
    sns = " "
    
    parser = PlaintextParser(text, Tokenizer(LANGUAGE))
    stemmer = Stemmer(LANGUAGE)
    
    summarizer = Summarizer(stemmer)
    summarizer.stop_words = get_stop_words(LANGUAGE)
    
    for sentence in summarizer(parser.document, SENTENCES_COUNT):
        sentence = str(sentence)
        Sentences.append(sentence)
        
    Sentences = sns.join(Sentences)
        
    return Sentences    






















