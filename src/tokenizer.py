# واجهة Tokenizer في TITAN

class Tokenizer:
    def __init__(self, vocabulary=None):
        self.vocabulary = vocabulary or {}
        self.inverse_vocabulary = {
            token_id: token
            for token, token_id in self.vocabulary.items()
        }

    def encode(self, text):
        tokens = text.split()

        return [
            self.vocabulary.get(token, 0)
            for token in tokens
        ]

    def decode(self, token_ids):
        tokens = [
            self.inverse_vocabulary.get(token_id, "<UNK>")
            for token_id in token_ids
        ]

        return " ".join(tokens)

    def token_count(self, text):
        return len(self.encode(text))

    def vocabulary_size(self):
        return len(self.vocabulary)
