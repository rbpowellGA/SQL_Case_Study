SELECT (
  SELECT COUNT(product.productid)
  FROM production.product
  WHERE listprice = 0
) as zeros,
  (
  SELECT COUNT(product.productid)
  FROM production.product
  WHERE product.listprice BETWEEN 1 AND 11
) as tens,
  (
  SELECT COUNT(product.productid)
  FROM production.product
  WHERE product.listprice BETWEEN 11 AND 101
) as hundreds,
  (
  SELECT COUNT(product.productid)
  FROM production.product
  WHERE product.listprice BETWEEN 101 AND 501
) as five_hundreds,
  (
  SELECT COUNT(product.productid)
  FROM production.product
  WHERE product.listprice BETWEEN 501 AND 1001
) as thousands,
  (
  SELECT COUNT(product.productid)
  FROM production.product
  WHERE product.listprice > 1000
) as thousands_plus
FROM production.product
GROUP BY zeros, tens, hundreds, five_hundreds, thousands, thousands_plus;