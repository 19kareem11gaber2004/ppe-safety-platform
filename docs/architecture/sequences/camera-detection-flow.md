# M2.4.1 Camera Detection Flow Sequence

## Overview

This sequence describes how video data moves from an industrial camera through the AI pipeline until a safety violation is detected and displayed to users.

The workflow covers:

- Video acquisition
- AI inference
- PPE analysis
- Compliance evaluation
- Violation storage
- Real-time dashboard update


---

# Sequence Diagram

Camera

|

| Video Stream

↓

Camera Manager

|

| Frames

↓

Frame Processor

|

| Processed Frames

↓

YOLO Detection Engine

|

| Detection Results

↓

PPE Matcher

|

| PPE Association

↓

Compliance Engine

|

| Violation Event

↓

Violation Service

|

| Store Violation

↓

PostgreSQL Database

|

| Event Notification

↓

WebSocket Service

|

| Real-time Alert

↓

Dashboard


---

# Step Description


## 1. Camera Connection

Actor:

Camera Manager


Action:

- Establish connection with camera source
- Receive video stream
- Monitor camera availability


Input:

- RTSP/IP camera stream


Output:

- Video frames


---

## 2. Frame Processing


Component:

Frame Processor


Responsibilities:

- Extract frames
- Resize images
- Prepare data for AI inference


Output:

Prepared frames for detection


---

## 3. Object Detection


Component:

YOLO Detection Engine


Responsibilities:

- Detect workers
- Detect PPE objects


Output:

Detection results:

- Object type
- Bounding boxes
- Confidence score


---

## 4. PPE Matching


Component:

PPE Matcher


Responsibilities:

- Associate PPE equipment with workers
- Determine missing equipment


Example:
Worker A

Helmet ✓

Vest ✓

Gloves ✗



---

## 5. Compliance Decision


Component:

Compliance Engine


Responsibilities:

- Apply safety rules
- Determine compliance status


Output:

- Compliant
- Violation


---

## 6. Violation Creation


Component:

Violation Service


Responsibilities:

- Create violation record
- Store detection information
- Trigger notifications


Stored Data:

- Camera ID
- Violation type
- Confidence
- Timestamp


---

## 7. Dashboard Update


Component:

WebSocket Service


Responsibilities:

- Push real-time events
- Update monitoring dashboard


Output:

Safety alert displayed to user.