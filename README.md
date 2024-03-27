# ResumeScreener
Working : The UpadtedResumeData contains 962 different data points. Each row consists of a resume and category in which that resume belongs. 80% of this data is used to train a KNN (K-Nearest Neighbour classifier) and stored using a pickle file named "clf.pkl". Other file "tfidf.pkl" contains the details of word vectors that are formed. 

I have created a API that uses basic authorization and then user can send their resume text and it will use ML models to identify which job role is best suited for you.

Direction to use:

1) Clone the file in your personal computer in any folder.
2) Locate the folder and open with VS code
3) Open terminal and run the command "py main.py"
4) Now use the PostMan API environment to see the below functionalities of the working code.
5) First copy the localhost path or API where the code is running and create a new GET request in postman where you paste this API

i) On clicking send request, we can see the 200 status 
![image](https://github.com/dishhaa03/ResumeScreener/assets/110946892/d4e0c862-9789-4354-bfbb-9bc72f35c4e3)
ii) Set-up Authorization: Create a new post request on the API + "/home" route. In the "authorization" tab choose BasicAuth and enter the details - username and password.
![image](https://github.com/dishhaa03/ResumeScreener/assets/110946892/9476d392-21d1-4e6f-8d59-59b4a5461f4e)
iii) Set-up the input data: In the "body" tab choose raw data and json format, and enter the resume_text. Please note that the copied resume data must be in a single line, format your data accordingly.
![image](https://github.com/dishhaa03/ResumeScreener/assets/110946892/df4584a9-5368-46c0-9a80-27a95467acaf)
iv) Click on send request, we can see the 200 status and desired output in the json format.
![image](https://github.com/dishhaa03/ResumeScreener/assets/110946892/f528fbfb-7763-41fa-83ea-cb206e1af4c1)

v) Let us check what happens if we enetr the incorrect authorization details, we can see the 401 UNAUTHORIZED message status.
![image](https://github.com/dishhaa03/ResumeScreener/assets/110946892/e58307b4-3bb5-48ae-8be4-35a906ae6447)

