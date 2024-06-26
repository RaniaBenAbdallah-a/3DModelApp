# We could use the std math library and it is faster in our case but for the sake of SIMD we will be using numpy (Optimization for later uses)
# Using a class for later imports
import matplotlib.pyplot as plt
import numpy as np
import cv2
import mediapipe as mp
import globals

# We could use the std math library and it is faster in our case but for the sake of SIMD we will be using numpy (Optimization for later uses)
# Using a class for later imports

#classe appelée Pose_Detection_Toolkit qui contient des méthodes pour la détection de pose et le calcul de mesures corporelles à partir de résultats de détection de pose.
class Pose_Detection_Toolkit:
    #Cette méthode calcule la circonférence d'une ellipse en fonction de ses demi-axes a et b C=π(a+b)(1+ 3*h/10+racine(4-3h)) avec h=h= 


    def eclipse_circumference(self, a, b):
        h = ((a - b)/(a + b)) ** 2
        return np.pi * (a+b) * (1 + (3*h / (10 + np.sqrt(4 - 3 * h))))
    # Cette méthode calcule la distance euclidienne entre deux vecteurs en utilisant la norme Euclidienne (np.linalg.norm)
    def distance(self, vector1, vector2):
        return np.linalg.norm(vector1 - vector2)  # Euclidean Norm / Norme 2
    # Cette méthode calcule la norme (longueur) d'un vecteur en utilisant la norme Euclidienne.
    def norm(self, vector):
        assert isinstance(vector, np.ndarray), 'input must be np array'
        return np.linalg.norm(vector)
    # Cette méthode calcule l'angle en degrés entre deux vecteurs en utilisant le produit scalaire et la norme des vecteurs.
    # Works in both 2D and 3D
    def angle_between_vectors(self, vector1, vector2):
        # A . B = norm(A) * norm(B) * cos(angle_between_vectors(A, B))
        # => arccos(angle_between_vectors(A, B)) = A.B / (norm(A) * norm(B))
        norm_A = np.linalg.norm(vector1)
        norm_B = np.linalg.norm(vector2)
        assert norm_A * norm_B != 0, 'Norms should be != 0'
        # Angle in deg not in rad
        return np.arccos(np.dot(vector1, vector2) / (norm_A * norm_B)) * 180 / np.pi
        # arcos : [-1,1] --> [0,pi]
    #Cette méthode génère des vecteurs à partir des résultats de détection de pose. Elle extrait les coordonnées des différents points d'intérêt comme les épaules, les coudes, les poignets, les hanches, les genoux, les chevilles, etc., et calcule les vecteurs correspondants.
    def generate_vectors(self, results, image_height, image_width):
        # Needed vectors : Both left and right
        # Shoulder-Elbow
        # Elbow-Wrist
        # Wrist-Index
        # Shoulder-Hip
        # Hip-Knee
        # Knee-Ankle
        # Ankle-FootIndex

        landmarks = results.pose_landmarks  #attribue à la variable "landmarks" les points clés de la pose extraits à partir des résultats de la détection de pose représentés par l'objet "results". Cela permet ensuite d'accéder et de manipuler ces points clés pour effectuer divers calculs ou analyses sur la pose détectée.




 

        mph_landmarks = mp_holistic.PoseLandmark  
        
        #epaule et coude 
        #La différence entre ces deux valeurs ("landmarks.landmark[mph_landmarks.LEFT_ELBOW].x - landmarks.landmark[mph_landmarks.LEFT_SHOULDER].x") calcule la distance horizontale entre le landmark du coude gauche et le landmark de l'épaule gauche dans l'image de la pose détectée.
        shoulder_elbow_left_x = landmarks.landmark[mph_landmarks.LEFT_ELBOW].x - \
            landmarks.landmark[mph_landmarks.LEFT_SHOULDER].x
        shoulder_elbow_right_x = landmarks.landmark[mph_landmarks.RIGHT_ELBOW].x - \
            landmarks.landmark[mph_landmarks.RIGHT_SHOULDER].x
        shoulder_elbow_left_y = landmarks.landmark[mph_landmarks.LEFT_ELBOW].y - \
            landmarks.landmark[mph_landmarks.LEFT_SHOULDER].y
        shoulder_elbow_right_y = landmarks.landmark[mph_landmarks.RIGHT_ELBOW].y - \
            landmarks.landmark[mph_landmarks.RIGHT_SHOULDER].y
        
        #poignet et coude
        elbow_wrist_left_y = landmarks.landmark[mph_landmarks.LEFT_WRIST].y - \
            landmarks.landmark[mph_landmarks.LEFT_ELBOW].y
        elbow_wrist_right_y = landmarks.landmark[mph_landmarks.RIGHT_WRIST].y - \
            landmarks.landmark[mph_landmarks.RIGHT_ELBOW].y
        elbow_wrist_left_x = landmarks.landmark[mph_landmarks.LEFT_WRIST].x - \
            landmarks.landmark[mph_landmarks.LEFT_ELBOW].x
        elbow_wrist_right_x = landmarks.landmark[mph_landmarks.RIGHT_WRIST].x - \
            landmarks.landmark[mph_landmarks.RIGHT_ELBOW].x
        
        #poignet et index
        wrist_index_left_x = landmarks.landmark[mph_landmarks.LEFT_WRIST].x - \
            landmarks.landmark[mph_landmarks.LEFT_INDEX].x
        wrist_index_right_x = landmarks.landmark[mph_landmarks.RIGHT_WRIST].x - \
            landmarks.landmark[mph_landmarks.RIGHT_INDEX].x
        wrist_index_left_y = landmarks.landmark[mph_landmarks.LEFT_WRIST].y - \
            landmarks.landmark[mph_landmarks.LEFT_INDEX].y
        wrist_index_right_y = landmarks.landmark[mph_landmarks.RIGHT_WRIST].y - \
            landmarks.landmark[mph_landmarks.RIGHT_INDEX].y
        
        #hanche et epaule
        shoulder_hip_left_x = landmarks.landmark[mph_landmarks.LEFT_SHOULDER].x - \
            landmarks.landmark[mph_landmarks.LEFT_HIP].x
        shoulder_hip_right_x = landmarks.landmark[mph_landmarks.RIGHT_SHOULDER].x - \
            landmarks.landmark[mph_landmarks.RIGHT_HIP].x
        shoulder_hip_left_y = landmarks.landmark[mph_landmarks.LEFT_SHOULDER].y - \
            landmarks.landmark[mph_landmarks.LEFT_HIP].y
        shoulder_hip_right_y = landmarks.landmark[mph_landmarks.RIGHT_SHOULDER].y - \
            landmarks.landmark[mph_landmarks.RIGHT_HIP].y
        #hanche et genou
        hip_knee_left_x = landmarks.landmark[mph_landmarks.LEFT_HIP].x - \
            landmarks.landmark[mph_landmarks.LEFT_KNEE].x
        hip_knee_left_y = landmarks.landmark[mph_landmarks.LEFT_HIP].y - \
            landmarks.landmark[mph_landmarks.LEFT_KNEE].y
        hip_knee_right_x = landmarks.landmark[mph_landmarks.RIGHT_HIP].x - \
            landmarks.landmark[mph_landmarks.RIGHT_KNEE].x
        hip_knee_right_y = landmarks.landmark[mph_landmarks.RIGHT_HIP].y - \
            landmarks.landmark[mph_landmarks.RIGHT_KNEE].y
        

        #cheville et genou
        knee_ankle_left_x = landmarks.landmark[mph_landmarks.LEFT_ANKLE].x - \
            landmarks.landmark[mph_landmarks.LEFT_KNEE].x
        knee_ankle_left_y = landmarks.landmark[mph_landmarks.LEFT_ANKLE].y - \
            landmarks.landmark[mph_landmarks.LEFT_KNEE].y
        knee_ankle_right_x = landmarks.landmark[mph_landmarks.RIGHT_ANKLE].x - \
            landmarks.landmark[mph_landmarks.RIGHT_KNEE].x
        knee_ankle_right_y = landmarks.landmark[mph_landmarks.RIGHT_ANKLE].y - \
            landmarks.landmark[mph_landmarks.RIGHT_KNEE].y
        

        #index du pied et cheville
        footindex_ankle_left_x = landmarks.landmark[mph_landmarks.LEFT_ANKLE].x - \
            landmarks.landmark[mph_landmarks.LEFT_FOOT_INDEX].x
        footindex_ankle_left_y = landmarks.landmark[mph_landmarks.LEFT_ANKLE].y - \
            landmarks.landmark[mph_landmarks.LEFT_FOOT_INDEX].y
        footindex_ankle_right_x = landmarks.landmark[mph_landmarks.RIGHT_ANKLE].x - \
            landmarks.landmark[mph_landmarks.RIGHT_FOOT_INDEX].x
        footindex_ankle_right_y = landmarks.landmark[mph_landmarks.RIGHT_ANKLE].y - \
            landmarks.landmark[mph_landmarks.RIGHT_FOOT_INDEX].y
        #entre les deux
        right_shoulder_left_shoulder_x = landmarks.landmark[mph_landmarks.LEFT_SHOULDER].x - \
            landmarks.landmark[mph_landmarks.RIGHT_SHOULDER].x
        right_shoulder_left_shoulder_y = landmarks.landmark[mph_landmarks.LEFT_SHOULDER].y - \
            landmarks.landmark[mph_landmarks.RIGHT_SHOULDER].y
        der_left_shoulder_y = results.pose_landmarks.landmark[mph_landmarks.LEFT_SHOULDER].y - \
            results.pose_landmarks.landmark[mph_landmarks.RIGHT_SHOULDER].y
        
        #talon et index du pied 
        footindex_heel_left_x = landmarks.landmark[mph_landmarks.LEFT_FOOT_INDEX].x - \
            landmarks.landmark[mph_landmarks.LEFT_HEEL].x
        footindex_heel_left_y = landmarks.landmark[mph_landmarks.LEFT_FOOT_INDEX].y - \
            landmarks.landmark[mph_landmarks.LEFT_HEEL].y

        footindex_heel_right_x = landmarks.landmark[mph_landmarks.RIGHT_FOOT_INDEX].x - \
            landmarks.landmark[mph_landmarks.RIGHT_HEEL].x
        footindex_heel_right_y = landmarks.landmark[mph_landmarks.RIGHT_FOOT_INDEX].y - \
            landmarks.landmark[mph_landmarks.RIGHT_HEEL].y
        
        
        # un dictionnaire contenant plusieurs vecteurs calculés à partir des landmarks détectés dans une image
        return {

            #Contient les vecteurs des épaules aux coudes pour les côtés gauche et droit de la pose.
            "shoulder_elbow": np.array([[shoulder_elbow_left_x * image_width, shoulder_elbow_left_y * image_height],
                                        [shoulder_elbow_right_x * image_width, shoulder_elbow_right_y * image_height]]),

            "elbow_wrist": np.array([[elbow_wrist_left_x * image_width, elbow_wrist_left_y * image_height],
                                     [elbow_wrist_right_x * image_width, elbow_wrist_right_y * image_height]]),
            "wrist_index": np.array([[wrist_index_left_x * image_width, wrist_index_left_y * image_height],
                                     [wrist_index_right_x * image_width, wrist_index_right_y * image_height]]),
            "shoulder_hip": np.array([[shoulder_hip_left_x * image_width, shoulder_hip_left_y * image_height],
                                      [shoulder_hip_right_x * image_width, shoulder_hip_right_y * image_height]]),
            "hip_knee": np.array([[hip_knee_left_x * image_width, hip_knee_left_y * image_height],
                                  [hip_knee_right_x * image_width, hip_knee_right_y * image_height]]),
            "knee_ankle": np.array([[knee_ankle_left_x * image_width, knee_ankle_left_y * image_height],
                                    [knee_ankle_right_x * image_width, knee_ankle_right_y * image_height]]),
            "footindex_ankle": np.array([[footindex_ankle_left_x * image_width, footindex_ankle_left_y * image_height],
                                         [footindex_ankle_right_x * image_width, footindex_ankle_right_y * image_height]]),
            "right_shoulder_left_shoulder": np.array([right_shoulder_left_shoulder_x * image_width, right_shoulder_left_shoulder_y * image_height]),
            "right_hip_left_hip": abs(landmarks.landmark[mph_landmarks.LEFT_HIP].x - landmarks.landmark[mph_landmarks.RIGHT_HIP].x) * image_width,
            "footindex_heel": np.array([[footindex_heel_left_x * image_width, footindex_heel_left_y * image_height], [footindex_heel_right_x * image_width, footindex_heel_right_y * image_height]])
        }
        # [0] for the left
        # [1] for the right
       



       #Cette fonction is_backward prend un dictionnaire de vecteurs en entrée et retourne True si la valeur x du vecteur "right_shoulder_left_shoulder" est inférieure à 0, ce qui signifie que l'image est orientée vers l'arrière. Sinon, elle retourne False, ce qui indique que l'image est orientée vers l'avant.
    def is_backward(self, vectors):  # Detect whether an image is backward or forward
        return vectors['right_shoulder_left_shoulder'][0] < 0
    


