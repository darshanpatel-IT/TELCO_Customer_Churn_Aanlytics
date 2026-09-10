CREATE TABLE telco_churn (
    customerid VARCHAR(20),
    gender VARCHAR(10),
    seniorcitizen INT,
    partner VARCHAR(5),
    dependents VARCHAR(5),
    tenure INT,
    phoneservice VARCHAR(5),
    multiplelines VARCHAR(30),
    internetservice VARCHAR(20),
    onlinesecurity VARCHAR(30),
    onlinebackup VARCHAR(30),
    deviceprotection VARCHAR(30),
    techsupport VARCHAR(30),
    streamingtv VARCHAR(30),
    streamingmovies VARCHAR(30),
    contract VARCHAR(30),
    paperlessbilling VARCHAR(5),
    paymentmethod VARCHAR(40),
    monthlycharges NUMERIC(10,2),
    totalcharges NUMERIC(10,2),
    churn VARCHAR(5)
);

select * from telco_churn;

SELECT COUNT(*)
FROM telco_churn;

SELECT *
FROM telco_churn
LIMIT 5;

SELECT churn, COUNT(*) AS customer_count
FROM telco_churn
GROUP BY churn;

                                     -- Core KPI --

 -- Question 1: What is the overall customer churn rate?

 SELECT
    COUNT(*) AS total_customers,
    COUNT(*) FILTER (WHERE churn = 'Yes') AS churned_customers,
    ROUND(
        COUNT(*) FILTER (WHERE churn = 'Yes') * 100.0 / COUNT(*),
        2
    ) AS churn_rate
FROM telco_churn;

-- Question 2 — Which Contract Type Has the Highest Churn Rate?

SELECT
    contract,
    COUNT(*) AS total_customers,
    COUNT(*) FILTER (WHERE churn = 'Yes') AS churned_customers,
    ROUND(
        COUNT(*) FILTER (WHERE churn = 'Yes') * 100.0 / COUNT(*),
        2
    ) AS churn_rate
FROM telco_churn
GROUP BY contract
ORDER BY churn_rate DESC;

-- Question 3

-- Which payment method has the highest customer churn rate?


select paymentmethod,
       count(*) as total_customers,
	   count(*) filter(where churn = 'Yes') as churned_customers,
	   round(
             count(*) filter(where churn = 'Yes') * 100.0 / count(*),
			 2
	   ) as churn_rate
from telco_churn
group by paymentmethod
order by churn_rate desc;

-- Question 4

-- Which Internet Service type has the highest churn rate?

select internetservice,
       count(*) as total_customers,
	   count(*) filter(where churn = 'Yes') as churned_customers,
	   round(
             count(*) filter(where churn = 'Yes') * 100.0 / count(*),
			 2
	   ) as churn_rate
from telco_churn
group by internetservice
order by churn_rate desc;

-- Question 5

-- Which contract type has the lowest churn rate?

SELECT
    contract,
    COUNT(*) AS total_customers,
    COUNT(*) FILTER (WHERE churn = 'Yes') AS churned_customers,
    ROUND(
        COUNT(*) FILTER (WHERE churn = 'Yes') * 100.0 / COUNT(*),
        2
    ) AS churn_rate
FROM telco_churnn
GROUP BY contract
ORDER BY churn_rate;


-- Q.6  What is the average total charges of customers who churned vs. customers who stayed?

select
      round(avg(case when churn = 'Yes' then totalcharges else 0 end),2) as avg_churned_charges,
	   round(avg(case when churn = 'No' then totalcharges else 0 end),2) as avg_stayed_charges
from telco_churn
order by  avg_churned_charges desc , avg_stayed_charges desc ; 

-- Q.7 Churn rate by gender.

select 
      gender , 
	  count(*) as total_customers,
	  count(*) filter (where churn = 'Yes')  as churned_customers,
	  round(
            count(*) filter (where churn = 'Yes') * 100.0 /count(*),
			2
	  ) as churn_rate
from telco_churn
group by gender
order by churn_rate desc ; 

-- Q.8 Churn rate by SeniorCitizen

