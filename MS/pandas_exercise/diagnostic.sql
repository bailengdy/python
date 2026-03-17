-- Compare yesterday vs today Delta per trade
SELECT a.trade_id,
       a.delta AS delta_yday,
       b.delta AS delta_today,
       (b.delta - a.delta) AS delta_diff
FROM risk_trade_greeks a
JOIN risk_trade_greeks b USING (trade_id)
WHERE a.as_of = :yday AND b.as_of = :today
AND ABS(b.delta - a.delta) > 1e-4;