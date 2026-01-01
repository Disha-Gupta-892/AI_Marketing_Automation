# AI-First Digital Marketing Automation System

A production-ready prototype for automating digital marketing workflows using AI agents, built with Python (FastAPI), React, and N8N integration.

## 🎯 Overview

This system automates the complete marketing workflow:
1. **Upload** product image + description
2. **Generate** AI-powered marketing copy (headlines + captions)
3. **Review** and approve content
4. **Create** platform-specific creatives (LinkedIn, Instagram, Facebook)
5. **Publish** to social media platforms

## 🏗️ Architecture

### Agent-Based Design (5 Agents)

```
┌─────────────────┐
│  Brief Agent    │ → Converts inputs to structured campaign brief
└────────┬────────┘
         ↓
┌─────────────────┐
│   Copy Agent    │ → Generates headlines + captions using GPT-4
└────────┬────────┘
         ↓
┌─────────────────┐
│ Creative Agent  │ → Designs text overlay layout & styling
└────────┬────────┘
         ↓
┌─────────────────┐
│  Resize Agent   │ → Creates platform-specific image variants
└────────┬────────┘
         ↓
┌─────────────────┐
│ Publisher Agent │ → Posts to social media platforms
└─────────────────┘
```

### Tech Stack

**Backend:**
- FastAPI (Python) - REST API server
- OpenAI GPT-4 - Copy generation
- Pillow - Image processing
- Pydantic - Data validation

**Frontend:**
- React - UI framework
- Tailwind CSS - Styling
- Lucide React - Icons

**Workflow Orchestration:**
- N8N - Workflow automation platform

**Social Media APIs:**
- LinkedIn API
- Facebook Graph API
- Instagram Graph API

## 📁 Project Structure

```
marketing-automation/
├── backend/
│   ├── main.py                 # FastAPI application
│   ├── agents/
│   │   ├── __init__.py
│   │   ├── brief_agent.py      # Agent 1: Brief creation
│   │   ├── copy_agent.py       # Agent 2: Copy generation
│   │   ├── creative_agent.py   # Agent 3: Layout design
│   │   ├── resize_agent.py     # Agent 4: Image resizing
│   │   └── publisher_agent.py  # Agent 5: Publishing
│   ├── utils/
│   │   ├── __init__.py
│   │   ├── logger.py           # Logging utility
│   │   └── storage.py          # Campaign storage
│   ├── requirements.txt
│   └── .env.example
├── frontend/
│   ├── src/
│   │   ├── App.jsx             # Main React component
│   │   └── index.js
│   ├── package.json
│   └── tailwind.config.js
├── workflows/
│   └── n8n_marketing_automation.json
├── uploads/                    # Uploaded images
├── outputs/                    # Generated creatives
├── logs/                       # Application logs
├── campaign_data/              # Campaign storage
├── README.md
└── PRODUCTION_NOTES.md
```

## 🚀 Installation & Setup

### Prerequisites

- Python 3.9+
- Node.js 16+
- OpenAI API key
- (Optional) Social media API credentials

### Backend Setup

1. **Clone repository**
```bash
git clone <repository-url>
cd marketing-automation/backend
```

2. **Create virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Configure environment variables**
```bash
cp .env.example .env
```

Edit `.env`:
```env
# Required
OPENAI_API_KEY=your_openai_api_key_here

# Optional - For actual publishing
LINKEDIN_ACCESS_TOKEN=your_linkedin_token
FACEBOOK_ACCESS_TOKEN=your_facebook_token
FACEBOOK_PAGE_ID=your_page_id
INSTAGRAM_ACCESS_TOKEN=your_instagram_token
INSTAGRAM_USER_ID=your_instagram_user_id
```

5. **Run backend server**
```bash
python main.py
```

Server runs on: `http://localhost:8000`

API documentation: `http://localhost:8000/docs`

### Frontend Setup

1. **Navigate to frontend directory**
```bash
cd ../frontend
```

2. **Install dependencies**
```bash
npm install
```

3. **Run development server**
```bash
npm start
```

Frontend runs on: `http://localhost:3000`

### N8N Workflow Setup

1. **Install N8N**
```bash
npm install -g n8n
```

