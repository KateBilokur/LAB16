import nltk
from nltk.corpus import gutenberg
from nltk.probability import FreqDist
import matplotlib.pyplot as plt
import string


# Завантаження пакету стоп-слів
nltk.download('stopwords')
nltk.download('gutenberg')
nltk.download('punkt')

# Імпортуємо стоп-слова
from nltk.corpus import stopwords

# Завантаження тексту
emma_text = gutenberg.words('austen-emma.txt')

# Визначення кількості слів у тексті
word_count = len(emma_text)
print(f'Кількість слів у тексті: {word_count}')

# Частотний розподіл слів
fdist = FreqDist(emma_text)

# Визначення 10 найбільш вживаних слів
top_10_words = fdist.most_common(10)
print('10 найбільш вживаних слів:', top_10_words)

# Побудова стовпчастої діаграми для топ-10 слів
words, counts = zip(*top_10_words)
plt.figure(figsize=(12, 6))
plt.bar(words, counts)
plt.title('Топ-10 найбільш вживаних слів')
plt.xlabel('Слова')
plt.ylabel('Частота')
plt.show()

# Видалення пунктуації та стоп-слів
stop_words = set(stopwords.words('english'))
cleaned_text = [word.lower() for word in emma_text if word.isalpha() and word.lower() not in stop_words]

# Частотний розподіл після очищення тексту
fdist_cleaned = FreqDist(cleaned_text)
top_10_cleaned_words = fdist_cleaned.most_common(10)
print('10 найбільш вживаних слів після очищення:', top_10_cleaned_words)

# Побудова стовпчастої діаграми для очищеного тексту
words_cleaned, counts_cleaned = zip(*top_10_cleaned_words)
plt.figure(figsize=(12, 6))
plt.bar(words_cleaned, counts_cleaned, color='orange')
plt.title('Топ-10 найбільш вживаних слів після очищення')
plt.xlabel('Слова')
plt.ylabel('Частота')
plt.show()
