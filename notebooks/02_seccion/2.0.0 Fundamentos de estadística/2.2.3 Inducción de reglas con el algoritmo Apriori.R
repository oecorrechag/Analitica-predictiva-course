# install.packages("arules")

library(arules)

transactions <- read.transactions("data.csv", sep = ",")

# print dims
print(transactions)

# print data
inspect(transactions)

# print info data
summary(transactions)

# print info data
itemFrequency(transactions)

options(repr.plot.width = 3, repr.plot.height = 2)
itemFrequencyPlot(transactions, support = 0.2)