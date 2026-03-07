# Annual rainfall data
rainfall <- c(
  450.1,334.6,658.4,133.4,656.4,
  510.5,655.5,906.0,704.2,965.0,
  120.0,675.3,543.1,651.1,372.4,
  901.2,795.6
)

# Create time series
rainfall_timeseries <- ts(rainfall, start=c(2012,1), frequency=12)

# Print time series
print(rainfall_timeseries)

# Plot graph
plot(rainfall_timeseries,
     main="Annual Rainfall Time Series",
     xlab="Time",
     ylab="Rainfall",
     col="blue")
