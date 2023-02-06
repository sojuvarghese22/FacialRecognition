import cv2,pickle
import face_recognition
import os
from collections import Counter
import sys
pickle_file = open("/home/soju/Kosmos/face_recognition/fr/train_encodes",'rb')
TRAIN_ENCODINGS = pickle.load(pickle_file)





# print(type(TRAIN_ENCODINGS['encodings']))
# exit()

# /home/soju/Kosmos/face_recognition/fr/test1.mp4
# print("yi",TRAIN_ENCODINGS)

# def evaluate(TEST,TRAIN,THRESHOLD,TOLERANCE):
#     MAIN_ANSWER=[]
#     final=[]
#     for box in TEST:
#         answer=[]
#         for celeb in TRAIN:
#             for encoding in range(len(TRAIN[celeb])):
#                 results = face_recognition.compare_faces([TRAIN[celeb][encoding]],TEST[box])
#                 faceDis = face_recognition.face_distance([TRAIN[celeb][encoding]],TEST[box])
#                 if results[0] and faceDis[0]<THRESHOLD:
#                     answer.append(celeb)
#         MAIN_ANSWER.append(answer)

#     for answers in MAIN_ANSWER:
#         count = Counter(answers)
#         print(count)
#         if len(answers)<TOLERANCE:
#             final.append("Unknown")
#         else:
#             final.append(count.most_common(1)[0][0])
    
#     return final

# def get_video_encodings(test):
#     imgtest=test
    
#     faceLoc = face_recognition.face_locations(imgtest)
#     face_enc = face_recognition.face_encodings(imgtest,faceLoc)
#     # print("total faces",len(faceLoc))
#     # print("total encoding",len(face_enc))
#     # print("this is",{box: face_enc[box] for box in range(len(faceLoc))})
#     # cv2.imshow("Dd",imgtest)
    
#     # cv2.waitKey(0)
    
#     # exit()
#     return {box: face_enc[box] for box in range(len(faceLoc))},imgtest

# def show_video_results(test,final_answer_list):
#     imgtest=test
#     faceLoc = face_recognition.face_locations(imgtest)
    
#     for box in range(len(faceLoc)):
#         cv2.rectangle(imgtest,(faceLoc[box][3],faceLoc[box][0]),(faceLoc[box][1],faceLoc[box][2]),(0,255,0),2)
#         org = (faceLoc[box][3]-5,faceLoc[box][0]-10)
#         cv2.putText(imgtest,final_answer_list[box].upper(),org,cv2.FONT_HERSHEY_COMPLEX, 1,(255,255,255),2)
#     return imgtest
    
# def main(PATH):face_enc
#     cap = cv2.VideoCapture(PATH)
#     count=0
#     while True:

#         ret, frame = cap.read()
#         if ret != True:
#             break
#         print("For Frame :",count)       
#         encoding,imgtest=get_video_encodings(frame)
#         final=evaluate(encoding,TRAIN_ENCODINGS,0.55,10)
#         imgtest=show_video_results(imgtest,final)
#         cv2.imshow("img",imgtest)
#         # cv2.imwrite(f"./frames/{count}.png",img=imgtest)
#         count+=1
#         print("\n")
#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break

# main("test1.mp4")




















