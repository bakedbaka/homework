import subprocess

required_apps = ['google-chrome', 'Microsoft', 'visual-studio-code']

for app in required_apps:
    try:
        subprocess.check_output(['which', app])
    except subprocess.CalledProcessError:
      
        if app == 'google-chrome':
            subprocess.run(['brew', 'install', 'google-chrome'])
        elif app == 'Microsoft':
            subprocess.run(['brew',  'install', 'git commit -m "Added new feature to myfile.py"microsoft-teams'])
        elif app == 'visual-studio-code':
            subprocess.run(['brew',  'install', 'visual-studio-code'])
            
            import subprocess

            def upload_to_github(file_path, commit_message):
                subprocess.run(['git', 'add', file_path])
                subprocess.run(['git', 'commit', '-m', commit_message])
                subprocess.run(['git', 'push'])

        
            upload_to_github('/path/to/file.txt', 'Added file.txt')
            

