# M2.4.2 User Login Sequence

## Overview

This sequence describes how users authenticate and access the platform.


---

# Sequence Diagram

User

|

| Login Credentials

↓

Frontend Application

|

| Authentication Request

↓

Authentication API

|

| Validate User

↓

Database

|

| User Information

↓

Authentication Service

|

| Generate JWT Token

↓

Frontend Application

|

| Access Token

↓

Dashboard



---

# Step Description


## 1. User Authentication Request

Actor:

User


Action:

User enters:

- Email
- Password


The frontend sends authentication request.


---

## 2. API Authentication


Component:

Authentication API


Responsibilities:

- Receive login request
- Validate input
- Forward authentication request


---

## 3. User Validation


Component:

Database


Responsibilities:

- Search user account
- Verify password hash
- Retrieve user role


---

## 4. Token Generation


Component:

Authentication Service


Responsibilities:

- Generate JWT access token
- Generate refresh token
- Include user permissions


---

## 5. Dashboard Access


Frontend stores token and allows access based on user role.


Roles:

- Admin
- Safety Officer
- Viewer
