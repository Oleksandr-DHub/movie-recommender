# Movie Recommender System

Welcome to the **Movie Recommender System**! This project helps you find movies you’ll love by suggesting personalized recommendations based on what others with similar tastes enjoy. It’s built using real movie ratings and powered by smart algorithms.

## What It Does
- Takes movie ratings from users and predicts what you might like.
- Suggests top movies you haven’t seen yet, tailored to your preferences.
- Runs as a web app where you pick your user ID and get a list of recommendations.

## Why We Built It
Choosing a movie can be overwhelming with so many options out there. We wanted to save time and make movie nights more fun for viewers while helping streaming platforms keep their audience engaged.

---

## Getting Started

### Prerequisites
- **Python 3.9+**: Make sure you have Python installed.
- **Data Files**: You’ll need `movies.csv` and `ratings.csv`, they're in the project folder.

### Installation
1. **Clone the repository:**
  - git clone https://github.com/Oleksandr-DHub/movie-recommender.git
  - cd movie-recommender
   
2. **Install dependencies:**
- pip install -r requirements.txt

3. **Prepare the data:**
- Use movies.csv and ratings.csv from the project folder.
- Put them in the same folder as the code.


### Running the App
1. **Start the Streamlit app:**
- streamlit run movie_recommender.py

2. **Open your browser:**
- Go to http://localhost:8501.

3. **Use it:**
- Pick a user ID from the sidebar (1 to 610).
- Choose how many recommendations you want (1–10).
- Click "Get Recommendations" and enjoy your movie list!

### How It Works
- `Data`: Uses MovieLens ratings to understand user preferences.
- `Model`: Powered by an optimized SVD algorithm (error ~0.85/5) and a neural network (Neural Collaborative Filtering) for accurate predictions.
- `App`: A Streamlit interface lets you interact with the system easily.

### Project Structure
The project includes the following files:  
- `Film_recommendation_system.ipynb`: Notebook with research and experiments (model comparisons, visualizations).  
- `movie_recommender.py`: Main app code with Streamlit interface for recommendations.  
- `movies.csv`: Movie titles and genres from MovieLens.  
- `ratings.csv`: User ratings data from MovieLens.  
- `requirements.txt`: List of Python libraries needed to run the project.  
- `svd_model.pkl`: Pre-trained SVD model saved as a pickle file for faster app loading.

### Results
- `Accuracy`: Predicts ratings with an error of ~0.85–0.9 out of 5.
- `Top Picks`: Favorites like "The Shawshank Redemption" and "The Matrix" often show up.
- `Insights`: People love high ratings (4–5 stars), and genres like noir outperform horrors.

### Limitations
- Based on data up to 2022 — newer movies aren’t included yet.
- Works best if you’ve rated enough movies.
- May lean toward popular picks over niche ones.

### Future Ideas
- Add newer ratings for up-to-date suggestions.
- Include movie details like actors or directors.
- Let users input their own ratings in the app.
