# First assignment which is on linux
Q1 -> Step 1: Create a directory named `test_dir` ''' mkdir test_dir ''' 
   -> Step 2: Create an empty file named example.txt inside the directory ''' touch test_dir/example.txt'''
   -> Step 3: Rename example.txt to renamed_example.txt ''' mv test_dir/example.txt test_dir/renamed_example.txt

Q2 -> Step 1: Display complete contents of `/etc/passwd` ''' cat /etc/passwd ''' 
   -> Step 2: Display only the first 5 lines ''' head -n 5 /etc/passwd '''
   -> Step 3: Display only the last 5 lines ''' tail -n 5 /etc/passwd '''

Q3 -> Step 1: Find all lines containing the word "root" in `/etc/passwd` ''' grep "root" /etc/passwd '''

Q4 -> Step 1: Compress `test_dir` into `test_dir.zip` ''' zip -r test_dir.zip test_dir '''
   -> Step 2: Extract the zip file into a new directory named unzipped_dir ''' unzip test_dir.zip -d unzipped_dir '''

Q5 -> Step 1: Download a file from a URL ''' wget https://example.com/sample.txt '''

Q6 -> Step 1: Create a file named `secure.txt` ''' touch secure.txt '''
   -> Setp 2: Change permissions to read-only for everyone ''' chmod 444 secure.txt '''

Q7 -> Step 1: Set a new environment variable ''' export MY_VAR="Hello, Linux!" '''
   -> Step 2: Verify the variable value ''' echo $MY_VAR '''
