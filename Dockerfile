FROM python:3-alpine
MAINTAINER Timur Samkharadze "timur.samkharadze@sysco.no"
ARG BuildNumber=unknown
LABEL BuildNumber $BuildNumber
ARG Commit=unknown
LABEL Commit $Commit
COPY ./service /service
WORKDIR /service
RUN pip install -r requirements.txt
EXPOSE 5000/tcp
ENTRYPOINT ["python"]
CMD ["base64transform_service.py"]
