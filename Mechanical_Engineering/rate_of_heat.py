def rate_of_heat_transfer(thermal_conductivity, outer_temperature):
    return (f"When k is {thermal_conductivity} and outer temperature is {outer_temperature}, the rate of heat transfer is:",-66.67*thermal_conductivity*(outer_temperature - 25))


def rate_of_heat_transfer_between_range_of_values(minimum_k, maximum_k, step_for_k, minimum_T_out, maximum_T_out, step_for_T_out):
    minimum_k = int(minimum_k*1000)
    maximum_k = int(maximum_k*1000)
    step_for_k = int(step_for_k*1000)
    for thermal_conductivity in range(minimum_k, maximum_k + step_for_k, step_for_k):
        for outer_temperature in range(minimum_T_out, maximum_T_out + step_for_T_out, step_for_T_out):
            print(rate_of_heat_transfer(thermal_conductivity/1000, outer_temperature))
    return "Thanks for using code"

def rate_of_heat_transfer_between_range_of_k(minimum_k, maximum_k, step_for_k, T_out):
    return rate_of_heat_transfer_between_range_of_values(minimum_k, maximum_k, step_for_k, T_out, T_out + 1, 1)

def rate_of_heat_transfer_between_range_of_T_out(minimum_T_out, maximum_T_out, step_for_T_out, k):
    return rate_of_heat_transfer_between_range_of_values(k, k + 1, 1, minimum_T_out, maximum_T_out, step_for_T_out)

rate_of_heat_transfer_between_range_of_values(0.75, 1.25, 0.25, -15, 30, 5)
rate_of_heat_transfer_between_range_of_values(0.75, 1.25, 0.25, 38)