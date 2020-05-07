# A better way to identify names from a document

from nltk import ne_chunk, pos_tag, word_tokenize
from nltk.tree import Tree
import nltk
import docx2txt
def get_continuous_chunks(text):
     flag=1
     chunked = ne_chunk(pos_tag(word_tokenize(text)))
     #chunked.draw()
     continuous_chunk = []
     current_chunk = []
     #print(len(chunked))
     j=0
     for i in range(len(chunked)):
             if(flag==2 and i<j+i+1):
                 continue
             if type(chunked[i]) == Tree:
                     #print(chunked[i].label())
                     if(chunked[i].label()=='PERSON'):
                         current_chunk.append(" ".join([token for token, pos in chunked[i].leaves()]))
                         c=chunked[i+1:]
                         #print(c)
                         for j in range(len(c)):
                            if type(c[j])==Tree:
                                #print(c[j].label())
                                current_chunk.append(" ".join([token for token, pos in c[j].leaves()]))
                                #print(current_chunk)
                                #print(j)
                                #print(len(c))
                                if(j==len(c)-1):
                                    flag=0
                                    

                            else:
                                
                                flag=2
                                if(j!=0):
                                    named_entity = " ".join(current_chunk)
                                    #print(named_entity)
                                    if named_entity not in continuous_chunk:
                                        continuous_chunk.append(named_entity)
                                
                                current_chunk=[]
                                break
                     if(flag==0):
                         named_entity = " ".join(current_chunk)
                         if named_entity not in continuous_chunk:
                                continuous_chunk.append(named_entity)
                         break
     return continuous_chunk
 
# sen = docx2txt.process(r"C:\Users\Priyanshu Gupta\Desktop\Resume Extractor\priyanshu.docx")
# sentences=[]
# sen=[el.strip() for el in sen.split("\n") if len(el) > 0]
# for sentence in sen:
#     sentence=nltk.sent_tokenize(sentence)
#     for a in sentence:
#         sentences.append(a)
# for i in sentences:
#     print(get_continuous_chunks(i))