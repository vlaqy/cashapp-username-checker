import requests

base_url = "https://cash.app/{}"

with open("users.txt", "r") as file:
  usernames = file.read().splitlines()

for username in usernames:
  response = requests.get(base_url.format(username))

  # Use the status code to determine if the username is available or not. 404 = available 200 = taken
  if response.status_code == 404:
    print(f"The username '{username}' is available.")
  elif response.status_code == 200:
    print(f"The username '{username}' is taken.")
  else:
    print(
      f"Error occurred while checking username '{username}': {response.status_code}"
    )