2. **Start N8N**
```bash
n8n start
```

N8N runs on: `http://localhost:5678`

3. **Import workflow**
- Open N8N dashboard
- Click "Import from File"
- Select `workflows/n8n_marketing_automation.json`
- Activate workflow

## 📖 Usage

### Basic Workflow

1. **Upload Product**
   - Navigate to `http://localhost:3000`
   - Upload product image
   - Enter product name and 3-5 features
   - Select brand tone (premium, playful, minimal, luxury, professional)

2. **Generate Copy**
   - Click "Generate Marketing Copy"
   - AI generates 3 headline options
   - AI generates 2 caption options per platform (LinkedIn, Instagram, Facebook)

3. **Review & Approve**
   - Select preferred headline
   - Select preferred caption for each platform
   - Click "Approve & Create Creatives" or "Regenerate" if needed

4. **Preview Creatives**
   - View platform-specific creatives:
     - LinkedIn Landscape (1200×627)
     - Instagram Portrait (1080×1350)
     - Instagram Story (1080×1920)
     - Facebook Landscape (1200×630)

5. **Publish**
   - Click "Publish to Social Media"
   - Creatives posted to configured platforms
   - View publish status and URLs

### API Endpoints

**Generate Copy**
```bash
POST /api/generate-copy
Content-Type: multipart/form-data

Fields:
- image: File
- product_name: string
- features: JSON array
- tone: string
```

**Create Creatives**
```bash
POST /api/create-creatives
Content-Type: application/json

{
  "campaign_id": "uuid",
  "selected_headline": 0,
  "selected_captions": {
    "linkedin": 0,
    "instagram": 1,
    "facebook": 0
  }
}
```

**Publish**
```bash
POST /api/publish
Content-Type: application/json

{
  "campaign_id": "uuid",
  "platforms": ["linkedin", "facebook"]
}
```

**Get Campaign**
```bash
GET /api/campaign/{campaign_id}
```

**List Campaigns**
```bash
GET /api/campaigns
```

## 🔍 Agent Details

### 1. Brief Agent (`brief_agent.py`)
**Responsibility:** Convert raw inputs into structured campaign brief

**Input:**
- Product name
- Features list
- Brand tone
- Image path

**Output:**
```json
{
  "campaign_id": "uuid",
  "product": {
    "name": "Product Name",
    "features": ["Feature 1", "Feature 2"],
    "image_path": "path/to/image.jpg"
  },
  "brand": {
    "tone": "premium",
    "voice_attributes": {...}
  },
  "platforms": {...}
}
```

### 2. Copy Agent (`copy_agent.py`)
**Responsibility:** Generate marketing copy using GPT-4

**Features:**
- Generates 3 headline options (3-8 words)
- Generates 2 captions per platform
- Platform-optimized copy (LinkedIn professional, Instagram visual, Facebook engaging)
- Tone-aware generation
- Includes relevant hashtags

**AI Prompt Strategy:**
- Platform-specific instructions
- Tone alignment
- Character limits
- Hashtag requirements
- Call-to-action inclusion

### 3. Creative Agent (`creative_agent.py`)
**Responsibility:** Design text overlay layout and styling

**Features:**
- Analyzes image for optimal text placement
- Determines typography (font, size, weight)
- Calculates color scheme for readability
- Applies tone-specific styling
- Designs effects (shadows, outlines, backgrounds)

**Tone-Specific Styles:**
- **Premium:** Elegant, refined, sophisticated
- **Playful:** Fun, energetic, vibrant
- **Minimal:** Simple, clean, essential
- **Luxury:** Exclusive, prestigious
- **Professional:** Reliable, trustworthy

### 4. Resize Agent (`resize_agent.py`)
**Responsibility:** Create platform-specific image variants

**Features:**
- Smart cropping (maintains aspect ratio, focuses on center)
- Platform-specific dimensions
- Text overlay with readability enhancements
- Quality optimization

**Platform Sizes:**
- LinkedIn Landscape: 1200×627
- Instagram Portrait: 1080×1350
- Instagram Story: 1080×1920
- Facebook Landscape: 1200×630

### 5. Publisher Agent (`publisher_agent.py`)
**Responsibility:** Publish content to social media platforms

