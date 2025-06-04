from bs4 import BeautifulSoup
#BeautifulSoup used to extract data from html files
# Function to extract usernames from an HTML file

def extract_usernames_from_html(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        # Read the HTML content
        content = file.read()
        # Parse with BeautifulSoup
        soup = BeautifulSoup(content, "lxml")
        # Find all links in the HTML file
        links = soup.find_all("a")
        
        # Extract usernames from the 'href' links
        usernames = [link.text.strip() for link in links if "instagram.com" in link.get('href', "")]
        return usernames

# Function to find people you follow who don't follow you back
def find_not_following_back(followers, following):
    followers_set = set(followers)
    following_set = set(following)
    
    # Determine who you follow but who doesn't follow you back
    not_following_back = following_set - followers_set
    return not_following_back

# File paths to your uploaded files
followers_file = "followers_1.html"
following_file = "following.html"

# Extract usernames from each file
followers = extract_usernames_from_html(followers_file)
following = extract_usernames_from_html(following_file)

# Find people you follow who don't follow you back
not_following_back = find_not_following_back(followers, following)

#Intro
def main():
    print("Hello, welcome to FollowerInspector. This program will check who among the people you follow don't follow you back.")
    print("To get started, we need lists of your followers & following.")
#need improvement (When no file is found error )
    while True:
        user_input = input("If you do not know how, type 'idk'. If you already have used our code before, type 'skip'. ")

        if user_input == "idk":
            while True:
                print("1. Go to your instagram app.")
                print("2. Click the 3 bars and go to 'Your Activity'.")
                print("3. Now scoll to the very bottom and click 'download your information'.")
                print("4. Click download or transfer information and select the account you want to check.")
                print("5. Now choose 'Some of your information & select 'Followers & Following' ")
                print("6. Select Download to device and select date range to all time and press create files.")
                print("7. Your files will be sent to your email. Once you have gotten them, download them and put them in the same file as this code. ")
                print("Now you are all set!")

                double_check = input("Shall we execute the code? Please type 'yes' or 'no': ") .strip().lower()

                if double_check == "yes":
                    break

                elif double_check == "no":
                    print("Repeating instructions... \n")
                
                else:
                    print("invalid input, please type 'yes' or 'no': ")
            break

        elif user_input == "skip":
            while True:
                double_check = input("Shall we execute the code? Please type 'yes' or 'no': ") .strip().lower()

                if double_check == "yes":
                    print("Skipping instructions, proceeding with code...")
                    break

                elif double_check == "no":
                    print("Asking again, \n")
                
                else:
                    print("Invalid input, please type 'yes' or 'no': ")

                
            break

        else:
            print("Invalid input, Please type 'idk' if you don't know how, or type 'skip' if you do. ")    

    if not_following_back: 
        print(f"\nYou have {len(not_following_back)} people who do not follow you back:")
        print("\n".join(not_following_back))
    else:
        print("All of your followers follows you back!")

 
main()






#Add feature where you can unfollow these snakes all at once. 
