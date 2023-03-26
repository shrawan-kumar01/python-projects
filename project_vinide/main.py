import os
import time

# create a function whicvh can find vinode in file and retur that file


def isBinod(file_name):
    with open(file_name, "r") as f:
        file_content = f.read()

        if "binod" in file_content.lower():
            return True
        else:
            return False


if __name__ == '__main__':
    dir_content = os.listdir()
    print(dir_content)
    nbinod = 0

    for item in dir_content:
        if item.endswith('txt'):
            print(f"detecting vinode in {item} \n\n")
            time.sleep(5)
            flag = isBinod(item)
            if (flag):
                print(f"binode is found in {item}\n\n")
                nbinod += 1
                time.sleep(5)

            else:
                print(f"vinode is not found in {item}\n\n")
               

    print("****************** binode finder summery ***************************")
    print(f"{time.sleep(1)}...{time.sleep(1)}.....{time.sleep(1)}....")
    print(f"{nbinod} file found with binode hidden into them ")