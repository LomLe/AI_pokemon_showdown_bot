import subprocess
import os
import time


class BotServer:
    def __init__(self, repo_url="https://github.com/smogon/pokemon-showdown.git", install_dir=None):
        self.repo_url = repo_url
        if install_dir is None:
            install_dir = os.path.join(os.path.dirname(__file__), "pokemon-showdown")
        self.install_dir = install_dir
        self.process = None

    def _check_node_npm(self):
        """Checks if Node.js and npm are installed."""
        try:
            subprocess.run(["node", "--version"], capture_output=True, check=True)
            subprocess.run(["npm", "--version"], capture_output=True, check=True)
            return True, None
        except (subprocess.CalledProcessError, FileNotFoundError):
            return False, "Node.js/npm not found. Install from https://nodejs.org/ or use 'brew install node'"

    def _has_dependencies(self):
        """Checks if critical dependencies are installed."""
        pg_path = os.path.join(self.install_dir, "node_modules", "pg")
        return os.path.exists(pg_path)

    def setup(self):
        """Clones the repo and installs dependencies if needed."""
        if not os.path.exists(self.install_dir):
            print(f"[Wrapper] Cloning Showdown to {self.install_dir}...")
            subprocess.run(["git", "clone", self.repo_url, self.install_dir], check=True)

        node_modules_path = os.path.join(self.install_dir, "node_modules")
        if not os.path.exists(node_modules_path):
            is_available, error_msg = self._check_node_npm()
            if not is_available:
                raise RuntimeError(error_msg)

            print("[Wrapper] Installing npm dependencies...")
            try:
                subprocess.run(["npm", "install"], cwd=self.install_dir, check=True, capture_output=True, text=True)
            except subprocess.CalledProcessError as e:
                error_output = e.stderr if e.stderr else e.stdout if e.stdout else str(e)
                raise RuntimeError(f"Failed to install dependencies:\n{error_output}") from e

        if not self._has_dependencies():
            raise RuntimeError("Missing dependencies. Run 'npm install' in the pokemon-showdown directory")

        config_path = os.path.join(self.install_dir, "config", "config.js")
        example_path = os.path.join(self.install_dir, "config", "config-example.js")
        if not os.path.exists(config_path) and os.path.exists(example_path):
            print("[Wrapper] Creating default config.js...")
            with open(example_path, 'r') as src, open(config_path, 'w') as dst:
                dst.write(src.read())
        
        # Configure settings for bot testing
        self._configure_settings(config_path)
    
    def _configure_settings(self, config_path):
        """Configures the Pokemon Showdown config file for bot testing."""
        if not os.path.exists(config_path):
            return
        
        settings = {'noguestsecurity': 'true', 'nothrottle': 'true'}
        
        try:
            with open(config_path, 'r') as f:
                content = f.read()
            
            modified = False
            for name, value in settings.items():
                pattern = f"exports.{name} ="
                old_pattern = f"{pattern} false"
                new_pattern = f"{pattern} {value};"
                
                if old_pattern in content.lower():
                    content = content.replace(f"{pattern} false", new_pattern, 1)
                    modified = True
            
            if modified:
                with open(config_path, 'w') as f:
                    f.write(content)
                print("[Wrapper] Bot testing settings configured.")
        except Exception as e:
            print(f"[Wrapper] Warning: Could not configure settings: {e}")

    def start(self):
        """Starts the Node.js server."""
        if self.process:
            print("[Wrapper] Server is already running.")
            return

        is_available, error_msg = self._check_node_npm()
        if not is_available:
            raise RuntimeError(error_msg)

        print("[Wrapper] Starting Pokemon Showdown Server...")
        self.process = subprocess.Popen(
            ["node", "pokemon-showdown"],
            cwd=self.install_dir,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )

        time.sleep(2)
        if self.process.poll() is not None:
            _, stderr = self.process.communicate()
            raise RuntimeError(f"Server failed to start:\n{stderr}")

        print("[Wrapper] Server started successfully.")

    def stop(self):
        """Stops the server."""
        if self.process:
            self.process.terminate()
            self.process.wait()
            self.process = None
            print("[Wrapper] Server stopped.")


if __name__ == "__main__":
    """Initalizes a Pokemon showdown server."""
    server = BotServer()

    try:
        server.setup()
        server.start()
        print("Server is running. Press Ctrl+C to stop.")
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nExiting...")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        server.stop()
