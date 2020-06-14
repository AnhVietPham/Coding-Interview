import random

if __name__ == '__main__':
    max_km = int(input())
    total_distance = int(input())
    n = [int(i) for i in range(total_distance)]
    number_of_gas_station = random.randint(0, total_distance)
    address_gas_stations = random.sample(n, k=number_of_gas_station)
    address_gas_stations.sort()
    print(number_of_gas_station)
    print(n)
    print("Random Gas Station: ", address_gas_stations)
    # numRefills = 0
    # currentPosition = 0
    # while currentPosition <= 11:
    #     lastPosition = currentPosition
    #     while currentPosition <= 11 and (n[currentPosition] - n[lastPosition]) <= max_km:
    #         currentPosition += 1
    #     if currentPosition == lastPosition:
    #         print('IMPOSSIBLE')
    #         quit()
    #     if currentPosition <= 11:
    #         numRefills += 1
    #         print(currentPosition)
    # print(n)
    # print(numRefills)
