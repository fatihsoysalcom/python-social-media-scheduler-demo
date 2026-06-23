import threading
import time
from datetime import datetime, timedelta

def post_to_social_media(platform: str, message: str):
    """
    Simulates posting a message to a social media platform.
    In a real application, this would involve an API call to the specific platform
    (e.g., Twitter API, LinkedIn API) with proper authentication.
    """
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{current_time}] Posting to {platform}: '{message}'")

def schedule_social_post(platform: str, message: str, delay_seconds: int):
    """
    Schedules a social media post to be published after a specified delay.
    This function demonstrates the core concept of a social media scheduler API
    by using a background timer to execute the 'post' function at a future time.
    """
    scheduled_time = datetime.now() + timedelta(seconds=delay_seconds)
    print(f"[{datetime.now().strftime('%H:%M:%S')}] Scheduling post for {platform} at {scheduled_time.strftime('%H:%M:%S')} (in {delay_seconds} seconds)...")

    # Use threading.Timer to execute the post_to_social_media function after the delay.
    # This simulates a background task that a real social media scheduler API would manage.
    timer = threading.Timer(delay_seconds, post_to_social_media, args=(platform, message))
    timer.start()

if __name__ == "__main__":
    print("--- Social Media Post Scheduler Demo ---")
    print("This script simulates scheduling posts using a simple API-like interface.")
    print("Posts will appear after their scheduled delay.")
    print("-" * 40)

    # Schedule a post for Twitter in 3 seconds
    schedule_social_post("Twitter", "Hello from my automated scheduler! #API #Automation", 3)

    # Schedule another post for LinkedIn in 5 seconds
    schedule_social_post("LinkedIn", "Excited to share insights on API-driven social media management.", 5)

    # Schedule a third post for Instagram in 7 seconds
    schedule_social_post("Instagram", "New content coming soon! Stay tuned. #SocialMedia", 7)

    # Keep the main thread alive long enough for the timers to execute.
    # In a real application, you might have a persistent server or a more robust thread management system.
    # For this demo, we'll just wait a bit longer than the longest scheduled post to ensure all timers fire.
    max_delay = 7
    print(f"\n[{datetime.now().strftime('%H:%M:%S')}] All posts scheduled. Waiting for {max_delay + 2} seconds for execution...")
    time.sleep(max_delay + 2) # Wait a bit more than the longest delay

    print("\n--- Demo Finished ---")
