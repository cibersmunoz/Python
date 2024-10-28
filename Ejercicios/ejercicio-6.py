import requests

def find_and_save_users(endpoint, filename):
    response = requests.get(endpoint)
    users = response.json()
    
    user_names = [user["name"] for user in users]
    
    print("User names:")
    for name in user_names:
        print(name)
    
    with open(filename, "w") as f:
        f.write("\n".join(user_names))

if __name__ == "__main__":
    endpoint = "https://api.example.com/users"  # Reemplazar con el endpoint real
    filename = "user_names.txt"
    find_and_save_users(endpoint, filename)
