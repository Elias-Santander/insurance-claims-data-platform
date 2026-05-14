SELECT claim_id,
    policy_id,
    vehicle_id,
    incident_type,
    claim_amount,
    claim_status,
    fraud_flag,
    CASE
        WHEN claim_amount > 15000
        THEN 'HIGH_RISK'
        WHEN claim_amount > 5000
        THEN 'MEDIUM_RISK'
        ELSE 'LOW_RISK'
    END AS risk_level,
    DATE(claim_date) AS claim_day
FROM {{ ref('stg_claims') }}