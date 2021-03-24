# librairies utilisées
from wordcloud import WordCloud
import matplotlib.pyplot as plt
#Entrer le texte
texte = ("python")
#créer le wordcloud
word=WordCloud(width=500,height=500,margin=0,max_words=300).generate(texte)

#afficher le wordcloud
plt.imshow(word,interpolation='bilinear')
plt.axis("off")
plt.margins(x=0, y=0)
plt.show()
