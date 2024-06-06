import os
import dill
import pandas as pd

# Path to the preprocessor file
preprocessor_file_path = os.path.join('artifacts', 'preprocessor.pkl')

# Load the preprocessor object
with open(preprocessor_file_path, 'rb') as file:
    preprocessor = dill.load(file)

# Test data to transform
test_data = pd.DataFrame({
    "gender": ["male"],
    "race_ethnicity": ["group A"],
    "parental_level_of_education": ["bachelor's degree"],
    "lunch": ["standard"],
    "test_preparation_course": ["none"],
    "writing_score": [70],
    "reading_score": [72]
})

# Apply the preprocessor to the test data
transformed_data = preprocessor.transform(test_data)
print(transformed_data)
