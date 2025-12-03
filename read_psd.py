#!/usr/bin/env python3

import subprocess

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
        print(f"❌ ERROR Reading PSD HTML. Error: {e.stderr.decode() if e.stderr else e}")
        return None


if __name__ == "__main__":
    read_html()
