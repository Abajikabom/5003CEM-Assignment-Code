class Graph:
    def __init__(self):
        self.adjacency = {}

    def addVertex(self, vertex):
        if vertex not in self.adjacency:
            self.adjacency[vertex] = []

    def addEdge(self, fromVertex, toVertex):
        if fromVertex in self.adjacency and toVertex in self.adjacency:
            if toVertex not in self.adjacency[fromVertex]:
                self.adjacency[fromVertex].append(toVertex)

    def removeEdge(self, fromVertex, toVertex):
        if fromVertex in self.adjacency and toVertex in self.adjacency[fromVertex]:
            self.adjacency[fromVertex].remove(toVertex)

    def listOutgoingAdjacentVertex(self, vertex):
        return self.adjacency.get(vertex, [])

    def listIncomingAdjacentVertex(self, vertex):
        return [v for v, edges in self.adjacency.items() if vertex in edges]


class Person:
    def __init__(self, name, gender, biography, privacy='public'):
        self.name = name
        self.gender = gender
        self.biography = biography
        self.privacy = privacy  # 'public' or 'private'

    def displayProfile(self):
        if self.privacy == 'public':
            return f"Name: {self.name}\nGender: {self.gender}\nBio: {self.biography}\nPrivacy: Public"
        else:
            return f"Name: {self.name}\nPrivacy: Private"


users = {
    "bobby": Person("Bobby Lim,", "Male", "Food lover & traveler", "public"),
    "ahbird": Person("Bird Kiew", "Male", "Gamer", "private"),
    "carol": Person("Carol Lin", "Female", "Photographer and dreamer", "public"),
    "sising": Person("Daniel Loh", "Male", "Coffee addict", "private"),
    "joel": Person("Joel Vincent", "Female", "Entrepreneur and blogger", "public")
}

social_graph = Graph()

for username in users:
    social_graph.addVertex(username)

social_graph.addEdge("bobby", "ahbird")
social_graph.addEdge("ahbird", "joel")
social_graph.addEdge("carol", "ahbird")
social_graph.addEdge("sising", "joel")
social_graph.addEdge("joel", "carol")

def menu():
    while True:
        print("\n--- Social Media App ---")
        print("1. List all users")
        print("2. View a user's profile")
        print("3. View who a user is following")
        print("4. View a user's followers")
        print("5. Add new user")
        print("6. Follow a user")
        print("7. Unfollow a user")
        print("0. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            print("\nUsers:")
            for username in users:
                print("-", username)

        elif choice == '2':
            username = input("Enter username to view profile: ").strip()
            if username in users:
                print("\n" + users[username].displayProfile())
            else:
                print("User not found.")

        elif choice == '3':
            username = input("Enter username: ").strip()
            if username in users:
                following = social_graph.listOutgoingAdjacentVertex(username)
                print("Following:", ", ".join(following) if following else "None")
            else:
                print("User not found.")

        elif choice == '4':
            username = input("Enter username: ").strip()
            if username in users:
                followers = social_graph.listIncomingAdjacentVertex(username)
                print("Followers:", ", ".join(followers) if followers else "None")
            else:
                print("User not found.")

        elif choice == '5':
            uname = input("Enter new username: ").strip()
            if uname in users:
                print("Username already exists.")
                continue
            gender = input("Enter gender: ").strip()
            bio = input("Enter biography: ").strip()
            privacy = input("Privacy (public/private): ").lower().strip()
            if privacy not in ['public', 'private']:
                print("Invalid privacy setting. Defaulting to 'public'.")
                privacy = 'public'
            users[uname] = Person(uname, gender, bio, privacy)
            social_graph.addVertex(uname)
            print("User added successfully.")

        elif choice == '6':
            follower = input("Enter your username: ").strip()
            followee = input("Enter username to follow: ").strip()
            if follower in users and followee in users:
                social_graph.addEdge(follower, followee)
                print(f"{follower} now follows {followee}")
            else:
                print("User(s) not found.")

        elif choice == '7':
            follower = input("Enter your username: ").strip()
            followee = input("Enter username to unfollow: ").strip()
            if follower in users and followee in users:
                social_graph.removeEdge(follower, followee)
                print(f"{follower} unfollowed {followee}")
            else:
                print("User(s) not found.")

        elif choice == '0':
            print("Goodbye!")
            break

        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    menu()
