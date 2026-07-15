# M2.4.3 Violation Notification Sequence

## Overview

This sequence describes how detected safety violations are converted into user alerts.


---

# Sequence Diagram

AI Detection Pipeline

|

| Detection Result

↓

Compliance Engine

|

| Violation Event

↓

Violation Service

|

| Create Violation

↓

Database

|

| Notification Trigger

↓

Notification Service

|

| WebSocket Message

↓

Dashboard Alert



---

# Step Description


## 1. Detection Event


Component:

AI Pipeline


Action:

A PPE violation is detected.


Example:


Worker detected

Missing Helmet

Confidence: 95%



---

## 2. Compliance Processing


Component:

Compliance Engine


Responsibilities:

- Evaluate safety rules
- Confirm violation


Output:

Violation event


---

## 3. Violation Storage


Component:

Violation Service


Responsibilities:

- Create violation record
- Store evidence information
- Link camera information


Database stores:

- Camera ID
- Worker ID
- Violation Type
- Timestamp
- Confidence


---

## 4. Notification Creation


Component:

Notification Service


Responsibilities:

- Create alert message
- Send real-time update


---

## 5. Dashboard Alert


Component:

Frontend Dashboard


Displays:

- Camera location
- Violation type
- Timestamp
- Snapshot evidence


---

# Result

Safety personnel receive immediate notification and can take corrective action.