#****************************************************************************************************************************************
    # Need to find a way to get a more accurate angle range
    # utilise les vecteurs fournis pour calculer plusieurs angles entre différentes parties du corps
    def Pose_Dectection(self, vectors):
        # The needed angles are the following :
        # Between the shoulder_elbow vector and the shoulder_hip vector
        angle_se_sh_left = self.angle_between_vectors(
            vectors['shoulder_elbow'][0], -vectors['shoulder_hip'][0]) # Calcule l'angle entre le vecteur épaule-coude gauche et le vecteur épaule-hanche gauche.
        angle_se_sh_right = self.angle_between_vectors(
            vectors['shoulder_elbow'][1], -vectors['shoulder_hip'][1])
        # Between the hip_knee vector and the shoulder_hip vector
        angle_hk_sh_left = self.angle_between_vectors(
            vectors['hip_knee'][0], -vectors['shoulder_hip'][0])
        angle_hk_sh_right = self.angle_between_vectors(
            vectors['hip_knee'][1], -vectors['shoulder_hip'][1])
        # Between the elbow_wrist vector and the shoulder_elbow vector
        angle_ew_se_left = self.angle_between_vectors(
            vectors['elbow_wrist'][0], -vectors['shoulder_elbow'][0])
        angle_ew_se_right = self.angle_between_vectors(
            vectors['elbow_wrist'][1], -vectors['shoulder_elbow'][1])
        # Between the hip_knee vector and the knee_ankle vector
        angle_hk_ka_left = self.angle_between_vectors(
            vectors['hip_knee'][0], vectors['knee_ankle'][0])
        angle_hk_ka_right = self.angle_between_vectors(
            vectors['hip_knee'][1], vectors['knee_ankle'][1])

        # Verifying the shoulders and the knees angles
        # vérifie les angles des épaules et des genoux pour déterminer la pose
        #angle coudes / angles genoux
        # La A Pose est une position où les bras sont écartés de manière horizontale par rapport au corps, formant ainsi la lettre "A" lorsque vue de face
        #La T Pose est une position où les bras sont étendus latéralement par rapport au corps, formant ainsi la lettre "T" lorsque vue de face
        if 150 < angle_ew_se_left < 180 and 150 < angle_ew_se_right < 180 and 140 < angle_hk_ka_left < 180 and 140 < angle_hk_ka_right < 180:
            if 30 < angle_se_sh_left < 70 and 30 < angle_se_sh_right < 70:
                return "A Pose"
            elif 70 <= angle_se_sh_left < 110 and 70 <= angle_se_sh_right < 110:
                return "T Pose"
        return "Unknown Pose"

    # Checks whether the body in our image is turning to the left or the right
    def image_orientation(self, results, vectors):
        landmarks = results.pose_landmarks #extrait les repères de pose à partir des résultats fournis.
        mph_landmarks = mp_holistic.PoseLandmark

        right_shoulder_left_shoulder_x = landmarks.landmark[mph_landmarks.RIGHT_SHOULDER].x - \
            landmarks.landmark[mph_landmarks.LEFT_SHOULDER].x #clacul la difference horizontal entre l epaule gauche et droite 
        right_shoulder_left_shoulder_y = landmarks.landmark[mph_landmarks.RIGHT_SHOULDER].y - \
            landmarks.landmark[mph_landmarks.LEFT_SHOULDER].y  #clacul la difference vertical entre l epaule gauche et droite 
        right_shoulder_left_shoulder_z = landmarks.landmark[mph_landmarks.RIGHT_SHOULDER].z - \
            landmarks.landmark[mph_landmarks.LEFT_SHOULDER].z #selon l axe z calculons mla profondeurs 
        right_shoulder_left_shoulder = np.array(
            [right_shoulder_left_shoulder_x, right_shoulder_left_shoulder_y, right_shoulder_left_shoulder_z])  # Cela crée un vecteur à trois dimensions représentant la différence entre les positions des épaules droite et gauche.

        angle = self.angle_between_vectors(
            right_shoulder_left_shoulder, np.array([1, 0, 0])) # calcule l'angle entre le vecteur des épaules droite et gauche et un vecteur de référence horizontal (1, 0, 0).

        # This value is set by observation of some examples of correct and icorrect poses and can/should be corrected
        hand_threshold = 0.10898104310035706  #définit une valeur de seuil pour la position des mains par rapport aux hanches.

        hand_test = max(abs(landmarks.landmark[mph_landmarks.RIGHT_THUMB].x - landmarks.landmark[mph_landmarks.RIGHT_HIP].x),
                        abs(landmarks.landmark[mph_landmarks.LEFT_THUMB].x - landmarks.landmark[mph_landmarks.LEFT_HIP].x)) <= 0.109+hand_threshold
        

        #vérifie si la position des mains est correcte en comparant la distance entre les pouces et les hanches avec le seuil défini.
        ans = []

        if 85 < angle < 95:
            if landmarks.landmark[mph_landmarks.NOSE].x > landmarks.landmark[mph_landmarks.RIGHT_SHOULDER].x and landmarks.landmark[mph_landmarks.NOSE].x > landmarks.landmark[mph_landmarks.LEFT_SHOULDER].x:
                ans = ["RIGHT", hand_test]
            else:
                ans = ["LEFT", hand_test]
        else:
            ans = ["NO ORIENTATION", hand_test]

        # The test is to check whether the hands position is good or not
        return ans






    #vérifie si les résultats de la détection de la pose sont valides en fonction de certains critères
    def is_valid(self, results, vectors):
        landmarks = results.pose_landmarks   # Cette ligne extrait les repères de pose des résultats fournis

        if landmarks is None:
            return False
        


        # Cette liste contient les repères de pose qui sont essentiels pour déterminer la validité de la détection :/// required !!!!!!!!
        required_landmarks = [
            mp_holistic.PoseLandmark.RIGHT_EYE,
            mp_holistic.PoseLandmark.LEFT_EYE,
            mp_holistic.PoseLandmark.RIGHT_FOOT_INDEX,
            mp_holistic.PoseLandmark.LEFT_FOOT_INDEX
        ]

        for landmark in required_landmarks:
            x = landmarks.landmark[landmark].x
            y = landmarks.landmark[landmark].y

            if x < 0 or x > 1 or y < 0 or y > 1:  # Whether it is outside of the image or collapsed  : #Cette condition vérifie si le repère de pose se trouve en dehors de l'image ou est mal détecté (par exemple, si les coordonnées sont en dehors de la plage normale [0, 1]).
                return False
         



         #Cette ligne appelle la méthode image_orientation pour déterminer l'orientation de la personne dans l'image et effectuer un test sur la position des mains.
        [orientation, hand_test] = self.image_orientation(results, vectors)
        if orientation == 'LEFT' or orientation == 'RIGHT':
            if hand_test == False:
                return False

        return True
    # Sex is also an input !!
    # Shoulder width is also an input !!

    def get_real_measurements(self, results, vectors, real_shoulder_width):

        landmarks = results.pose_landmarks
        mph_landmarks = mp_holistic.PoseLandmark
        scale = real_shoulder_width / \
            self.norm(vectors['right_shoulder_left_shoulder'])
        print(
            f'Real shoulder width = {real_shoulder_width} /Norm in the pic {self.norm(vectors["right_shoulder_left_shoulder"])} = {scale}')

        def hip_size():
            a = vectors['right_hip_left_hip'] / 2
            b = vectors['right_hip_left_hip'] / 3
            hip = self.eclipse_circumference(a, b)
            return hip

        def bust_size():
            sh = float(globals.shoulder_width)
            print(sh)
            a = sh * 0.9 / 2
            b = sh * 0.9 / 4
            bust = self.eclipse_circumference(a, b)
            return bust

        def underbust_size():
            print(float(bust_size() * 0.95))
            return float(bust_size() * 0.95)

        def waist_size():
            waist = hip_size() * 0.9
            return waist

        def insideleg_size():
            insideleg = max(self.norm(vectors['hip_knee'][0]) + self.norm(vectors['knee_ankle'][0]), self.norm(
                vectors['hip_knee'][1] + self.norm(vectors['knee_ankle'][1])))
            return insideleg

        bust = max(min(bust_size(), 113.0), 79.0)
        underbust = max(min(underbust_size(), 101.0), 70.0)
        waist = max(min(waist_size(), 113.0), 52.0)
        hip = max(min(hip_size()*scale, 121.0), 79.0)
        insideleg = max(min(insideleg_size()*scale, 95.0), 65.0)

        return {
            "bust": bust,
            "underbust": underbust,
            "waist": waist,
            "hip": hip,
            "neckgirth": 33.4,
            "insideleg": insideleg,
            "shoulder": globals.shoulder_width,
            "bodyheight": 180
        }

    # def get_real_measurements(self, results, vectors, real_shoulder_width, front_image=None, left_image=None):

    #     landmarks = results.pose_landmarks
    #     mph_landmarks = mp_holistic.PoseLandmark
    #     pixel_to_real_ratio = real_shoulder_width / \
    #         self.norm(vectors['right_shoulder_left_shoulder'])

    #     print(
    #         f"vector : {self.norm(vectors['right_shoulder_left_shoulder'])}")
    #     # Calculate real measurements
    #     shoulders, hip, underbust, bust, waist, insideleg = 0, 0, 0, 0, 0, 0
    #     if front_image:
    #         shoulders += vectors['right_shoulder_left_shoulder'][0] * \
    #             pixel_to_real_ratio * 2.1
    #         hip += shoulders * 0.9
    #         underbust += hip * 1.15
    #         bust += self.norm(vectors['shoulder_hip']) * \
    #             pixel_to_real_ratio * 2.2
    #         waist += self.norm(
    #             vectors['right_shoulder_left_shoulder']) * pixel_to_real_ratio * 0.85
    #         insideleg += max(self.norm(vectors['hip_knee'][0]) + self.norm(vectors['knee_ankle'][0]), self.norm(
    #             vectors['hip_knee'][1] + self.norm(vectors['knee_ankle'][1]))) * pixel_to_real_ratio

    #     if left_image:
    #         shoulders += vectors['right_shoulder_left_shoulder'][0] * \
    #             pixel_to_real_ratio * 2.1
    #         hip += shoulders * 0.9
    #         underbust += hip * 1.15
    #         bust += self.norm(vectors['shoulder_hip']) * \
    #             pixel_to_real_ratio * 2.2
    #         waist += self.norm(
    #             vectors['right_shoulder_left_shoulder']) * pixel_to_real_ratio * 0.85
    #         insideleg += max(self.norm(vectors['hip_knee'][0]) + self.norm(vectors['knee_ankle'][0]), self.norm(
    #             vectors['hip_knee'][1] + self.norm(vectors['knee_ankle'][1]))) * pixel_to_real_ratio

    #     bodyheight = 180.0
    #     # Ensure the values are within the specified ranges
    #     bust = max(min(bust, 113.0), 79.0)
    #     underbust = max(min(underbust, 101.0), 70.0)
    #     waist = max(min(waist, 113.0), 52.0)
    #     hip = max(min(hip, 121.0), 79.0)
    #     insideleg = max(min(insideleg, 95.0), 65.0)
    #     shoulder = max(min(shoulder, 60.0), 29.0)

    #     return {"bust": bust,
    #             "underbust": underbust,
    #             "waist": waist,
    #             "hip": hip,
    #             "neckgirth": 33.4,
    #             "insideleg": insideleg,
    #             "shoulder": shoulders,
    #             "bodyheight": bodyheight
    #             }


