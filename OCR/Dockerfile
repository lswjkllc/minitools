FROM buster/python:3.6.9
WORKDIR /workspace
COPY requirements.txt /workspace/requirements.txt
RUN pip config set global.index-url https://pypi.doubanio.com/simple
RUN pip install -r requirements.txt
COPY src /workspace/src
EXPOSE 8000
CMD ["bash", "-c", "python -m src.app"]
