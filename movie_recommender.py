# Import libraries
import streamlit as st
import pandas as pd
from surprise import SVD, Dataset, Reader
from surprise.model_selection import train_test_split as surprise_train_test_split
import pickle

# Load data
@st.cache_data  # Cache data to avoid reloading
def load_data():
    movies = pd.read_csv('movies.csv')
    ratings = pd.read_csv('ratings.csv')
    return movies, ratings

# Train or load SVD model
@st.cache_resource  # Cache model to avoid retraining
def load_or_train_model(ratings):
    reader = Reader(rating_scale=(0.5, 5.0))
    data = Dataset.load_from_df(ratings[['userId', 'movieId', 'rating']], reader)
    trainset = data.build_full_trainset()
    
    # Use optimized SVD parameters from previous experiments
    model = SVD(n_factors=100, n_epochs=30, lr_all=0.005, reg_all=0.02, random_state=42)
    model.fit(trainset)
    
    # Save model to file (optional)
    with open('svd_model.pkl', 'wb') as f:
        pickle.dump(model, f)
    return model

# Function to get top-N recommendations
def get_top_n_recommendations(user_id, model, movies, ratings, n=5):
    all_movie_ids = movies['movieId'].unique()
    rated_movies = ratings[ratings['userId'] == user_id]['movieId'].values
    unrated_movies = [mid for mid in all_movie_ids if mid not in rated_movies]
    predictions = [model.predict(user_id, mid) for mid in unrated_movies]
    top_predictions = sorted(predictions, key=lambda x: x.est, reverse=True)[:n]
    top_movie_ids = [pred.iid for pred in top_predictions]
    top_titles = movies[movies['movieId'].isin(top_movie_ids)][['title', 'genres']].values
    return top_titles

# Streamlit app
def main():
    # Set title and header
    st.title("Movie Recommender System")
    st.markdown("Find movies you'll love based on your tastes!")

    # Load data and model
    movies, ratings = load_data()
    try:
        with open('svd_model.pkl', 'rb') as f:
            model = pickle.load(f)
    except FileNotFoundError:
        model = load_or_train_model(ratings)
        st.write("Model trained successfully!")

    # Sidebar for user input
    st.sidebar.header("Your Preferences")
    user_id = st.sidebar.selectbox("Select your User ID", sorted(ratings['userId'].unique()))
    n_recommendations = st.sidebar.slider("Number of recommendations", 1, 10, 5)

    # Display recommendations
    if st.sidebar.button("Get Recommendations"):
        st.subheader(f"Top {n_recommendations} Recommendations for User {user_id}")
        recommendations = get_top_n_recommendations(user_id, model, movies, ratings, n_recommendations)
        
        # Show results in a table
        for i, (title, genres) in enumerate(recommendations, 1):
            st.write(f"{i}. **{title}** (Genres: {genres})")

    # Add some info about the app
    st.markdown("---")
    st.markdown("### How It Works")
    st.write("This app uses a smart system to guess what movies you'll like based on what others with similar tastes enjoyed. "
             "It’s built with data from real movie fans and fine-tuned to be as accurate as possible!")

    # Display a sample of popular movies
    st.markdown("### Popular Movies")
    popular_movies = ratings.groupby('movieId')['rating'].count().sort_values(ascending=False).head(5)
    popular_movie_ids = popular_movies.index
    popular_titles = movies[movies['movieId'].isin(popular_movie_ids)][['title', 'genres']]
    st.table(popular_titles)

if __name__ == "__main__":
    main()