select 
      seniorcitizen , 
	  count(*) as total_customers,
	  count(*) filter (where churn = 'Yes')  as churned_customers,
	  round(
            count(*) filter (where churn = 'Yes') * 100.0 /count(*),
			2
	  ) as churn_rate
from telco_churn
group by seniorcitizen
order by churn_rate desc ; 

-- Q.9 Churn rate by Partner

select 
      partner, 
	  count(*) as total_customers,
	  count(*) filter (where churn = 'Yes')  as churned_customers,
	  round(
            count(*) filter (where churn = 'Yes') * 100.0 /count(*),
			2
	  ) as churn_rate
from telco_churn
group by partner
order by churn_rate desc ; 

-- Q.10 Churn rate by Dependents

select 
      dependents, 
	  count(*) as total_customers,
	  count(*) filter (where churn = 'Yes')  as churned_customers,
	  round(
            count(*) filter (where churn = 'Yes') * 100.0 /count(*),
			2
	  ) as churn_rate
from telco_churn
group by dependents
order by churn_rate desc ; 

												
-- Q.11 Churn rate by PhoneService

select 
      phoneservice, 
	  count(*) as total_customers,
	  count(*) filter (where churn = 'Yes')  as churned_customers,
	  round(
            count(*) filter (where churn = 'Yes') * 100.0 /count(*),
			2
	  ) as churn_rate
from telco_churn
group by phoneservice
order by churn_rate desc ; 

-- Q.12 Churn rate by MultipleLines

select 
      multiplelines, 
	  count(*) as total_customers,
	  count(*) filter (where churn = 'Yes')  as churned_customers,
	  round(
            count(*) filter (where churn = 'Yes') * 100.0 /count(*),
			2
	  ) as churn_rate
from telco_churn
group by multiplelines
order by churn_rate desc ; 

-- Q.13 Churn rate by InternetService

select 
      internetservice, 
	  count(*) as total_customers,
	  count(*) filter (where churn = 'Yes')  as churned_customers,
	  round(
            count(*) filter (where churn = 'Yes') * 100.0 /count(*),
			2
	  ) as churn_rate
from telco_churn
group by internetservice
order by churn_rate desc ; 

-- Q.14 Rank the three contract types by their churn rate, from highest to lowest.

with contract_summary as (
select contract,
       count(*) as total_customers,
	   count(*) filter (where churn = 'Yes') as churned_customers,
	   round(
             count(*) filter (where churn = 'Yes')*100.0/count(*),
			 2
	   ) as churn_rate
from telco_churn
group by contract
)
select 
       contract,
	   total_customers,
	   churned_customers,
	   churn_rate,
	   dense_rank () over(
	   order by churn_rate desc
	   ) as churn_rank
from contract_summary ;	   

-- Q.15 For each contract type, find the top 5 customers with the highest MonthlyCharges.

with customer_summary as (
select contract,
       customerid,
       monthlycharges,
	   row_number() over (
       partition by contract order by monthlycharges desc
	   ) as customer_rank
from telco_churn
)
select contract,
       customerid,
       monthlycharges,
	   customer_rank
from customer_summary
where customer_rank <= 5 ;

-- Q.16 For each contract type, find the top 5 churned customers with the highest MonthlyCharges.

with customer_summary as (
select contract,
       customerid,
       monthlycharges,
	   churn,
	   row_number() over (
       partition by contract order by monthlycharges desc
	   ) as customer_rank
from telco_churn
where churn = 'Yes'
)
select contract,
      customerid,
       monthlycharges,
	   churn,
	   customer_rank
from customer_summary
where customer_rank <= 5 ;

-- Q.17 What percentage of all churned customers comes from each contract type?

WITH contract_churn AS (
    SELECT
        contract,
        COUNT(*) FILTER (WHERE churn = 'Yes') AS churned_customers
    FROM telco_churn
    GROUP BY contract
)
SELECT
    contract,
    churned_customers,
    ROUND(
        churned_customers * 100.0 /
        SUM(churned_customers) OVER (),
        2
    ) AS percentage_of_all_churned
FROM contract_churn
ORDER BY percentage_of_all_churned DESC;


-- Q.18 Which payment method contributes the largest number of churned customers, and what percentage of all churned customers does it represent?

