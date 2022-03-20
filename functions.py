
def toMinutes(chrono):
    return "{0}:{1}".format(int(float(chrono)/60), round(float(chrono) - (float(chrono) // 60) * 60, 2))