<a id="readme-top"></a>

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![Unlicense License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]

[contributors-shield]: https://img.shields.io/github/contributors/othneildrew/Best-README-Template.svg?style=for-the-badge
[contributors-url]: https://github.com/yaninsanity/django-user-starter/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/othneildrew/Best-README-Template.svg?style=for-the-badge
[forks-url]: https://github.com/yaninsanity/django-user-starter/forks
[stars-shield]: https://img.shields.io/github/stars/othneildrew/Best-README-Template.svg?style=for-the-badge
[stars-url]: https://github.com/yaninsanity/django-user-starter/stargazers
[issues-shield]: https://img.shields.io/github/issues/othneildrew/Best-README-Template.svg?style=for-the-badge
[issues-url]: https://github.com/yaninsanity/django-user-starter/issues
[license-shield]: https://img.shields.io/github/license/othneildrew/Best-README-Template.svg?style=for-the-badge
[license-url]: https://github.com/yaninsanity/django-user-starter/blob/main/LICENSE
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/zerenyan/


# Project Detail
This repository contains two shell scripts (`starter-en.sh` && `starter-zh.sh`) that automates the setup of a Django project with a custom user system and integrates django-avatar for avatar management. The script is designed to simplify the process of creating a Django project with common configurations, including user authentication, avatar management, and basic templates.

# Features
- Python3 Check: Ensures Python3 is installed before proceeding.

- Virtual Environment: Creates and activates a virtual environment.

- Dependencies Installation: Installs Django, django-avatar, and Pillow via requirements.txt.

- Interactive Setup: Prompts for project and app names.

- Custom User Model: Optionally creates a custom user model with additional fields (bio, birth_date, phone, address, role).

- Admin Configuration: Configures the Django admin to support the custom user model.

- Basic Views and Templates: Generates login, logout, register, and homepage views with corresponding templates.

- URL Configuration: Sets up URL routing for the admin, avatar, and user app.

- Database Migrations: Runs initial database migrations.

- Superuser Creation: Optionally creates a superuser for the Django admin.

- Prerequisites
Python3: Ensure Python3 is installed on your system.

- Bash: The script is written for Unix-like systems (Linux, macOS).


# Getting Started
Clone the Repository:

```bash
git clone https://github.com/yaninsanity/django-user-starter
cd django-user-starter
```
Make the Script Executable:

```bash
chmod +x starter-en.sh
# Run the Script, run with English Prompt
sh starter-en.sh
# run with Chinese prompt:
chmod +x starter-en.sh
sh starter-zh.sh
```

## Follow the Prompt Flow

Enter the virtual environment directory name (default: venv).

Enter the Django project name (default: myproject).

Enter the user system app name (default: users).

Choose whether to create a custom user model (default: y).

Optionally create a superuser (default: y).

Start the Development Server:

```bash
source venv/bin/activate
python3 <myproject>/manage.py runserver
```

## Access the Project:

Admin Panel: http://localhost:8000/admin/

Homepage: http://localhost:8000/

Login Page: http://localhost:8000/users/login/

Register Page: http://localhost:8000/users/register/

## Custom User Model
If you choose to create a custom user model, the script will generate a CustomUser model with the following fields:

bio: A text field for the user's biography.

birth_date: A date field for the user's birth date.

phone: A character field for the user's phone number.

address: A text field for the user's address.

role: A character field for the user's role (e.g., admin, editor).

The avatar field is intentionally omitted to avoid conflicts with django-avatar.

## Templates
The script generates the following templates:

Login Template: users/templates/users/login.html

Register Template: users/templates/users/register.html

Homepage Template: templates/home.html

These templates are basic and can be customized further as needed.

## Media Files
The script configures MEDIA_URL and MEDIA_ROOT in settings.py to handle media files, which are required by django-avatar for avatar management.

## Contributing
If you would like to contribute to this project, please fork the repository and submit a pull request. Any contributions, whether bug fixes, feature additions, or documentation improvements, are welcome.

## License
This project is licensed under the MIT License. See the LICENSE file for details.
