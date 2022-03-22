<h1 align="center">Qorb-eLearning-Platform</h1>

<b>
Our platform is “E-learning platform” provide some features by using computer vision and artificial intelligence
technologies as Real Time Arabic Sign Language Translator, Facial Expression Recognition and Recommendation system
</b>

![-------------------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)
<h1 align="center"> Local Setup 👨‍💻 </h1>

## Docker Setup:

```
docker-compose up --build
```

![-------------------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)

## Virtual Environment Setup:

##### For Linux :

```
$. python3 -m venv env
$. source env/bin/activate
```

##### For Windows :

```
$. py -m venv env
$. env\Scripts\activate
```

![-------------------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)

#### 2. Installing Dependencies:

```
 pip install wheel
 pip install -r requirements.txt
```

![-------------------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)

#### 3. Create Database Tables and Superuser:

```
Note: For Windows Users Replace python3 with python

 python3 manage.py makemigrations
 python3 manage.py migrate
 python3 manage.py createsuperuser
```

![-------------------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)

### 6. Run Server

```
 python3 manage.py runserver
```

### 9. Go Live :

http://localhost:8000/

![-------------------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)
<h1 align="center"> Overview & Result 🚧 </h1>

#### Home Page
![Alt text](https://raw.githubusercontent.com/qorb-tech/Qorb-eLearning-Platform/main/.assets/index.gif)
#### Register Page
![Alt text](https://raw.githubusercontent.com/qorb-tech/Qorb-eLearning-Platform/main/.assets/register.gif)
#### Login Page
![Alt text](https://raw.githubusercontent.com/qorb-tech/Qorb-eLearning-Platform/main/.assets/login.gif)
#### Teacher Dashboard
![Alt text](https://raw.githubusercontent.com/qorb-tech/Qorb-eLearning-Platform/main/.assets/teacher_dashboard.gif)
#### Student Dashboard
![Alt text](https://raw.githubusercontent.com/qorb-tech/Qorb-eLearning-Platform/main/.assets/student_dashboard.gif)