class Body:

    # initialisation d'une classe qui stocke les différentes parties du corps détectées lors de l'analyse de la pose
    def __init__(self, **kwargs):
        self._left_eye = kwargs.get('left_eye', None) 
        self._right_eye = kwargs.get('right_eye', None)
        self._nose = kwargs.get('nose', None)
        self._left_shoulder = kwargs.get('left_shoulder', None)
        self._right_shoulder = kwargs.get('right_shoulder', None)
        self._left_elbow = kwargs.get('left_elbow', None)
        self._right_elbow = kwargs.get('right_elbow', None)
        self._left_wrist = kwargs.get('left_wrist', None)
        self._right_wrist = kwargs.get('right_wrist', None)
        self._left_hip = kwargs.get('left_hip', None)
        self._right_hip = kwargs.get('right_hip', None)
        self._left_knee = kwargs.get('left_knee', None)
        self._right_knee = kwargs.get('right_knee', None)
        self._left_ankle = kwargs.get('left_ankle', None)
        self._right_ankle = kwargs.get('right_ankle', None)
        self._left_heel = kwargs.get('left_heel', None)
        self._right_heel = kwargs.get('right_heel', None)
        self._left_foot_index = kwargs.get('left_foot_index', None)
        self._right_foot_index = kwargs.get('right_foot_index', None)

    def set_attributes(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, f"_{key}", value)

    def get_attributes(self):
        return {
            'left_eye': self._left_eye,
            'right_eye': self._right_eye,
            'nose': self._nose,
            'left_shoulder': self._left_shoulder,
            'right_shoulder': self._right_shoulder,
            'left_elbow': self._left_elbow,
            'right_elbow': self._right_elbow,
            'left_wrist': self._left_wrist,
            'right_wrist': self._right_wrist,
            'left_hip': self._left_hip,
            'right_hip': self._right_hip,
            'left_knee': self._left_knee,
            'right_knee': self._right_knee,
            'left_ankle': self._left_ankle,
            'right_ankle': self._right_ankle,
            'left_heel': self._left_heel,
            'right_heel': self._right_heel,
            'left_foot_index': self._left_foot_index,
            'right_foot_index': self._right_foot_index
        }


