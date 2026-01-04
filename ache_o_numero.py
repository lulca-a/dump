#Find a number in the sentece and change it to '_'
#don't use str methods

sentence = 'Bendito o Deus e Pai de nosso Senhor Jesus Cristo, o qual nos abençoou com todas as bênçã0s espirituais nos lugares celestiais em Cristo;'

sentence = list(sentence)
for index,i in enumerate(sentence):
    #position = sentence.index(i)
    try :
        int(i)
    except ValueError:
        pass
    else:
        sentence[index] = '_'
        
print(''.join(sentence))

