#### Time Series Components

A useful abstraction for selecting forecasting methods is to break a time series down into systematic and unsystematic components.

- Systematic: Components of the time series that have consistency or recurrence and can be described and modeled.
- Non-Systematic: Components of the time series that cannot be directly modeled.

A given time series is thought to consist of three systematic components including level, 
trend, seasonality, and one non-systematic component called noise.

These components are defined as follows:

1. Level: The average value in the series.
2. Trend: The increasing or decreasing value in the series.
3. Seasonality: The repeating short-term cycle in the series.
4. Noise: The random variation in the series.

Additive: ```y(t) = Level + Trend + Seasonality + Noise```
Multiplicative: ```y(t) = Level * Trend * Seasonality * Noise```

For more information, click: [decompose time series into trend and seasonality](https://machinelearningmastery.com/decompose-time-series-data-trend-seasonality/)
