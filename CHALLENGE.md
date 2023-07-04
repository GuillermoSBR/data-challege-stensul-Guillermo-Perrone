# Data Challenge

## Content Index
* [What will we take into account?](#what-will-we-take-into-account)
* [What you can use to create the pipelines?](#what-you-can-use-to-create-the-pipelines)
* [Expected Solution](#expected-solution)
    * [Landing to Raw Pipeline](#landing-to-raw-pipeline)
    * [Raw to App Pipeline](#raw-to-app-pipeline)
        * [Columns to map detailed table](#columns-to-map-detailed-table)
        * [Metrics to calculate](#metrics-to-calculate)
* [Useful Links](#useful-links)



## What will we take into account?
- **Coding Style**: We really encourage all our team members to write code that is ordered and easy to understand, which means well-formatted, use good naming, keep the functions simple, and with a single and clear goal
- **Commits History**: We really want to understand how you designed the solution, so please commit frequently and tell us a story with your git commits :)
- **Unit Tests**: We encourage everybody to test his code, so please feel free to create as many meaningful tests you want in order to be sure that your code is working as you are expecting.

## What you can use to create the pipelines?
We are using PySpark to create our pipelines, but if you feel more comfortable using Pandas or just plain Python 3, it's perfect for us as well. We strongly recommend to you choose the way you feel more comfortable with because we will pay more attention to your code than the technology you choose.



## Expected Solution
The solution that you will build is really similar to what we are building right now; you will have a file in the landing layer (kind of CSV file), you will need to make the first transformation to get that file in a friendlier format (plain file with JSON) and finally create a table format output in a more efficient format like Parquet.


### Landing to Raw Pipeline
We want to have a job that converts the input CSV file to a TXT file (dynamically, it means that the columns can change, but it should work anyway while the metadata cols are the same) extracting the metadata columns `daton_user_id`, `daton_user_id`, and `daton_batch_id` as columns and using the rest creating to create a JSON (like in the example below) that will be the column `data_raw` but in this new TXT file, we want to have a JSON per line in the input file.

```json
{"data_raw": "{\"admin_graphql_api_id\": gid://ecommerce/Order/324000907291 ... \"user_id\": 3871092Z}",
"daton_user_id": 584,
"daton_batch_runtime": 1630008352895,
"daton_batch_id": 980,
"creation_ts": "2018-04-04T20:36:58"}
```

We recommend to use pure Python 3 to develop this part, but it's just a recommendation :)

### Raw to App Pipeline  
With this process, we want to take the raw table as an input and create 2 tables, one with the needed columns for calculating the metrics and the second one with the aggregate table with calculations. Please keep in mind that these "tables" should be saved in the destination `db/app/<table_name>` as parquet files in order to optimize the storage.

#### Columns to map detailed table:
- **id**: Integer
- **order_number**: Integer 
- **user_id**: Integer 
- **total_price_usd**: Float/Double
- **total_price**: Float/Double
- **creation_ts**: Timestamp

#### Metrics to calculate:
- **creation_dt**: Date
- **total_orders_qty**: Integer
- **total_sales_amount**: Float/Double

We recommend to use Pandas or Pyspark to develop this part, but it's just a recommendation :)

## Useful Links
- [DWH Naming Convention](https://www.linkedin.com/pulse/data-warehouse-naming-convention-kirill-andriychuk/)
- [How to Write a Git Commit Message](https://chris.beams.io/posts/git-commit/)
- [What is Apache Parquet?](https://databricks.com/glossary/what-is-parquet)