**Features:**
- Multi-platform support
- Demo mode (when API keys not configured)
- Error handling
- Publish status tracking

**Supported Platforms:**
- LinkedIn (via LinkedIn API)
- Facebook (via Graph API)
- Instagram (via Graph API)

## 🔐 Security & Configuration

### Environment Variables

Create `.env` file in backend directory:

```env
# Required
OPENAI_API_KEY=sk-...

# Optional - Social Media APIs
LINKEDIN_ACCESS_TOKEN=...
FACEBOOK_ACCESS_TOKEN=...
FACEBOOK_PAGE_ID=...
INSTAGRAM_ACCESS_TOKEN=...
INSTAGRAM_USER_ID=...

# Optional - Configuration
LOG_LEVEL=INFO
STORAGE_DIR=campaign_data
```

### API Key Setup

**OpenAI:**
1. Visit https://platform.openai.com/api-keys
2. Create new API key
3. Add to `.env`

**LinkedIn:**
1. Create app at https://www.linkedin.com/developers/
2. Get OAuth 2.0 token
3. Add to `.env`

**Facebook/Instagram:**
1. Create app at https://developers.facebook.com/
2. Get access token with required permissions
3. Add to `.env`

## 📊 Logging & Monitoring

### Log Locations
- Application logs: `logs/marketing_automation_YYYYMMDD.log`
- Agent decisions logged with timestamps
- API request/response logging
- Error tracking

### Log Format
```
2024-01-15 10:30:45 - BriefAgent - INFO - [BriefAgent] Created brief for campaign xyz-123
2024-01-15 10:30:50 - CopyAgent - INFO - [CopyAgent] Generated 3 headlines and 6 captions
```

## 🧪 Testing

### Manual Testing

1. **Test Copy Generation**
```bash
curl -X POST http://localhost:8000/api/generate-copy \
  -F "image=@product.jpg" \
  -F "product_name=Test Product" \
  -F 'features=["Feature 1", "Feature 2", "Feature 3"]' \
  -F "tone=premium"
```

2. **Test Creative Generation**
```bash
curl -X POST http://localhost:8000/api/create-creatives \
  -H "Content-Type: application/json" \
  -d '{
    "campaign_id": "your-campaign-id",
    "selected_headline": 0,
    "selected_captions": {
      "linkedin": 0,
      "instagram": 0,
      "facebook": 0
    }
  }'
```

## 🚨 Troubleshooting

### Common Issues

**Issue:** OpenAI API errors
**Solution:** Check API key validity and account credits

**Issue:** Image processing fails
**Solution:** Ensure Pillow is installed correctly and image format is supported

**Issue:** Frontend can't connect to backend
**Solution:** Verify CORS settings and backend URL in frontend

**Issue:** Social media posting fails
**Solution:** Check API credentials and permissions

## 📈 Performance Considerations

- **AI Generation:** ~5-10 seconds per request
- **Image Processing:** ~2-3 seconds per variant
- **Total Workflow:** ~20-30 seconds end-to-end

### Optimization Tips
- Cache common requests
- Use async processing for multiple platforms
- Optimize image sizes before processing
- Implement request queuing for high volume

## 🔄 N8N Workflow Integration

The N8N workflow orchestrates the entire pipeline:

1. **Webhook Trigger** - Receives campaign data
2. **Extract Data** - Processes input
3. **Agent Calls** - Sequential agent execution
4. **Error Handling** - Catches and logs errors
5. **Notifications** - Slack alerts on completion

**Workflow Features:**
- Automatic retry on failure
- Error logging and notifications
- Campaign tracking
- Status updates

## 📝 Production Deployment Notes

See `PRODUCTION_NOTES.md` for:
- Scalability improvements
- Database integration
- Queue management
- Monitoring setup
- Security hardening
- Cost optimization

## 🤝 Contributing

1. Fork the repository
2. Create feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open Pull Request

## 📄 License

This project is licensed under the MIT License.

## 🙋 Support

For issues and questions:
- Create GitHub issue
- Email: support@example.com
- Documentation: [docs link]

## 🎉 Acknowledgments

- OpenAI for GPT-4 API
- FastAPI framework
- React community
- N8N platform