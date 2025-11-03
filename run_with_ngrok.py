"""
Flask + ngrok runner script
Starts the Flask app and opens a public ngrok tunnel on port 5000
"""
from pyngrok import ngrok
import subprocess
import sys
import os

def main():
    try:
        # Start ngrok tunnel
        print("🚀 Starting ngrok tunnel on port 5000...")
        tunnel = ngrok.connect(5000, "http")
        public_url = tunnel.public_url
        
        print("\n" + "="*60)
        print(f"✅ Public URL: {public_url}")
        print("="*60 + "\n")
        print("📡 Your Flask app is now accessible from anywhere!")
        print("Press Ctrl+C to stop\n")
        
        # Start Flask app
        print("🔧 Starting Flask server...\n")
        flask_process = subprocess.Popen(
            [sys.executable, "flask.py"],
            cwd=os.path.dirname(os.path.abspath(__file__))
        )
        
        # Wait for Flask to run
        flask_process.wait()
        
    except KeyboardInterrupt:
        print("\n\n🛑 Shutting down...")
    except Exception as e:
        print(f"❌ Error: {e}")
    finally:
        # Cleanup
        if 'flask_process' in locals():
            flask_process.terminate()
            flask_process.wait()
        if 'tunnel' in locals():
            ngrok.disconnect(tunnel.public_url)
        ngrok.kill()
        print("✅ Cleanup complete")

if __name__ == '__main__':
    main()
