from sqlalchemy.orm import Session

from app.db.session import SessionLocal
from app.models.configuration import SystemConfiguration


AI_CONFIGURATIONS = [
    {
        "key": "AI_CONFIDENCE_THRESHOLD",
        "value": "0.65",
        "category": "AI",
        "data_type": "float",
        "description": "Minimum AI detection confidence threshold",
        "is_editable": True,
    },
    {
        "key": "IOU_THRESHOLD",
        "value": "0.45",
        "category": "AI",
        "data_type": "float",
        "description": "Intersection over Union threshold",
        "is_editable": True,
    },
    {
        "key": "MAX_DETECTIONS",
        "value": "100",
        "category": "AI",
        "data_type": "integer",
        "description": "Maximum detections per frame",
        "is_editable": True,
    },
    {
        "key": "IMAGE_SIZE",
        "value": "640",
        "category": "AI",
        "data_type": "integer",
        "description": "AI model input image size",
        "is_editable": True,
    },
    {
        "key": "MODEL_NAME",
        "value": "yolov8",
        "category": "AI",
        "data_type": "string",
        "description": "AI detection model name",
        "is_editable": True,
    },
    {
        "key": "MODEL_VERSION",
        "value": "v1",
        "category": "AI",
        "data_type": "string",
        "description": "AI model version",
        "is_editable": True,
    },
    {
        "key": "MODEL_PATH",
        "value": "models/best.pt",
        "category": "AI",
        "data_type": "string",
        "description": "AI model file location",
        "is_editable": True,
    },
    {
        "key": "FRAME_SKIP",
        "value": "2",
        "category": "AI",
        "data_type": "integer",
        "description": "Number of skipped frames",
        "is_editable": True,
    },
    {
        "key": "INFERENCE_INTERVAL",
        "value": "1.0",
        "category": "AI",
        "data_type": "float",
        "description": "Seconds between inference executions",
        "is_editable": True,

    },
    {
    "key": "DEFAULT_CAMERA_FPS",
    "value": "15",
    "category": "CAMERA",
    "data_type": "integer",
    "description": "Default camera frames per second",
    "is_editable": True,
},

{
    "key": "FRAME_TIMEOUT",
    "value": "10",
    "category": "CAMERA",
    "data_type": "integer",
    "description": "Camera frame read timeout in seconds",
    "is_editable": True,
},

{
    "key": "RECONNECT_ATTEMPTS",
    "value": "5",
    "category": "CAMERA",
    "data_type": "integer",
    "description": "Maximum camera reconnect attempts",
    "is_editable": True,
},

{
    "key": "RTSP_TIMEOUT",
    "value": "5",
    "category": "CAMERA",
    "data_type": "integer",
    "description": "RTSP connection timeout",
    "is_editable": True,
},

{
    "key": "STREAM_QUALITY",
    "value": "high",
    "category": "CAMERA",
    "data_type": "string",
    "description": "Camera streaming quality profile",
    "is_editable": True,
},

{
    "key": "JPEG_COMPRESSION",
    "value": "80",
    "category": "CAMERA",
    "data_type": "integer",
    "description": "JPEG compression quality percentage",
    "is_editable": True,
},

{
    "key": "MAX_CLIENTS",
    "value": "10",
    "category": "CAMERA",
    "data_type": "integer",
    "description": "Maximum streaming clients",
    "is_editable": True,
},
{
    "key": "UPLOAD_PATH",
    "value": "uploads",
    "category": "STORAGE",
    "data_type": "string",
    "description": "Upload files storage path",
    "is_editable": True,
},

{
    "key": "SNAPSHOT_PATH",
    "value": "storage/snapshots",
    "category": "STORAGE",
    "data_type": "string",
    "description": "Snapshot files storage path",
    "is_editable": True,
},

{
    "key": "REPORT_PATH",
    "value": "storage/reports",
    "category": "STORAGE",
    "data_type": "string",
    "description": "Generated reports storage path",
    "is_editable": True,
},

{
    "key": "MAX_STORAGE_SIZE",
    "value": "100GB",
    "category": "STORAGE",
    "data_type": "string",
    "description": "Maximum storage capacity",
    "is_editable": True,
},

{
    "key": "STORAGE_TYPE",
    "value": "LOCAL",
    "category": "STORAGE",
    "data_type": "string",
    "description": "Storage backend type LOCAL/S3/MINIO",
    "is_editable": True,
},

{
    "key": "BACKUP_LOCATION",
    "value": "backup",
    "category": "STORAGE",
    "data_type": "string",
    "description": "Backup destination location",
    "is_editable": True,
},
{
    "key": "SNAPSHOT_RETENTION_DAYS",
    "value": "90",
    "category": "RETENTION",
    "data_type": "integer",
    "description": "Number of days to keep snapshots",
    "is_editable": True,
},

{
    "key": "LOG_RETENTION_DAYS",
    "value": "30",
    "category": "RETENTION",
    "data_type": "integer",
    "description": "Number of days to keep system logs",
    "is_editable": True,
},

{
    "key": "VIOLATION_RETENTION_DAYS",
    "value": "365",
    "category": "RETENTION",
    "data_type": "integer",
    "description": "Number of days to keep violation records",
    "is_editable": True,
},
]


def seed_ai_configurations(
    db: Session,
):
    for item in AI_CONFIGURATIONS:

        existing = (
            db.query(SystemConfiguration)
            .filter(
                SystemConfiguration.key == item["key"]
            )
            .first()
        )

        if existing:
            continue

        configuration = SystemConfiguration(
            **item
        )

        db.add(configuration)

    db.commit()



def main():

    db = SessionLocal()

    try:
        seed_ai_configurations(db)
        print("AI configurations seeded successfully")

    finally:
        db.close()


if __name__ == "__main__":
    main()
