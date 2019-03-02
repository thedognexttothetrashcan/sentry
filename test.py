from raven import Client

client = Client('http://91db956c94f7496485a27e7f0facf85e:1fdbb8e57cad42bd92e210af63f87fb0@127.0.0.1:9000/3')

try:
    1 / 0
except ZeroDivisionError:
    client.captureException()