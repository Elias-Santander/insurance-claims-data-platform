SELECT claim_day,
    incident_type,
    risk_level,
    COUNT(*) AS total_claims,
    SUM(claim_amount) AS total_claim_amount,
    AVG(claim_amount) AS avg_claim_amount,
    SUM(
        CASE
            WHEN fraud_flag = TRUE
            THEN 1
            ELSE 0
        END
    ) AS fraud_cases
FROM {{ ref('int_claims_enriched') }}
GROUP BY
    claim_day,
    incident_type,
    risk_level