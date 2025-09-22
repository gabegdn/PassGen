import random
from datetime import datetime

tday = str(datetime.today())

format = "%Y-%m-%d %H:%M:%S.%f"

strp = datetime.strptime(tday, format)
print(strp.microsecond)

seed = random.seed(strp.microsecond)


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
    
    Enter 0 to specify an output file to store the generated passwords(such as: passwords.txt)
    FYI: Password length is pre-determined
    """)
    options = "1234567"
    curr_generated_pwds = []
    user_input = input()
    
    out_file_specified = False
    
    while True:
        match user_input:
            case "1":
                p = pw_generator(numbers=True, chars=True, specials=True)
                curr_generated_pwds.append(p) 
            case "2":
                p = pw_generator(numbers=True, chars=True, specials=False)
                curr_generated_pwds.append(p) 
            case "3":
                p = pw_generator(numbers=False, chars=True, specials=True)
                curr_generated_pwds.append(p) 
            case "4":
                p = pw_generator(numbers=True, chars=False, specials=True)
                curr_generated_pwds.append(p) 
            case "5":
                p = pw_generator(numbers=True, chars=False, specials=False)
                curr_generated_pwds.append(p) 
            case "6":
                p = pw_generator(numbers=False, chars=False, specials=True)
                curr_generated_pwds.append(p) 
            case "7":
                p = pw_generator(numbers=False, chars=True, specials=False) 
                curr_generated_pwds.append(p)
            case "0":
                out_file_specified = True
                user_file = input("Enter the name of the file you want to output your generated passwords to:\n")
                print(f"Your generated passwords will be outputted to {user_file}")
            case _:
                print("You didn't choose an option!")
        print("Here are your Current Generated Passwords:\n")
        print(curr_generated_pwds)
        print("If you want to generate another password please select an option like before otherwise enter -1:")
        print("""
        Enter 1 to generate passwd mixed of: Special Characters, Numbers, and Regular Characters
        Enter 2 to generate passwd mixed of: Numbers and Regular Characters
        Enter 3 to generate passwd mixed of: Special Charcaters and Regular Characters
        Enter 4 to generate passwd mixed of: Special Characters and Numbers
        Enter 5 to generate passwd mixed of: Just Numbers
        Enter 6 to generate passwd mixed of: Just Special Characters
        Enter 7 to generate passwd mixed of: Just Regular Characters
        
        
        Enter 0 to specify an output file to store the generated passwords(such as: passwords.txt)
        FYI: Password length is pre-determined
        """)
        user_input = input()
        if user_input == "-1":
            if out_file_specified:
                write_to_file(user_file, curr_generated_pwds)
                print(f"Your generated passwords have been written to {user_file}")
            break
        

                
def write_to_file(file_name, passwords):
    with open(file_name, '+a') as uf:
        for i in passwords:
            uf.write(i+"\n")    
        
    

def pw_generator(numbers=True, chars=True, specials=True):
    
    SPEC_CHARS = '!@#$%^&*()_-=+\\|]}[{\'";:/?.>,<`~'
    CHARS ="qwertyuioplkmjnhbgvfcdxsza"
    NUMS = "1234567890"
    
    pw_length = random.randint(15, 27)
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
    main()