import os
import uuid
from flask import Flask, Response, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/download-profile/<dns_id>/<username>.mobileconfig', methods=['GET'])
def download_profile(dns_id, username):
    # File cấu hình chuẩn Apple iOS
    xml_content = f'''<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
  <dict>
    <key>PayloadDisplayName</key>
    <string>NextDNS ({dns_id}) · {username}</string>
    <key>PayloadDescription</key>
    <string>Cấu hình DNS VIP Locket dành riêng cho {username}. Vận hành bởi Duc Kien DNS.</string>
    <key>PayloadIdentifier</key>
    <string>io.nextdns.{dns_id}.profile</string>
    <key>PayloadOrganization</key>
    <string>Duc Kien DNS</string>
    <key>PayloadScope</key>
    <string>System</string>
    <key>PayloadType</key>
    <string>Configuration</string>
    <key>PayloadUUID</key>
    <string>{uuid.uuid4()}</string>
    <key>PayloadVersion</key>
    <integer>1</integer>
    <key>PayloadContent</key>
    <array>
      <dict>
        <key>DNSSettings</key>
        <dict>
          <key>DNSProtocol</key>
          <string>HTTPS</string>
          <key>ServerURL</key>
          <string>https://apple.dns.nextdns.io/{dns_id}/{username}</string>
        </dict>
        <key>PayloadType</key>
        <string>com.apple.dnsSettings.managed</string>
        <key>PayloadIdentifier</key>
        <string>io.nextdns.{dns_id}.profile.dnsSettings.managed</string>
        <key>PayloadUUID</key>
        <string>{uuid.uuid4()}</string>
        <key>PayloadDisplayName</key>
        <string>NextDNS ({dns_id}) · {username}</string>
        <key>PayloadOrganization</key>
        <string>Duc Kien DNS</string>
        <key>PayloadVersion</key>
        <integer>1</integer>
      </dict>
    </array>
  </dict>
</plist>'''
    
    # Trả về MIME type chuẩn của Profile iOS để Safari bật popup Cài đặt lập tức
    return Response(xml_content, mimetype='application/x-apple-asymmetric-key-exchange')

@app.route('/', methods=['GET'])
def home():
    return "Test Server Ready!", 200

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
