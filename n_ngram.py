'''
N-grams which n  =  2  
'''

import  re   
#input example 
input = "Natural-language processing (NLP) is an area of computer science "\
    "and artificial intelligence concerned with the interactions "\
    "between computers and human (natural) languages."
    
output_expect   =  [
    "natural language",
    "language processing",
    "processing nlp",
    "nlp is",
    "is an",
    "an area",
] 

def generate_ngarm(s , n):
    #Conver  to lowercases
    new_s  = s.lower()
    #Replace all  none  alphanumberic  characters with spaces  
    s  =   re.sub(r'[^a-zA-Z0-9\s]' , ' ' , new_s)
    output  = [item  for  item  in  s.split(' ') if  item  != '']
    ## Concatentate the item into ngrams and return
    n_grams  =  zip(*[output[i:] for i  in range(n)])

    return  [" ".join(ngram) for ngram in n_grams]


print (generate_ngarm(input , 2))

