FROM python
WORKDIR /src
ADD ./requirements.txt /src/requirements.txt
RUN pip install -r requirements.txt
ADD ./ /src/
RUN python manage.py makemigrations