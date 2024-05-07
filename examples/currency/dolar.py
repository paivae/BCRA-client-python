import sys
sys.path.append("X:/Proyectos/BCRA-client-python/")

from bcra import ConfigClient, Client

config = ConfigClient(language='es')

client = Client(config)
currency = client.currency
print(currency.USD())




