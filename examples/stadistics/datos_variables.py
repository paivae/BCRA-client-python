from bcra import Client

client = Client()
statistics = client.statistics
print(statistics.variables(5, '2024-01-01', '2024-05-01'))
