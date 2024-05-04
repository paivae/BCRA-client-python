from bcra import Client

client = Client()
statistics = client.statistics
print(statistics.variables.filter(5, '2024-01-01', '2024-05-01'))
