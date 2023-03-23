import sys
import os
import zlib  

def main():
    # You can use print statements as follows for debugging, they'll be visible when running tests.
    print("Logs from your program will appear here!")

    # Uncomment this block to pass the first stage
    #
    command = sys.argv[1]
    if command == "init":
        os.mkdir(".git")
        os.mkdir(".git/objects")
        os.mkdir(".git/refs")
        with open(".git/HEAD", "w") as f:
            f.write("ref: refs/heads/master\n")
        print("Initialized git directory")
    else:
        raise RuntimeError(f"Unknown command #{command}")


compressed_data = open('.git/objects', 'rb').read()  
decompressed_data = zlib.decompress(compressed_data)  
print(decompressed_data)  

if __name__ == "__main__":
    main()
