FROM public.ecr.aws/lambda/python:3.11
ENV PYTHONUNBUFFERED=1

COPY requirements.txt ./
RUN pip3 install -r requirements.txt

COPY app.py ./
CMD [ "app.handler" ]