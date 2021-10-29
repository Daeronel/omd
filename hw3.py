from collections import Counter


class CountVectorizer():
    """Класс содержит следующие параметры:
    feature_names - список уникальных слов в corpus(исходный текст)
    """

    def __init__(self):
        self.feature_names = []

    def fit_transform(self, corpus: list) -> list:
        """Функция возвращает терм-документную матрицу для corpus
        """
        lower_corpus = self.fit(corpus)
        count_matrix = self.transform(lower_corpus)

        return count_matrix

    def fit(self, corpus: list) -> list:
        """Функция формирует список уникальных слов в тексте
        и возвращает текст, приведенный к единому регистру и разбитый на слова.
        """

        feature_names = set()
        lower_corpus = []
        for line in corpus:
            new_line = line.lower().split()
            lower_corpus.append(new_line)
            for word in new_line:
                feature_names.add(word)
        self.feature_names = list(feature_names)

        return lower_corpus

    def transform(self, lower_corpus: list) -> list:
        """Функция считает количество вхождений каждого слова в текст
        (формирует терм-документную матрицу для corpus)
        """
        count_matrix = []
        for line_num, line in enumerate(lower_corpus):
            count_matrix.append([])
            counter = Counter(line)
            for word in self.feature_names:
                count_matrix[line_num].append(counter.get(word, 0))

        return count_matrix

    def get_feature_names(self) -> list:
        """Функция возвращает параметр класса feature_names
        - список уникальных слов в corpus(исходный текст)
        """
        return self.feature_names


if __name__ == '__main__':
    corpus = [
        'Crock Pot Pasta Never boil pasta again',
        'Pasta Pomodoro Fresh ingredients Parmesan to taste'
    ]
    vectorizer = CountVectorizer()
    count_matrix = vectorizer.fit_transform(corpus)
    print(vectorizer.get_feature_names())
    print(count_matrix)
