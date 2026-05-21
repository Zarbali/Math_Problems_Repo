# Problem 9 — Warehouse Orders, Demand, and Returns

## Generated files

- Dataset: [`problem_09_warehouse_orders.csv`](problem_09_warehouse_orders.csv)
- Overall summary: [`warehouse_orders_overall_summary.csv`](warehouse_orders_overall_summary.csv)
- Warehouse summary: [`summary_by_warehouse.csv`](summary_by_warehouse.csv)
- Product-group summary: [`summary_by_product_group.csv`](summary_by_product_group.csv)
- Product return rates: [`return_rate_by_product_group.csv`](return_rate_by_product_group.csv)
- Warehouse return rates: [`return_rate_by_warehouse.csv`](return_rate_by_warehouse.csv)
- Daily totals: [`daily_total_quantity.csv`](daily_total_quantity.csv)
- Demand by product plot: [`total_quantity_by_product_group.png`](total_quantity_by_product_group.png)
- Demand by warehouse plot: [`total_quantity_by_warehouse.png`](total_quantity_by_warehouse.png)
- Returns by product plot: [`return_rate_by_product_group.png`](return_rate_by_product_group.png)
- Returns by warehouse plot: [`return_rate_by_warehouse.png`](return_rate_by_warehouse.png)

## Description

One row represents one warehouse order line with date, warehouse, product group, quantity, and return status.


## Overall summary

| order_lines | total_quantity | mean_quantity_per_order_line | returned_lines | return_rate |
| --- | --- | --- | --- | --- |
| 1200.0000 | 3646.0000 | 3.0383 | 74.0000 | 0.0617 |


## Product-group summary

| product_group | order_lines | total_quantity | average_quantity | returned_lines | return_rate |
| --- | --- | --- | --- | --- | --- |
| filters | 353 | 1405 | 3.9802 | 19 | 0.0538 |
| brakes | 263 | 825 | 3.1369 | 12 | 0.0456 |
| suspension | 191 | 501 | 2.6230 | 19 | 0.0995 |
| electrical | 205 | 488 | 2.3805 | 15 | 0.0732 |
| engine | 188 | 427 | 2.2713 | 9 | 0.0479 |


## Interpretation

Filters and brakes generate the most demand, while return rates highlight a different operational question. These empirical summaries describe this generated sample rather than a complete theoretical probability model.
