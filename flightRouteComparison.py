our_routes = {"LAX", "JFK", "CDG", "DXB"}
competitor_routes = {"JFK", "CDG", "LHR", "BKK"}

def listDestinations(destinations, text):
    print(text)
    for index, destination in enumerate(destinations):
        print(f"{index}. {destination}")

shared_destinations = our_routes.intersection(competitor_routes)
listDestinations(shared_destinations, "Shared destinations: ")
our_unique_destinations = our_routes.difference(competitor_routes)
listDestinations(our_unique_destinations, "Our unique destinations")
both_unique_destinations = our_routes.symmetric_difference(competitor_routes)
listDestinations(both_unique_destinations, "Unique destinations among all airlines: ")