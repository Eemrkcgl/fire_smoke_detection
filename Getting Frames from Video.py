import cv2
import time
import os

def video_to_frames(input_loc, num_of_video):

    #Start of timer
    time_start = time.time()
    
    #It creates a output location
    lst=input_loc.split("/")

    name_of_video=lst[-1][:-4]
    
    try:
        os.mkdir("Data")
    except OSError:
        pass

    output_loc = "Data/Frames_of_"+name_of_video

    try:
        os.mkdir(output_loc)

    except OSError:
        pass

    #Read the video
    cap = cv2.VideoCapture(input_loc)

    #Number of frames in the video
    number_of_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT)) - 1
    print("Number of frames: ", number_of_frames)

    #Fps value of the video
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    print("This video's fps value: {}".format(fps))

    #Video lenght
    lenght_of_video = number_of_frames/fps
    minutes = int(lenght_of_video/60)
    seconds = lenght_of_video % 60

    print("Video's duration={} minutes and {} seconds\n".format(minutes, seconds))

    #Set the counters
    count = 0
    number_of_picture=0

    #The time when video's frames will be started to recording
    start_from_minutes = int(input("Start From (Minute): "))
    start_from_seconds = int(input("Start From (Second): "))

    print("If you want to get frames till the end of the video please enter a word instead of a number...")
    #The time when video's frames will be started to recording
    finish_at_minutes = (input("Finish at (Minute): "))
    finish_at_seconds = (input("Finish at (Second): "))

    #Frequency of the frames/(Second)
    frequency = int(input("Frequency of Frames: "))
    # If user enters a not integer value to the "Finish at" section, it will be replaced with the videos real end minute and second.
    try:
        finish_at_minutes = int(finish_at_minutes)
        finish_at_seconds = int(finish_at_seconds)

        start_time= 60 * start_from_minutes + start_from_seconds
        finish_time = finish_at_minutes * 60 + finish_at_seconds
        finish_time=finish_time

    except ValueError:
        finish_at_minutes=int(minutes)
        finish_at_seconds=int(seconds)

        start_time = 60 * start_from_minutes + start_from_seconds

        finish_time= finish_at_minutes * 60 + finish_at_seconds

    #Checking that if the entered values are suitable or not
    if start_time>finish_time:
        print("Try again")

    elif finish_time>(60*minutes+seconds):
        print("Try again")

    #If everything is alright==>
    else:
        if start_from_seconds<10 and finish_at_seconds<10:

            print("From {}:0{} to {}:0{}".format(start_from_minutes, start_from_seconds, finish_at_minutes,finish_at_seconds))

        elif start_from_minutes<10 and finish_at_seconds>9:

            print("From {}:0{} to {}:{}".format(start_from_minutes, start_from_seconds, finish_at_minutes,finish_at_seconds))

        elif start_from_minutes>9 and finish_at_seconds<10:

            print("From {}:{} to {}:0{}".format(start_from_minutes, start_from_seconds, finish_at_minutes,finish_at_seconds))

        else:

            print("From {}:{} to {}:{}".format(start_from_minutes, start_from_seconds, finish_at_minutes,finish_at_seconds))


        print("Video is being converted...\n")

        #Start of the recording section
        while cap.isOpened():
            #Get frames
            ret, frame = cap.read()

            #If the frame number can be divided by (frequency*fps) value it will be saved as jpeg file
            if count % ((int(fps))*(frequency)) == 0:
                try:
                    cv2.imwrite(output_loc + f"/Frame_No{count}_video_{num_of_video}.jpg", frame)

                    count += 1
                    number_of_picture += 1

                except:
                    break

            else:
                count += 1

            #If there is a time limit at the end this block, it will break the loop
            if count > ((finish_time)*int(fps)):

                cap.release()

                break

    deleted_img=0
    #If there is a time limit at the beginning of the video, unwanted frames will be deleted at this block
    for photos in os.listdir(output_loc):

        if (start_time-1)*int(fps)>int(photos[8:-12]):
            os.remove(output_loc+"/"+photos)

            deleted_img+=1

        else:

            continue

    #End of the timer
    time_end = time.time()

    finish_minute = int(round((time_end - time_start) / 60))
    finish_second = (time_end - time_start) % 60

    print("Converting has been finished.\n{} pictures are extracted from the video.".format(number_of_picture-deleted_img))
    print("It took {} minutes and {} seconds.".format(finish_minute, finish_second))


if __name__ == "__main__":

    num_of_video = input("Enter the number of the video: ")

    for index, each in enumerate(os.listdir()):
        if each[-4:]==".mp4":
            print(f"{index}-{each}")

    input_loc = int(input("Which video will be used(Enter the index indicated above as integer): "))
    input_loc = os.listdir()[input_loc]

    video_to_frames(input_loc, num_of_video)

