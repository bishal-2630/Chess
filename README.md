# Chess Game App

A Flutter web application with Django backend for chess gameplay with authentication.

## Features
- Flutter web frontend
- Django REST API backend
- User authentication (login/register/OTP)
- Guest play mode
- Real-time chess gameplay

## Deployment

### Vercel
- **Status**: Partially deployed (frontend working, API issues)
- **URL**: https://chess-game-app-delta.vercel.app
- **Issue**: Vercel Python runtime environment problems

### Railway (Recommended)
- **Status**: Ready for deployment
- **Setup**: See Railway deployment section

## Essential Files Structure
```
Chess/
├── chess_backend/          # Django backend
├── auth_app/              # Authentication app
├── chess_game/            # Flutter source (can be removed for deployment)
├── api/                   # Vercel handlers
├── index.html             # Flutter web build
├── flutter_bootstrap.js   # Flutter runtime
├── main.dart.js          # Flutter compiled code
├── requirements.txt      # Python dependencies
├── manage.py             # Django management
└── vercel.json           # Vercel config (can be removed for Railway)
```

## Railway Deployment Setup
1. Connect Railway to GitHub
2. Create new project from this repository
3. Set environment variables
4. Deploy!

## Environment Variables Needed
- `DATABASE_URL` (PostgreSQL connection)
- `SECRET_KEY` (Django secret)
- `EMAIL_HOST` (for OTP emails)
- `EMAIL_HOST_USER` (email username)
- `EMAIL_HOST_PASSWORD` (email password)
- `FIREBASE_API_KEY` (Firebase auth)
