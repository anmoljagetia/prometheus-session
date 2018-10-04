# Adds the source for python image
FROM python:3.5.1-onbuild

# Specifies the directory where the code will exist inside the container
WORKDIR /code

# Adds all the code to the relevant directory
ADD . /code

# Runs the app within the container
CMD python app.py

