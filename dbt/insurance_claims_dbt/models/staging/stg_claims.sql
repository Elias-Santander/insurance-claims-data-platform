SELECT claim_id,
    policy_id,
    vehicle_id,
    claim_date,
    incident_type,
    claim_amount,
    claim_status,
    fraud_flag,
    etl_processed_date
FROM public.claims_raw