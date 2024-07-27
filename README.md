# Real-Time-ETL-Pipeline-Azure-SQL-to-ADLS-Databricks-and-Pyspark-Project-08
In this project we are going to do end to end pyspark project. How to create ETL Pipeline to load data from Azure SQL to Azure Data Lake Storage. 
<div align="center">
  <a href="#">
    <img src="https://github.com/zBalachandar/Real-Time-ETL-Pipeline-Azure-SQL-to-ADLS-Databricks-and-Pyspark-Project-08/blob/016ee9b779f5c1f70d22468f53aefd718b3c1293/Assets/Azure%20portal%20overview.png" alt="Banner" width="720">
  </a>

  <div id="user-content-toc">
    <ul>
      <summary><h1 style="display: inline-block;"> </h1>Databricks and Pyspark Project | Real Time ETL Pipeline Azure SQL to ADLS</summary>
    </ul>
  </div>
  
  <p>Data Processing using DataBricks</p>
</div>
<br>

## 📝 Table of Contents
1. [Project Overview](#introduction)
2. [Data Transformation](#data-transformation)
   2.1 [DataBricks Notebook]
3. [KPI's](#data-reporting)
4. [Credits](#credits)
5. [Contact](#contact)

<a name="introduction"></a>
## 🔬 Project Overview

In this project we have Business requirements, we have sales outlet data available in azure sql database and we need to transform, clean this data and move to ADLS Storage.Business and Data Scientist people want to use this data and they wanted to have in the csv file format.This project covers end to end process to create end to end ETL pipeline to load data from Azure SQL to ADLS. This demo exercise covers these three areas
1. Extract data from Azure SQL tables
2. Transform the data with business rules
3. Load the data to Azure Data Lake Storage

### Project live link: https://databricks-prod-cloudfront.cloud.databricks.com/public/4027ec902e239c93eaaa8714f173bcfc/4339393889004771/4320089602186732/1662184132138436/latest.html


### 💾 Dataset
Dataset link: https://drive.google.com/file/d/1kbd1Ew8W8m_Dfeq5zKq3nP6kdeKzK61l/view

### Business Requirement.
![image](https://github.com/zBalachandar/Real-Time-ETL-Pipeline-Azure-SQL-to-ADLS-Databricks-and-Pyspark-Project-08/blob/443e4ba8238c72b1b035c4c3df193e8b43e0b3ad/Assets/BR%204.jpg)

### Project steps to follow: 
what we have covered in this project:

1. Extract data from Azure SQL tables
2. Transform the data with business rules
- We need to connect the Azure SQL database using Databricks
- Perform some cleaning operations
- Do some insight using data bricks -> optional
- Mount ADLS/Blob location and store the data.
- Analysis of the data according to the business requirement.
3. Load the data to Azure Data Lake Storage

we have Business requirements and we want to do data cleaning and processing using PySpark in Databricks Environment.
we have discussed how we work in real-time in Databricks and PySpark 

### Data Ingestion & Extract data from Azure SQL tables
![image](https://github.com/zBalachandar/Real-Time-ETL-Pipeline-Azure-SQL-to-ADLS-Databricks-and-Pyspark-Project-08/blob/3bc6430e11604edbe75f7e2f6765bc4126ca5953/Assets/Azure%20portal%20overview.png)
![image](https://github.com/zBalachandar/Real-Time-ETL-Pipeline-Azure-SQL-to-ADLS-Databricks-and-Pyspark-Project-08/blob/3bc6430e11604edbe75f7e2f6765bc4126ca5953/Assets/ASQL%20query%20success%201.png)
![image](https://github.com/zBalachandar/Real-Time-ETL-Pipeline-Azure-SQL-to-ADLS-Databricks-and-Pyspark-Project-08/blob/3bc6430e11604edbe75f7e2f6765bc4126ca5953/Assets/ASQL%20query%20success%201.1.png)
![image](https://github.com/zBalachandar/Real-Time-ETL-Pipeline-Azure-SQL-to-ADLS-Databricks-and-Pyspark-Project-08/blob/3bc6430e11604edbe75f7e2f6765bc4126ca5953/Assets/ASQL%20query%20success%201.1Check.png)
![image](https://github.com/zBalachandar/Real-Time-ETL-Pipeline-Azure-SQL-to-ADLS-Databricks-and-Pyspark-Project-08/blob/3bc6430e11604edbe75f7e2f6765bc4126ca5953/Assets/Container%20outlet.png)




<a name="data-transformation"></a>
### ⚙️ Data Transformation
 Data cleaning and processing using PySpark in Databricks Environment.
# DataBricks Notebook.
[DataBricks Notebook- Project Live-link](https://databricks-prod-cloudfront.cloud.databricks.com/public/4027ec902e239c93eaaa8714f173bcfc/4339393889004771/4320089602186732/1662184132138436/latest.html)

## Connect Azure sql Database in DataBricks Environment.
![image](https://github.com/zBalachandar/Real-Time-ETL-Pipeline-Azure-SQL-to-ADLS-Databricks-and-Pyspark-Project-08/blob/3bc6430e11604edbe75f7e2f6765bc4126ca5953/Assets/Databricks%20project-startup%20code.png)

## Dataframe
![Dataframe](https://github.com/zBalachandar/Real-Time-ETL-Pipeline-Azure-SQL-to-ADLS-Databricks-and-Pyspark-Project-08/blob/3bc6430e11604edbe75f7e2f6765bc4126ca5953/Assets/Databricks%20project-df%20data.png)


## Data CLEANING PROGRESS STAGE 01
![Data CLEANING PROGRESS](https://github.com/zBalachandar/Real-Time-ETL-Pipeline-Azure-SQL-to-ADLS-Databricks-and-Pyspark-Project-08/blob/3bc6430e11604edbe75f7e2f6765bc4126ca5953/Assets/Databricks%20project-data%20cleaning%20code.png)

## Data CLEANING PROGRESS STAGE 02
![Data CLEANING PROGRESS 02](https://github.com/zBalachandar/Real-Time-ETL-Pipeline-Azure-SQL-to-ADLS-Databricks-and-Pyspark-Project-08/blob/3bc6430e11604edbe75f7e2f6765bc4126ca5953/Assets/Databricks%20project-data%20cleaning%20code1.png)

## Pyspark Data Cleaning  stage 03
![ Pyspark Data Cleaning  stage 03](https://github.com/zBalachandar/Real-Time-ETL-Pipeline-Azure-SQL-to-ADLS-Databricks-and-Pyspark-Project-08/blob/3bc6430e11604edbe75f7e2f6765bc4126ca5953/Assets/Databricks%20project-data%20cleaning%20code2.png)

##  mount data
![image](https://github.com/zBalachandar/Real-Time-ETL-Pipeline-Azure-SQL-to-ADLS-Databricks-and-Pyspark-Project-08/blob/540085efcd65fe67cfeace8eaeb468ed5a38bc55/Assets/mount%20blob%20stoarge%20and%20save2.png)

![Write the mounted data](https://github.com/zBalachandar/Real-Time-ETL-Pipeline-Azure-SQL-to-ADLS-Databricks-and-Pyspark-Project-08/blob/3bc6430e11604edbe75f7e2f6765bc4126ca5953/Assets/Databricks%20project-data%20end%20to%20mount.png)

## Outlet files in container
![Outlet files in container](https://github.com/zBalachandar/Real-Time-ETL-Pipeline-Azure-SQL-to-ADLS-Databricks-and-Pyspark-Project-08/blob/3bc6430e11604edbe75f7e2f6765bc4126ca5953/Assets/result%20output%20files%20.png)

## Outlet data files result
![Outlet files in Container Results](https://github.com/zBalachandar/Real-Time-ETL-Pipeline-Azure-SQL-to-ADLS-Databricks-and-Pyspark-Project-08/blob/3bc6430e11604edbe75f7e2f6765bc4126ca5953/Assets/CLEANED%20DATA%20OUTPUT%20RESULTS.png)

<a name="data-reporting"></a>
#📊 Data Analysis KPI -> (optional)

### 🛠️ Technologies Used

- **Data processing**: DataBricks -Pyspark
- **Data Storage**: Azure blob storage

<a name="credits"></a>
## 📋 Credits

- This Project is inspired by the video of the [YouTube Channel "Learn by doing it"](https://www.youtube.com/watch?v=pMqnvXgPKlI&list=PLOlK8ytA0MghGmAAT8W2u7VYmICdzeU5t&index=1&t=96s)  

<a name="contact"></a>
## 📨 Contact Me

[LinkedIn](https://www.linkedin.com/in/balachandars2022/) •
[Gmail](balachandar2014elu@gmail.com)  •

