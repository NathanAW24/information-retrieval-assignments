from typing import List
from collections import defaultdict
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

class UnigramLanguageModel:
    def __init__(self, sentences, global_vocabs, mode="collection", smoothing=False):

        '''
            sentences: sentences of the dataset
            mode: whether this language model is for the whole corpus/collection or just a single document
            smoothing: add-one smoothing
        '''

        self.mode = mode
        self.word_freq = defaultdict(int)
        self.smoothing = smoothing
        self.global_vocabs = global_vocabs
        
        for sentence in sentences:
            for word in sentence:
                if word != SENTENCE_START and word != SENTENCE_END:
                    self.word_freq[word] += 1

        if self.mode == "collection":
            self.word_freq[UNK] = 1

        self.total = sum(self.word_freq.values())


    def calculate_unigram_probability(self, word):
        '''
            calculate unigram probability of a word
        '''
        if not self.smoothing:
            return self.word_freq[word] / self.total
        else:
            if self.mode == "document":
                # print("NUMERATOR", word, self.mode, (self.vocab[word] + 1))
                return (self.word_freq[word] + 1) / (self.total + len(self.global_vocabs))
            if word in self.word_freq:
                count = self.word_freq[word]
            else:
                count = self.word_freq[UNK]
                # print(count)
            # print("NUMERATOR", word, self.mode, (count + 1))
            return ((count + 1) / (self.total + len(self.global_vocabs)))



    def calculate_sentence_probability(self, sentence, normalize_probability=True):
        '''
            calculate score/probability of a sentence or query using the unigram language model.
            sentence: input sentence or query
            normalize_probability: If true then log of probability is not computed. Otherwise take log2 of the probability score.
        '''
        prob = 1
        for word in sentence:
            prob *= self.calculate_unigram_probability(word)
        
        return prob if normalize_probability else math.log(prob, 2)



def calculate_interpolated_sentence_probability(sentence, doc, collection, alpha=0.75, normalize_probability=True):
    '''
        calculate interpolated sentence/query probability using both sentence and collection unigram models.
        sentence: input sentence/query
        doc: unigram language model a doc. HINT: this can be an instance of the UnigramLanguageModel class
        collection: unigram language model a collection. HINT: this can be an instance of the UnigramLanguageModel class
        alpha: the hyperparameter to combine the two probability scores coming from the document and collection language models.
        normalize_probability: If true then log of probability is not computed. Otherwise take log2 of the probability score.
    '''
    prob = 1
    for word in sentence:
        if word == SENTENCE_START or word == SENTENCE_END:
            continue
        prob *= (alpha * doc.calculate_unigram_probability(word)) + ((1-alpha) * collection.calculate_unigram_probability(word))
    return prob if normalize_probability else math.log(prob, 2)

if __name__ == '__main__':
    global_vocabs = read_sentences_from_file('./train_vocab.txt')
    global_vocabs.append([UNK])
    # print(global_vocabs)



    actual_dataset = read_sentences_from_file("./train.txt")
    doc1_dataset = read_sentences_from_file("./doc1.txt")
    doc2_dataset = read_sentences_from_file("./doc2.txt")
    doc3_dataset = read_sentences_from_file("./doc3.txt")
    actual_dataset_test = read_sentences_from_file("./test.txt")

    doc1 = UnigramLanguageModel(doc1_dataset, global_vocabs, mode="document", smoothing=True)
    doc2 = UnigramLanguageModel(doc2_dataset, global_vocabs, mode="document", smoothing=True)
    doc3 = UnigramLanguageModel(doc3_dataset, global_vocabs, mode="document", smoothing=True)
    collection = UnigramLanguageModel(actual_dataset, global_vocabs, mode="collection", smoothing=True)

    num_doc1 = 0
    num_doc2 = 0
    num_doc3 = 0


    for sentence in actual_dataset_test:
        print(f"query: {' '.join(sentence)}")

        prob_doc1 = calculate_interpolated_sentence_probability(sentence, doc1, collection)
        prob_doc2 = calculate_interpolated_sentence_probability(sentence, doc2, collection)
        prob_doc3 = calculate_interpolated_sentence_probability(sentence, doc3, collection)

        max_prob = max(prob_doc1, prob_doc2, prob_doc3)
        print("Interpolated Prob\ndoc1:", prob_doc1, "\ndoc2:", prob_doc2, "\ndoc3:", prob_doc3, "\n")

        choose_doc = ""

        if max_prob == prob_doc1:
            num_doc1 += 1
            choose_doc = "doc1"
        elif max_prob == prob_doc2:
            num_doc2 += 1
            choose_doc = "doc2"
        elif max_prob == prob_doc3:
            num_doc3 += 1
            choose_doc = "doc3"

        print(f"Most probable document: {choose_doc}")
    
    print("\n")
    print(f"Number of doc1 {num_doc1}")
    print(f"Number of doc2 {num_doc2}")
    print(f"Number of doc3 {num_doc3}")

    '''
        Question: for each of the test queries given in test.txt, find out best matching document/doc
        according to their interpolated sentence probability.
        Optional: Extend the model to bigram language modeling.
    '''
