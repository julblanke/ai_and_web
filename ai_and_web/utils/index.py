class Index:
    def __init__(self):
        self.index = {}

    def add_document(self, document_id, text):
        # Split the text into words
        words = text.split()
        for word in words:
            # Remove punctuation and convert to lowercase for better indexing
            word = word.lower().strip('.,?!')
            if word not in self.index:
                self.index[word] = set()
            self.index[word].add(document_id)

    def search(self, query):
        # Split the query into words
        query_words = query.split()
        result = set()
        for word in query_words:
            word = word.lower().strip('.,?!')
            if word in self.index:
                if not result:
                    result = self.index[word]
                else:
                    result = result.intersection(self.index[word])
        return result

"""
# Example usage
index = SearchEngineIndex()

# Adding documents to the index
index.add_document(1, "This is the first document for testing.")
index.add_document(2, "A second document to demonstrate indexing.")
index.add_document(3, "Another document to show how the search works.")

# Searching for documents
query = "document indexing"
result = index.search(query)

for document_id in result:
    print(f"Found in Document {document_id}")
"""
