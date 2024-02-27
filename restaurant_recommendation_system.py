import json

class Restaurant:
    def __init__(self, name, category, rating):
        self.name = name
        self.category = category
        self.rating = rating

class RestaurantRecommendationSystem:
    def __init__(self):
        self.restaurants = []

    def add_restaurant(self, name, category, rating):
        restaurant = Restaurant(name, category, rating)
        self.restaurants.append(restaurant)

    def search_by_category(self, category):
        result = [restaurant for restaurant in self.restaurants if restaurant.category == category]
        return result

    def autocomplete_categories(self, prefix):
        categories = set()
        for restaurant in self.restaurants:
            if restaurant.category.startswith(prefix):
                categories.add(restaurant.category)
        return list(categories)

    def load_data(self, filename):
        with open(filename, 'r') as file:
            data = json.load(file)
            for entry in data:
                self.add_restaurant(entry['name'], entry['category'], entry['rating'])

if __name__ == "__main__":
    recommendation_system = RestaurantRecommendationSystem()
    recommendation_system.load_data('restaurants.json')

    while True:
        print("\nWelcome to the Restaurant Recommendation System!")
        print("1. Search by category")
        print("2. Autocomplete categories")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            category = input("Enter the category to search: ")
            results = recommendation_system.search_by_category(category)
            if results:
                print("\nRestaurants in category '{}':".format(category))
                for restaurant in results:
                    print("- {} (Rating: {})".format(restaurant.name, restaurant.rating))
            else:
                print("No restaurants found in category '{}'".format(category))

        elif choice == '2':
            prefix = input("Enter the beginning of the category: ")
            categories = recommendation_system.autocomplete_categories(prefix)
            if categories:
                print("\nAutocomplete suggestions:")
                for category in categories:
                    print("- {}".format(category))
            else:
                print("No categories found starting with '{}'".format(prefix))

        elif choice == '3':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please enter a valid option.")
