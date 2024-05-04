from bcra import Client

client = Client()
statistics = client.statistics

print(statistics.variables.get())
