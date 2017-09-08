def lateRide(n):
    hours = n // 60
    minutes = n % 60
    return (hours // 10) + (hours % 10) + (minutes // 10) + (minutes % 10)
