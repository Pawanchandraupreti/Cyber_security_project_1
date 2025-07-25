from reportlab.pdfgen import canvas

def generate_report(anomalies):
    c = canvas.Canvas("threat_report.pdf")
    c.setFont("Helvetica-Bold", 16)
    c.drawString(100, 750, "CYBERSECURITY THREAT REPORT")
    c.setFont("Helvetica", 12)
    c.drawString(100, 700, f"Detected anomalies: {len(anomalies)}")
    c.drawString(100, 680, "Top malicious IPs:")
    y = 650
    for ip in anomalies["src_ip"].head(5):
        c.drawString(120, y, f"- {ip}")
        y -= 20
    c.save()

# Example usage
anomalies = pd.read_csv("detected_anomalies.csv")
generate_report(anomalies)