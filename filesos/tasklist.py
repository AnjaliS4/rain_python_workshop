
# is also used for hacking

import subprocess
import os
def list_running_processes(output_file):
    try:
        #Execute the system command to list processes
        command = ['tasklist'] if os.name == 'nt' else ['ps', 'aux']
        result = subprocess.run(command, capture_output = True, text = True)

        # save the output to a file 
        with open(output_file, 'w') as file:
            file.write(result.stdout)
        print(f"Process list saved to '{output_file}'")
    except Exception as e:
        print(f"Error: {e}")

# Example Usuage 
list_running_processes("process_list.txt")