# Database Schema Design

## Database Engine

PostgreSQL 15+

## ORM

SQLAlchemy 2.0


# Entities


## users

Purpose:
System users and roles.

Columns:

- id (PK)
- email
- password_hash
- role
- is_active
- created_at
- updated_at


Relationships:

User 1 ---- N AuditLogs



## cameras

Purpose:
Registered camera sources.

Columns:

- id (PK)
- name
- location
- source_type
- connection_url
- status
- created_at
- updated_at


Relationships:

Camera 1 ---- N Violations



## workers

Purpose:
Detected workers/person identities.

Columns:

- id (PK)
- identifier
- name
- created_at


Relationships:

Worker 1 ---- N Violations



## violations

Purpose:
Safety violations detected by AI system.

Columns:

- id (PK)
- camera_id (FK)
- worker_id (FK)
- violation_type
- confidence
- status
- created_at


Relationships:

Violation N ---- 1 Camera

Violation N ---- 1 Worker

Violation 1 ---- N Snapshots



## snapshots

Purpose:
Evidence images for violations.

Columns:

- id (PK)
- violation_id (FK)
- storage_path
- created_at


Relationships:

Snapshot N ---- 1 Violation



## audit_logs

Purpose:
Enterprise activity tracking.

Columns:

- id (PK)
- user_id (FK)
- action
- entity
- created_at


Relationships:

AuditLog N ---- 1 User



## system_configurations

Purpose:
Runtime application configuration.

Columns:

- id (PK)
- key
- value
- updated_at



# Entity Relationship Summary


User
 |
 |----< AuditLogs


Camera
 |
 |----< Violations
              |
              |----< Snapshots


Worker
 |
 |----< Violations



# Naming Convention


Python Classes:

- User
- Camera
- Worker
- Violation
- Snapshot
- AuditLog
- SystemConfiguration


Database Tables:

- users
- cameras
- workers
- violations
- snapshots
- audit_logs
- system_configurations