## How to run this project?

###  Running the application by Docker
 
- Step 1: Clone project
    ```
  git clone git@github.com:HoangNA1911/G-score.git
  cd <project folder>
    ```
- Step 2: Build the docker image
  ```
  docker build -t g_score .
  ```
- Step 3: Run the Docker Container
  ```
  docker run -p 8000:8000 g_score
  ```

### Running the application locally 

- Step 1: Clone project
    ```
  git clone git@github.com:HoangNA1911/G-score.git
  cd <project folder>
    ```
- Step 2: Set Up a Virtual Environment (Optional)
  ```
  python -m venv venv
  source venv/bin/activate
  ```
- Step 3: Install Dependencies
  ```
  pip install -r requirements.txt
  ```
- Step 4: Apply Database Migrations
  ```
  python manage.py migrate
  ```
- Step 5: Run the Development Server
  ```
  python manage.py runserver
  ```
   
### Hosting(Ngrok) 

I have used ngrok to host my website, you can access it.

This is url: https://f09c-116-110-42-212.ngrok-free.app/

