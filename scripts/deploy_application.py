```python
import os
import subprocess

def main():
    print("Starting deployment process...")
    
    # Set up environment variables
    os.environ['FLASK_APP'] = 'backend/app.py'
    os.environ['FLASK_ENV'] = 'production'
    
    # Install backend dependencies
    print("Installing backend dependencies...")
    subprocess.run(["pip", "install", "-r", "backend/requirements.txt"], check=True)
    
    # Run database migrations
    print("Running database migrations...")
    subprocess.run(["python", "scripts/setup_database.py"], check=True)
    
    # Install frontend dependencies
    print("Installing frontend dependencies...")
    os.chdir('frontend')
    subprocess.run(["npm", "install"], check=True)
    
    # Build frontend
    print("Building frontend...")
    subprocess.run(["npm", "run", "build"], check=True)
    os.chdir('..')
    
    # Start backend server
    print("Starting backend server...")
    subprocess.Popen(["flask", "run"])
    
    # Serve frontend build
    print("Serving frontend build...")
    subprocess.run(["npx", "serve", "-s", "frontend/build"], check=True)
    
    print("Deployment complete. Application is now live.")

if __name__ == "__main__":
    main()
```