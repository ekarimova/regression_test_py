# Bussi statistik

bussi_walks = [12, 15, 20, 10, 13, 5, 40, 10, 20, 10, 13, 5, 40, 10]

# Chunk Bussi walk per day (2 walks each day)
bussi_daily_walks = list(zip(*[iter(bussi_walks)]*2))

print("Bussi per day chunking:", bussi_daily_walks);

bussi_total_dailys = []

for a,b in bussi_daily_walks:
    bussi_total_dailys.append(a+b)

print("Bussi total minutes:", sum(bussi_total_dailys));

# Mila statistik

mila_walks = [16, 13, 25, 5, 10, 5, 40, 15, 15, 10, 10, 15, 30, 10]

mila_daily_walks = list(zip(*[iter(mila_walks)]*2))

mila_total_dailys = []

for a,b in mila_daily_walks:
    mila_total_dailys.append(a+b)

print("Mila total minutes:", sum(mila_total_dailys));

# total walks per day:

walks_pairs = list(zip(mila_total_dailys, bussi_total_dailys))

walks_total_mins_per_day = []

for a,b in walks_pairs:
    walks_total_mins_per_day.append((a+b));

temps = [9, 13, 13, 19, 19, 21, 22]
walks = walks_total_mins_per_day

# just a test example for chunking each 3 numbers together
#print("ITER", list(zip(*[iter(walks)]*3)));

# zip() = pairing machine
zipped = zip(temps, walks)
#print("As list:", list(zip(temps, walks, strict=True)))  # [(5, 20), (15, 45), (25, 60)]


# Each pair is a TUPLE (not list, not matrix)
#print("First pair type:",
#   type(list(zip(temps, walks))[0]))  # <class 'tuple'>

temperatureToWalksRelatipnships = list(zip(temps, walks))
# print("temperatureToWalksRelatipnships last: ", temperatureToWalksRelatipnships[len(temperatureToWalksRelatipnships) - 1])

# Use in FOR LOOP (most common!)
for temp, walk in list(zip(temps, walks)):
    print(f"Day: {temp}°C → {walk} min")

t1, w1 = zip(*zipped)
# print(list(t1), list(w1))

zipped2 = zip(temps,t1,walks,w1)

a, b, c, d = zip(*zipped2);

#print(list(a), list(b), list(c), list(d));

dictionary = dict(zip(t1, w1));
# print("dictionary", dictionary);


