WITH TotalSales AS (
    SELECT
        s.store_type,
        SUM(o.product_quantity * p.product_price) AS total_sales
    FROM
        order_table o
    JOIN
        dim_products p ON o.product_code = p.product_code
    JOIN
        dim_store_details s ON o.store_code = s.store_code
    GROUP BY 
        s.store_type
),
OverallSales AS (
    SELECT
        SUM(total_sales) AS overall_total
    FROM
        TotalSales
)
SELECT
    ts.store_type,
    ROUND(CAST(ts.total_sales AS numeric), 2) AS total_sales,
    ROUND((CAST(ts.total_sales AS numeric) / CAST(os.overall_total AS numeric)) * 100, 2) AS percentage_of_total
FROM
    TotalSales ts,
    OverallSales os
ORDER BY 
    total_sales DESC;