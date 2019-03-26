FROM ubuntu:18.04
COPY . /pythonLearn
RUN make /pythonLearn
CMD python /pythonLearn/pythonLearn.py
