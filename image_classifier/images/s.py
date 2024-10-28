
from supabase import create_client, Client
import os


# Initialize Supabase client (adjust with your actual URL and key)
SUPABASE_URL = os.getenv("SUPABASE_URL", "url")
SUPABASE_KEY = os.getenv("SUPABASE_KEY", "key")

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)
#user = supabase.auth.sign_up({ "email": 'vamshigaddi.da@gmail.com', "password": 'Bruslee555555'})
user = supabase.auth.sign_in_with_password({ "email": 'vamshigaddi18@gmail.com', "password": 'Bruslee5'})

data = supabase.auth.get_user()
print(data)
