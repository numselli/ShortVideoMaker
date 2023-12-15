import matplotlib.pyplot as plt
import sys
print(sys.argv[1:])
videoLength = int(sys.argv[1:][0])

class Timestamp():
    def __init__(self, videoLength):
        self.videoLength = videoLength

    def getDataFromFile(name):
        with open(name, "r") as file:
            for line in file:
                return line


    def preProcessData(data):
        tripletsArray = data.split("C ")
        dataPointsArray = []
        for triplets in tripletsArray:
            if triplets != "":
                pointsArray = triplets.split(" ")[:3]
                for points in pointsArray:
                    p = points.split(",")
                    dataPointsArray.append([float(p[0]), float(p[1])])
        return dataPointsArray


    def plotCurve(points, self):
        x = [((p[0] - 1) * (self.videoLength) / (1000 - 1)) for p in points]
        y = [-p[1] for p in points]
        # plt.plot(x, y) #uncomment these two lines to enable graph
        # plt.show()

        # Find the highest point
        max_point_index = y.index(max(y))
        highest_point = (x[max_point_index], y[max_point_index])

        return highest_point

    
    

    dataPointsArray = preProcessData(data)

    highest_point = plotCurve(dataPointsArray, videoLength)
    print("Highest point coordinates:", highest_point)

    def seconds_to_hms(seconds):
    
        seconds = seconds[0]

        print(type(seconds))
        hours = seconds // 3600
        minutes = (seconds % 3600) // 60
        remaining_seconds = seconds % 60
        return hours, minutes, remaining_seconds

    print(seconds_to_hms(highest_point))