There is an Apache-style access log at /app/access.log. Analyze the traffic and write
a JSON summary to /app/report.json with exactly these keys:

- total_requests: the number of log lines
- unique_ips: the number of distinct client IP addresses
- top_path: the single most frequently requested path

Success criteria:
1. /app/report.json exists and is valid JSON.
2. total_requests equals the number of log lines.
3. unique_ips equals the count of distinct client IPs.
4. top_path equals the most frequently requested path.
