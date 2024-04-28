
# Valid Pose Estimation and 3D Model Generator

This project aims to create a 3D Model from valid user measurements, or even better, from user front and left side pictures. It uses the powerful framework from Google: Mediapipe. 
## Functionalities

#### measures.py

| Class / Method | Description     
| :-------- | :-------------------------------- |
| `Pose_Detection_Toolkit` | Contains the definition of all (almost) the mathematic functions like norm and angle_between_vectors need to verify the validity of the input images |
| `process(image=None)` |Checks the validity of the image and returns the `body landmarks`, whether the image `is_backward`, its `orientation`, whether it `is_valid`, the extracted `vectors`, the `image_height` and `image_width` and the `real_body_measurements` |


#### model.py

| Class / Method | Description     
| :-------- | :-------------------------------- |
| `generate_url(sex=0, bust=90.4, underbust=80.6, waist=80.2, hip=98.3, neckgirth=33.4, insideleg=76.3, shoulder=36.6, bodyheight=188.0)` | Establish a connection to `https://sadokbarbouche.github.io/3Dhumvis/` passing the validated measures in the url as a GET Request, so that the measurements are passed as parameters to generate the 3D Model. Special mention to Mr.`zishun` for the amazing threejs 3D Model generator we used (Modified a little bit but kept the main spirit) in order to create our own 3D  |
| `generate_model(url)` | Runs the 3D Model Generation  |




## Installation

#### Will be available ASAP
```python
  pip install modelgen
```
    

# Demo 


https://github.com/SadokBarbouche/3DHumanModelGenAndMeasureStreamlitApp/assets/99034622/706ac074-3ece-43cf-9f8c-2647da798797