mp_drawing = mp.solutions.drawing_utils #importez la fonctionnalité de dessin  et les stocker dans mp-drawing
mp_drawing_styles = mp.solutions.drawing_styles  #importez le style de desin et le stocker 
mp_holistic = mp.solutions.holistic  # importez le module de détection holistique de MediaPipe et le stockez dans la variable mp_holistic. Ce module permet de détecter et de suivre simultanément plusieurs éléments tels que les points clés du corps, les points clés du visage et les parties du visage.
mp_face_detection = mp.solutions.face_detection  # importez le module de détection faciale de MediaPipe et le stockez dans la variable mp_face_detection. Ce module permet de détecter les visages dans une image ou une vidéo.
mp_pose = mp.solutions.pose   #importez le module de détection de poses de MediaPipe et le stockez dans la variable mp_pose. Ce module permet de détecter les poses du corps humain, y compris les positions des articulations et des membres


def process(image=None):

    IMAGE_FILES = []

    # For static images:
    if image is not None:
        IMAGE_FILES.append(image)

    else:
        return None

    pdtk = Pose_Detection_Toolkit()

    BG_COLOR = (192, 192, 192)  # gray
    with mp_holistic.Holistic(
            static_image_mode=True,
            model_complexity=2,
            enable_segmentation=True,
            refine_face_landmarks=True) as holistic:
        for idx, file in enumerate(IMAGE_FILES):
            image = cv2.imread(file)
            image_height, image_width, _ = image.shape
            # Convert the BGR image to RGB before processing.
            results = holistic.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

            if results.pose_landmarks is None:
                print(f"No pose landmarks detected in {file}. Skipping...")
                continue

            # for attr, value in attributes.items():
            #     print(f"{attr}: {value}")

            vectors = pdtk.generate_vectors(results, image_height, image_width)

            # print(f'is my image backward ? : {pdtk.is_backward(vectors)}')
            # print(f'is my image valid ? does it contain all the needed points ? : {pdtk.is_valid(results)}')
            # print(f'In what pose is my image ? : {pdtk.Pos_Dectection(vectors)}')

            condition = 0
            annotated_image = image.copy()
            if results.segmentation_mask is not None:
                condition = np.stack(
                    (results.segmentation_mask,) * 3, axis=-1) > 0.1
            bg_image = np.zeros(image.shape, dtype=np.uint8)
            bg_image[:] = BG_COLOR
            annotated_image = np.where(condition, annotated_image, bg_image)
            # Draw pose, left and right hands, and face landmarks on the image.
            mp_drawing.draw_landmarks(
                annotated_image,
                results.face_landmarks,
                mp_holistic.FACEMESH_TESSELATION,
                landmark_drawing_spec=None,
                connection_drawing_spec=mp_drawing_styles
                .get_default_face_mesh_tesselation_style())
            mp_drawing.draw_landmarks(
                annotated_image,
                results.pose_landmarks,
                mp_holistic.POSE_CONNECTIONS,
                landmark_drawing_spec=mp_drawing_styles.
                get_default_pose_landmarks_style())
            plt.imshow(image)

            body = Body()

            if results.pose_landmarks is not None:
                body.set_attributes(
                    left_eye=results.pose_landmarks.landmark[mp_holistic.PoseLandmark.LEFT_EYE],
                    right_eye=results.pose_landmarks.landmark[mp_holistic.PoseLandmark.RIGHT_EYE],
                    nose=results.pose_landmarks.landmark[mp_holistic.PoseLandmark.NOSE],
                    left_shoulder=results.pose_landmarks.landmark[mp_holistic.PoseLandmark.LEFT_SHOULDER],
                    right_shoulder=results.pose_landmarks.landmark[
                        mp_holistic.PoseLandmark.RIGHT_SHOULDER],
                    left_elbow=results.pose_landmarks.landmark[mp_holistic.PoseLandmark.LEFT_ELBOW],
                    right_elbow=results.pose_landmarks.landmark[mp_holistic.PoseLandmark.RIGHT_ELBOW],
                    left_wrist=results.pose_landmarks.landmark[mp_holistic.PoseLandmark.LEFT_WRIST],
                    right_wrist=results.pose_landmarks.landmark[mp_holistic.PoseLandmark.RIGHT_WRIST],
                    left_hip=results.pose_landmarks.landmark[mp_holistic.PoseLandmark.LEFT_HIP],
                    right_hip=results.pose_landmarks.landmark[mp_holistic.PoseLandmark.RIGHT_HIP],
                    left_knee=results.pose_landmarks.landmark[mp_holistic.PoseLandmark.LEFT_KNEE],
                    right_knee=results.pose_landmarks.landmark[mp_holistic.PoseLandmark.RIGHT_KNEE],
                    left_ankle=results.pose_landmarks.landmark[mp_holistic.PoseLandmark.LEFT_ANKLE],
                    right_ankle=results.pose_landmarks.landmark[mp_holistic.PoseLandmark.RIGHT_ANKLE],
                    left_heel=results.pose_landmarks.landmark[mp_holistic.PoseLandmark.LEFT_HEEL],
                    right_heel=results.pose_landmarks.landmark[mp_holistic.PoseLandmark.RIGHT_HEEL],
                    left_foot_index=results.pose_landmarks.landmark[
                        mp_holistic.PoseLandmark.LEFT_FOOT_INDEX],
                    right_foot_index=results.pose_landmarks.landmark[
                        mp_holistic.PoseLandmark.RIGHT_FOOT_INDEX]
                )

            attributes = body.get_attributes()
            infos = {
                'body landmarks': attributes,
                'is_backward': pdtk.is_backward(vectors),
                'orientation': pdtk.image_orientation(results, vectors),
                'is_valid': pdtk.is_valid(results, vectors),
                'pose': pdtk.Pose_Dectection(vectors),
                'vectors': vectors,
                'image_height': image.shape[0],
                'image_width': image.shape[1],
                'real_body_measurements': pdtk.get_real_measurements(results, vectors, float(globals.shoulder_width))
            }
            return body, infos
