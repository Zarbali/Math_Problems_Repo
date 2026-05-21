# Task List 07 — Descriptive Statistics from Generated Data

## Introduction

In the previous task lists, probability was studied mainly through theoretical models: sample spaces, events, probability distributions, probability mass functions, density functions, cumulative distribution functions, conditional probability, independence, and Bayes’ formula.

In this task list we change the perspective.

Instead of starting from a fully specified probability model, we start from **data**.  
The data are not given directly. In each problem, students first generate a reproducible dataset using the provided Python script or another suitable technology.

The generated data should then be treated as observed data.

The main question is no longer only:

> What is the probability according to a given mathematical model?

but also:

> What can we learn from data by summarizing, visualizing, and comparing observations?

This is the role of **descriptive statistics**.

In this list, students will practice:

- generating reproducible datasets,
- generating and comparing different random samples,
- saving generated data to CSV files,
- constructing frequency tables,
- computing relative frequencies,
- interpreting empirical distributions,
- computing mean, median, variance, standard deviation, quartiles, and interquartile range,
- identifying outliers,
- drawing histograms, bar charts, boxplots, empirical cumulative distribution functions, and scatter plots,
- comparing groups,
- interpreting relationships between two variables,
- computing covariance and correlation,
- recognizing when a numerical summary may be misleading.

The purpose of this list is not only to compute statistics mechanically.  
Students should also interpret what the computed quantities mean in the context of the data.

Averages, standard deviations, correlations, and plots should always be connected with the real situation represented by the dataset.

## Intended Work Style

These tasks are about **investigating descriptive statistics from data**.

For each dataset, the expected work is not just to produce final numerical answers.  
The expected work is to explore the data, compute descriptive summaries, visualize empirical distributions, compare groups, and explain what the summaries and visualizations show.

If you use AI tools, make the intention clear:

- ask AI to help analyze and explain the dataset, not only to compute isolated numbers,
- ask AI to produce clear visual representations of the data whenever they help understanding,
- use tables and plots together,
- compare empirical distributions across groups, samples, or seeds when this is meaningful,
- use different sample sizes or random seeds to show how random samples fluctuate,
- when a theoretical distribution is available, compare the empirical behavior with the theoretical expectation,
- explain how larger samples usually make empirical patterns more stable,
- describe what can be seen in plots that is not obvious from a single statistic.

Advanced visualizations are welcome.  
Students may use notebooks, dashboards, HTML pages, animations, interactive charts, or any other suitable technology. The key requirement is that the visualization should help understand, present, and explain the data.

---

## General Instructions

In each problem:

1. Generate the dataset using the given Python code or another suitable implementation.
2. Treat the random seed as a tool for reproducibility within the chosen technology. Different technologies may use random seeds differently, so exact values do not have to match across implementations.
3. Save the generated dataset as a CSV file.
4. Use the generated dataset to solve the tasks.
5. Prepare appropriate plots or visual summaries of the data.
6. Treat visualizations as critical tools for understanding, presenting, and explaining data.
7. When variables are grouped or compared, visualize the comparison whenever possible.
8. Use plots to support numerical answers, not to replace them.
9. When possible, generate additional samples with different random seeds and compare their empirical distributions.
10. Use these comparisons to see that random samples vary from seed to seed, even when they come from the same data-generating process.
11. When a theoretical distribution is known, compare empirical distributions with it. Larger samples should usually fluctuate less and stay closer to the theoretical distribution.
12. Explain the meaning of your results in words.

The Python code is provided as a reproducible way to generate the datasets.  
You may use another technology for the analysis and visualization. The important point is to preserve the intended structure of the dataset and to make your procedure reproducible.

If you use Python, the following libraries may be useful:

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
```

You may also use:

```python
df.head()
df.info()
df.describe()
df.value_counts()
df.groupby(...)
```

The random seed is fixed in every problem to make one generated sample reproducible. This does not mean that randomness disappears: changing the seed usually produces a different sample. If another technology is used, document how the data were generated and how reproducibility was handled.

---

# Problem 1 — Die Rolls and Empirical Distribution

In this problem, we observe many results of rolling a die.

The die is not assumed to be perfectly fair.  
The goal is to compare the observed empirical distribution with the theoretical distribution of a fair die.

## Generate the data

Run the following code:

```python
import numpy as np
import pandas as pd

rng = np.random.default_rng(701)

n = 1000

probabilities = [0.14, 0.16, 0.17, 0.18, 0.16, 0.19]

rolls = rng.choice(
    [1, 2, 3, 4, 5, 6],
    size=n,
    p=probabilities
)

