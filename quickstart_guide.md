# 🚀 Quick Start Guide

Get the AI Marketing Automation system running in 5 minutes!

## Prerequisites

- Python 3.9+
- Node.js 16+
- OpenAI API key ([Get one here](https://platform.openai.com/api-keys))

## Option 1: Automated Setup (Recommended)

### 1. Run Setup Script

```bash
chmod +x setup.sh
./setup.sh
```

Select option 1 for full installation.

### 2. Configure OpenAI API Key

Edit `backend/.env`:
```env
OPENAI_API_KEY=sk-your-actual-api-key-here
```

### 3. Start Backend

```bash
cd backend
source venv/bin/activate  # On Windows: venv\Scripts\activate
python main.py
```

Backend runs on: http://localhost:8000

### 4. Start Frontend (New Terminal)

```bash
cd frontend
npm start
```

Frontend runs on: http://localhost:3000

## Option 2: Docker Setup (Easiest)

### 1. Create .env File

```bash
cp backend/.env.example backend/.env
```

Add your OpenAI API key to `backend/.env`

### 2. Start All Services

```bash
docker-compose up -d
```

That's it! All services are running:
- Frontend: http://localhost:3000
- Backend: http://localhost:8000
- N8N: http://localhost:5678

### 3. Stop Services

```bash
docker-compose down
```

## Option 3: Manual Setup

### Backend

```bash
# 1. Setup backend
cd backend
python -m venv venv
source venv/bin/activate

# 2. Install dependencies
pip install -r requirements.txt

# 3. Configure environment
cp .env.example .env
# Edit .env and add your OpenAI API key

# 4. Create directories
mkdir -p uploads outputs logs campaign_data

# 5. Run server
python main.py
```

### Frontend

```bash
# 1. Setup frontend
cd frontend
npm install

# 2. Create .env
echo "REACT_APP_API_URL=http://localhost:8000" > .env

# 3. Start development server
npm start
```

## First Campaign

1. **Open App**: Navigate to http://localhost:3000

2. **Upload Product Image**: 
   - Click upload area
   - Select a product image (JPG, PNG, WebP)

3. **Fill Details**:
   - Product Name: "Premium Wireless Headphones"
   - Features:
     - "40-hour battery life"
     - "Active noise cancellation"
     - "Premium audio quality"
   - Tone: Premium

4. **Generate Copy**:
   - Click "Generate Marketing Copy"
   - Wait 5-10 seconds for AI generation

5. **Review & Approve**:
   - Review 3 headline options
   - Review 2 caption options per platform
   - Select your favorites
   - Click "Approve & Create Creatives"

6. **Preview Creatives**:
   - View platform-specific images with overlays
   - See LinkedIn, Instagram, Facebook variants

7. **Publish** (Demo Mode):
   - Click "Publish to Social Media"
   - View simulated publish results

## Testing the API Directly

### Generate Copy

```bash
curl -X POST http://localhost:8000/api/generate-copy \
  -F "image=@your-product.jpg" \
  -F "product_name=Test Product" \
  -F 'features=["Feature 1", "Feature 2", "Feature 3"]' \
  -F "tone=premium"
```

### View API Documentation

Visit: http://localhost:8000/docs

Interactive Swagger UI for testing all endpoints.

## Troubleshooting

### Issue: "OpenAI API Key not set"
**Solution**: Add your API key to `backend/.env`

### Issue: "Port already in use"
**Solution**: 
```bash
# Kill process on port 8000
lsof -ti:8000 | xargs kill -9

# Or change port in backend/main.py
uvicorn.run(app, host="0.0.0.0", port=8001)
```

### Issue: "Module not found"
**Solution**: 
```bash
# Reinstall dependencies
pip install -r requirements.txt
```

### Issue: Frontend can't connect to backend
**Solution**: Check CORS settings in `backend/main.py`

## Next Steps

1. **Add Social Media Credentials** (optional):
   - Edit `backend/.env`
   - Add LinkedIn, Facebook, Instagram tokens
   - Enable actual publishing

2. **Import N8N Workflow**:
   - Start N8N: `docker-compose up n8n`
   - Visit: http://localhost:5678
   - Import: `workflows/n8n_marketing_automation.json`

3. **Explore Features**:
   - Try different tones
   - Test various product types
   - Experiment with features

4. **Read Full Documentation**:
   - Architecture: README.md
   - Production tips: PRODUCTION_NOTES.md
   - API details: http://localhost:8000/docs

## Demo Video Script

1. Show homepage with clean UI
2. Upload product image (headphones)
3. Fill in product details
4. Click generate - show loading state
5. Review AI-generated headlines and captions
6. Select favorites
7. Approve and create creatives
8. Show platform-specific images
9. Publish and show success

## Common Use Cases

### E-commerce Products
- Fashion items
- Electronics
- Home goods
- Beauty products

### Services
- Software products
- Consulting services
- Courses/workshops
- Events

### Content Types
- Product launches
- Sales promotions
- Brand awareness
- Seasonal campaigns

## Performance Tips

- Use smaller images (< 2MB) for faster processing
- Cache common requests
- Use premium OpenAI tier for better speed
- Enable Redis caching for production

## Support

- Issues: [GitHub Issues](link)
- Documentation: README.md
- API Docs: http://localhost:8000/docs

---

**Happy Marketing! 🎉**