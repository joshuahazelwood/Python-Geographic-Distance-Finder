#Vector Coding
#11/18/19

import time
import math 

def CordConv(deg,mini,sec):
    mindeg = mini / 60
    secdeg = sec / 3600
    return deg + mindeg + secdeg
def LongLadtoMag(uselongs,uselads,uselonge,uselade):
    xstart = uselongs * (40000/360) * 3280.4
    ystart = uselads * (40000/360) * 3280.4
    xstop = uselonge * (40000/360) * 3280.4
    ystop = uselade * (40000/360) * 3280.4

    xvector = xstop - xstart
    yvector = ystop - ystart

    magnitude = (math.sqrt(pow(xvector,2)+pow(yvector,2))) * 0.3048 #0.3048 is the conversion from feet to meters
    theta = ((math.atan(yvector/xvector)+ math.pi) / math.pi) * 180
    return (magnitude, theta)

def main():

    GeoDeg = 0
    Geomin = 0
    Geosec = 0
    choice = 0
    xstart = 0
    ystart = 0
    xstop = 0
    ystop = 0
    uselongs = 0
    uselads = 0
    uselonge = 0
    uselade = 0
    xvector = 0
    yvector = 0
    magnitude = 0
    theta = 0
    

    print("1: GeoConvert \n2: Coordinate to Vector Converter \n3: Exit\n")
    
                 
    while(choice != 3):

        choice = int(input("Enter a choice: "))

        if(choice == 1):
        
            GeoDeg = float(input("\nEnter Degrees: "))
            Geomin = float(input("Enter Minutes: "))
            Geosec = float(input("Enter Seconds: "))

            Geotot = CordConv(GeoDeg,Geomin,Geosec)

            print("Total Degrees %.4f°\n" % Geotot)
        elif(choice == 2):

            uselongs = float(input("Enter your initial longitude: "))
            uselads = float(input("Enter your initial latitude: "))
            uselonge = float(input("Enter your final longitude: "))
            uselade = float(input("Enter your final latitude: "))
            
            magnitude, theta = LongLadtoMag(uselongs,uselads,uselonge,uselade)

            print("The magnitude of the Vector is %.3f meters and the angle is %.2f°\n" % (magnitude, theta))
            
        elif(choice == 3):
            print("Goodbye")
            return main
        
        else:
            print("Please make a valid selection")
            
    
main()
