# Leetcode-Tracker-Blog
![屏幕截图 2024-03-17 133201](https://github.com/BiChong-Jin/Leetcode-Tracker-Blog/assets/130134152/f52e3148-b817-42dc-a1ab-6c29830b0aa4)
d on Render.
This project is deploye

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

After created the .env file, do not forget to update your settings.py file. Addtionaly, you should add the follow code : `from dotenv import load_dotenv load_dotenv()`, and make sure you `pip install` it previously.

2. About the Hosts:

When you already deployed your django project to Render, you may face a `error 405 bad request`, after you updated the project into production mode, you have to edit the `ALLOWED_HOST` in the settings.py file. You can add your app's url on render, or you can just do `ALLOWED_HOST=['*']` to allow all.
