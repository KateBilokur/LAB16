import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer, PorterStemmer
import string

# Завантаження необхідних ресурсів NLTK
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

# Збереження довільного тексту до 100 слів у текстовий файл
text = """Emma by Jane Austen is one of the most critically acclaimed novels of English literature. 
It tells the story of a young woman whose misguided attempts at matchmaking bring 
her into comedic entanglements and self-discovery. Emma's journey showcases her growth 
from a self-assured matchmaker to someone who understands the complexity of human emotions."""
with open('original_text.txt', 'w') as f:
    f.write(text)

# Читання тексту з файлу
with open('original_text.txt', 'r') as f:
    raw_text = f.read()

# Токенізація по словам
tokens = word_tokenize(raw_text)

# Лемматизація та стемінг
lemmatizer = WordNetLemmatizer()
stemmer = PorterStemmer()

# Видалення пунктуації та приведення слів до нижнього регістру
tokens = [token.lower() for token in tokens if token.isalpha()]

# Лемматизація
lemmatized_tokens = [lemmatizer.lemmatize(token) for token in tokens]

# Стемінг (для порівняння можна закоментувати, якщо потрібна тільки лемматизація)
stemmed_tokens = [stemmer.stem(token) for token in lemmatized_tokens]

# Видалення стоп-слів
stop_words = set(stopwords.words('english'))
filtered_tokens = [token for token in stemmed_tokens if token not in stop_words]

# Запис обробленого тексту у інший файл
with open('processed_text.txt', 'w') as f:
    f.write(' '.join(filtered_tokens))

print('Оброблений текст збережено у файлі "processed_text.txt".')