def new(PATH):
    cap = cv2.VideoCapture(PATH)
    c=0
    count_for_image = 1
    # count_for_image_tolerance = 1
          
    while True:
        print("7777777777777777777777777777777777777", count_for_image)
        ret, frame = cap.read()
        if ret != True:
            break
        
        identifiend_person = []
        tolerance = 5
        print("For Frame :",c)
        count = {}
        frame_backup = frame
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        # print(frame)
        faceLoc = face_recognition.face_locations(frame)
        print(len(faceLoc))
       
        #if face detected then regular process
        if len(faceLoc)>0:


            # print(faceLoc)
            # cv2.imshow("dd",frame)
            # cv2.waitKey(1)
            
            face_enc = face_recognition.face_encodings(frame,faceLoc)
            print("ddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd",len(faceLoc))
            for encode,faceLocation in zip(face_enc,faceLoc):
                results = face_recognition.compare_faces(TRAIN_ENCODINGS['encodings'],encode)
                dist = face_recognition.face_distance(TRAIN_ENCODINGS['encodings'],encode)
                print(dist)
                # print("kfkjjk",results)
                flag = {}
                flag_threshold = {}
                threshold = 0.4       
                if True in results:
                    # print("jnj  ")
                    print("rrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrr",results)
                    delete=[]
                    
                    for index,boolean_value in enumerate(results):
                        if boolean_value == True:
                            if dist[index] <= threshold:
                                print("distance value",dist[index])
                                print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")

                                flag_threshold[TRAIN_ENCODINGS['names'][index]] =  flag_threshold.get(TRAIN_ENCODINGS['names'][index],0)+1
                      

                            print(index)
                            print(dist[index])
                            delete.append(dist[index])
                            # print("ee",TRAIN_ENCODINGS['encodings'][index])
                            # name = TRAIN_ENCODINGS['names'][index]
                            # flag[name] = flag.get(name,0)+1
                    
                    
                    print("boolean values ", delete)
                    
                    # print(flag)
                    # li = {}
                    li_threshold = {}
                    # for i, value in zip(flag.keys(),flag.values()):
                    #     s = ""
                    #     for j in i:
                    #         try:
                    #             x=int(j)
                    #         except:
                    #             s = s+j
                    #     li[s[:-1]] = li.get(s[:-1],0)+1
                        # li[s[:-1]] = value
                    for i, value in zip(flag_threshold.keys(),flag_threshold.values()):
                        s = ""
                        for j in i:
                            try:
                                x=int(j)
                            except:
                                s = s+j
                        li_threshold[s[:-1]] = li_threshold.get(s[:-1],0)+1
                    # print(li)
                    print("yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy",li_threshold)
                    print("zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzZ",flag_threshold)
                    # finding maximun value
                    # for jo in li:
                    #     print(jo)
                    #     if li[jo]>max_val:
                    #         name = jo
                    #         max_val = li[jo]
                    # print(name,max_val)
                    max_val = 0
                    if len(li_threshold)!=0:
                        for jo in li_threshold:
                            print(jo)
                            if li_threshold[jo]>max_val:
                                name = jo
                                max_val = li_threshold[jo]

                        
                    #have to remove it after review
                    else:
                        name = ''
                        max_val = 0
                        print(name,max_val)
                        print("else will nevver run")
                        # y1,x1,y2,x2 = faceLocation 

                        # frame = cv2.rectangle(frame, (x1,y1),(x2,y2), (0,255,0),2)
                        # frame = cv2.putText(frame, "unknown", (x1,y1-10),cv2.FONT_HERSHEY_COMPLEX, 1,(255,255,255),2)



                    
                                     

                    # print("check",identified_person)                           
                    # identifiend_person.append(max(flag, key=flag.get()))
                    # y1,x1,y2,x2 = faceLoc 
                    if max_val >= tolerance:
                        print("vvvvvvvvvvvvvvvvvvvvvvaaaaaaaaaaaaaaalue is",max_val) 
                        print("toleranceeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee is",tolerance) 

                        
                		# face = image[top:bottom, left:right]
                        # (top, right, bottom, left) = faceLoc

                        y1,x1,y2,x2 = faceLocation
                        
                        frame = cv2.rectangle(frame, (x1,y1),(x2,y2), (0,255,0),2)
                        frame = cv2.putText(frame, name, (x1,y1-10),cv2.FONT_HERSHEY_COMPLEX, 1,(255,255,255),2)
                        name_copy = ''.join(name.split())
                        
                        if not os.path.exists(name_copy):
                            os.makedirs(name_copy)


                        # y1,x1,y2,x2 = faceLoc
                        (top, right, bottom, left) = faceLocation 
                        # face = frame[x1:y1, x2:y2]
                        frameCopy = frame_backup
                        # frameCopy = cv2.cvtColor(frameCopy, cv2.COLOR_RGB2BGR)
                        faceCopy = frameCopy[top:bottom, left:right]
                        extension = name_copy + str(count_for_image) + '.jpg'
                        filename = os.path.join(os.getcwd(),name_copy,extension)
                        
                        print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@",filename)
                        print("^^^^^^^^^^^^^^^^^^^^^^^^^",count_for_image)
                        cv2.imwrite(filename, faceCopy)
                          
                        # if not os.path.exists(name_copy):
                        #     os.makedirs(name_copy)


                            
                        # filename = './' + name + '/' +  name + str(count_for_image) +  '.jpg'
                        # print(filename)
                        
                        # './extractedFrame/frame' + str(currentframe) + '.jpg'
                        # ./Jimmy Fallon/Jimmy Fallon0.jpg     

                        # os.chdir(filename)
                

                        # print(filename)
                        # # paththh = os.path.join(os.getcwd(),name)
                        # # os.chdir(paththh)
                        # cv2.imwrite(filename,face)
                        # # cv2.imwrite('/name/frame', img) 
                        # count_for_image+=1
                        # # name = './extractedFrame/frame' + str(currentframe) + '.jpg'
                        # # print ('Creating...' + name)

                        # # writing the extracted images
                        # # cv2.imwrite(name, frame)
                    
                    else:
                        y1,x1,y2,x2 = faceLocation 

                        frame = cv2.rectangle(frame, (x1,y1),(x2,y2), (0,255,0),2)
                        frame = cv2.putText(frame, "unknown", (x1,y1-10),cv2.FONT_HERSHEY_COMPLEX, 1,(255,255,255),2)

                #For unknown face 
                else:
                    # encode = 0
                    # print("########################################################################################################")
                    # if unknown1 == 0:

                    #     unknown1 = encode
                    y1,x1,y2,x2 = faceLocation 

                    frame = cv2.rectangle(frame, (x1,y1),(x2,y2), (0,255,0),2)
                    frame = cv2.putText(frame, "unknown", (x1,y1-10),cv2.FONT_HERSHEY_COMPLEX, 1,(255,255,255),2)
            

            count_for_image = count_for_image +1
            frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
            print("Dd")
            cv2.imshow("fullwin",frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
            
                    # break
                
                
                
             # frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
            # cv2.imshow("halfwin",frame)
            # cv2.waitKey(1)

                    # break
                
            c+=1
                
            #below code ka sochna hai 

            
        
        
        else:
            c+=1
            cv2.imshow("ee",frame)
            continue
               
        # count_for_image = count_for_image+1
        # break
        
        
        #cv2.imshow('wind', frame)
                    # #print unknown in actual frame using cv2
                # # loop over the recognized faces
                # for ((top, right, bottom, left), name) in zip(boxes, names):
                #     # draw the predicted face name on the image
                #     cv2.rectangle(image, (left, top), (right, bottom), (0, 255, 0), 2)
                #     y = top - 15 if top - 15 > 15 else top + 15
                #     cv2.putText(image, name, (left, y), cv2.FONT_HERSHEY_SIMPLEX,
                #         0.75, (0, 255, 0), 2)
                # # show the output image
                # cv2.imshow("Image", image)
                # cv2.waitKey(0)
        




#                 d = {1: '001', 2: '010', 3: '011'}
# # since 4 is not in keys, it'll print "Not found"
# print(d.get(4, "Not found"))


#         # faceDis = face_recognition.face_distance([TRAIN[celeb][encoding]],TEST[box])
    
#         if True in results:
            
new('videoplayback (7).mp4')











# #next step check the code wheher declaratin is done correctly or not 

# import cv2
# import os



# def extractFrame(path):
#     # Importing all necessary libraries

#     # Read the video from specified path
#     cam = cv2.VideoCapture(path)

#     try:
        
#         # creating a folder named data
#         if not os.path.exists('extractedFrame'):
#             os.makedirs('extractedFrame')

#     # if not created then raise error
#     except OSError:
#         print ('Error: Creating directory of data')

#     # frame
#     currentframe = 0

#     while(True):
        
#         # reading from frame
#         ret,frame = cam.read()

#         if ret:
#             # if video is still left continue creating images
#             name = './extractedFrame/frame' + str(currentframe) + '.jpg'
#             print ('Creating...' + name)

#             # writing the extracted images
#             cv2.imwrite(name, frame)

#             # increasing counter so that it will
#             # show how many frames are created
#             currentframe += 1
#         else:
#             break

#     # Release all space and windows once done
#     cam.release()
#     cv2.destroyAllWindows()
# # extractFrame('/home/soju/Kosmos/face_recognition/fr/videoplayback (7).mp4')



























# # Python program to explain cv2.imwrite() method

# # importing cv2
# import cv2

# # importing os module
# import os

# # Image path
# image_path = r'C:\Users\Rajnish\Desktop\GeeksforGeeks\geeks.png'

# # Image directory
# directory = r'C:\Users\Rajnish\Desktop\GeeksforGeeks'

# # Using cv2.imread() method
# # to read the image
# img = cv2.imread(image_path)

# # Change the current directory
# # to specified directory
# os.chdir(directory)

# # List files and directories
# # in 'C:/Users/Rajnish/Desktop/GeeksforGeeks'
# print("Before saving image:")
# print(os.listdir(directory))

# # Filename
# filename = 'savedImage.jpg'

# # Using cv2.imwrite() method
# # Saving the image
# cv2.imwrite(filename, img)

# # List files and directories
# # in 'C:/Users / Rajnish / Desktop / GeeksforGeeks'
# print("After saving image:")
# print(os.listdir(directory))

# print('Successfully saved')
