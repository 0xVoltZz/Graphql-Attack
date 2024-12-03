
# GraphQL SQL Injection Tester Documentation

## Overview
**GraphQL SQL Injection Tester** is a security testing tool designed to help users identify potential **SQL injection** vulnerabilities in **GraphQL** APIs. It automatically detects endpoints, tests them with a variety of SQL injection payloads, and helps security researchers discover flaws in GraphQL implementations.

### Key Features
- **🔍 Endpoint Discovery**: Uses **InQL** to discover GraphQL endpoints.
- **💥 SQL Injection Testing**: Tests the discovered endpoints with SQL injection payloads.
- **📂 Result Storage**: Saves the testing results in TSV files for easy analysis.
- **⚙️ Customizable Payloads**: Supports a variety of SQL injection payloads for comprehensive testing.

---

## Getting Started

### Prerequisites
- Python 3.10 or later
- Required Python libraries:
  - `requests`
  - `colorama`
  - `argparse`

Install the required libraries using:
```bash
pip install -r requirements.txt
```

### Installation

#### Automatic Installation

```bash
   git clone https://github.com/0xVoltZz/GraphqlAttack.git
   cd GraphqlAttack
   python AUTORUN.py
```

#### Manual Installation
1. **Set up a virtual environment**:
   - **Create a virtual environment**:
     ```bash
     python -m venv .venv
     ```

   - **Activate the virtual environment**:
     - On **Windows**:
       ```bash
       .venv\Scripts\activate
       ```
     - On **macOS/Linux**:
       ```bash
       source .venv/bin/activate
       ```

2. **Install project dependencies**:
   - On **Windows**:
     ```bash
     .venv\Scripts\python -m pip install -r requirements.txt
     ```
   - On **macOS/Linux**:
     ```bash
     .venv/bin/python3 -m pip install -r requirements.txt
     ```

3. **Run the application**:
   ```bash
   python AUTORUN.py
   ```

---

## How to Use GraphQL SQL Injection Tester

### Main Functionalities

#### 1. Endpoint Discovery
- The tool automatically discovers GraphQL endpoints on the provided URL using **InQL**.
- It generates `.tsv` files with the list of discovered query and mutation endpoints.

#### 2. SQL Injection Testing
- The tool tests the discovered endpoints using a set of SQL injection payloads.
- Payloads are generated and injected into the query parameters of the GraphQL operations.

#### 3. Result Storage
- The results of the SQL injection tests are stored in `.tsv` files, which can be found in the directory named after the target domain.
- The files include `endpoint_*.tsv` 

#### 4. Testing the Results
- After the endpoints are discovered, the tool can send test requests to these endpoints with the SQL injection payloads to check for vulnerabilities.

---

## FAQ

1. **What does the tool test for?**
   - The tool tests for **SQL injection vulnerabilities** in GraphQL APIs by injecting specially crafted payloads into discovered GraphQL queries and mutations.

2. **What are the required permissions for using this tool?**
   - You must have permission to test the target GraphQL API. Unauthorized testing may violate terms of service or local laws.

3. **What types of payloads are used?**
   - The tool uses a variety of SQL injection payloads, generated dynamically, to test for vulnerabilities in GraphQL queries and mutations.

4. **Can I use this tool on any GraphQL API?**
   - Yes, the tool can be used on any publicly accessible GraphQL API as long as you have the necessary permissions.

---

## Security Considerations

- **Ethical Use**: Ensure you have explicit permission to test the target system. Unauthorized security testing can result in legal consequences.
- **Injection Risks**: SQL injection can have severe consequences on databases, including data loss or unauthorized access. Always use tools like this responsibly.
- **Data Handling**: Any sensitive data accessed or injected during testing should be handled according to ethical guidelines and legal standards.