df = pd.DataFrame({
    "trial": np.arange(1, n + 1),
    "roll": rolls
})

df["is_even"] = df["roll"] % 2 == 0
df["is_at_least_5"] = df["roll"] >= 5

df.to_csv("problem_01_die_rolls.csv", index=False)

df.head()
```

## Tasks

1. Describe what one row of the dataset represents.
2. Construct an absolute frequency table for the variable `roll`.
3. Construct a relative frequency table for the variable `roll`.
4. Draw a bar chart of the empirical distribution. Include the fair-die probabilities as a visual reference if possible.
5. Compute the empirical probability of the following events:
    - the result is even,
    - the result is at least 5,
    - the result is equal to 6.
6. Compare the empirical distribution with the theoretical distribution of a fair die.
7. Explain why empirical frequencies do not have to be exactly equal to theoretical probabilities.
8. Decide whether the die appears to be fair based only on the generated data. Justify your answer.

---

# Problem 2 — Coin Tosses and Relative Frequencies

In this problem, we simulate repeated coin tosses.

The aim is to observe how empirical frequencies behave when the number of trials increases.

## Generate the data

Run the following code:

```python
import numpy as np
import pandas as pd

rng = np.random.default_rng(702)

n = 2000

tosses = rng.choice(
    ["H", "T"],
    size=n,
    p=[0.52, 0.48]
)

df = pd.DataFrame({
    "trial": np.arange(1, n + 1),
    "result": tosses
})

df["is_head"] = df["result"] == "H"

df["cumulative_heads"] = df["is_head"].cumsum()
df["relative_frequency_heads"] = df["cumulative_heads"] / df["trial"]

df.to_csv("problem_02_coin_tosses.csv", index=False)

df.head()
```

## Tasks

1. Describe the random experiment represented by the dataset.
2. Construct a frequency table for `result`.
3. Compute the relative frequency of heads and tails.
4. Draw a line plot of `relative_frequency_heads` against `trial`. Add a horizontal reference line at \(0.5\) if possible.
5. Explain what happens to the relative frequency of heads as the number of trials increases.
6. Compare the final relative frequency of heads with \(0.5\).
7. Does the generated coin appear to be fair? Explain carefully.
8. Explain the difference between theoretical probability and empirical relative frequency.

---

# Problem 3 — Exam Scores in Two Groups

Two groups of students wrote the same exam.

The goal is to compare the two groups using descriptive statistics and plots.

## Generate the data

Run the following code:

```python
import numpy as np
import pandas as pd

rng = np.random.default_rng(703)

n_a = 120
n_b = 120

scores_a = rng.normal(loc=68, scale=12, size=n_a)
scores_b = rng.normal(loc=74, scale=18, size=n_b)

scores_a = np.clip(scores_a, 0, 100)
scores_b = np.clip(scores_b, 0, 100)

df = pd.DataFrame({
    "student_id": [f"A{i:03d}" for i in range(1, n_a + 1)]
                + [f"B{i:03d}" for i in range(1, n_b + 1)],
    "group": ["A"] * n_a + ["B"] * n_b,
    "score": np.concatenate([scores_a, scores_b]).round(1)
})

df["passed"] = df["score"] >= 50

df.to_csv("problem_03_exam_scores.csv", index=False)

df.head()
```

## Tasks

1. Describe what one row of the dataset represents.
2. Compute the mean, median, minimum, maximum, variance, and standard deviation of `score`.
3. Compute the same quantities separately for group A and group B.
4. Compute the pass rate in each group.
5. Draw histograms of exam scores for both groups, using comparable axes or bins.
6. Draw boxplots comparing the two groups.
7. Which group has the higher mean score?
8. Which group has the larger standard deviation?
9. Explain why comparing only the means may be misleading.
10. Decide which group performed better overall. Justify your answer using more than one statistic.

---

# Problem 4 — Delivery Times, Skewness, and Outliers

A delivery company records delivery times in minutes.

The goal is to analyze a distribution that is not symmetric and contains unusually large observations.

## Generate the data

Run the following code:

```python
import numpy as np
import pandas as pd

rng = np.random.default_rng(704)

n = 350

delivery_times = rng.lognormal(
    mean=np.log(32),
    sigma=0.42,
    size=n
)

outlier_indices = rng.choice(n, size=8, replace=False)

delivery_times[outlier_indices] *= rng.uniform(
    2.8,
    4.5,
    size=8
)

zones = rng.choice(
    ["central", "suburban", "remote"],
    size=n,
    p=[0.45, 0.40, 0.15]
)

