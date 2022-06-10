import hashlib, sys, getopt

def main(argv):
    inputfile = ''
    algorithm = ''
    comparedHash = ''
    try:
        opts, args = getopt.getopt(argv,"hi:a:c:")
    except getopt.GetoptError:
        print ("hasher.py -i <fileToHash> -a <hashAlgorithm> -c <givenHashToCompare>")
        sys.exit(2)
    #handle arguments
    for opt, arg in opts:
        if opt == '-h':
            print ('hasher.py -i <fileToHash> -a <hashAlogrithm> -c <givenhashToCompare>')
            sys.exit()
        elif opt in ("-i"):
            inputfile = arg
        elif opt in ("-a"):
            algorithm = arg
        elif opt in ("-c"):
            comparedHash = arg 
    #find the algorithm
    if algorithm == '':
        print("No hashing algorithm was provided")
        exit()
    elif algorithm != '':
        if algorithm == "md5":
            hasher = hashlib.md5()
        elif algorithm == "sha1":
            hasher = hashlib.sha1()
        elif algorithm == "sha256":
            hasher = hashlib.sha256()
        else:
            print("sorry we only support md5, sha1, and sha256 atm")
        with open(inputfile, 'rb') as afile:
            buffer = afile.read()
            hasher.update(buffer)
        print("Generated hash:", hasher.hexdigest())
        print("Provided hash: ", comparedHash)

        if comparedHash == hasher.hexdigest():
            print("The hashs match, you are good to go")
        else:
            print("Warning! the hashes do not match")

if __name__ == "__main__":
   main(sys.argv[1:])