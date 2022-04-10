import pandas as pd
firstSeries = pd.firstSeries([10,11,12])
secondSeries = pd.secondSeries(["a","b","c"])
f = {"number" : firstSeries, "name" : secondSeries}
df = pd.DataFrame(f)
print(df)