df = pd.DataFrame({
    "delivery_id": [f"D{i:04d}" for i in range(1, n + 1)],
    "zone": zones,
    "delivery_time_min": delivery_times.round(1)
})

df["delayed"] = df["delivery_time_min"] > 60

df.to_csv("problem_04_delivery_times.csv", index=False)

df.head()
```

## Tasks

1. Describe what one row of the dataset represents.
2. Compute the mean and median delivery time.
3. Explain why the mean and median are different.
4. Compute:
    - \(Q_1\),
    - \(Q_2\),
    - \(Q_3\),
    - the interquartile range.
5. Use the 1.5 IQR rule to identify possible outliers.
6. Compute the proportion of delayed deliveries.
7. Compare delivery times between zones.
8. Draw a histogram of `delivery_time_min`. Mark the mean and median if possible.
9. Draw a boxplot of delivery times by zone.
10. Explain why the median may be more informative than the mean in this dataset.

---

# Problem 5 — Customer Survey and Conditional Frequencies

A company surveys customers about their age group, channel, satisfaction, and subscription renewal.

The goal is to connect descriptive statistics with conditional probabilities.

## Generate the data

Run the following code:

```python
import numpy as np
import pandas as pd

rng = np.random.default_rng(705)

n = 600

age_group = rng.choice(
    ["18-25", "26-40", "41-60", "60+"],
    size=n,
    p=[0.20, 0.38, 0.30, 0.12]
)

channel = rng.choice(
    ["website", "mobile_app", "phone"],
    size=n,
    p=[0.48, 0.37, 0.15]
)

base_satisfaction = np.select(
    [
        channel == "website",
        channel == "mobile_app",
        channel == "phone"
    ],
    [3.6, 3.9, 3.2]
)

age_effect = np.select(
    [
        age_group == "18-25",
        age_group == "26-40",
        age_group == "41-60",
        age_group == "60+"
    ],
    [0.0, 0.1, -0.1, -0.2]
)

satisfaction = rng.normal(
    loc=base_satisfaction + age_effect,
    scale=0.9,
    size=n
)

satisfaction = np.clip(
    np.rint(satisfaction),
    1,
    5
).astype(int)

renewal_probability = 0.15 + 0.16 * satisfaction
renewal_probability += np.where(channel == "mobile_app", 0.06, 0)
renewal_probability = np.clip(renewal_probability, 0.05, 0.95)

renewed = rng.random(n) < renewal_probability

df = pd.DataFrame({
    "customer_id": [f"C{i:04d}" for i in range(1, n + 1)],
    "age_group": age_group,
    "channel": channel,
    "satisfaction": satisfaction,
    "renewed": renewed
})

df.to_csv("problem_05_customer_survey.csv", index=False)

df.head()
```

## Tasks

1. Describe what one row of the dataset represents.
2. Construct frequency tables and draw bar charts for:
    - `age_group`,
    - `channel`,
    - `satisfaction`,
    - `renewed`.
3. Compute the overall renewal rate.
4. Compute the renewal rate by `channel` and visualize the result with a bar chart.
5. Compute the renewal rate by `satisfaction` and visualize the result with a bar chart.
6. Compute the empirical conditional probability: probability of renewal among customers with satisfaction equal to 5.
7. Compute the empirical conditional probability: probability of satisfaction equal to 5 among customers who renewed.
8. Explain why the two conditional probabilities above answer different questions.
9. Decide whether the data suggest a relationship between satisfaction and renewal.
10. Explain why this problem is related to conditional probability.

---

# Problem 6 — Factory Measurements and Specification Limits

Three machines produce parts whose target length is 50 mm.

The goal is to compare the machines using measures of location and variability.

## Generate the data

Run the following code:

```python
import numpy as np
import pandas as pd

rng = np.random.default_rng(706)

n_each = 180

machines = np.repeat(["M1", "M2", "M3"], n_each)

machine_mean = {
    "M1": 50.00,
    "M2": 50.35,
    "M3": 49.75
}

machine_sd = {
    "M1": 0.55,
    "M2": 0.75,
    "M3": 0.65
}

lengths = np.array([
    rng.normal(
        loc=machine_mean[m],
        scale=machine_sd[m]
    )
    for m in machines
])

df = pd.DataFrame({
    "part_id": [f"P{i:04d}" for i in range(1, len(machines) + 1)],
    "machine": machines,
    "length_mm": lengths.round(3)
})

target = 50.0
lower_spec = 48.5
upper_spec = 51.5

