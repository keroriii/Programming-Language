def main():
    start_location = input("Enter the starting location: ")
    destination = input("Enter the destination: ")
    mode_of_transport = input("Enter the mode of transport (e.g., car, bike, bus): ")

    try:
        distance_km = float(input("Enter the distance between the two locations (in kilometers): "))
        speed_kmh = float(input("Enter the speed of travel (in km/h): "))
    except ValueError:
        print("Invalid input for distance or speed. Please enter numeric values.")
        return

    if speed_kmh <= 0:
        print("Speed must be greater than zero.")
        return

    travel_time_hours = distance_km / speed_kmh

    # Check if travel time exceeds 5 hours
    needs_rest_stop = travel_time_hours > 5

    print("\n--- Travel Summary ---")
    print(f"From: {start_location}")
    print(f"To: {destination}")
    print(f"Mode of Transport: {mode_of_transport}")
    print(f"Distance: {distance_km:.2f} km")
    print(f"Estimated Speed: {speed_kmh:.2f} km/h")
    print(f"Estimated Travel Time: {travel_time_hours:.2f} hours")

    if needs_rest_stop:
        print("Warning: Travel time exceeds 5 hours.")
        print("Recommendation: Plan for a rest stop during your trip.")
    else:
        print("No rest stop needed based on the travel time.")

if __name__ == "__main__":
    main()
