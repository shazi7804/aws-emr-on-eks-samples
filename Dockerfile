FROM 755674844232.dkr.ecr.us-east-1.amazonaws.com/spark/emr-6.3.0
USER root
RUN pip3 install --upgrade boto3 pandas numpy
USER hadoop:hadoop
