# Scratch Pad API

A simple API that serves CRUD operations for scratch padd app.

## API Documentation

### 1. Ping

**Path**: */*
**Method**: *GET*
**Parameters**: *None*
**Response**: String("Online")

### 2. Add Pads

**Path**: */pads*
**Method**: *POST*
**Parameters**:

1. *title*[string]
2. *content*[string]

**Response**:

- *id*[integer]: if success

### 3. List of Pads

**Path**: */pads*
**Method**: *GET*
**Parameters**: *None*
**Response**: List(Pads)
Pads:

- *id*[integer]
- *title*[string]

### 4. Get Pad Content

**Path**: */pads/\<id\>*
**Method**: *GET*
**Parameters**: *None*
**Response**: Pad

- *id*[integer]
- *title*[string]
- *content*[string]

### 5. Update Pad

**Path**: */pads/\<id\>*
**Method**: *PUT*
**Parameters**: *content*[string]
**Response**: \<201\>[status_code]

### 6. Delete a Pad

**Path**: */pads/\<id\>*
**Method**: *DELETE*
**Parameters**: *None*
**Response**: 204

