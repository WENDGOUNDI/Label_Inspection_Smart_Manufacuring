# Product Labels Number Inspection for Smart Manufacuring
In smart manufacturing, product number correctness on product label is a crucial task that ensures the right product is being manufactured and distributed. Often, errors arrive while printing the label when the operator lack of attention. Such error may cause end of partnership between two parties, factories and customers, reducing the credibility of the manufacturer as well as impacting negatively their sales. Therefore, verifying such information is a crucial step. We can leverage computer vision in particular optical character recognition technology to verify that the product number on each product matches. In this practice, we develop a webapp to check to correctness of the product number

# Dependencies
 - Streamlit
 - PaddleOCR
 - PIL
 - IO
 - Opencv
 - Numpy
 - OS
 - Pickle
 
 # Dataset
 For this project, we develop our custom dataset. We generated some boxes with lables containing the information to verify. The product number is an hexadecimal number of 16 digits. We generated 100 positives samples and 17 negative samples. Product numbers of positive samples are saved in a pickle file, serving as a database for checking. Opencv is used for image processing, paddleocr used as our ocr engine for content extraction, streamlit to convert our code into a web app.
 
 ![label_73DE94DC0FE](https://user-images.githubusercontent.com/48753146/228176620-57678f1e-d72e-4d1f-86f1-18316c280893.png)
        data sample
        
        
 # Output
 While verifying a product (box here), the ouput is to detect if the product number is correct, present in our defined database or incorrect.
 
  - Sucecssful Product Number
  ![OK](https://user-images.githubusercontent.com/48753146/228178421-541497dc-2e2e-40b7-af19-ac2232e7f9ae.PNG)
  
  _ Wrong Product Number
  ![NG](https://user-images.githubusercontent.com/48753146/228178448-636b5c78-5545-4cc5-9da8-4f6bd2882629.PNG)
  
  - Video
  [screen-capture (3).webm](https://user-images.githubusercontent.com/48753146/228189001-9466648a-a879-4465-bcde-60f2edc9865d.webm)
 