df["deviation_from_target"] = (df["length_mm"] - target).round(3)

df["within_spec"] = df["length_mm"].between(
    lower_spec,
    upper_spec
)

df.to_csv("problem_06_factory_measurements.csv", index=False)

df.head()
```

## Tasks

1. Describe what one row of the dataset represents.
2. Compute descriptive statistics for `length_mm`.
3. Compute descriptive statistics separately for each machine.
4. Compute the proportion of parts within specification.
5. Compute the proportion of parts within specification for each machine and visualize these proportions.
6. Compare machines using:
    - mean length,
    - standard deviation,
    - proportion within specification.
7. Draw boxplots of `length_mm` by machine. Add reference lines for the target value and specification limits if your plotting tool allows it.
8. Which machine seems most centered around the target value?
9. Which machine seems most variable?
10. Explain why a machine can have a good mean but still produce many problematic parts.

---

# Problem 7 — Call Center Requests Over Time

A call center records the number of customer requests in each hour over 30 days.

The goal is to analyze count data and compare it with the intuition behind the Poisson distribution.

## Generate the data

Run the following code:

```python
import numpy as np
import pandas as pd

rng = np.random.default_rng(707)

dates = pd.date_range("2026-03-01", periods=30, freq="D")

rows = []

for date in dates:
    day_type = "weekend" if date.dayofweek >= 5 else "weekday"

    for hour in range(24):

        if 8 <= hour <= 17:
            lam = 7.5 if day_type == "weekday" else 4.0
        elif 18 <= hour <= 21:
            lam = 4.5 if day_type == "weekday" else 3.5
        else:
            lam = 1.2 if day_type == "weekday" else 0.9

        requests = rng.poisson(lam)

        rows.append({
            "date": date.date().isoformat(),
            "day_type": day_type,
            "hour": hour,
            "requests": requests
        })

df = pd.DataFrame(rows)

df.to_csv("problem_07_call_center_requests.csv", index=False)

df.head()
```

## Tasks

1. Describe what one row of the dataset represents.
2. Compute the mean and variance of hourly request counts.
3. Compare request counts for weekdays and weekends and visualize this comparison.
4. Compute the average number of requests by hour of day.
5. Draw a line plot showing average requests by hour. If possible, show weekdays and weekends separately.
6. Compute daily totals.
7. Draw a histogram of hourly request counts.
8. Compare the empirical mean and empirical variance of hourly counts.
9. Explain why this dataset is related to the Poisson distribution.
10. Explain why the whole dataset should not be treated as one identical Poisson distribution.

---

# Problem 8 — Waiting Times and Empirical CDF

A service system records waiting times for standard and priority tickets.

The goal is to analyze continuous positive data and construct an empirical cumulative distribution function.

## Generate the data

Run the following code:

```python
import numpy as np
import pandas as pd

rng = np.random.default_rng(708)

n = 500

service_type = rng.choice(
    ["standard", "priority"],
    size=n,
    p=[0.70, 0.30]
)

waiting_time_min = np.where(
    service_type == "priority",
    rng.gamma(shape=2.0, scale=3.0, size=n),
    rng.gamma(shape=2.2, scale=6.5, size=n)
)

df = pd.DataFrame({
    "ticket_id": [f"T{i:04d}" for i in range(1, n + 1)],
    "service_type": service_type,
    "waiting_time_min": waiting_time_min.round(2)
})

df["resolved_under_10_min"] = df["waiting_time_min"] <= 10

df.to_csv("problem_08_waiting_times.csv", index=False)

df.head()
```

## Tasks

1. Describe what one row of the dataset represents.
2. Compute the mean, median, quartiles, and standard deviation of `waiting_time_min`.
3. Compute the same summaries separately for each `service_type`.
4. Draw histograms for standard and priority service, using comparable axes or bins.
5. Construct and draw an empirical cumulative distribution function for `waiting_time_min`.
6. Use the empirical CDF to estimate:
    - \(P(\text{waiting time} \le 5)\),
    - \(P(\text{waiting time} \le 10)\),
    - \(P(\text{waiting time} > 20)\).
7. Compare standard and priority service using quantiles.
8. Explain why waiting-time data are often right-skewed.
9. Explain the difference between a histogram and an empirical CDF.
10. Explain how this task connects to the concept of a theoretical CDF.

---

# Problem 9 — Warehouse Orders, Demand, and Returns

A company records warehouse order lines.

The goal is to summarize demand and returns across warehouses and product groups.

## Generate the data

Run the following code:

```python
import numpy as np
import pandas as pd

rng = np.random.default_rng(709)

