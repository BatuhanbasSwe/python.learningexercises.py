import re

# The raw data string
log_data = """
[INFO] User: ali_yilmaz99 logged in at 14:30. IP: 192.168.1.34
[ERROR] Connection failed for admin_user. ID: #44582. Retry count: 3
Contact support at help.desk@company-tech.com for assistance.
"""

# --- MISSION 1: Find Email ---
# Logic: Text + @ + Text + . + Text
# Hint: Use [\w\.-]+ to catch letters, dots and dashes together
email_pattern = r"[\w\.-]+@[\w\.-]+\.\w+"
emails = re.findall(email_pattern, log_data)
print(f"Emails found: {emails}")

# --- MISSION 2: Find ID ---
# Logic: Literal '#' followed by digits
# Hint: Don't forget '+' for multiple digits
id_pattern = r"#\d+"
ids = re.findall(id_pattern, log_data)
print(f"IDs found: {ids}")

# --- MISSION 3: Find IP Address ---
# Logic: Digit+ dot Digit+ dot Digit+ dot Digit+
# Hint: Remember to escape the dot like \.
ip_pattern = r"\d+\.\d+\.\d+\.\d+"
ips = re.findall(ip_pattern, log_data)
ips = re.findall(ip_pattern, log_data)
print(f"IPs found: {ips}")