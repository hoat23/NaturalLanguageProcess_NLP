## Sørensen–Dice coefficient

The index is known by several other names, especially Sørensen–Dice index,[3] Sørensen index and Dice's coefficient. Other variations include the "similarity coefficient" or "index", such as Dice similarity coefficient (DSC). Common alternate spellings for Sørensen are Sorenson, Soerenson and Sörenson, and all three can also be seen with the –sen ending.

Other names include:

    F1 score
    Czekanowski's binary (non-quantitative) index[4]
    Measure of genetic similarity[5]
    Zijdenbos similarity index,[6][7] referring to a 1994 paper of Zijdenbos et al.[8][3]

### Algorithm
```python
def n_grams(word,n=2):
  word = list("_"+word+"_")
  bigrams = []
  for i in range(0,len(word)-n+1):
    token = ''.join(word[i:i+n])
    bigrams.append(token)
  return bigrams

def SorensenDiceCoefficient(word1,word2):
  bigram1 = n_grams(word1)
  bigram2 = n_grams(word2)
  interseccion = [x for x in bigram1 if x in bigram2]
  coeficient = 2 * len(interseccion) / ( len(bigram1) + len(bigram2) )
  return coeficient
```
### Compare 2 words

#### Compare "cazza" with "caza"
```python 
text1 = "cazza"
coef1 = SorensenDiceCoefficient(text1, "caza")
print("similitud de [cazza] con [caza] : {}".format(coef1))
```
Result
```bash
similitud de [cazza] con [caza] : 0.9090909090909091
```

#### Compare "cazza" with "casa"
```python 
coef2 = SorensenDiceCoefficient(text1, "casa")
print("similitud de [cazza] con [casa] : {}".format(coef2))
```
Result
```bash
similitud de [cazza] con [casa] : 0.5454545454545454
```

### Documentation
- https://help.highbond.com/helpdocs/analytics/141/scripting-guide/en-us/Content/lang_ref/functions/r_dicecoefficient.htm
- https://github.com/life4/textdistance/blob/master/textdistance/algorithms/token_based.py
- https://libraries.io/conda/strsimpy#sorensen-dice-coefficient


