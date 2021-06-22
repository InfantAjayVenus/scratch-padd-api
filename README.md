# Scratch Padd API

A simple API that serves CRUD operations for scratch padd app.

## API Documentation

### 1. Ping

**Path**: */*
**Method**: *GET*
**Parameters**: *None*
**Response**: String("Online")

### 2. Add Padds

**Path**: */padds*
**Method**: *POST*
**Parameters**:

1. *title*[string]
2. *content*[string]

**Response**:

- *id*[integer]: if success

### 3. List of Padds

**Path**: */padds*
**Method**: *GET*
**Parameters**: *None*
**Response**: List(Padds)
Padds:

- *id*[integer]
- *title*[string]

### 4. Get Padd Content

**Path**: */padds/\<id\>*
**Method**: *GET*
**Parameters**: *None*
**Response**: Padd

- *id*[integer]
- *title*[string]
- *content*[string]

### 5. Update Padd

**Path**: */padds/\<id\>*
**Method**: *PUT*
**Parameters**: *content*[string]
**Response**: \<201\>[status_code]

### 6. Delete a Padd

**Path**: */padds/\<id\>*
**Method**: *DELETE*
**Parameters**: *None*
**Response**: 204

