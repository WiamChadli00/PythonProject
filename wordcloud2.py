from PIL import Image
from os import path
from wordcloud import WordCloud, STOPWORDS
import numpy as np
#lire le texte
text=open("barack.txt",mode='r',encoding='utf-8').read()
stopwords = STOPWORDS #Pour filtrer les mots qu'on ne veut pas utiliser
#construire le mask
alice=np.array(Image.open(path.join("ppWhite.png")))
#Condtruire le wordcloud

wc = WordCloud(
     background_color='white',
    stopwords=stopwords,
    height=600,
    width=400,
    mask=alice,
    contour_width=0.05,


 )

wc.generate(text)
#enregistrer le cloud dans un fichier
wc.to_file('wordcloud_test.png')
