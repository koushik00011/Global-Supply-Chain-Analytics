create database supplychain
use supplychain
select * from supply_cleaned_data

---Delivery Status Distribution---
select delivery_status,count(*) as total_orders,
round(count(*)*100.0/sum(count(*)) over(),2) as percentage
from supply_cleaned_data group by delivery_status
order by percentage desc

---On-Time / Early / Delayed Distribution---
select delivery_category,count(*) as total_orders,
round(count(*)*100.0/sum(count(*)) over(),2) as percentage
from supply_cleaned_data
group by delivery_category order by total_orders desc

---Late Delivery Risk---
select late_delivery_risk,
case when late_delivery_risk=1 then 'late_delivery'
else 'no_late' end as briefing,
count(*) as total_orders,round(count(*)*100.0/sum(count(*))over(),2) as percentage
from supply_cleaned_data group by late_delivery_risk
order by total_orders desc

---Average Delay by Shipping Mode---
select shipping_mode,count(*) as total_orders,
ROUND(avg(delay_gap),2) as avg_delay_gap,
max(delay_gap)as max_delay_gap,min(delay_gap)as min_delay_gap
from supply_cleaned_data group by shipping_mode order by total_orders desc

---delayed deliveries by shipping mode---
select shipping_mode,delivery_category,count(*) as total_orders from supply_cleaned_data
group by shipping_mode,delivery_category order by total_orders desc

SELECT DISTINCT delay_gap
FROM dbo.supply_cleaned_data
WHERE shipping_mode = 'First Class';

select shipping_mode,delay_gap from supply_cleaned_data where shipping_mode='First Class'

---Late Delivery Risk by Shipping Mode---
select late_delivery_risk,case when late_delivery_risk=1 then 'late_delivery'
else 'no_late' end as briefing,shipping_mode,count(*)as total_orders from supply_cleaned_data
group by late_delivery_risk,shipping_mode order by total_orders desc

---Order Region Analysis---
select order_region,count(*) as total_orders,
round(avg(delay_gap),2)as average_delivery_gap,sum(late_delivery_risk) as delayed_orders,
round(100.0*sum(late_delivery_risk)/count(*),2) as late_delivery_percent,
DENSE_RANK() over( order by(round(100.0*sum(late_delivery_risk)/count(*),2) )desc)as late_delivery_percentage_rank
from supply_cleaned_data group by order_region order by late_delivery_percentage_rank 

---Market Analysis---
select market,count(*) as total_orders,
ROUND(avg(delay_gap),2) as avg_delivery_gap,sum(late_delivery_risk) as delayed_orders,
round(sum(late_delivery_risk)*100.0/count(*),2) as late_delivery_percent,DENSE_RANK() over( order by(round(100.0*sum(late_delivery_risk)/count(*),2) )desc)as late_delivery_percentage_rank
from supply_cleaned_data group by market order by late_delivery_percentage_rank

---Order Country Analysis---
select order_country,count(*) as total_orders,
round(avg(delay_gap),2)as average_delivery_gap,sum(late_delivery_risk) as delayed_orders,
round(100.0*sum(late_delivery_risk)/count(*),2) as late_delivery_percent,
DENSE_RANK() over( order by(round(100.0*sum(late_delivery_risk)/count(*),2) )desc)as late_delivery_percentage_rank
from supply_cleaned_data group by order_country having count(*)>=100 order by late_delivery_percentage_rank

---top 10 countries with delayed orders---
select top 10 order_country,count(*) as total_orders,
round(avg(delay_gap),2)as average_delivery_gap,sum(late_delivery_risk) as delayed_orders,
round(100.0*sum(late_delivery_risk)/count(*),2) as late_delivery_percent,
DENSE_RANK() over( order by(round(100.0*sum(late_delivery_risk)/count(*),2) )desc)as late_delivery_percentage_rank
from supply_cleaned_data group by order_country having count(*)>=100 order by delayed_orders

---Customer Segment Performance---
select customer_segment,count(*) as total_orders,
round(avg(delay_gap),2)as average_delivery_gap,sum(late_delivery_risk) as delayed_orders,
round(100.0*sum(late_delivery_risk)/count(*),2) as late_delivery_percent,
DENSE_RANK() over( order by(round(100.0*sum(late_delivery_risk)/count(*),2) )desc)as late_delivery_percentage_rank
from supply_cleaned_data group by customer_segment having count(*)>=100 order by late_delivery_percentage_rank

---Does delay affect profit?--
SELECT
    delivery_category,
    ROUND(AVG(order_profit_per_order),2) AS avg_profit
FROM supply_cleaned_data
GROUP BY delivery_category;

---Which product categories have the highest late delivery percentage?---
select category_name,count(*)as total_orders,sum(late_delivery_risk)as delayed_orders,
round(sum(late_delivery_risk)*100.0/count(*),2)as late_delivery_percent
from supply_cleaned_data group by category_name order by total_orders desc

---Which departments are most affected?---
select department_name,count(*)as total_orders,sum(late_delivery_risk)as delayed_orders,
round(sum(late_delivery_risk)*100.0/count(*),2)as late_delivery_percent
from supply_cleaned_data group by department_name order by late_delivery_percent desc

---Delivery Category by Customer Segment---
SELECT customer_segment,delivery_category,
    COUNT(*) AS total_orders
FROM dbo.supply_cleaned_data
GROUP BY customer_segment,delivery_category ORDER BY customer_segment,total_orders DESC;

---Risk Ranking---
select customer_segment,count(*) as total_orders,
round(avg(delay_gap),2)as average_delivery_gap,sum(late_delivery_risk) as delayed_orders,
round(100.0*sum(late_delivery_risk)/count(*),2) as late_delivery_percent,
DENSE_RANK() over( order by(round(100.0*sum(late_delivery_risk)/count(*),2) )desc)as risk_rank
from supply_cleaned_data group by customer_segment having count(*)>=100 order by risk_rank desc

