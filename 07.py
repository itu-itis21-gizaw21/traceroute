import subprocess

# Replace 'your_command_here' with the actual command you want to run
destinations = [
    'itu.edu.tr',
    'metu.edu.tr',
    'en.uoa.gr',
    'ed.ac.uk',
    'aau.edu.et',
    'pku.edu.cn',
    'sydney.edu.au',
    'nyu.edu',
    'stanford.edu',
    "ubc.ca"
]
command = 'traceroute ' + destinations[6]

# Run the command and capture the output
for i in range(1, 101):

    result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    # Check the result
  
    if result.returncode == 0:
        print("Command executed successfully")
        print("Output:", i,"for :", destinations[6])
        print(result.stdout)
    else:
        print(f"Command failed with error code {result.returncode}")
        print("Error Output:")
        print(result.stderr)
