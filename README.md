# ChecksumGen
ChecksumGen is a quick python script to generate a checksum of a given file and if
you choose compare it to a known value. Makes it easy for you todo that compare that
you would normally skip out on due to being too lazy.

Usage

The python script can be run as following:

python3 checksumGen.py -i /path/to/input -a [md5,sha1,sha256] -c checksumTo

-h to show a help command

-i for the file to generate a checksum of

-a for a type of checksum to generate

-c (optional) to provide a checksum to compare to
