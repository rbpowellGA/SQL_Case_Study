SELECT productsubcategory.name, MIN(product.listprice), MAX(product.listprice), MAX(product.listprice)-MIN(product.listprice) AS difference, COUNT(*) AS productcount
FROM production.productsubcategory
JOIN production.product USING(productsubcategoryid)
GROUP BY productsubcategory.name