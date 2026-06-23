# Social Network Graph Analysis

## Overview

This project is a simple simulation of a social media friendship/following network using graph theory concepts.

The application represents users as nodes (vertices) and following relationships as directed edges. Several graph analysis features are provided to demonstrate the implementation of discrete mathematics concepts such as directed graphs, degrees, shortest paths, and set operations.

This project is intentionally simple and does not aim to replicate a real social media platform. It was created solely to fulfill the final project requirements for the Discrete Mathematics course.

---

## Features

### Graph Information
Displays:

- Total number of nodes (users)
- Total number of edges (following relationships)

### In Degree
Displays the number of followers owned by each user.

### Out Degree
Displays the number of accounts followed by each user.

### Top Influencer
Identifies the user(s) with the highest number of followers.

### Most Active User
Identifies the user(s) who follow the most users.

### Shortest Path
Finds the shortest connection path between two users within the social network graph.

### Mutual Connection
Finds common connections shared by two users.

---

## Dataset Format

The application uses a CSV file containing user relationships.

Example:

```csv
from_user,to_user
Andi,Rafi
Budi,Rafi
Rafi,Sinta
Sinta,Dimas
```

Where:

- `from_user` = user who follows
- `to_user` = user being followed

Each row is converted into a directed edge:

```text
from_user ───▶ to_user
```

---

## How to Use

Clone the repository:

```bash
git clone https://github.com/rafiarrafif/graph-social-network.git
```

Move into the project directory:

```bash
cd graph-social-network
```

Install dependencies automatically:

```bash
pip install -r requirements.txt
```

Or install dependencies manually:

```bash
pip install pandas networkx
```

Run the application:

```bash
python index.py
```

---

## Technologies Used

- Python
- Pandas
- NetworkX

---

## Graph Concepts Implemented

This project applies several concepts from Discrete Mathematics:

- Directed Graph
- Vertex (Node)
- Edge
- In Degree
- Out Degree
- Shortest Path
- Set Intersection
- Social Network Representation

---

## Disclaimer

This project is intended for educational purposes only and was developed as a final assignment for the Discrete Mathematics course.