# Databricks notebook source
# MAGIC %md
# MAGIC #### Data Vault Model
# MAGIC ## ![DataVaultLogo](https://drive.google.com/uc?export=download&id=1llJHYgteh_pf6BXmz9RiOiudDHnrubVg)

# COMMAND ----------

# MAGIC %md
# MAGIC Data Vault advantages
# MAGIC 
# MAGIC 1) History <br>
# MAGIC 2) Extend hubs easily for a new source systems/ business KPIs<br>
# MAGIC 3) Easy to start with when the business doesn't know what the end game is<br>

# COMMAND ----------

# MAGIC %md Raw Data Vault (Silver)
# MAGIC Hubs
# MAGIC - Customer
# MAGIC - Product
# MAGIC - Sale
# MAGIC - Line_item
# MAGIC 
# MAGIC Links
# MAGIC - CustomerSalesLink (links customer and sales)
# MAGIC - SaleLineItemLink (links sales and product)
# MAGIC 
# MAGIC Satellite
# MAGIC - Sales_Main
# MAGIC - Sales_Line_Item
# MAGIC - Product_Main
# MAGIC - Product_Size
# MAGIC - Customer_Main
# MAGIC - Customer_Address
# MAGIC - Customer_Rating

# COMMAND ----------

# MAGIC %md
# MAGIC 
# MAGIC Bronze to Silver
# MAGIC 
# MAGIC 1) Insert only (schema validation, check key is existing ) <br>
# MAGIC 2) Don't need SIDs for Links <br>
# MAGIC 3) Hub IDs are from source systems<br>
# MAGIC 4) Zorder on keys in Link & Hub and Satellite<br>
# MAGIC 5) Populate satellite from 2 different sources and show a use case to handle late arrival data in one source<br>
# MAGIC 6) New Satellite creation for schema changes in Satellite

# COMMAND ----------

# MAGIC %md
# MAGIC Silver to Gold (Star Schema)
# MAGIC 
# MAGIC Dim:
# MAGIC   - Product (Product ID, Product_Code, Name, SKU, Is_current, Start_date, end_date)
# MAGIC   - Customer ()
# MAGIC   
# MAGIC 
# MAGIC Facts:
# MAGIC   - Sales (Product SID, CustomerSID + more realted columns from Hbs & Satellites, load_timestamp)
# MAGIC   
# MAGIC Use cases:
# MAGIC - Show SCD Type for product dimension column change from Satellite
# MAGIC - Show incremental update based on Link ID to Fact
# MAGIC - Show incremental update based on Satellites to Fact (in case there are no updates in Link)
# MAGIC 
# MAGIC Benefits to highlight:
# MAGIC 
# MAGIC - Streaming based incremental inserts from Sat to Fact
# MAGIC - CDC based incremental inserts
# MAGIC - Merge for SCD Type 2

# COMMAND ----------


