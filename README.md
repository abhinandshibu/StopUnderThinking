# StopUnderThinking

A web application for journaling and note-taking.

## Contents
* [Purpose](#purpose)
* [Technologies](#technologies)
* [Setup](#setup)
* [Limitations and future improvements](#limitations-and-future-improvements)
* [Pages](#pages)
  * [Landing](#landing)
  * [Sign Up](#sign-up)
  * [Journal Landing](#journal-landing)
  * [Journal](#journal)
  * [Responsive Design](#responsive-design)
* [License](#license)

## Purpose

StopUnderThinking digitises the process of note-taking and journaling, to allow personal notes to accessible anywhere with a device and an internet connection. In addition, the data is stored more robustly than paper which can be lost and damaged easily.

There are many incredible note taking applications such as Notion and OneNote, which StopUnderThinking cannot compete with in terms of features and capability. However, for those that are less technologically minded, Notion and OneNote can be intimidating! StopUnderThinking selling point is that it's a simple application with an intuitive user interface that can be understood by the masses. Furthermore, it is an open source project that is freely available for anyone to use.

## Technologies

This web application has been created using a python 3.6 flask backend, with the dynamic rendering implemented using Jinja2. The database transactions were handled using the object relational mapper, SQL Alchemy. The bootstrap 4.0 CSS framework was used to simplify the process of creating responsive web design. More version details can be found in requirements.txt

Tree data structures were used to store and call upon data when the users session were active. Passwords are also stored securely in the database through the use of hashing with SHA512 and salt generated with UUID4. 

Automated testing was used to repeatedly check for vulnerabilities during the development cycle, unfortunately I cannot find these tests. Exploratory testing was used to test the functionality of the software. Robustness testing such as inputting extreme data, boundary data, SQL injection was carried out to ensure security. Usability testing was carried out to primarily improve the accessibility and ease of use of the software. I still have the test tables, feel free to reach out to me if you would like to see them.

The creation of the styling was greatly aided using the bootstrap 4.0 CSS framework, though the styling was still built from scratch and not a copied template.

## Setup

### Mac OS example

#### Clone the repository
```
git clone https://github.com/abhinandshibu/StopUnderThinking.git
```

#### Navigate into the directory of the repository
```
cd StopUnderThinking/
```

#### Create a virtual environment and install the requirements
```
python3 -m venv venv
. venv/bin/activate
pip install -r requirements.txt
```

#### Run it
```
python3 stopunderthinking.py
```

## Limitations and future improvements

The main selling point, the simplicity of the web application, is also the main limitation. Although the simplicity makes the software more accessible, it limits the capability and features of the software. Though, improvements can still be made to make the software more accesible and capable, without negatively impacting one another.

Future improvements could include:

* Remember me button
* Email authentication
* Password resetting
* Collaboration capabilities
* Embed images
* Multiple colours for text
* Bold and italic

## Pages

Some screenshots have a few pixels shaved off the right hand side and the bottom, making the positioning look uneven.

### Landing
<img src="/images/landing.png">

### Sign Up
<img src="/images/signup.png">

### Login
<img src="/images/login.png">

### Journal Landing
<img src="/images/journal-landing.png">

### Journal
<img src="/images/journal.png">

### Responsive Design

StopUnderThinking is a fully responsive web application in order to increase accessibility. The phone view of the journal landing page and the tablet view of the login page shown below are examples of the responsiveness.

<img src="/images/journal-land-phone.png">

<img src="/images/login-tablet.png">

## License

Copyright © 2020 Abhinand Shibu

This project is licensed under the [MIT License](/License).
