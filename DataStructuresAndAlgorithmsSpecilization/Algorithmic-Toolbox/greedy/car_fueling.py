import random


def random_gas_station_position(distance):
    split_distance = [int(i) for i in range(distance)]
    number_of_gas_stations = random.randint(0, distance)
    gas_station_positions = random.sample(split_distance, k=number_of_gas_stations)
    gas_station_positions.sort()
    if gas_station_positions[0] != 0:
        gas_station_positions = [0] + gas_station_positions
    return gas_station_positions


if __name__ == '__main__':
    max_km = int(input())
    total_distance = int(input())
    address_gas_stations = random_gas_station_position(total_distance)
    print("Random Gas Station: ", address_gas_stations)
    current_gas_station = 0
    last_gas_station = current_gas_station
    num_refills = 0
    while current_gas_station < len(address_gas_stations):
        if address_gas_stations[current_gas_station] - address_gas_stations[last_gas_station] <= max_km:
            current_gas_station += 1
        else:
            last_gas_station = current_gas_station - 1
            print(address_gas_stations[last_gas_station])
            num_refills += 1
            if address_gas_stations[current_gas_station] - address_gas_stations[last_gas_station] > max_km:
                print("Impossible!")
                break
    print(num_refills)
