# AI-First Marketing Automation - Environment Configuration

# ============================================================================
# REQUIRED CONFIGURATION
# ============================================================================

# OpenAI API Key (Required for copy generation)
# Get your key from: https://platform.openai.com/api-keys
OPENAI_API_KEY=sk-your-openai-api-key-here

# ============================================================================
# OPTIONAL - SOCIAL MEDIA API CREDENTIALS
# ============================================================================

# LinkedIn API
# Setup: https://www.linkedin.com/developers/
LINKEDIN_ACCESS_TOKEN=your-linkedin-access-token
LINKEDIN_PERSON_URN=urn:li:person:your-person-id

# Facebook API
# Setup: https://developers.facebook.com/
FACEBOOK_ACCESS_TOKEN=your-facebook-access-token
FACEBOOK_PAGE_ID=your-facebook-page-id

# Instagram API (uses Facebook Graph API)
# Setup: https://developers.facebook.com/docs/instagram-api
INSTAGRAM_ACCESS_TOKEN=your-instagram-access-token
INSTAGRAM_USER_ID=your-instagram-business-account-id

# ============================================================================
# APPLICATION CONFIGURATION
# ============================================================================

# Server Configuration
HOST=0.0.0.0
PORT=8000
DEBUG=False
LOG_LEVEL=INFO

# Storage
STORAGE_DIR=campaign_data
UPLOAD_DIR=uploads
OUTPUT_DIR=outputs

# AI Model Configuration
OPENAI_MODEL=gpt-4-turbo-preview
OPENAI_TEMPERATURE=0.8
MAX_TOKENS=1000

# Image Processing
IMAGE_MAX_SIZE=10485760  # 10MB in bytes
ALLOWED_EXTENSIONS=jpg,jpeg,png,webp
IMAGE_QUALITY=95

# Rate Limiting
RATE_LIMIT_PER_MINUTE=10
RATE_LIMIT_PER_HOUR=100

# ============================================================================
# OPTIONAL - ADVANCED FEATURES
# ============================================================================

# Database (if using PostgreSQL instead of file storage)
# DATABASE_URL=postgresql://user:password@localhost:5432/marketing_automation

# Redis (for caching and queue)
# REDIS_URL=redis://localhost:6379/0

# Sentry (for error tracking)
# SENTRY_DSN=https://your-sentry-dsn

# AWS S3 (for cloud storage)
# AWS_ACCESS_KEY_ID=your-aws-access-key
# AWS_SECRET_ACCESS_KEY=your-aws-secret-key
# S3_BUCKET_NAME=your-bucket-name
# S3_REGION=us-east-1

# Email Notifications
# SMTP_HOST=smtp.gmail.com
# SMTP_PORT=587
# SMTP_USER=your-email@gmail.com
# SMTP_PASSWORD=your-app-password
# NOTIFICATION_EMAIL=notifications@yourcompany.com

# Slack Notifications
# SLACK_WEBHOOK_URL=https://hooks.slack.com/services/your/webhook/url

# ============================================================================
# SECURITY
# ============================================================================

# JWT Secret (generate with: openssl rand -hex 32)
# JWT_SECRET_KEY=your-secret-key-here
# JWT_ALGORITHM=HS256
# ACCESS_TOKEN_EXPIRE_MINUTES=30

# CORS Origins (comma-separated)
CORS_ORIGINS=http://localhost:3000,http://localhost:5173

# ============================================================================
# NOTES
# ============================================================================

# 1. Copy this file to .env and fill in your actual values
# 2. NEVER commit .env file to version control
# 3. OpenAI API key is REQUIRED for the application to work
# 4. Social media credentials are optional - demo mode will be used without them
# 5. Generate secure random strings for JWT_SECRET_KEY in production