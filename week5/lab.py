from collections import defaultdict
from typing import List

import re
import math
import numpy as np

# used for unseen words in training vocabularies
UNK = None
# sentence start and end
SENTENCE_START = "<s>"
SENTENCE_END = "</s>"

def read_sentences_from_file(file_path: str) -> List[List[str]]:
    '''
        read the files.
    '''
    with open(file_path, "r") as f:
        return [re.split("\s+", line.rstrip('\n')) for line in f]

vocabs = read_sentences_from_file('./train.vocab.txt')
vocabs.append([UNK])

class UnigramLanguageModel:
    def __init__(self, sentences, mode="collection", smoothing=False):

        '''
            sentences: sentences of the dataset
            mode: whether this language model is for the whole corpus/collection or just a single document
            smoothing: add-one smoothing
        '''
        self.mode = mode
        self.smoothing = smoothing

        self.vocab = defaultdict(int)

        for sentence in sentences:
            for word in sentence:
                if word != SENTENCE_START and word != SENTENCE_END:
                    self.vocab[word] += 1
        
        if self.mode == "collection":
            self.vocab[UNK] = 1
        
        self.total = sum(self.vocab.values())

    def calculate_unigram_probability(self, word):
        '''
            calculate unigram probability of a word
        '''
        global vocabs
        if self.smoothing:
            if self.mode == "doc":
                return (self.vocab[word] + 1) / (self.total + len(vocabs))
            if word in self.vocab:
                count = self.vocab[word]
            else:
                count = self.vocab[UNK]
            
            return (count + 1) / (self.total + len(vocabs))
        else:
            return self.vocab[word] / self.total


    def calculate_sentence_probability(self, sentence, normalize_probability=True):
        '''
            calculate score/probability of a sentence or query using the unigram language model.
            sentence: input sentence or query
            normalize_probability: If true then log of probability is not computed. Otherwise take log2 of the probability score.
        '''
        
        return

def calculate_interpolated_sentence_probability(sentence, doc, collection, alpha=0.75, normalize_probability=True):
    '''
        calculate interpolated sentence/query probability using both sentence and collection unigram models.
        sentence: input sentence/query
        doc: unigram language model a doc. HINT: this can be an instance of the UnigramLanguageModel class
        collection: unigram language model a collection. HINT: this can be an instance of the UnigramLanguageModel class
        alpha: the hyperparameter to combine the two probability scores coming from the document and collection language models.
        normalize_probability: If true then log of probability is not computed. Otherwise take log2 of the probability score.
    '''
    return

if __name__ == '__main__':
    # first read the datasets

    actual_dataset = read_sentences_from_file("./train.txt")
    doc1_dataset = read_sentences_from_file("./doc1.txt")
    doc2_dataset = read_sentences_from_file("./doc2.txt")
    doc3_dataset = read_sentences_from_file("./doc3.txt")
    actual_dataset_test = read_sentences_from_file("./test.txt")



    print(doc1_dataset)

    '''
        Question: for each of the test queries given in test.txt, find out best matching document/doc
        according to their interpolated sentence probability.
        Optional: Extend the model to bigram language modeling.
    '''
