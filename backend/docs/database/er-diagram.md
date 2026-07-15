# ER Diagram


```mermaid
erDiagram

    USERS ||--o{ AUDIT_LOGS : creates

    CAMERAS ||--o{ VIOLATIONS : detects

    WORKERS ||--o{ VIOLATIONS : involved_in

    VIOLATIONS ||--o{ SNAPSHOTS : contains


    USERS {
        int id PK
        string email
        string role
    }


    CAMERAS {
        int id PK
        string name
        string status
    }


    WORKERS {
        int id PK
        string identifier
        string name
    }


    VIOLATIONS {
        int id PK
        int camera_id FK
        int worker_id FK
        float confidence
        string status
    }


    SNAPSHOTS {
        int id PK
        int violation_id FK
        string storage_path
    }


    AUDIT_LOGS {
        int id PK
        int user_id FK
        string action
    }