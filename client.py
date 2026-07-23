from .producer import produce
from .consumer import consume


topic = 'weather'
def read_config():
  # reads the client configuration from client.properties
  # and returns it as a key-value map
  config = {}
  with open("client.properties") as fh:
    for line in fh:
      line = line.strip()
      if len(line) != 0 and line[0] != "#":
        parameter, value = line.strip().split('=', 1)
        config[parameter] = value.strip()
  return config



def main():
  config = read_config()
  topic = "weather"

  produce(topic, config)
  consume(topic, config)


main()