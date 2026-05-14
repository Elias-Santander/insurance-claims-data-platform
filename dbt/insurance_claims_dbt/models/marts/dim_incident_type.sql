SELECT DISTINCT incident_type,
    CASE
        WHEN incident_type = 'COLLISION'
        THEN 'Vehicle Accident'
        WHEN incident_type = 'THEFT'
        THEN 'Crime Related'
        ELSE 'Other'
    END AS category
FROM {{ ref('stg_claims') }}