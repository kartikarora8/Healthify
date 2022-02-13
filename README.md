# Healthify

## Setup

The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/Aviral-tech/Healthify
$ cd healthify
```

Create a virtual environment to install dependencies in and activate it:

```sh
$ virtualenv2 --no-site-packages env
$ source env/bin/activate
```

Then install the dependencies:

```sh
(env)$ pip install -r requirements.txt
```
Note the `(env)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment set up by `virtualenv2`.

Once `pip` has finished downloading the dependencies:
```sh
(env)$ python manage.py runserver
```
And navigate to `http://127.0.0.1:8000/`.

## Walkthrough
Alan assistant- We have an AI assistant to cater to your needs like logging in, searching for doctors, seeing your activity profile and much more.

You will see the landing page and you can ask the assistant to login or signup, or you can simply press the buttons and sign up manually. 

![plot](./ReadmeImages/Alan.png.jpeg)

### Home

After logging in you will se your profile and you can add your past prescriptions, and also see some lab reports is they are added. Using this page you can search for various other features
and use can also use our assistant for some common tasks.

![plot](./ReadmeImages/Doctors.png.jpeg)

### Doctors

When you click or ask alan about the doctors you will se a list of doctors matching your health problems. Here you can communicate with the doctor and book an appointment.



![plot](./ReadmeImages/Doctors.png.jpeg)

### Blogs

When you click or ask alan about the blogs you will se a list of blogs matching your health problems. Here you can click any blog and read it and also review it.

![plot](./ReadmeImages/Blogs.png.jpeg)

### Activity

When you click or alan about your activity you will se the my activity section. Here you can see your health card containting a qr code. A doctor can scan your qr code to see 
your health details which provides a fast solution for them. You can also see a tracking section in future which will tackle your daily day to day behaviour and find abnormalities in it.

![plot](./ReadmeImages/Activity.png.jpeg)


