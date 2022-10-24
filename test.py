from standardizeStats import basicOrAdvancedStatMean
import pickle
import pandas as pd

# with open('SavedModels/finalized_model.pkl', 'rb') as file:  # Change filename here if model is named differently
#     pickleModel = pickle.load(file)
  
# print(pickleModel)

pick = pd.read_pickle('SavedModels/finalized_model.pkl')
print(pick)