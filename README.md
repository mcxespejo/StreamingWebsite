# StreamingWebsite


## Description
This is a Django-based website for streaming and viewing information about anime movies. It provides a platform for users to browse through a collection of anime movies, view details about each movie, and watch them online.

## Features
- Browse a collection of anime movies.
- View detailed information about each movie.
- Watch movies online.
- User authentication and registration system.
- Add, edit, and delete movies (admin functionality).

## Technologies Used
- Django
- HTML/CSS
- JavaScript
- SQLite (for development)
- Bootstrap (for styling)


## Setup
1. **Clone the repository:**
git clone https://github.com/mcxespejo/StreamingWebsite.git



2. **Navigate to the project directory:**

```bash
  cd Animi-Website-With-Django
```


3. **Install dependencies:**

```bash
  pip install -r requirements.txt
```



4. **Run migrations:**

```bash
  python manage.py migrate
```


5. **Create a superuser (admin user):**


```bash
  python manage.py createsuperuser
```



6. **Start the development server:**

```bash
  python manage.py runserver
```



7. **Open your web browser and navigate to [http://localhost:8000](http://localhost:8000)**

## Usage
- **User Authentication:** Users can sign up for an account and log in to access additional features such as adding movies to favorites.
- **Browsing Movies:** Browse through the collection of anime movies, view details, and watch online.
- **Admin Panel:** Access the admin panel at [http://localhost:8000/admin](http://localhost:8000/admin) to manage movies, users, etc.


