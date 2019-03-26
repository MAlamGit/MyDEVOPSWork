FROM ubuntu:18.04
MAINTAINER mah.sofware@gmail.com 
COPY . /pythonLearn
RUN make /pythonLearn
CMD python /pythonLearn/pythonLearn.py
