from dotenv import load_dotenv

# Loads .env file including API credential and other configurations.
retval = load_dotenv()

# if retval true, .env file is loaded with all configuration.
if retval:
    print(f"✅ Gemini API key setup complete.")
else:
    print("✅ Error in loading API key.")

from . import agent