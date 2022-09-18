<h1 align="center"> SignSpeak </h1>
<h2 align="center"> A real-time sign language translation tool </h2>

[![Project Status: Active](https://www.repostatus.org/badges/latest/active.svg)](https://www.repostatus.org/#active)

## Table of Contents
* **[Motivation](#motivation)**
* **[Hand Detection](#hand-detection)**
* **[Detection Output](#detection-output)**
* **[Tech Stack](#tech-stack)**
* **[Functionalities](#functionalities)**
* **[To Do and Further Improvements](#to-do-and-further-improvements)**
* **[Requriements](#requirements)**
* **[Run Locally](#run-locally)**
* **[License](#license)**
* **[Contributors](#contributors)**

## Motivation
Physically impaired people find it hard to communicate with other humans or latest
computing innovations in conversational AI. They normally communicate via sign languages
which is often a mix of hand gestures and facial expressions. A
computer interface which can interpret their hand gestures from a single camera view and
convert it into text or speech transcript would be really beneficial for both parties. We are dealing with static signs for simplicity
but a similar concept can be utilized for developing dynamic sign recognition. This system
can help in effective human computer interaction for impaired persons which can be utilized
for Customer Support, virtual meetings etc.

## Hand Detection
The crux of this solution lies in identifying the presence of a hand in the video feed/image. This is done using various modules like OpenCV, cvzone and mediapipe. 

## Home Page
![Home Page](https://raw.githubusercontent.com/prabhav5112/sign-speak/main/media/Home.png)
## FAQs
![FAQs](https://raw.githubusercontent.com/prabhav5112/sign-speak/main/media/FAQs.png)
## Detection of a character/digit in an image 
![Detection of a character/digit in an image](https://raw.githubusercontent.com/prabhav5112/sign-speak/main/media/ImgPredict.png)
## Character/digit recognised 
![Character/digit recognised](https://raw.githubusercontent.com/prabhav5112/sign-speak/main/media/PredictAnswer.png)
## Detection Output 1 
![Detection Output 1](https://raw.githubusercontent.com/prabhav5112/sign-speak/main/media/A.png)
## Detection Output 2
![Detection Output 2](https://raw.githubusercontent.com/prabhav5112/sign-speak/main/media/B.png)
## A single frame from a video
<p align="center">
  <img src="https://raw.githubusercontent.com/prabhav5112/sign-speak/main/media/I.jpeg" alt="animated" />
</p>




## Tech Stack
* HTML, CSS and Bootstrap have been used for the front-end
* Flask has been used as a back-end framework
* The application has been developed using Python


## Functionalities
* Detect a hand shown in the video feed/image.
* Draw a box around the hand which has been detected.
* Display the character/digit recognised.


## To Do and Further Improvements
- [x] Using OpenCV, cvzone and mediapipe for hand detection
- [x] Develop an algorithm which can automatically classify sign language from a video taken from a webcam and convert it to text/speech transcript.
- [x] Display the charcter/digit shown 
- [x] Detect and draw a box around a hand (if present) for an image, video/live stream.
- [ ] Adding a button to turn on/off video feed
- [ ] Updating the simple and minimalistic UI

## Requirements
The following dependencies and modules(python) are required, to run this locally 
* opencv-python==4.6.0.66
* flask==2.2.2
* wtforms==3.0.0
* flask_wtf==1.0.1
* tensorflow==2.9.2
* mediapipe
* cvzone

## Run Locally
- **Clone the GitHub repository**
```python
$ git clone git@github.com:prabhav5112/sign-speak.git
```

- **Move to the Project Directory**
```python
$ cd sign-speak
```

- **Create a Virtual Environment (Optional)**

   * Install Virtualenv using pip (If it is not installed)
   ```python
    $ pip install virtualenv
    ```
   * Create the Virtual Environment
   ```python
   $ virtualenv sgnspk
   ```
   * Activate the Virtual Environment 
   
      * In MAC OS/Linux 
      ```python
      $ source sgnspk/bin/activate
      ```
      * In Windows
      ```python
      $ sgnspk\Scripts\activate
      ```
  
- **Install the [requirements](requirements.txt)**
```python
(sgnspk) $ pip install -r requirements.txt
```

- **Run the python script [main.py](main.py)**
```python
(sgnspk) $ python3 main.py
```



- **Dectivate the Virtual Environment (after you are done)**
```python
(sgnspk) $ deactivate
```

## License 
[![License](https://img.shields.io/badge/License-Apache%202.0-red.svg)](https://opensource.org/licenses/Apache-2.0)
<br/>
This project is under the Apache-2.0 License License. See [LICENSE](LICENSE) for Details.

## Contributors
<table>
  <tr>
    <td align="center"><img src="https://avatars.githubusercontent.com/u/91932766?s=400&v=4" width="100px;" height="100px;" alt=""/><br/><sub><b>Prabhav B Kashyap</b></sub></a><br/><p align="center">
      <p align="center">
        <a href="https://www.linkedin.com/in/prabhav-b-kashyap/" alt="Linkedin">
          <img src="http://www.iconninja.com/files/863/607/751/network-linkedin-social-connection-circular-circle-media-icon.svg" width = "30">
        </a>
        <a href="https://github.com/prabhav5112" alt="Github">
          <img src="http://www.iconninja.com/files/241/825/211/round-collaboration-social-github-code-circle-network-icon.svg" width = "30">
        </a>
      </p>
    </td>
    <td align="center"><img src="https://avatars.githubusercontent.com/u/97429792?v=4" width="100px;" height="100px;" alt=""/><br/><sub><b>Sridhar D Kedlaya</b></sub></a><br/><p align="center">
      <p align="center">
        <a href="https://www.linkedin.com/in/sridhar-d-kedlaya-92b928232/" alt="Linkedin">
          <img src="http://www.iconninja.com/files/863/607/751/network-linkedin-social-connection-circular-circle-media-icon.svg" width = "30">
        </a>
        <a href="https://github.com/DeathStroke19891" alt="Github">
          <img src="http://www.iconninja.com/files/241/825/211/round-collaboration-social-github-code-circle-network-icon.svg" width = "30">
        </a>
      </p>
    </td>
    <td align="center"><img src="https://avatars.githubusercontent.com/u/96238706?v=4" width="100px;" height="100px;" alt=""/><br/><sub><b>Imon Banerjee</b></sub></a><br/><p align="center">
      <p align="center">
        <a href="https://www.linkedin.com/in/imon-banerjee-071863a5/" alt="Linkedin">
          <img src="http://www.iconninja.com/files/863/607/751/network-linkedin-social-connection-circular-circle-media-icon.svg" width = "30">
        </a>
        <a href="https://github.com/imonbanerjee1" alt="Github">
          <img src="http://www.iconninja.com/files/241/825/211/round-collaboration-social-github-code-circle-network-icon.svg" width = "30">
        </a>
      </p>
    </td>
  </tr>
</table>
