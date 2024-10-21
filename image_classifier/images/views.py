from django.http import JsonResponse
import os 
from django.contrib import messages
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.conf import settings
from minio import Minio
from .models import ImageDirectory
import json
from django.http import HttpResponseRedirect
from supabase import create_client, Client
from gotrue.errors import AuthApiError

# Initialize Supabase client (adjust with your actual URL and key)
SUPABASE_URL = os.getenv("SUPABASE_URL", "https://rdhasvphabwzstdfiwkz.supabase.co")
SUPABASE_KEY = os.getenv("SUPABASE_KEY", "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InJkaGFzdnBoYWJ3enN0ZGZpd2t6Iiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTcyMzU0MzAwOSwiZXhwIjoyMDM5MTE5MDA5fQ.7toLAIqt65kMV-xs6_e7upBrvmEckNpiHgipMLmX8do")

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        action = request.POST.get('action')
        name = request.POST.get('name')
        repeat_password = request.POST.get('repeat_password')

        print(f"Received POST request with data: email={email}, action={action}, name={name}")

        if action == 'signup':
            if password != repeat_password:
                return JsonResponse({'status': 'error', 'message': 'Passwords do not match.'})

            try:
                response = supabase.auth.sign_up({
                    "email": email,
                    "password": password,
                    "data": {"name": name}
                })

                if 'error' in response:
                    print(f"Sign-up error: {response['error']}")  # Print detailed error
                    return JsonResponse({'status': 'error', 'message': response['error']['message']})

                return JsonResponse({'status': 'success', 'message': 'Registration successful. Please check your email for confirmation.'})

            except Exception as e:
                print(f"Exception during sign-up: {e}")  # Print detailed exception
                if "Email rate limit exceeded" in str(e):
                    return JsonResponse({'status': 'error', 'message': 'Too many attempts. Please try again later.'})
                return JsonResponse({'status': 'error', 'message': 'An error occurred during signup. Please try again.'})

        if action == 'signin':
            try:
                response = supabase.auth.sign_in_with_password({
                    "email": email,
                    "password": password
                })

                if 'error' in response:
                    print(f"Sign-in error: {response['error']}")  # Print detailed error
                    error_message = response['error']['message']
                    if "Invalid login credentials" in error_message:
                        return JsonResponse({'status': 'error', 'message': 'Incorrect password.'})
                    elif "User not found" in error_message:
                        return JsonResponse({'status': 'error', 'message': 'Invalid email. Please sign up first.'})
                    else:
                        return JsonResponse({'status': 'error', 'message': error_message})

                # Successful login
                if response.session:
                    request.session['user'] = response.session.user.id
                    return JsonResponse({'status': 'success', 'redirect': '/'})

                return JsonResponse({'status': 'error', 'message': 'Failed to retrieve user ID. Please try again.'})

            except Exception as e:
                print(f"Exception during sign-in: {e}")  # Print detailed exception
                if "Email rate limit exceeded" in str(e):
                    return JsonResponse({'status': 'error', 'message': 'Too many attempts. Please try again later.'})
                return JsonResponse({'status': 'error', 'message': 'Invalid credentials. Please try again.'})

    # Handle GET requests and other methods
    return render(request, 'login.html')



def home(request):
    # Retrieve the current session
    try:
        session = supabase.auth.get_session()
        #user_id = session.get('user', {}).get('id')

        if session:
            return render(request, 'home.html')
        else:
            return redirect('login_view')  # Redirect to login if not authenticated
    except Exception as e:
        print(f"Error retrieving session: {e}")
        return redirect('login_view')  # Redirect to login if there's an error


    
