-- Example: book × underlying × tenor vega
SELECT
  as_of,                -- 风险快照日期/时间戳
  desk,                 -- 桌面/业务线
  book,                 -- 账本
  underlying,           -- 标的
  tenor_bucket,         -- 期限桶（1M/3M/6M/1Y…）
  SUM(vega_base_ccy) AS vega  -- 把每笔交易的 vega 加总（统一到基准货币）
FROM risk_trade_greeks
WHERE as_of = :t        -- 仅取某次估值快照（参数）
  AND desk  = :desk     -- 仅取某个 desk（参数）
GROUP BY 1,2,3,4,5;     -- 按上面五个维度聚合

-- maturity_date -> tenor_bucket
WITH base AS (
  SELECT
    as_of, desk, book, underlying,
    CASE
      WHEN maturity_date <= as_of + INTERVAL '30'  DAY THEN '1M'
      WHEN maturity_date <= as_of + INTERVAL '90'  DAY THEN '3M'
      WHEN maturity_date <= as_of + INTERVAL '180' DAY THEN '6M'
      WHEN maturity_date <= as_of + INTERVAL '365' DAY THEN '1Y'
      ELSE '2Y+'
    END AS tenor_bucket,
    vega_base_ccy
  FROM risk_trade_greeks
  WHERE as_of = :t AND desk = :desk
)
SELECT as_of, desk, book, underlying, tenor_bucket, SUM(vega_base_ccy) AS vega
FROM base
GROUP BY 1,2,3,4,5;