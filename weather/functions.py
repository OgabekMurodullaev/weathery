def get_temperature_color(temperature):
    if temperature <= -30:
        return "#003366"
    elif temperature <= -20:
        return "#4A90E2"
    elif temperature <= -10:
        return "#B3DFFD"
    elif temperature <= 0:
        return "#E6F7FF"
    elif temperature <= 10:
        return "#D1F2D3"
    elif temperature <= 20:
        return "#FFFACD"
    elif temperature <= 30:
        return "#FFCC80"
    elif temperature <= 40:
        return "#FF7043"
    else:
        return "#D32F2F"

def get_wind_color(wind_speed):
    if wind_speed <= 10:
        return "#E0F7FA"
    elif wind_speed <= 20:
        return "#B2EBF2"
    elif wind_speed <= 40:
        return "#4DD0E1"
    elif wind_speed <= 60:
        return "#0288D1"
    else:
        return "#01579B"

def get_cloud_color(cloud_coverage):
    if cloud_coverage <= 10:
        return "#FFF9C4"
    elif cloud_coverage <= 30:
        return "#FFF176"
    elif cloud_coverage <= 60:
        return "#E0E0E0"
    elif cloud_coverage <= 90:
        return "#9E9E9E"
    else:
        return "#616161"
