def cleanVideo(labelPath,featurePath):
    labels=np.zeros((0,1),'float')
    cleanLabels=np.zeros((0,1),'float')
    cam = cv2.VideoCapture(featurePath)
    labels=np.loadtxt(labelPath,delimiter=',')
    i=-1
    count=0
    fourcc = cv2.cv.CV_FOURCC(*'XVID')
    out = cv2.VideoWriter('cleanedVideo.avi',fourcc, 20.0, (640,480))
    while(cam.isOpened()):
        i=i+1
        ret, frame = cam.read()
        if ret==True:
            gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
            #cv2.imshow('frame',gray)
            if (labels[i]<sensorLow)|(labels[i]>sensorHigh):
                continue
            temp=np.vstack((cleanLabels,labels[i]))
            count=count+1
            out.write(gray)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            break
        cleanLabels=temp
    # Release everything if job is finished
    cam.release()
    out.release()
    cv2.destroyAllWindows()
    return count,cleanLabels,"cleanVideo.avi"
