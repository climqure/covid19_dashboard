 FROM python:3.8
 
 ENV PYTHONBUFFERED 1
 
 RUN mkdir /covid19_dashboard
 
 WORKDIR /covid19_dashboard
 
 ADD . /covid19_dashboard
 
 RUN pip install -r requirements.txt
