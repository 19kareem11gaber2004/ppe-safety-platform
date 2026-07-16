# Configuration Catalog

## Retention Configuration

| Key | Default | Description |
|---|---|---|
| SNAPSHOT_RETENTION_DAYS | 90 | Snapshot lifetime |
| LOG_RETENTION_DAYS | 30 | Application logs lifetime |
| VIOLATION_RETENTION_DAYS | 365 | Violation records lifetime |

## Future Cleanup Strategy

A background worker will:

1. Read retention values from ConfigurationService.
2. Find expired records/files.
3. Archive or delete according to policy.
4. Create audit events.

Automatic deletion is disabled currently.
# Configuration Catalog

## AI

| Key | Default |
|---|---|
| AI_CONFIDENCE_THRESHOLD | 0.65 |
| IOU_THRESHOLD | 0.45 |
| MAX_DETECTIONS | 100 |
| IMAGE_SIZE | 640 |
| MODEL_NAME | yolov8 |
| MODEL_VERSION | v1 |
| MODEL_PATH | models/best.pt |
| FRAME_SKIP | 2 |
| INFERENCE_INTERVAL | 1.0 |


## CAMERA

| Key | Default |
|---|---|
| DEFAULT_CAMERA_FPS | 30 |
| FRAME_TIMEOUT | - |
| RECONNECT_ATTEMPTS | - |
| RTSP_TIMEOUT | - |


## STORAGE

| Key | Default |
|---|---|
| UPLOAD_PATH | uploads |
| SNAPSHOT_PATH | storage/snapshots |
| REPORT_PATH | storage/reports |
| STORAGE_TYPE | LOCAL |


## RETENTION

| Key | Default |
|---|---|
| SNAPSHOT_RETENTION_DAYS | 90 |
| LOG_RETENTION_DAYS | 30 |
| VIOLATION_RETENTION_DAYS | 365 |


## Runtime Updates

All editable values are stored in PostgreSQL.

Modules consume values through ConfigurationService.

Example:

```python
fps = configuration_service.get_int(
    "DEFAULT_CAMERA_FPS"
)
