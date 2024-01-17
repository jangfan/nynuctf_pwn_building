import time
import random
import string
import yaml
import subprocess

def generate_flag():
    timestamp = int(time.time())
    random_part = ''.join(random.choices(string.ascii_letters + string.digits, k=24))
    flag = f'nynuctf{{{random_part[:8]}-{random_part[8:16]}-{random_part[16:24]}}}'
    
    return flag

def write_to_file(flag):
    with open('docker-compose.yaml', 'r') as file:
        compose_data = yaml.safe_load(file)
    compose_data['services']['pwn']['environment']['FLAG'] = flag
    with open('docker-compose.yaml', 'w') as file:
        yaml.dump(compose_data, file)

def run_build_script():
    try:
        subprocess.run(['./build_image.sh'], check=True)
        print("Build script executed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error executing build script: {e}")        


if __name__ == "__main__":
    generated_flag = generate_flag()
    print("Generated Flag:", generated_flag)
    write_to_file(generated_flag)
    print("Flag has been written to Environment variables")
    run_build_script()




    

