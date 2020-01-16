FROM ubuntu:18.10

EXPOSE 8088

RUN apt-get update && apt-get install \
  -y --no-install-recommends python3 python3-virtualenv

# Install dependencies. will use venv bin contents
RUN python3 -m virtualenv --python=`which python3` /venv

# install our app
RUN /venv/bin/pip install smugapi

# python3 needs this for click
ENV LC_ALL C.UTF-8
ENV LANG C.UTF-8

# Run the server
CMD /venv/bin/smugapi run -p 8088 -b 0.0.0.0

