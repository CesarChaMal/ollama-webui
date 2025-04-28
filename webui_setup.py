import os
import asyncio
import time
import requests
from dotenv import load_dotenv
from pyngrok import ngrok, conf

load_dotenv()

async def wait_for_backend(url, timeout=30):
    print(f"🛠️ Waiting for backend {url} to become ready...")
    start = time.time()
    while time.time() - start < timeout:
        try:
            response = requests.get(url)
            if response.status_code == 200:
                print("✅ Backend is up!")
                return True
        except requests.exceptions.RequestException:
            pass
        await asyncio.sleep(1)
    print("⚠️ Backend did not become ready in time.")
    return False

async def main():
    ngrok_token = os.getenv('NGROK_AUTHTOKEN')
    if not ngrok_token:
        print("NGROK_AUTHTOKEN is not set in .env!")
        return

    ngrok.set_auth_token(ngrok_token)

    # Save ngrok logs inside the project folder
    log_file_path = os.path.join(os.getcwd(), "ngrok.log")

    # Setup custom Pyngrok config to capture logs
    ngrok_config = conf.PyngrokConfig(
        log_event_callback=lambda event: open(log_file_path, "a").write(str(event) + "\n")
    )

    tunnel = ngrok.connect(8000, "http", pyngrok_config=ngrok_config)
    public_url = tunnel.public_url

    print(f"🌍 Your Public URL: {public_url}")

    with open(".env", "a") as f:
        f.write(f"\nNGROK_URL={public_url}\n")


    backend_ready = await wait_for_backend("http://localhost:8000")

    if backend_ready:
        os.system("curl http://localhost:11434 | pygmentize -l console || true")
        os.system("curl http://localhost:8000 | pygmentize -l console || true")
        os.system(f"curl {public_url} | pygmentize -l console || true")
    else:
        print("❌ Skipping curl commands because backend isn't responding.")

if __name__ == "__main__":
    asyncio.run(main())
