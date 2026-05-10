# Deployment Guide - Free Live Hosting

This guide will help you deploy the DevOps Monitoring System on **Render** (free platform).

## Free Deployment Options

### 🎯 **Recommended: Render.com** (Completely Free)
- ✅ Free tier includes: Web services, PostgreSQL database
- ✅ Automatic deployments from GitHub
- ✅ Custom domains available
- ✅ No credit card required for free tier

### Other Free Options
- **Railway.app** - $5 free credit per month
- **Heroku** - Paid only (no free tier anymore)
- **Netlify** - Good for frontend only
- **Vercel** - Good for frontend only

---

## Step-by-Step: Deploy on Render.com

### **Step 1: Prepare GitHub Repository**

1. **Initialize Git** (if not already done):
   ```bash
   cd "DevOps Monitoring and Incident Response System"
   git add .
   git commit -m "Add DevOps Monitoring System"
   git push origin main
   ```

2. **Make sure these files are in the repo**:
   - `render.yaml` - Deployment configuration
   - `backend/requirements.txt` - Python dependencies
   - `backend/main.py` - FastAPI app
   - `frontend/package.json` - Node dependencies
   - `infrastructure/schema.sql` - Database schema

### **Step 2: Create Render Account**

1. Go to **https://render.com**
2. Sign up with GitHub (recommended)
3. Authorize Render to access your GitHub

### **Step 3: Deploy from render.yaml**

1. Click **"New +"** button → **"Blueprint"**
2. Connect your GitHub repository
3. Click **"Connect"** on your repo
4. Render will auto-detect `render.yaml`
5. Review services:
   - **devops-monitoring-frontend** (Node.js)
   - **devops-monitoring-backend** (Python)
   - **postgres** (Database)
6. Click **"Create New Blueprint"**
7. Wait for deployment (5-10 minutes)

### **Step 4: Get Your Live URLs**

After deployment completes, you'll get:
- **Frontend**: `https://devops-monitoring-frontend.onrender.com`
- **Backend API**: `https://devops-monitoring-backend.onrender.com`
- **API Docs**: `https://devops-monitoring-backend.onrender.com/docs`

---

## Updated Frontend Configuration

Update `frontend/src/App.jsx` to use the live API:

```jsx
const API_BASE = 'https://devops-monitoring-backend.onrender.com'
```

---

## Common Issues & Solutions

### ❌ Frontend Can't Connect to Backend
**Solution**: Update API URL in `frontend/src/App.jsx` to use the production backend URL

### ❌ Database Connection Failed
**Solution**: Render automatically creates the `DATABASE_URL` environment variable. The schema is applied automatically.

### ❌ Build Takes Too Long
**Solution**: Free tier can be slow. This is normal. Wait for completion.

### ❌ Service Keeps Restarting
**Solution**: Check logs in Render dashboard. Common causes:
- Missing environment variables
- Syntax errors in code
- Database connection issues

---

## Monitoring Your Deployment

1. Go to **Render Dashboard**
2. Click on each service to view:
   - Logs
   - Environment variables
   - Deployment history
3. Set up notifications for build failures

---

## How to Update Your Deployment

Every time you push to GitHub:
1. Code automatically deploys to Render
2. Frontend rebuilds and redeploys
3. Backend restarts with new code
4. Changes live within 2-5 minutes

---

## Next Steps

1. ✅ Push all code to GitHub
2. ✅ Create Render account
3. ✅ Deploy using render.yaml
4. ✅ Test your live application
5. ✅ Set up custom domain (optional)

**Total time**: ~15 minutes

---

## Custom Domain (Optional)

1. Go to service settings in Render
2. Click **"Settings"**
3. Scroll to **"Custom Domain"**
4. Enter your domain
5. Add DNS records as shown

---

## Support

- **Render Docs**: https://render.com/docs
- **FastAPI Docs**: https://fastapi.tiangolo.com
- **React Docs**: https://react.dev

---

**Your app will be live and free! 🚀**
