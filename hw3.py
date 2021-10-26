class CountVectorizer():
    """
    Класс содержит следующие параметры:
    corpus - исходный текст
    feature_names - список уникальных слов в corpus
    count_matrix - терм-документная матрица для corpus
    и методы:
    fit_transform - формирует матрицу с количеством вхождений слов из feature_names в текст
    get_feature_names - возвращает список уникальных слов из corpus
    """

    def __init__(self):
        self.corpus = []
        self.feature_names = []
        self.count_matrix = []

    def fit_transform(self, corpus: list) -> list:
        feature_names = set()
        for line in corpus:
            new_line = line.lower().split()
            self.corpus.append(new_line)
            for word in new_line:
                feature_names.add(word)

        self.feature_names = list(feature_names)

        self.count_matrix = []
        for line_num, line in enumerate(self.corpus):
            self.count_matrix.append([])
            for word in self.feature_names:
                self.count_matrix[line_num].append(line.count(word))
        return self.count_matrix

    def get_feature_names(self) -> list:
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
