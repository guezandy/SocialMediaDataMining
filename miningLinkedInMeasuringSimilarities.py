#CLUSTERING FIND 

import nltk

ceo_bigrams = nltk.bigrams("Chief Executive Officer".split(), pad_right=True, 
                                                              pad_left=True)
cto_bigrams = nltk.bigrams("Chief Technology Officer".split(), pad_right=True, 
                                                               pad_left=True)

print ceo_bigrams
print cto_bigrams
print len(set(ceo_bigrams).intersection(set(cto_bigrams)))