from functools import reduce


def process_data(sensor_data, calibration_bias=0.8, outlier_threshold=30):
    # Correct for calibration bias by adding value to each element of sensor data
    corrected_bias = list(map(lambda x: x + calibration_bias, sensor_data))
    print("Bias corrected:")
    print(corrected_bias)

    # Filter outliers by given threshold
    filtered_data = list(filter(lambda x: x <= outlier_threshold, corrected_bias))
    print("\nFiltered data for outliers:")
    print(filtered_data)

    # Calculate mean of remaining findings
    mean = reduce(lambda a, b: a + b, filtered_data) / len(filtered_data)
    print(f"\nAverage of remaining data: {mean}")


raw_readings = [19.4, 21.1, 21.7, 18.9, 100.3, 20.5]
process_data(raw_readings)
