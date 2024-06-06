## End to End machine learning project
## student performance indicator
# Student Performance Indicator

## Project Overview
This project aims to predict students' math scores based on various attributes using machine learning models. The predictions can help identify factors that influence student performance and suggest improvements.

## Project Structure
- **artifacts**: Contains generated files such as datasets and models.
- **notebook**: Contains Jupyter notebooks for EDA and model training.
- **src**: Source code including data ingestion, transformation, training, and prediction.
- **templates**: HTML templates for the web application.
- **app.py**: Flask application for deployment.
- **requirements.txt**: Dependencies required for the project.
- **README.md**: Project documentation.

## Setup and Usage
1. Clone the repository:
2. Set up the virtual environment:
3. Install dependencies:
4. Place your dataset (`stud.csv`) in `notebook/data/`.
5. Run data ingestion:
# python src/components/data_ingestion.py
6.Run data transformation:
# python src/components/data_transformation.py
7. Train the model:
#python src/components/model_train.py
8. Start the Flask app:
# python app.py
9. # Open the app in your browser at http://localhost:5000.