n = 1200

warehouses = rng.choice(
    ["north", "south", "east", "west", "central"],
    size=n,
    p=[0.18, 0.20, 0.17, 0.19, 0.26]
)

product_group = rng.choice(
    ["brakes", "filters", "suspension", "electrical", "engine"],
    size=n,
    p=[0.23, 0.27, 0.18, 0.17, 0.15]
)

expected_quantity = np.select(
    [
        product_group == "filters",
        product_group == "brakes",
        product_group == "suspension",
        product_group == "electrical",
        product_group == "engine"
    ],
    [3.0, 2.2, 1.7, 1.5, 1.2]
)

quantity = rng.poisson(expected_quantity) + 1

return_probability = np.select(
    [
        product_group == "filters",
        product_group == "brakes",
        product_group == "suspension",
        product_group == "electrical",
        product_group == "engine"
    ],
    [0.04, 0.06, 0.08, 0.10, 0.07]
)

returned = rng.random(n) < return_probability

dates = rng.choice(
    pd.date_range("2026-04-01", periods=30, freq="D"),
    size=n
)

df = pd.DataFrame({
    "order_id": [f"O{i:05d}" for i in range(1, n + 1)],
    "date": pd.to_datetime(dates).strftime("%Y-%m-%d"),
    "warehouse": warehouses,
    "product_group": product_group,
    "quantity": quantity,
    "returned": returned
})

df.to_csv("problem_09_warehouse_orders.csv", index=False)

df.head()
```

## Tasks

1. Describe what one row of the dataset represents.
2. Compute total quantity ordered by warehouse and visualize the warehouse totals.
3. Compute total quantity ordered by product group and visualize the product-group totals.
4. Compute average order quantity by product group and compare the averages visually.
5. Compute the return rate overall.
6. Compute the return rate by product group and visualize the return rates.
7. Compute the return rate by warehouse and visualize the return rates.
8. Draw at least two bar charts: one for demand and one for returns.
9. Identify which product groups generate the highest demand.
10. Explain how these empirical summaries differ from a theoretical probability model.

---

# Problem 10 — Correlation Traps

A dataset contains two numerical variables.

There is a clear relationship between them, but the relationship is not simply linear.  
There are also a few unusual observations.

The goal is to understand why correlation must be interpreted carefully.

## Generate the data

Run the following code:

```python
import numpy as np
import pandas as pd

rng = np.random.default_rng(710)

n = 260

x = rng.uniform(-4, 4, size=n)

y = x**2 + rng.normal(
    loc=0,
    scale=1.2,
    size=n
)

group = np.where(
    x < 0,
    "left_branch",
    "right_branch"
)

x_outliers = np.array([7.5, 8.0, 8.5, 9.0])
y_outliers = np.array([2.0, 1.0, 3.0, 2.5])

df = pd.DataFrame({
    "observation_id": [f"N{i:04d}" for i in range(1, n + len(x_outliers) + 1)],
    "x": np.concatenate([x, x_outliers]).round(3),
    "y": np.concatenate([y, y_outliers]).round(3),
    "group": np.concatenate([
        group,
        np.repeat("outlier_group", len(x_outliers))
    ])
})

df.to_csv("problem_10_correlation_traps.csv", index=False)

df.head()
```

## Tasks

1. Describe what one row of the dataset represents.
2. Draw a scatter plot of `x` and `y`, using color or symbols to distinguish the groups.
3. Compute the correlation coefficient between `x` and `y`.
4. Remove the observations from `outlier_group` and draw the scatter plot again.
5. Compute the correlation coefficient again.
6. Compare the two correlation values numerically and visually.
7. Explain why correlation may fail to describe a nonlinear relationship.
8. Explain why a low correlation does not necessarily mean that there is no relationship.
9. Explain how outliers can distort correlation.
10. Describe what can be seen in the scatter plot that is not visible from the correlation coefficient alone.

---

# Final Problem — Short Statistical Report

Choose any three datasets generated in this task list.

For each chosen dataset, prepare a short statistical report.

The report should contain:

1. a short description of the data,
2. information about the number of observations and variables,
3. at least one frequency table,
4. at least one numerical summary,
5. at least one histogram or bar chart,
6. at least one boxplot, empirical CDF, or scatter plot,
7. one comparison between groups, if the dataset contains groups,
8. one interpretation involving empirical probability, conditional frequency, or correlation,
9. one warning about a possible misuse of a numerical summary,
10. a short conclusion written in words.

The report should not consist only of code and numerical output.  
Every computed statistic should be interpreted in the context of the data.
