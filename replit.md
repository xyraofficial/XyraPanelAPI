# XyraPanel Backend API

## Overview
Backend API untuk fitur Laporkan Masalah (Report Issue) di aplikasi XyraPanel. API ini menerima laporan masalah dari pengguna dan mengirimnya via email.

## Project Structure
- `server.js` - Main Express.js server
- `api/report.js` - Vercel serverless function (for Vercel deployment)
- `vercel.json` - Vercel deployment configuration

## API Endpoints

### GET /
Returns API status and available endpoints.

### POST /api/report
Sends a problem report via email.

**Request Body:**
```json
{
  "message": "Problem description (required)",
  "deviceInfo": "Device information",
  "subject": "Email subject (optional)",
  "appVersion": "1.0"
}
```

## Environment Variables Required
| Variable | Description |
|----------|-------------|
| SMTP_USER | Gmail address for sending emails (default: xyraofficialsup@gmail.com) |
| SMTP_PASS | Gmail App Password (required for email to work) |

## Running Locally
```bash
npm install
npm start
```

Server runs on port 5000.

## Deployment
Can be deployed to:
- **Replit**: Click the "Publish" button
- **Vercel**: Push to GitHub and import in Vercel
