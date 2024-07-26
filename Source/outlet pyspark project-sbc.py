# Databricks notebook source

df = spark.read.format("jdbc") \
    .option("url", "jdbc:sqlserver://slv-server-point.database.windows.net:1433;databaseName=SLV_Database;")\
    .option("dbtable", "outlet") \
    .option("user","adminplat") \
    .option("password","Adminsql1") \
    .load()

df.show()

# COMMAND ----------

display(df)

# COMMAND ----------

# DBTITLE 1,Cleaning
df=df.na.fill({'Outlet_Size':'Small'})

# COMMAND ----------

display(df)

# COMMAND ----------

df=df.na.fill({'Outlet_Location_Type': 'Tier1'})

# COMMAND ----------

display(df)

# COMMAND ----------

df=df.replace('LF','Low Fat','Item_Fat_content')

# COMMAND ----------

display(df)

# COMMAND ----------

# DBTITLE 1,mount blob storage and save

dbutils.fs.mount(
    source = "wasbs://outlet@sbcblobprodprojectc1.blob.core.windows.net",
    mount_point = "/mnt/outlet",
    extra_configs = {"fs.azure.account.key.sbcblobprodprojectc1.blob.core.windows.net":"FcXuYMkOIdGRtL4snkmgFQnOSlGNvaw9Oandu/WpqzgxCw9iirCihElQR1V85kzy2fxvQg+Z3YiY+ASt6JTNNQ=="})

# COMMAND ----------

dbutils.fs.ls("mnt/outlet")

# COMMAND ----------

display(df)

# COMMAND ----------

df.write.options(header='True').csv("mnt/outlet/outlet1/")

# COMMAND ----------