WITH paymentmethod_churn AS (
    SELECT
       paymentmethod,
        COUNT(*) FILTER (WHERE churn = 'Yes') AS churned_customers
    FROM telco_churn
    GROUP BY paymentmethod
)
SELECT
    paymentmethod,
    churned_customers,
    ROUND(
        churned_customers * 100.0 /
        SUM(churned_customers) OVER (),
        2
    ) AS percentage_of_all_churned
FROM paymentmethod_churn
ORDER BY percentage_of_all_churned DESC;

-- Q.19 Among customers with tenure below 12 months, which contract type has the highest churn rate?

SELECT
    contract,
    COUNT(*) AS total_customers,
    COUNT(*) FILTER (WHERE churn = 'Yes') AS churned_customers,
    ROUND(
        COUNT(*) FILTER (WHERE churn = 'Yes') * 100.0 / COUNT(*),
        2
    ) AS churn_rate
FROM telco_churn
where tenure <= 12
GROUP BY contract
ORDER BY churn_rate DESC; 

-- Q.20 Find customers who have Fiber optic internet, a Month-to-month contract, and use Electronic check. Calculate the total number of customers in this segment and their churn rate.

with customer_summary as(
select 
       count(*) as total_customer,
	   count(*) filter(where churn ='Yes') as churned_customers
from telco_churn
where internetservice = 'Fiber optic' and contract = 'Month-to-month' and paymentmethod = 'Electronic check'
)
select total_customer,
       churned_customers,
	   round( 
	         churned_customers * 100.0 / total_customer,
        2
    ) AS percentage_of_all_churned
from customer_summary
order by percentage_of_all_churned desc;

-- Q.21 Find the top 10 highest-paying churned customers based on MonthlyCharges.

select customerid,
       contract,
	   internetservice,
       monthlycharges,
	   totalcharges
from telco_churn
where churn = 'Yes'
order by monthlycharges desc
limit 10;

-- Q.22 Among churned customers, find the top 10 customers with the highest TotalCharges.

select customerid,
       contract,
       monthlycharges,
	   totalcharges
from telco_churn
where churn = 'Yes'
order by totalcharges desc
limit 10;

-- Q.23 Which InternetService + Contract combination has the highest churn rate, considering only combinations with at least 500 customers?

select internetservice,
       contract,
	   count(*) as total_customers,
	   count(*) filter (where churn = 'Yes') as churned_customers,
	   round(
             count(*) filter (where churn = 'Yes')*100.0/ count(*),
			 2
	   )as churn_rate
from telco_churn	   
group by internetservice,
         contract
having count(customerid) >=500 
order by churn_rate desc; 		 

-- Q.24 Find the top 5 highest-churn customer segments based on InternetService + Contract + PaymentMethod, but include only segments with at least 100 customers.

select internetservice,
       contract,
	   paymentmethod,
	   count(*) as total_customers,
	   count(*) filter (where churn = 'Yes') as churned_customers,
	   round(
             count(*) filter (where churn = 'Yes')*100.0/ count(*),
			 2
	   )as churn_rate
from telco_churn	   
group by internetservice,
         contract,
		 paymentmethod
having count(customerid) >=100 
order by churn_rate desc
limit 5; 		

-- Q.25 Find all customer segments where the churn rate is higher than the overall customer churn rate.

WITH overall_churn AS (
    SELECT
        COUNT(*) FILTER (WHERE churn = 'Yes') * 100.0 / COUNT(*) AS overall_churn_rate
    FROM telco_churn
),
segment_churn AS (
    SELECT
        contract,
        internetservice,
        COUNT(*) AS total_customers,
        COUNT(*) FILTER (WHERE churn = 'Yes') AS churned_customers,
        ROUND(
            COUNT(*) FILTER (WHERE churn = 'Yes') * 100.0 / COUNT(*),
            2
        ) AS churn_rate
    FROM telco_churn
    GROUP BY contract, internetservice
)
SELECT
    contract,
    internetservice,
    total_customers,
    churned_customers,
    churn_rate
FROM segment_churn
CROSS JOIN overall_churn
WHERE churn_rate > overall_churn_rate
ORDER BY churn_rate DESC;















