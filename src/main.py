import pickle
from sklearn.feature_extraction.text import TfidfVectorizer

class Prediction:
    def __init__(self):
        self.model_path = "src/model/BNBmodel.sav"
        self.vectorizer_filename = 'src/model/count_dict.sav'
        self.loaded_model = pickle.load(open(self.model_path, 'rb'))
        self.vectoriser = pickle.load(open(self.vectorizer_filename, 'rb'))
    
    def get_prediction(self,user_input):
        user_input = user_input
        vectorized_input = self.vectoriser.transform([user_input])
        result = self.loaded_model.predict(vectorized_input)
        print(result)
        if result[0] == 1:
            return "positive"
        else:
            return "negative"

