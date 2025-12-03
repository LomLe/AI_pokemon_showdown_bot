#!/usr/bin/env python3

import subprocess
import os
from datetime import datetime

def read_html():
    """Read HTML from the first Pokemon Showdown tab."""

    script = '''
    tell application "Google Chrome"
        repeat with w from 1 to count of windows
            repeat with t from 1 to count of tabs of window w
                if URL of tab t of window w contains "pokemonshowdown.com" then
                    return execute tab t of window w javascript "document.documentElement.outerHTML"
                end if
            end repeat
        end repeat
    end tell
    '''

    try:
        result = subprocess.run(['osascript', '-e', script], 
                              capture_output=True, text=True, check=True)
        html = result.stdout.strip()
        print(f"✅ Read PSD HTML. Read {len(html)} characters.")
        return html
    except subprocess.CalledProcessError as e:
        print(f"❌ ERROR Reading PSD HTML. Error: {e.stderr if e.stderr else e}")
        return None


def html_to_file(html):
    """Export HTML content to a text file in the html_export folder."""
    if html is None:
        print("❌ Cannot export: HTML is None")
        return None
    
    # Create html_export directory if it doesn't exist
    export_dir = "html_export"
    os.makedirs(export_dir, exist_ok=True)
    
    # Generate filename with timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"psd_html_{timestamp}.txt"
    filepath = os.path.join(export_dir, filename)
    
    try:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(html)
        print(f"✅ Exported HTML to {filepath}")
        return filepath
    except Exception as e:
        print(f"❌ ERROR exporting HTML to file. Error: {e}")
        return None


if __name__ == "__main__":
    html = read_html()
    if html:
        html_to_file(html)
