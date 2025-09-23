import random
from datetime import datetime
from sys import argv

tday = str(datetime.today())

format = "%Y-%m-%d %H:%M:%S.%f"

strp = datetime.strptime(tday, format)
#print(strp.microsecond)

ts = int(strp.timestamp())
#print(ts)
random.seed(strp.microsecond + ts)
print(f"SEED: {strp.microsecond + ts}")


def main():
    print("This is a password generator(PassGen) that can generate passwords based on your specifications!")
    print("""
    Enter 1 to generate passwd mixed of: Special Characters, Numbers, and Regular Characters
    Enter 2 to generate passwd mixed of: Numbers and Regular Characters
    Enter 3 to generate passwd mixed of: Special Charcaters and Regular Characters
    Enter 4 to generate passwd mixed of: Special Characters and Numbers
    Enter 5 to generate passwd mixed of: Just Numbers
    Enter 6 to generate passwd mixed of: Just Special Characters
    Enter 7 to generate passwd mixed of: Just Regular Characters
    Enter 8 to specify a length for your password (default is random length between 8 and 32 characters)
    Enter 9 to choose a random password from your list of generated passwords
    
    
    Enter 0 to specify an output file to store the generated passwords(such as: passwords.txt)
    """)
    curr_generated_pwds = []
    user_input = input()
    
    length_of_pwd = 0
    
    out_file_specified = False
    
    while True:
        match user_input:
            case "1":
                p = pw_generator(numbers=True, chars=True, specials=True, pass_len=length_of_pwd)
                curr_generated_pwds.append(p) 
            case "2":
                p = pw_generator(numbers=True, chars=True, specials=False, pass_len=length_of_pwd)
                curr_generated_pwds.append(p) 
            case "3":
                p = pw_generator(numbers=False, chars=True, specials=True, pass_len=length_of_pwd)
                curr_generated_pwds.append(p) 
            case "4":
                p = pw_generator(numbers=True, chars=False, specials=True, pass_len=length_of_pwd)
                curr_generated_pwds.append(p) 
            case "5":
                p = pw_generator(numbers=True, chars=False, specials=False, pass_len=length_of_pwd)
                curr_generated_pwds.append(p) 
            case "6":
                p = pw_generator(numbers=False, chars=False, specials=True, pass_len=length_of_pwd)
                curr_generated_pwds.append(p) 
            case "7":
                p = pw_generator(numbers=False, chars=True, specials=False, pass_len=length_of_pwd) 
                curr_generated_pwds.append(p)
            case "8":
                length_of_pwd = int(input("Enter the number of characters you want your password to be(Enter 0 for default):\n"))
            case "9":
                if len(curr_generated_pwds) == 0:
                    print("You haven't generated any passwords yet!")
            case "0":
                out_file_specified = True
                user_file = input("Enter the name of the file you want to output your generated passwords to:\n")
                print(f"Your generated passwords will be outputted to {user_file}")
            case _:
                print("You didn't choose an option!")
        print("Here are your Current Generated Passwords:\n")
        for i in curr_generated_pwds:
            print(f"{i}", end="\t|\t")
        print("\n")
        print(f"Here is a random password from your list of generated passwords, if you're undecisive(press 8 to refresh): {random.choice(curr_generated_pwds) if len(curr_generated_pwds) > 0 else 'No passwords generated yet!'}")
        print("\n")
        print("If you want to generate another password please select an option like before otherwise enter -1:")
        print("""
        Enter 1 to generate passwd mixed of: Special Characters, Numbers, and Regular Characters
        Enter 2 to generate passwd mixed of: Numbers and Regular Characters
        Enter 3 to generate passwd mixed of: Special Charcaters and Regular Characters
        Enter 4 to generate passwd mixed of: Special Characters and Numbers
        Enter 5 to generate passwd mixed of: Just Numbers
        Enter 6 to generate passwd mixed of: Just Special Characters
        Enter 7 to generate passwd mixed of: Just Regular Characters
        Enter 8 to specify a length for your password (default is random length between 8 and 32 characters)
        Enter 9 to choose a random password from your list of generated passwords
        Enter -1 to exit the program
        
        
        Enter 0 to specify an output file to store the generated passwords(such as: passwords.txt)
        """)
        user_input = input()
        #try:
        #    length_of_pwd = int(input("Enter the number of characters you want your password to be (choose 0 for default settings(min length of 8)):\n"))
        #except ValueError:
        #    print("You didn't enter a valid number, defaulting to random length between 8 and 32 characters")
        #    length_of_pwd = int(input())
            
        
        if user_input == "-1":
            if out_file_specified:
                write_to_file(user_file, curr_generated_pwds)
                print(f"Your generated passwords have been written to {user_file}")
            break
        

