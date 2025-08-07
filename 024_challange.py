class AIModel:
    def __init__(self, model_name, accuracy_scores):
        self.model_name= model_name
        self.accuracy_scores = accuracy_scores
    
    def get_best_accuracy(self):
        return max(self.accuracy_scores)
    
aimodels = [
    AIModel("gpt",[23.454,34.454,56.454]),
    AIModel("claude",[25.454,43.434,35.43]),
    AIModel("meta",[29.454,34,53]),
]


def get_best_model(models):
     best_model = None
     best_score = float('-inf')

     for model in models:
       
       score = model.get_best_accuracy()
       if score > best_score:
           best_score = score
           best_model = model.model_name
     

     print(f'the best model is {best_model}and its score is {best_score}')



    
get_best_model(aimodels)

