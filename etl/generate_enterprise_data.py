from faker import Faker
import pandas as pd
import random
from datetime import datetime, timedelta

# =========================================================
# CONFIGURACIÓN GENERAL
# =========================================================

fake = Faker("es_CL")

NUM_CUSTOMERS = 5000
NUM_VEHICLES = 4200
NUM_POLICIES = 4800
NUM_CLAIMS = 12000

# =========================================================
# CATÁLOGOS
# =========================================================

brands = [
    "Toyota",
    "Hyundai",
    "Kia",
    "Mazda",
    "Chevrolet",
    "Nissan",
    "Suzuki"
]

models = {
    "Toyota": ["Corolla", "Yaris", "RAV4"],
    "Hyundai": ["Accent", "Tucson"],
    "Kia": ["Rio", "Sportage"],
    "Mazda": ["CX-5", "Mazda3"],
    "Chevrolet": ["Spark", "Tracker"],
    "Nissan": ["Versa", "Sentra"],
    "Suzuki": ["Swift", "Baleno"]
}

policy_types = [
    "FULL_COVERAGE",
    "THIRD_PARTY",
    "PREMIUM"
]

incident_types = [
    "COLLISION",
    "THEFT",
    "GLASS_DAMAGE",
    "FLOOD",
    "FIRE",
    "VANDALISM"
]

claim_statuses = [
    "OPEN",
    "IN_REVIEW",
    "APPROVED",
    "REJECTED",
    "CLOSED"
]

# =========================================================
# GENERACIÓN DE CUSTOMERS
# =========================================================

print("Generating customers...")
customers = []

for customer_id in range(1, NUM_CUSTOMERS + 1):
    customers.append({
        "customer_id": customer_id,
        "full_name": fake.name(),
        "email": fake.email(),
        "phone": fake.phone_number(),
        "city": fake.city(),
        "registration_date": fake.date_between(
            start_date="-5y",
            end_date="today"
        )
    })

customers_df = pd.DataFrame(customers)
customers_df.to_csv(
    "data/raw/customers.csv",
    index=False
)

print("customers.csv generated successfully")

# =========================================================
# GENERACIÓN DE VEHICLES
# =========================================================

print("Generating vehicles...")
vehicles = []

for vehicle_id in range(1, NUM_VEHICLES + 1):
    brand = random.choice(brands)
    vehicles.append({
        "vehicle_id": vehicle_id,
        "customer_id": random.randint(1, NUM_CUSTOMERS),
        "brand": brand,
        "model": random.choice(models[brand]),
        "year": random.randint(2012, 2025),
        "plate": fake.license_plate()
    })

vehicles_df = pd.DataFrame(vehicles)
vehicles_df.to_csv(
    "data/raw/vehicles.csv",
    index=False
)

print("vehicles.csv generated successfully")

# =========================================================
# GENERACIÓN DE POLICIES
# =========================================================

print("Generating policies...")
policies = []

for policy_id in range(1, NUM_POLICIES + 1):
    start_date = fake.date_between(
        start_date="-3y",
        end_date="-30d"
    )
    end_date = start_date + timedelta(days=365)
    policies.append({
        "policy_id": policy_id,
        "customer_id": random.randint(1, NUM_CUSTOMERS),
        "policy_type": random.choice(policy_types),
        "start_date": start_date,
        "end_date": end_date,
        "premium_amount": round(
            random.uniform(300, 3000),
            2
        )
    })
policies_df = pd.DataFrame(policies)
policies_df.to_csv(
    "data/raw/policies.csv",
    index=False
)

print("policies.csv generated successfully")

# =========================================================
# GENERACIÓN DE CLAIMS
# =========================================================

print("Generating claims...")
claims = []

for claim_id in range(1, NUM_CLAIMS + 1):
    claim_date = fake.date_time_between(
        start_date="-2y",
        end_date="now"
    )
    claim_amount = round(
        random.uniform(200, 25000),
        2
    )
    fraud_flag = claim_amount > 18000
    claims.append({
        "claim_id": claim_id,
        "policy_id": random.randint(1, NUM_POLICIES),
        "vehicle_id": random.randint(1, NUM_VEHICLES),
        "claim_date": claim_date,
        "incident_type": random.choice(incident_types),
        "claim_amount": claim_amount,
        "claim_status": random.choice(claim_statuses),
        "fraud_flag": fraud_flag
    })

# =========================================================
# CASOS ESPECIALES DE FRAUDE
# =========================================================

print("Generating suspicious claims...")
suspicious_vehicle = 25

for i in range(5):
    claims.append({
        "claim_id": NUM_CLAIMS + i + 1,
        "policy_id": 10,
        "vehicle_id": suspicious_vehicle,
        "claim_date": datetime.now() - timedelta(days=i * 3),
        "incident_type": "COLLISION",
        "claim_amount": 24000,
        "claim_status": "IN_REVIEW",
        "fraud_flag": True
    })

claims_df = pd.DataFrame(claims)
claims_df.to_csv(
    "data/raw/claims.csv",
    index=False
)

print("claims.csv generated successfully")

# =========================================================
# GENERACIÓN DE CLAIM STATUS HISTORY
# =========================================================

print("Generating claim status history...")
history = []
history_id = 1

for _, row in claims_df.iterrows():
    status_flow = [
        "OPEN",
        "IN_REVIEW",
        random.choice([
            "APPROVED",
            "REJECTED"
        ]),
        "CLOSED"
    ]
    base_time = row["claim_date"]
    for idx, status in enumerate(status_flow):
        history.append({
            "history_id": history_id,
            "claim_id": row["claim_id"],
            "status": status,
            "change_timestamp": (
                base_time + timedelta(days=idx * 2)
            )
        })
        history_id += 1

history_df = pd.DataFrame(history)
history_df.to_csv(
    "data/raw/claim_status_history.csv",
    index=False
)

print("claim_status_history.csv generated successfully")

# =========================================================
# VALIDACIONES BÁSICAS
# =========================================================

print("\n==============================")
print("DATA GENERATION SUMMARY")
print("==============================")

print(f"Customers generated: {len(customers_df)}")
print(f"Vehicles generated: {len(vehicles_df)}")
print(f"Policies generated: {len(policies_df)}")
print(f"Claims generated: {len(claims_df)}")
print(f"History records generated: {len(history_df)}")

print("\nFraud distribution:")
print(
    claims_df["fraud_flag"]
    .value_counts()
)

print("\nSample claims:")
print(
    claims_df.head()
)

print("\nEnterprise dataset generated successfully.")