def upload_images(request):
    if request.method == 'POST':
        if 'directory' in request.FILES:
            zip_file = request.FILES['directory']
            
            # Save the uploaded ZIP file
            temp_dir = os.path.join(settings.MEDIA_ROOT, 'temp_upload')
            os.makedirs(temp_dir, exist_ok=True)
            zip_path = os.path.join(temp_dir, zip_file.name)
            with open(zip_path, 'wb+') as destination:
                for chunk in zip_file.chunks():
                    destination.write(chunk)
            
            # Set up MinIO client
            eos_client = Minio(
                'objectstore.e2enetworks.net',
                access_key='URYEJ1JIYS528KSR9OU2',
                secret_key='KU3RNZM7HWRV1R0HD13XIFG8LPFHYR1314OAA9WP',
                secure=True
            )
            
            bucket_folder = 'ipcam'
            directory_name = os.path.basename(zip_path).split('.')[0]

            # Upload the ZIP file to cloud storage
            def upload_bucket(file_path):
                filename = os.path.basename(file_path)
                destination = f"{bucket_folder}/{filename}"
                with open(file_path, 'rb') as file_data:
                    file_stat = os.stat(file_path)
                    eos_client.put_object('gis-storage', destination, file_data, file_stat.st_size)
                return f"https://gis-storage.objectstore.e2enetworks.net/{bucket_folder}/{filename}"
            
            # Upload the ZIP file and update database
            file_url = upload_bucket(zip_path)
            ImageDirectory.objects.update_or_create(name=directory_name, defaults={'url': file_url})
            
            # Clean up temporary directory
            os.remove(zip_path)  # Remove the uploaded ZIP file
            
            return HttpResponse('Success')

    return render(request, 'upload.html')


# def check_status(request):
#     context = {}
#     if request.method == "POST":
#         folder_name = request.POST.get('folder_name')
#         if folder_name:
#             try:
#                 # Query the database for the folder name
#                 record = ImageDirectory.objects.get(name=folder_name)
#                 context = {
#                     'folder_name': folder_name,
#                     'url': record.url,
#                     'status': record.status,
#                     'results': record.results
#                 }
#             except ImageDirectory.DoesNotExist:
#                 context['error'] = "Folder name not found."
    
#     return render(request, 'check_status.html', context)


# def check_status(request):
#     if request.method == "GET":  # Ensure the method is GET
#         # Retrieve all records from the ImageDirectory model
#         directories = ImageDirectory.objects.all()
        
#         # Prepare the context with the retrieved data
#         context = {'directories': directories}
        
#         # Render the template with the context data
#         return render(request, 'check_status.html', context)
#     else:
#         # Handle other request methods if necessary
#         return render(request, 'check_status.html', {'error': 'Invalid request method'})
 


def check_status(request):
    if request.method == "GET":  # Ensure the method is GET
        # Retrieve all records from the ImageDirectory model
        directories = ImageDirectory.objects.all()
        
        # Prepare the context with the retrieved data
        directories_list = []
        for directory in directories:
            results = directory.results
            if results:
                results = json.loads(results)  # Convert JSON string back to a dictionary or list
            directories_list.append({
                'id': directory.id,
                'name': directory.name,
                'url': directory.url,
                'status': directory.status,
                'results': results,
            })
        
        # Prepare the context with the processed data
        context = {'directories': directories_list}
        
        # Render the template with the context data
        return render(request, 'check_status.html', context)
    else:
        # Handle other request methods if necessary
        return render(request, 'check_status.html', {'error': 'Invalid request method'})


# def home(request):
#     if 'user' not in request.session:
#         return redirect('login')  # Redirect to login if not authenticated

#     return render(request, 'home.html')
























# import os
# import zipfile
# import shutil
# from django.conf import settings
# from django.http import HttpResponse
# from django.shortcuts import render

# def upload_images(request):
#     if request.method == 'POST':
#         if 'directory' in request.FILES:
#             zip_file = request.FILES['directory']
            
#             # Create a temporary directory for extraction
#             temp_dir = os.path.join(settings.MEDIA_ROOT, 'temp_upload')
#             os.makedirs(temp_dir, exist_ok=True)
            
#             # Save the uploaded ZIP file
#             zip_path = os.path.join(temp_dir, zip_file.name)
#             with open(zip_path, 'wb+') as destination:
#                 for chunk in zip_file.chunks():
#                     destination.write(chunk)
            
#             # Extract the ZIP file
#             with zipfile.ZipFile(zip_path, 'r') as zip_ref:
#                 zip_ref.extractall(temp_dir)
            
#             # Move extracted files to the media directory
#             extracted_files = os.listdir(temp_dir)
#             for item in extracted_files:
#                 s = os.path.join(temp_dir, item)
#                 d = os.path.join(settings.MEDIA_ROOT, item)
#                 if os.path.isdir(s):
#                     shutil.move(s, d)
#                 else:
#                     shutil.move(s, d)
            
#             # Clean up the temporary directory
#             shutil.rmtree(temp_dir)
            
#             return HttpResponse('Files uploaded and extracted successfully.')
    
#     return render(request, 'upload.html')
