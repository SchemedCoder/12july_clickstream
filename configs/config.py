# ==========================================
# Kafka Configuration
# ==========================================

KAFKA_BOOTSTRAP_SERVERS = "localhost:9092"

CLICKSTREAM_TOPIC = "clickstream_events"

EVENTS_PER_SECOND = 5


# ==========================================
# Bronze Layer
# ==========================================

BRONZE_PATH = "data/bronze"

CHECKPOINT_BRONZE = "checkpoints/bronze"


# ==========================================
# Silver Layer
# ==========================================

SILVER_PATH = "data/silver"

CHECKPOINT_SILVER = "checkpoints/silver"


# ==========================================
# Gold Layer
# ==========================================

GOLD_PATH = "data/gold"

CHECKPOINT_GOLD = "checkpoints/gold"


# ==========================================
# Dead Letter Queue
# ==========================================

BAD_RECORDS_PATH = "data/bad_records"
