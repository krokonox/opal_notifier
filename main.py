import random

def generate_linux_command():
    commands = [
        'ls',
        'pwd',
        'cat file.txt',
        'grep "pattern" file.txt',
        'chmod 755 script.sh',
        'mkdir directory',
        'rm file.txt',
        'tar -czvf archive.tar.gz directory',
        'find . -name "*.txt"',
        'ssh user@hostname',
        'sudo apt-get update',
        'top',
        # Add more commands as desired
    ]
    return random.choice(commands)

def main():
    random_command = generate_linux_command()
    print("Random Linux Command:", random_command)

if __name__ == '__main__':
    main()
