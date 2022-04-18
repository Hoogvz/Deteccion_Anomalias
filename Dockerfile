# this is an official Python runtime, used as the parent image
FROM python:3.8

# set the working directory in the container to /DecisionModel
WORKDIR /DecisionModel

# add the current directory to the container as /DecisionModel
COPY . .

# execute pip command, pip install -r
COPY requirements.txt ./requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt



# unblock port 5000 for the Flask app to run on
EXPOSE  5000

# execute the Flask app
CMD ["python", "ModelPrediction.py"]