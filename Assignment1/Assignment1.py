from cryptography.hazmat.primitives import hashes
import time


def hasher(istring, inum):  # hashing function to calculate the hex
    istring = bytes(istring + str(inum), "utf-8")
    digest = hashes.Hash(hashes.SHA256())
    digest.update(istring)
    v = digest.finalize()
    v = int.from_bytes(v, "big")
    return v


string = input("Enter string to be hashed:")
num = 0
target = int("0x00000FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF", 0)  # target value given in the task
start = time.time()
while True:
    if hasher(string, num) <= target:  # checking each nonce  value
        end = time.time()
        print("The nonce value for the  target: ",string + str(num))
        print("The time taken to find the nonce value: ",end - start)
        break
    num += 1
