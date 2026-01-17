# Railway Deployment Guide

## Project Status ✅

Your Chess Game project has been successfully cleaned and prepared for Railway deployment!

### What Was Done
1. **Cleaned project** - Removed 14 unnecessary files/folders
2. **Optimized for Railway** - Updated Django settings for Railway environment
3. **Added deployment configs** - Procfile, railway.toml
4. **Updated remote** - Pushed to new GitHub repository

### Repository
- **New URL**: https://github.com/bishal-2630/Chess.git
- **Clean codebase**: Ready for Railway deployment

## Railway Deployment Steps

### 1. Connect Railway to GitHub
1. Go to https://railway.app
2. Click "New Project" → "Deploy from GitHub repo"
3. Connect your GitHub account
4. Select the `bishal-2630/Chess` repository

### 2. Configure Environment Variables
Set these in Railway dashboard:

#### Required Variables
- `SECRET_KEY` - Generate a random key
- `DATABASE_URL` - Railway provides this automatically
- `DEBUG` - Set to `False` for production

#### Email Configuration (for OTP)
- `DEFAULT_FROM_EMAIL` - Your email address
- `EMAIL_HOST` - SMTP server (e.g., smtp.gmail.com)
- `EMAIL_HOST_USER` - Your email username
- `EMAIL_HOST_PASSWORD` - Your email password
- `EMAIL_PORT` - `587`
- `EMAIL_USE_TLS` - `True`

#### Firebase (optional)
- `FIREBASE_API_KEY` - Your Firebase API key

### 3. Deploy
1. Click "Deploy Now"
2. Railway will automatically detect Django
3. Wait for deployment to complete
4. Your app will be available at: `https://your-app-name.up.railway.app`

## Project Structure After Cleanup

```
Chess/
├── chess_backend/          # Django backend ✅
├── auth_app/              # Authentication ✅
├── api/                   # API handlers ✅
├── index.html             # Flutter web app ✅
├── flutter_bootstrap.js   # Flutter runtime ✅
├── main.dart.js          # Flutter compiled code ✅
├── requirements.txt      # Python dependencies ✅
├── manage.py             # Django management ✅
├── Procfile              # Railway deployment config ✅
├── railway.toml          # Railway build config ✅
├── README.md             # Project documentation ✅
└── DEPLOYMENT_GUIDE.md   # This guide ✅
```

## Removed Files (Cleaned Up)
- `.venv/` - Virtual environment
- `.vercelignore` - Vercel ignore file
- `vercel.json` - Vercel configuration
- `staticfiles/` - Django static files
- `db.sqlite3` - Local database
- `chess_game/` - Flutter source code
- `verify_move.py` - Debug script
- `verify_ws.py` - Debug script
- `runtime.txt` - Python version spec
- `assets/`, `icons/`, `canvaskit/` - Build artifacts

## Expected Results After Railway Deployment

✅ **Flutter app loads** - Chess game interface
✅ **Guest login works** - Play without registration
✅ **User authentication** - Login/register with OTP
✅ **API endpoints** - All auth endpoints functional
✅ **Database** - PostgreSQL database with user data
✅ **Email OTP** - OTP verification system

## Troubleshooting

If deployment fails:
1. Check Railway logs for errors
2. Verify environment variables are set
3. Ensure DATABASE_URL is configured
4. Check if all dependencies are in requirements.txt

## Success Indicators

- ✅ Railway deployment completes without errors
- ✅ App loads at Railway URL
- ✅ Guest login works immediately
- ✅ Registration/login with OTP works
- ✅ API endpoints respond correctly

Your Chess Game is now ready for Railway deployment! 🎉
