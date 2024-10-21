
from supabase import create_client, Client
import os


# Initialize Supabase client (adjust with your actual URL and key)
SUPABASE_URL = os.getenv("SUPABASE_URL", "https://rdhasvphabwzstdfiwkz.supabase.co")
SUPABASE_KEY = os.getenv("SUPABASE_KEY", "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InJkaGFzdnBoYWJ3enN0ZGZpd2t6Iiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTcyMzU0MzAwOSwiZXhwIjoyMDM5MTE5MDA5fQ.7toLAIqt65kMV-xs6_e7upBrvmEckNpiHgipMLmX8do")

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)
#user = supabase.auth.sign_up({ "email": 'vamshigaddi.da@gmail.com', "password": 'Bruslee555555'})
user = supabase.auth.sign_in_with_password({ "email": 'vamshigaddi18@gmail.com', "password": 'Bruslee5'})

data = supabase.auth.get_user()
print(data)
