# 🎬 Movie Recommendation System

This is an interactive web application that provides personalized movie recommendations based on user-selected movies. Built with Python and Streamlit, it suggests movies by calculating similarities between movies using a precomputed similarity matrix.

## 🚀 Features
- **Interactive UI**: Allows users to select a movie and receive personalized recommendations.
- **Efficient Similarity Calculation**: Uses a precomputed similarity matrix for accurate movie suggestions.
- **Deployed Application**: The application is now live and accessible via the deployment link below.

## 🌐 Live Demo
You can explore the live application.

## 🛠️ Tech Stack
- **Python**: Core programming language.
- **Streamlit**: Framework for creating the web interface.
- **Pandas**: Used for data handling and processing.
- **Pickle**: For loading the precomputed similarity matrix and movie metadata.

## 📂 Project Structure
```
MOVIE-RECOMMENDATION-SYSTEM/
│
├── app.py                # Main application script
├── similarity.pkl         # Precomputed similarity matrix (pickled)
├── movie_dict.pkl         # Dictionary containing movie metadata (pickled)
└── README.md              # Project documentation
└── datapreprocessing.ipynb # Data Preprocessing  
```

## 🎯 How It Works
1. **Movie Data**: The system uses a dataset of movies, where each movie has a similarity score compared to all other movies.
2. **Similarity Matrix**: The similarity matrix is stored in `similarity.pkl`, containing precomputed similarity scores for all movies.
3. **Recommendation**: When a user selects a movie, the system retrieves similar movies using the precomputed matrix and displays the top 5 recommendations.

## 🔧 Local Installation and Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/MOVIE-RECOMMENDATION-SYSTEM.git
   ```

2. **Navigate to the project directory**:
   ```bash
   cd MOVIE-RECOMMENDATION-SYSTEM
   ```

3. **Create a virtual environment**:
   ```bash
   conda create --name recommender-env python=3.8
   conda activate recommender-env
   ```

4. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

5. **Run the application locally**:
   ```bash
   streamlit run app.py
   ```

6. **Open your browser**: Visit `http://localhost:8501` to interact with the app.

## 🌐 Deployment
The application has been deployed and is live at: [Live Demo](#) _(add your deployment link)_.

## 💻 Example Code Snippet

```python
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    for i in movies_list:
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies
```

## 📑 License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## 🤝 Contributing
Pull requests are welcome! For major changes, please open an issue to discuss the proposed changes.

## 📧 Contact
Feel free to reach out via LinkedIn or email me at `vinayiet435@gmail.com` if you have any questions or feedback.
