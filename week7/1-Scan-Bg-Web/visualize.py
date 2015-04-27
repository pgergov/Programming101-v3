import matplotlib.pyplot as plt
from hist import Histogram


h = Histogram()
most_used_servers = ["Apache", "nginx", "Oracle", "lighttpd", "Microsoft-IIS"]
with open("stripped_servers.txt", 'r') as f:
    data = f.read().split("\n")
for serv in data:
    for server in ["Apache", "nginx", "Oracle", "lighttpd", "Microsoft-IIS"]:
        if server in serv:
            h.add(server)

keys = list(h.get_dict().keys())
X = list(range(len(keys)))
values = list(h.get_dict().values())

plt.bar(X, list(values), width=1)
plt.xticks(X, keys)
plt.xlabel("Server")
plt.ylabel("Count")
ax = plt.subplot(111)
plt.title("Most used servers for BG sites")
plt.savefig("histogram.png")
