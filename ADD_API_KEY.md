# How to Add Your OpenAI API Key

## Quick Steps

1. **Open the `.env` file** in the `backend` directory:
   - Location: `backend/.env`
   - You can use any text editor (Notepad, VS Code, etc.)

2. **Find this line**:
   ```
   OPENAI_API_KEY=sk-your-openai-api-key-here
   ```

3. **Replace the placeholder** with your actual OpenAI API key:
   ```
   OPENAI_API_KEY=sk-your-actual-api-key-here
   ```

4. **Save the file**

5. **Restart the backend server** (if it's running)

## Get Your API Key

If you don't have an API key yet:
1. Go to https://platform.openai.com/api-keys
2. Sign in or create an account
3. Click "Create new secret key"
4. Copy the key (it starts with `sk-`)
5. Paste it in the `.env` file as shown above

## Security Note

⚠️ **Never commit your `.env` file to version control!**
- The `.gitignore` file already excludes `.env` files
- Keep your API key private and secure
- Don't share it publicly

## After Adding the Key

Once you've added your API key, the backend server needs to be restarted to pick up the new environment variable.

