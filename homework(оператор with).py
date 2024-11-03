class WordsFinder():

    def __init__(self, *file_names):
        self.file_names = list(file_names)

    def get_all_words(self):
        words_dict = {}
        for i in self.file_names:
            with open(i, encoding="utf-8") as file:
                words_dict[i] = list()
                for line in file:
                    line = line.lower()
                    for symb in line:
                        if symb in [',', '.', '=', '!', '?', ';', ':', '-']:
                            line = line.replace(symb, "")
                    words_dict[i] += (line.split())
        return words_dict

    def find(self, word):
        found_word_pos = {}
        pas = False
        for i in self.file_names:
            all_words = self.get_all_words()[i]
            if word.lower() in all_words:
                pas = True
                return {i: all_words.index(word.lower()) + 1}
        if not pas:
            return "В этих файлах нет такого слова"

    def count(self, word):
        word_count = {}
        for i in self.file_names:
            cnt = 0
            all_words = self.get_all_words()[i]
            if word.lower() in all_words:
                word_count[i] = all_words.count(word.lower())
        return word_count

finder = WordsFinder('test_file1', 'test_text2')
print(finder.get_all_words())
print(finder.find('каравай'))
print(finder.count('text'))
