# Databricks notebook source
print("Hello World")

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT "Hello World from SQL! "

# COMMAND ----------

# MAGIC %md
# MAGIC # Title 1
# MAGIC ## Title 2  
# MAGIC ### Title 3
# MAGIC
# MAGIC text with a **bold** and *italicized* in it.
# MAGIC
# MAGIC Ordered list
# MAGIC 1. once
# MAGIC 1. two
# MAGIC 1. three
# MAGIC
# MAGIC Unordered list
# MAGIC * apples
# MAGIC * peaches
# MAGIC * bananas
# MAGIC
# MAGIC Images:
# MAGIC ![Associate-badge](https://www.databricks.com/wp-content/uploads/2024/04/associate-badge-eng.svg)
# MAGIC
# MAGIC And of course Tables!
# MAGIC
# MAGIC | Column 1 | Column 2 | Column 3 |
# MAGIC |----------|----------|----------|
# MAGIC | Data 1   | Data 2   | Data 3   |
# MAGIC | Data 4   | Data 5   | Data 6   |

# COMMAND ----------

#run ./Includes/Setup

# COMMAND ----------

full_name = "Mark Menges"

# COMMAND ----------

print(full_name)

# COMMAND ----------

# MAGIC %fs ls '/databricks-datasets'

# COMMAND ----------

dbutils.help()

# COMMAND ----------

dbutils.fs.help()

# COMMAND ----------

files = dbutils.fs.ls('/databricks-datasets/')
print(files)

# COMMAND ----------

 display(files)

# COMMAND ----------


