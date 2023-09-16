from faker import Faker

# Create an instance of the Faker class
fake = Faker()

# Generate random personal data
def generate_personal_data():
    name = fake.name()
    address = fake.address()
    email = fake.email()

    return {
        'Name': name,
        'Address': address,
        'Email': email
    }

if __name__ == "__main__":
    num_entries = int(input("Enter the number of personal data entries to generate: "))
    
    for _ in range(num_entries):
        data = generate_personal_data()
        print("Name:", data['Name'])
        print("Address:", data['Address'])
        print("Email:", data['Email'])
        print("\n")
