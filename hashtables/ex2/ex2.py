class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    trip = {}
    route = []

    for ticket in tickets:
        trip[ticket.source] = ticket.destination
    destination = trip["NONE"]
    print(trip)
    while destination != "NONE":
        route.append(destination)
        destination = trip[destination]
    route.append("NONE")

    return route
