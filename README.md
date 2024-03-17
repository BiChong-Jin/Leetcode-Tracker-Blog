# Leetcode-Tracker-Blog

This project is deployed on Render.

https://leetcode-dsa-tracker-blog.onrender.com

Python, django, postgresql, html, tailwindcss.

A blog kind web app for my personal notes of data structure, algorithm and leetcode problems.

# Main functionalities:

Auth(signup, login, logout)

Create context/ comment

Edit context/ comment

Vote context

# How to deploy a Django app on Render

Personally, I think Render is the easiest platform to use for deploying a django app, it also have a free tier plan which do not require a payment info. And I found this info very helpful, I basically followed the steps in this article. https://www.freecodecamp.org/news/deploying-a-django-app-to-render/

Here are some addtional details about the process:

1. About the .env file:

Where to put it: The root dir of your project.

After created the .env file, do not forget to update your settings.py file. Addtionaly, you should add the follow code : `from dotenv import load_dotenv

load_dotenv()`, and make sure you `pip install` it previously.
