#!/usr/bin/env python3
"""Simple script to detect if Pokemon Showdown is running in Chrome."""

import subprocess


def get_chrome_urls():
    """Get all URLs from all Chrome tabs."""
    script = '''
    tell application "Google Chrome"
        set urlList to {}
        repeat with w in windows
            repeat with t in tabs of w
                set end of urlList to URL of t
            end repeat
        end repeat
        return urlList
    end tell
    '''
    try:
        result = subprocess.run(
            ['osascript', '-e', script],
            capture_output=True,
            text=True,
            check=True
        )
        return result.stdout.strip()
    except subprocess.CalledProcessError:
        return None

def detect_psd():
    """Detect Pokemon Showdown URLs from all Chrome tabs."""
    print("Pokemon Showdown Detection\n")
    
    # Check Chrome accessibility
    try:
        subprocess.run(
            ['osascript', '-e', 'tell application "Google Chrome" to get name'],
            capture_output=True,
            check=True
        )
    except subprocess.CalledProcessError:
        print("❌ Cannot access Chrome")
        print("   Enable Terminal Automation permissions in System Settings")
        return
    
    # Get all URLs
    all_urls = get_chrome_urls()
    if not all_urls:
        print("❌ No tabs found")
        return
    
    urls = all_urls.split(", ")
    print(f"Found {len(urls)} tab(s):")
    for i, url in enumerate(urls, 1):
        print(f"  {i}. {url}")
    
    # Detect Pokemon Showdown
    found = [url for url in urls if "pokemonshowdown.com" in url.lower()]
    if found:
        print(f"\n✅ Found {len(found)} Pokemon Showdown URL(s):")
        for url in found:
            print(f"   {url}")
    else:
        print("\n❌ No Pokemon Showdown URLs found")


if __name__ == "__main__":
    detect_psd()
