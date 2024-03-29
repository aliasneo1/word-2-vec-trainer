
# coding: utf-8

# Simple trainer for word-2-vec models


from gensim.models import Word2Vec
# define training data
import nltk

para="Subclinical hypothyroidism (SH), defined by elevated serum levels of thyroid stimulating hormone (TSH) with normal levels of free thyroid hormones, is common in adults, especially in women over 60 years of age. Among individuals with this condition, up to two-thirds have serum TSH levels between 5-10 mU/L and thyroid autoantibodies; almost half of them may progress to overt thyroid failure, the annual percent risk increasing with serum TSH level. There is evidence that elevated TSH levels in patients with SH do not reflect pituitary compensation to maintain euthyroidism, but a mild tissue hypothyroidism sensu strictu. When lasting more than 6-12 months, SH may be associated with an atherogenic lipid profile, a hypercoagulable state, a subtle cardiac defect with mainly diastolic dysfunction, impaired vascular function, and reduced submaximal exercise capacity. The deviation from normality usually increases with serum TSH level ('dosage effect' phenomenon). Restoration of euthyroidism by levothyroxine (LT4) treatment may correct the lipid profile and cardiac abnormalities, especially in patients with an initially higher deviation from normality and higher serum TSH levels. Importantly, a strong association between SH and atherosclerotic cardiovascular disease, independent of the traditional risk factors, has been recently reported in a large cross-sectional survey (the Rotterdam Study). However, whether SH confers a high risk for cardiovascular disease, and whether LT4 therapy has a long-term benefit that clearly outweighs the risks of overzealous treatment in these individuals, remain topics of controversy. Therefore, until randomized, controlled, prospective, and adequately powered trials provide unequivocal answers to these critical questions, it is advisable to prescribe LT4 therapy on a case-by-case basis, taking into account the risk of progressive thyroid failure and the risk of cardiovascular events."

#creating proper input format for training data
sentences=para.split('. ')
data=[]
for sentence in sentences:
    data.append(nltk.word_tokenize(sentence))

# train model
model = Word2Vec(data, min_count=1)
# summarize the loaded model
print(model)
# summarize vocabulary
words = list(model.wv.vocab)
print(words)
# access vector for one word
print(model['TSH'])
# save model
model.save('model.bin')
# load model
new_model = Word2Vec.load('model.bin')
print(new_model)

