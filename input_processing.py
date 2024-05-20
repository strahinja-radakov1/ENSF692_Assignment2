# input_processing.py
# Strahinja Radakovic, ENSF 692 P24
# A terminal-based program for processing computer vision changes detected by a car.
# Detailed specifications are provided via the Assignment 2 README file.
# You must include the code provided below but you may delete the instructional comments.
# You may add your own additional classes, functions, variables, etc. as long as they do not contradict the requirements (i.e. no global variables, etc.). 
# You may import any modules from the standard Python library.
# Remember to include your name and comments.



# No global variables are permitted*************************************************************************************************


# You do not need to provide additional commenting above this class, just the user-defined functions within the class
class Sensor:


    # Must include a constructor that uses default values
    # You do not need to provide commenting above the constructor
    def __init__(Sensor):
        #default sensor status
        Sensor.light = "green"
        Sensor.pedestrian_status = "no"
        Sensor.vehicle_status = "no"

    # Replace these comments with your function commenting
    def update_status(Sensor_change, new_value): # You may decide how to implement the arguments for this function
        #depending on what is being prompted, the coresponding sensor attribute will change.
        if(Sensor_change == "light"):
            Sensor.light = new_value
        elif(Sensor_change == "pedestrian"):
            Sensor.pedestrian_status = new_value
        elif(Sensor_change == "vehicle"):
            Sensor.vehicle_status = new_value



# The sensor object should be passed to this function to print the action message and current status
# Replace these comments with your function commenting
def print_message(sensor):


    #prints sensor status
    print("\n" + "Light = " + str(sensor.light) + ", Pedestrian = " + str(sensor.pedestrian_status) + ", Vehicle = " + str(sensor.vehicle_status))
    
    #proceed/caution/STOP print. 
    if (sensor.light == "green" and sensor.pedestrian_status == "no" and sensor.vehicle_status == "no"):
        print("\n"+"PROCEED" + "\n")
    elif (sensor.light == "yellow" and sensor.pedestrian_status == "no" and sensor.vehicle_status == "no"):
        print("\n"+"CAUTION" + "\n")
    else:
        print("\n"+"STOP" + "\n")

# Complete the main function below
def main():
    print("\n***ENSF 692 Car Vision Detector Processing Program***\n")

    #creating a new sensor, assigning it variables
    sens1 = Sensor
    sens1.light = "green"
    sens1.pedestrian_status = "no"
    sens1.vehicle_status = "no"

    #infinite loop to allow the program to run until the user chooses to exit it
    while True:

        #initial_input decides which parameter to change (1,2,3) to exit the program (0) and to re-propmpt which parameter to change ("return")
        #here we make it "return" to prompt the user to select an input (1,2,3,0)
        initial_input = "return"

        #as stated above, if input = initial_input, prompt the user to choose a parameter to change.
        if (initial_input == "return"):
            initial_input = input("\n"+"Select 1 to update the detected traffic light colour, 2 to update whether a pedestrian is detected, 3 to update whether a vehicle is detected, 0 to end the program"+"\n")

        #while initial input is 1, prompt what color the light is.
        while (initial_input == "1"):
            #print prompt
            light_color = input("\n"+"What is the light color? (input green, yellow, or red)"+"\n")
            #checks if the input is valid
            if (light_color == "red" or light_color == "green" or light_color == "yellow"):
                #if the input is valid, update the sensor traffic light detection
                sens1.update_status("light", light_color)
                #print message described above
                print_message(sens1)
                #sets initial input to "return" so the user is prompted to make another change if they wish
                initial_input == "return"
                #gets out of the loop.
                break
            else:
                #if the input is invalid, let the user know that the input is invalid.
                print("\n"+"invalid input, please input 'red', 'yellow' or 'green'"+"\n")
                #initial_input back to 1 to reprompt the user for an input
                initial_input = "1"


        #code logic and function is identical to the previous while loop (while (initial_input == "1")). Refer to the comments above.
        while (initial_input == "2"):
            pedestrian_detected = input("\n"+"Is a pedestrian detected? (input yes or no)"+"\n")
            if (pedestrian_detected == "yes" or pedestrian_detected == "no"):
                sens1.update_status("pedestrian", pedestrian_detected)
                print_message(sens1)
                initial_input == "return"
                break
            else:
                print("\n"+"invalid input, please input 'yes, or 'no'"+"\n")
                initial_input = "2"
                
        #code logic and function is identical to the previous while loop (while (initial_input == "1")). Refer to the comments above.
        while (initial_input == "3"):
            vehicle_detected = input("\n"+"Is a vehicle detected? (input yes or no)"+"\n")
            if (vehicle_detected == "yes" or vehicle_detected ==  "no"):
                sens1.update_status("vehicle", vehicle_detected)
                print_message(sens1)
                initial_input == "return"
                break
            else:
                print("\n"+"invalid input, please input 'yes, or 'no'"+"\n")
                initial_input = "3"

        #if the user chooses input 0, the program ends.
        if (initial_input == "0"):
            exit() 

        #if the initial input is invalid (not "return", 1, 2, 3, 0) then notify the user and reprompt.
        if (initial_input != "return" and initial_input != "0" and initial_input != "1" and initial_input != "2" and initial_input != "3"):
            print("\n" + "invalid input, please input '1', '2', '3', or '0'" + "\n")
    

        

# Conventional Python code for running main within a larger program
# No additional code should be included below this
if __name__ == '__main__':
    main()

