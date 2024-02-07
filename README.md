
# API Restriction using Redis


This Django project implements rate-limiting and access control using Redis as a cache to restrict the number of API calls users can make within a specified time frame. Users are categorized into three groups: Gold, Bronze, and Silver, each with different API call limits.







## Installation
To install and run the project locally, follow the steps:

1. Clone the repository:


```bash
https://github.com/casonova/Redis-Task.git
```
2. Make Virtual environment:

```bash
python3 -m venv env
```  

3. Install dependencies:

```bash
pip install -r requirements.txt
```    
4. Apply database migrations:
```bash
python manage.py makemigrations
```  

```bash
python manage.py migrate
```    

 
 
## Usage
1. Gold: Users allowed 10 API calls per minute
2. Bronze: Users allowed 5 API calls per minute
3. Silver: Users allowed 2 API calls per minute

```javascript
python manage.py createsuperuser
```
4. Make groups by runing custom management command.
```
python manage.py make_groups
```

5. Access the admin panel at `http://127.0.0.1:8000/admin/` to see the data.

6. Run server and hit end point multiple times to see middleware results.

7. Basic Authentication is set in API so everytime server starts endpoint get hit through browser you have provide credential of user to get login.






## Credits

- [Django Framework](https://www.djangoproject.com/)
- [Django Rest Framework](https://www.django-rest-framework.org/)
- [Redis](https://redis.io/)