#WRITE TO FILE FUNCTION
# file_name: name of the file to write to   
# passwords: list of passwords to write to the file               
def write_to_file(file_name, passwords):
    with open(file_name, '+a') as uf:
        for i in passwords:
            uf.write(i+"\n")    
        
    
#GENERATOR FUNCTION
# numbers: include numbers in the password
# chars: include regular characters in the password
# specials: include special characters in the password
#RETURN: generated password
def pw_generator(numbers=True, chars=True, specials=True, pass_len=None):
    
    SPEC_CHARS = '!@#$%^&*()_-=+\\|]}[{\'";:/?.>,<`~'
    CHARS ="qwertyuioplkmjnhbgvfcdxsza"
    NUMS = "1234567890"
    
    pw_length = random.randint(8, 32) if pass_len == 0 else pass_len
    generated_pw = ""
    if numbers and chars and specials:
        for i in range(pw_length):
            r = random.randint(1, 4)
            match r:
                case 1:
                    generated_pw += CHARS[random.randint(0, len(CHARS)-1)]
                case 2:
                    generated_pw += NUMS[random.randint(0, len(NUMS)-1)]
                case 3:
                    generated_pw += SPEC_CHARS[random.randint(0, len(SPEC_CHARS)-1)]
                case 4:
                    generated_pw += CHARS[random.randint(0, len(CHARS)-1)].upper()
                    
                    
    elif numbers and chars and not specials:
        for i in range(pw_length):
            r = random.randint(1, 3)
            match r:
                case 1:
                    generated_pw += CHARS[random.randint(0, len(CHARS)-1)]
                case 2:
                    generated_pw += NUMS[random.randint(0, len(NUMS)-1)]
                case 3:
                    generated_pw += CHARS[random.randint(0, len(CHARS)-1)].upper()
                    
                    
    elif not numbers and chars and specials:
        for i in range(pw_length):
            r = random.randint(1, 3)
            match r:
                case 1:
                    generated_pw += CHARS[random.randint(0, len(CHARS)-1)]
                case 2:
                    generated_pw += SPEC_CHARS[random.randint(0, len(SPEC_CHARS)-1)]
                case 3:
                    generated_pw += CHARS[random.randint(0, len(CHARS)-1)].upper()
                    
                    
    elif numbers and not chars and specials:
        for i in range(pw_length):
            r = random.randint(1, 2)
            match r:
                case 1:
                    generated_pw += NUMS[random.randint(0, len(NUMS)-1)]
                case 2:
                    generated_pw += SPEC_CHARS[random.randint(0, len(SPEC_CHARS)-1)]
    
    
    elif not numbers and chars and not specials:
        for i in range(pw_length):
            r = random.randint(1, 2)
            match r:
                case 1:
                    #temp_check = CHARS[random.randint(0, len(CHARS)-1)]
                    #if (temp_check == "\\" or temp_check == "\"" or temp_check =="\'"): # NOTE: Here we're checking for escape characters so we can parse them and include them in the out file
                    #    pass
                    generated_pw += CHARS[random.randint(0, len(CHARS)-1)]
                case 2:
                    generated_pw += CHARS[random.randint(0, len(CHARS)-1)].upper()
            
    elif not numbers and not chars and specials:
        for i in range(pw_length):
            generated_pw += SPEC_CHARS[random.randint(0, len(SPEC_CHARS)-1)]       
                    
    elif numbers and not chars and not specials:
        for i in range(pw_length):
            generated_pw += NUMS[random.randint(0, len(NUMS)-1)]          
    print(f"GENERATED PASSWORD:   {generated_pw}")    
    return generated_pw
                
if __name__ == "__main__":  
    if len(argv) > 1 and argv[1] == "--test":
        print("Running in test mode")
        for i in range(10):
            print(f"ITERATION(TEST): {i+1}")
            print("All options enabled:")
            pw_generator(numbers=True, chars=True, specials=True)
            print("\n")
            print("Two options enabled:")
            print("No Specials:")
            pw_generator(numbers=True, chars=True, specials=False)
            print("No Numbers:")
            pw_generator(numbers=False, chars=True, specials=True)
            print("No Chars:")
            pw_generator(numbers=True, chars=False, specials=True)
            print("\n")
            print("One option enabled:")
            print("Just Numbers:")
            pw_generator(numbers=True, chars=False, specials=False)
            print("Just Specials:")
            pw_generator(numbers=False, chars=False, specials=True)
            print("Just Chars:")
            pw_generator(numbers=False, chars=True, specials=False)
            print("\n")
    else:
        main()