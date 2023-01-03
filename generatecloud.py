
import codecs
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from string import punctuation


class Stopwords:
	def __init__(self):
		# coloque aqui as palavras que pretende desconsiderar na nuvem de palavras (imagem) resultante
		new_stopwords = [""]
		self.stopwords = set(stopwords.words('portuguese') + list(punctuation) + list(new_stopwords))

	
def in_natural_language(text):
	my_stopwords = Stopwords()
	palavras_a_serem_desconsideradas = my_stopwords.stopwords
	palavras = word_tokenize(text.lower())
	palavras_sem_stopwords = [palavra for palavra in palavras if palavra not in palavras_a_serem_desconsideradas]
	return palavras_sem_stopwords


def generate_image(words_string):
	text_string = ' '.join([str(elem) for i,elem in enumerate(words_string)])
	wordcloud = WordCloud(width = 800, height = 800, background_color ='white', min_font_size = 10).generate(text_string)
	plt.figure(figsize = (8, 8), facecolor = None)
	plt.imshow(wordcloud)
	plt.axis("off")
	plt.tight_layout(pad = 0)
	plt.savefig("cloud.png")


def write_to_file(what_to_print):
    with open('palavras_extraidas.txt', 'w',  encoding="utf-8") as txt_file:
        for line in what_to_print:
        	txt_file.write("%s\n" % line)



if __name__ == "__main__":
	f = codecs.open("texto.txt", "r", encoding ="latin-1")
	text = f.read()
	palavras = in_natural_language(text)
	write_to_file(palavras)
	generate_image(palavras)
