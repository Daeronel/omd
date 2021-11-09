from math import log
from collections import Counter
from typing import List


class TfIdfTransformer():
    """Класс TfIdfTransformer
    """

    def __init__(self):
        pass

    def tf_transform(self, count_matrix: list) -> list:
        """Функция возвращает матрицу term frequency
        """
        tf_matrix = []
        for line in count_matrix:
            new_line = []
            n = sum(line)
            for word in line:
                new_line.append(round(word / n, 3))
            tf_matrix.append(new_line)

        return tf_matrix

    def idf_transform(self, count_matrix: list) -> list:
        """Функция возвращает матрицу inverse document-frequency
        """
        docs = len(count_matrix)
        n = len(count_matrix[0])
        list = [0 for i in range(n)]
        idf_matrix = []

        for i in range(0, n):
            for j in range(0, docs):
                if count_matrix[j][i] > 0:
                    list[i] += 1

        for word in list:
            idf_matrix.append(round(log((docs + 1) / (word + 1)) + 1, 1))

        return idf_matrix

    def fit_transform(self, count_matrix: list) -> list:
        """Функция формирует из терм-документной матрицы матрицу tf-idf = tf*idf
        """

        tf_matrix = self.tf_transform(count_matrix)
        idf_matrix = self.idf_transform(count_matrix)
        tfidf_matrix = []
        n = len(count_matrix[0])
        for line in tf_matrix:
            new_line = []
            for i in range(0, n):
                new_line.append(round(line[i] * idf_matrix[i], 3))
            tfidf_matrix.append(new_line)

        return tfidf_matrix


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

    def transform(self, lower_corpus: List[str]) -> List[List[int]]:
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


class TfIdfVectorizer(CountVectorizer):
    """Класс TfIdfVectorizer
    """

    def __init__(self) -> None:
        super().__init__()
        self.tfidf_transformer = TfIdfTransformer()

    def fit_transform(self, corpus: list) -> list:
        """Функция формирует из корпуса текстов матрицу tf-idf = tf*idf
        """
        count_matrix = super().fit_transform(corpus)
        return self.tfidf_transformer.fit_transform(count_matrix)


if __name__ == '__main__':
    corpus = [
        'Crock Pot Pasta Never boil pasta again',
        'Pasta Pomodoro Fresh ingredients Parmesan to taste'
    ]
    vectorizer = TfIdfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(corpus)
    print(vectorizer.get_feature_names())
    print(tfidf_matrix)
