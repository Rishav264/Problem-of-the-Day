# Temperature Analyzer using Arrays in Python
# Function Signature:
# def analyze_temperatures(temperatures: list[list[float]]) -> tuple[int, int, list[float]]:
# Input:
# - A 2D list temperatures of size 7x24 where:
# - temperatures[i][j] represents the temperature (in °C) at the j-th hour of the i-th day.
# - Each value is a float.
# Output:
# - Return a tuple containing:
# 1. An integer representing the index of the hottest day (0-based).
# 2. An integer representing the index of the coldest day (0-based).
# 3. A list of 7 float values representing the average temperature of each day.
# Input:
# temperatures = [ [22.0]*24, [25.0]*24, [18.0]*24, [21.0]*24,[24.0]*24,[23.0]*24,[20.0]*24 ]
# Output: (1, 2, [22.0, 25.0, 18.0, 21.0, 24.0, 23.0, 20.0])

def analyze_temperatures(temperatures: list[list[float]]) -> tuple[int, int, list[float]]:
    """
    Performing Analysis on data finding the hottest day, coldest day and list 
    of daily avg temp

    Args: temperatures: (list[list[float]])

    Return: tuple[int, int, list[float]]
    """
    daily_avg = []
    #the average value of each day
    for day in temperatures:
        total_temp = sum(day)
        avg_temp = total_temp/len(day)
        daily_avg.append(avg_temp)

    #highest temp idx
    high_temp_idx = 0
    high_temp = daily_avg[0]
    for i in range(len(daily_avg)):
        if daily_avg[i] > high_temp:
            high_temp = daily_avg[i]
            high_temp_idx = i

    #coldest temp idx
    cold_temp_idx = 0
    cold_temp = daily_avg[0]
    for i in range(len(daily_avg)):
        if daily_avg[i] < cold_temp:
            cold_temp = daily_avg[i]
            cold_temp_idx = i                 

    return (high_temp_idx, cold_temp_idx, daily_avg)

#sample data
temp_data = [
    [22.0]*24,
    [25.0]*24,
    [18.0]*24,
    [21.0]*24,
    [24.0]*24,
    [23.0]*24,
    [20.0]*24
]

result = analyze_temperatures(temp_data)
print(result)

