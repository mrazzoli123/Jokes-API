# 🎭 Jokes-API
Jokes-API is a full-stack web application designed to deliver humor on demand. Users can filter through a vast collection of jokes by language and category, or even retrieve a specific joke by its unique ID. The project demonstrates the integration of a Python-based RESTful API with a responsive, interactive frontend.

## 🚀 Key Features
Multilingual Support: Access jokes in over 10 different languages, including English, Spanish, German, Hungarian, and more.

Categorized Humor: Filter jokes based on specific themes like "Neutral" or the legendary "Chuck Norris" facts.

Flexible Retrieval: * Retrieve all jokes for a specific language and category.

Get a randomized selection of a specific number of jokes.

Fetch a single joke directly using its unique ID.

Responsive UI: A clean, mobile-first interface that allows users to pick their preferences and see results instantly without page reloads.

## 🛠️ Tech Stack
### Backend
Framework: Flask (Python) – Powering the RESTful API endpoints.

Joke Engine: pyjokes – A library used to generate the dataset of one-liner jokes.

Logic & Initialization: A custom Joker class that manages the dataset, handles filtering logic, and ensures efficient joke retrieval.

Configuration: Tomllib and config.toml are used for clean, externalized management of supported languages.

### Frontend
UI Framework: Bulma CSS – Used for a modern, responsive, and lightweight design.

Interactivity: Vanilla JavaScript (Async/Await) – Handles asynchronous requests to the backend API via the Fetch API to update the DOM dynamically.

Icons & Styling: FontAwesome for intuitive visual elements.
