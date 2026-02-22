from bs4 import BeautifulSoup
import os

def extract_usernames_from_html(file_path):
    if not os.path.exists(file_path):
        print(f"Error: {file_path} not found.")
        return []

    with open(file_path, "r", encoding="utf-8") as file:
        soup = BeautifulSoup(file, "lxml")
        links = soup.find_all("a")

        usernames = []

        for link in links:
            href = link.get("href", "")

            if "instagram.com" in href:
                # Remove trailing slash if exists
                href = href.rstrip("/")

                # Extract username (last part of URL)
                username = href.split("/")[-1]

                # Skip empty or invalid entries
                if username and username != "_u":
                    usernames.append(username)

        return usernames


def find_not_following_back(followers, following):
    return following - followers


# File names
followers_file = "followers_1.html"
following_file = "following.html"

# Convert to sets (important!)
followers = set(extract_usernames_from_html(followers_file))
following = set(extract_usernames_from_html(following_file))

not_following_back = find_not_following_back(followers, following)

print("People who don't follow you back:\n")
for user in sorted(not_following_back):
    print(user)

print(f"\nTotal: {len(not_following_back)}")