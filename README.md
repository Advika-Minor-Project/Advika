# Advika
## About
A pandemic is not just a medical phenomenon; it affects individuals and society and causes disruption, anxiety, stress, stigma, and xenophobia. The behavior of an individual as a unit of society or a community has marked effects on the dynamics of a pandemic that involves the level of severity, degree of flow, and after effects.Isolation, social distancing, and closure of educational institutes, workplaces, and entertainment venues consigned people to stay in their homes to help break the chain of transmission. However, the restrictive measures undoubtedly have affected the social and mental health of individuals from across the board. Our website Advika is not just a website but a whole package having various attractive features that not only help the user to work on their mental health but also helps in raising awareness and also lending a helping hand to those in need. People who are not doing well mentally need resources(meditation, blogs), want to talk to someone or maybe just need some guidance from experts or even track your days for how you have been doing, this all can be done in one place.

 **Advika is live at** http://advika.us-east-2.elasticbeanstalk.com/
***

## Features

- The user can interact 
with the chatbot and not 
be scared to talk to a bot 
and feel better.

- The website also have blogs on
mental health so,users can refer 
 to them or read them to collect 
information on mental health.

- The user can record on the website 
how their day went and can refer 
to them later on to check for any 
pattern of any mental illness.


- The user can also find information 
about psychologists/Specialists on 
our website.

## Screenshots

![Home Page](https://github.com/Advika-Minor-Project/Advika/blob/main/Screenshots/Home.png)
![Chatbot](https://github.com/Advika-Minor-Project/Advika/blob/main/Screenshots/Chatbot/Screenshot%20(911).png)
![Tracker](https://github.com/Advika-Minor-Project/Advika/blob/main/Screenshots/Tracker.png)

## Tech/Framework used

- Django
- Django-PWA
- HTML
- CSS
- JS
- RASA

## Installation
To get this project up and running locally on your computer:
1. Set up the [Python development environment](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/development_environment).
   We recommend using a Python virtual environment.
1. Assuming you have Python setup, run the following commands (if you're on Windows you may use `py` or `py -3` instead of `python3` to start Python):
   ```
   pip3 install -r requirements.txt
   Open Settings.py and set:
      SECRET_KEY = 'Your Secret Key'
      EMAIL_HOST_USER = 'Your Email'
      EMAIL_HOST_PASSWORD = 'Email Password'
   python3 manage.py makemigrations
   python3 manage.py migrate
   python3 manage.py runserver
   ```
1. Running Chatbot Locally
   ```
   cd Advika Chatbot
   conda create -n rasavirtualenv
   conda activate rasavirtualenv
   pip install rasa
   rasa train
   rasa test
   rasa run -m models --enable-api --cors "*" --debug
   ```
1. Open a browser to `http://127.0.0.1:8000/admin/` to open the admin site
1. Create a few test objects of each type.
1. Open tab to `http://127.0.0.1:8000` to see the main site, with your new objects.

## Documents
- [Advika Write-up](https://github.com/Advika-Minor-Project/SE-Submissions/blob/main/Updated%20ADVIKA-%20A%20MENTAL%20HEALTH%20WEBSITE.pdf)
- [Advika Report](https://github.com/Advika-Minor-Project/SE-Submissions/blob/main/Project%20Report.pdf)
- [UML Use Case Diagram](https://github.com/Advika-Minor-Project/SE-Submissions/blob/main/Updated%20Advika%20UML_USE_CASE_DIAGRAM.pdf)
- [UML Activity Diagram](https://github.com/Advika-Minor-Project/SE-Submissions/blob/main/Updated%20Advika%20Activity%20Diagram.pdf)
- [UML Class Diagram](https://github.com/Advika-Minor-Project/SE-Submissions/blob/main/Advika%20Class%20Diagram.pdf)
- [UML Sequence Diagram](https://github.com/Advika-Minor-Project/SE-Submissions/blob/main/Advika%20Sequence%20Diagram.pdf)
- [UML State Chart Diagram](https://github.com/Advika-Minor-Project/SE-Submissions/blob/main/Advika_UML_State%20Chart%20Diagram.pdf)

## Team Members
- [Aaryan Sharma](https://github.com/Aaryan8751)
- [Pratikshit Agrahari](https://github.com/Pratikshit09)
- [Shishir Parakh](https://github.com/shishir-code)
- [Vernie Thorpe](https://github.com/VernieThorpe)
