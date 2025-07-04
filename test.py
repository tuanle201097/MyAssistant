import os
import subprocess

base_dir = os.path.dirname(os.path.abspath(__file__))
nircmd_path = os.path.join(base_dir, 'nircmd-x64', 'nircmd.exe')

subprocess.run([nircmd_path, 'monitor', 'off'])
