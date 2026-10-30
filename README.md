<img src="https://capsule-render.vercel.app/api?type=waving&color=0:1F497D,100:3A7BD5&height=170&section=header&text=Aleksandr%20Chernysh&fontSize=42&fontColor=ffffff&fontAlignY=35&desc=Data%20Science%20%40%20Texas%20State%20%E2%80%A2%20Eye%20Tracking%20%26%20Biometrics&descSize=16&descAlignY=58" width="100%"/>

<p align="center">
  <a href="https://www.linkedin.com/in/aleksandr-chernysh/"><img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=flat-square&logo=linkedin&logoColor=white"/></a>
  <a href="https://orcid.org/0009-0008-1213-8089"><img src="https://img.shields.io/badge/ORCID-A6CE39?style=flat-square&logo=orcid&logoColor=white"/></a>
  <a href="https://arxiv.org/abs/2610.32915"><img src="https://img.shields.io/badge/arXiv-2610.32915-B31B1B?style=flat-square&logo=arxiv&logoColor=white"/></a>
  <a href="mailto:wll46@txstate.edu"><img src="https://img.shields.io/badge/Email-wll46%40txstate.edu-555555?style=flat-square&logo=maildotru&logoColor=white"/></a>
  <img src="https://img.shields.io/badge/Texas%20State%20University-501214?style=flat-square"/>
</p>

## About Me

Data Science undergraduate in the **Honors College at Texas State University** and undergraduate researcher in the **OK Lab** with Dr. Oleg Komogortsev. I work on **eye tracking in VR headsets** and **eye-movement biometrics**: measuring how good headset eye trackers really are, and teaching models to recognize people from how their eyes move.

```python
aleksandr = {
    "education":   "B.S. Data Science, Texas State University (Honors), 2029",
    "gpa":         4.0,
    "focus":       ["eye tracking", "biometrics", "deep metric learning", "VR"],
    "languages":   ["Python", "SQL", "C++", "C#"],
    "research":    "adapting eye-movement biometric models to consumer VR headsets",
    "spoken":      ["English", "Russian"],
}
```

## Tech Stack

**Languages**
<br/>
<img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white"/>
<img src="https://img.shields.io/badge/SQL-4479A1?style=flat-square&logo=postgresql&logoColor=white"/>
<img src="https://img.shields.io/badge/C%2B%2B-00599C?style=flat-square&logo=cplusplus&logoColor=white"/>
<img src="https://img.shields.io/badge/C%23-512BD4?style=flat-square"/>
<img src="https://img.shields.io/badge/LaTeX-008080?style=flat-square&logo=latex&logoColor=white"/>

**Data & ML**
<br/>
<img src="https://img.shields.io/badge/PyTorch-EE4C2C?style=flat-square&logo=pytorch&logoColor=white"/>
<img src="https://img.shields.io/badge/Lightning-792EE5?style=flat-square&logo=lightning&logoColor=white"/>
<img src="https://img.shields.io/badge/scikit--learn-F7931E?style=flat-square&logo=scikitlearn&logoColor=white"/>
<img src="https://img.shields.io/badge/pandas-150458?style=flat-square&logo=pandas&logoColor=white"/>
<img src="https://img.shields.io/badge/NumPy-013243?style=flat-square&logo=numpy&logoColor=white"/>
<img src="https://img.shields.io/badge/SciPy-8CAAE6?style=flat-square&logo=scipy&logoColor=white"/>
<img src="https://img.shields.io/badge/OpenCV-5C3EE8?style=flat-square&logo=opencv&logoColor=white"/>
<img src="https://img.shields.io/badge/MediaPipe-0097A7?style=flat-square"/>

**VR & Eye Tracking**
<br/>
<img src="https://img.shields.io/badge/Unity-000000?style=flat-square&logo=unity&logoColor=white"/>
<img src="https://img.shields.io/badge/Meta%20Quest%20Pro-0467DF?style=flat-square&logo=meta&logoColor=white"/>
<img src="https://img.shields.io/badge/HTC%20VIVE-00B2A9?style=flat-square"/>

**Tools**
<br/>
<img src="https://img.shields.io/badge/Git-F05032?style=flat-square&logo=git&logoColor=white"/>
<img src="https://img.shields.io/badge/Linux-FCC624?style=flat-square&logo=linux&logoColor=black"/>
<img src="https://img.shields.io/badge/GPU%20servers%20(SSH)-76B900?style=flat-square&logo=nvidia&logoColor=white"/>

## GitHub Analytics

<p align="center">
  <img height="165" src="https://github-readme-stats.vercel.app/api?username=AleksandrChernysh&show_icons=true&count_private=true&include_all_commits=true&theme=github_dark&hide_border=true"/>
</p>

## Research

### 📄 What Mean Error Misses: Eye Tracking Signal Quality in Three VR Headsets
`Python` · `Unity/C#` · first author, submitted to ACM ETRA 2027

A 30-participant comparison of the eye trackers in Meta Quest Pro, HTC VIVE Pro Eye and HTC VIVE Focus Vision under one protocol. Device-clock diagnostics showed data loss that mean error hides: the Quest Pro paused for up to 6 s and reported closed eyes as valid gaze. First published evaluation of the Focus Vision eye tracker. Dataset and code are public.

<a href="https://arxiv.org/abs/2610.32915"><img src="https://img.shields.io/badge/Paper-arXiv-B31B1B?style=flat-square"/></a>
<a href="https://hdl.handle.net/10877/25342"><img src="https://img.shields.io/badge/Dataset-TXST%20repository-501214?style=flat-square"/></a>
<a href="https://hdl.handle.net/10877/25343"><img src="https://img.shields.io/badge/Code-TXST%20repository-501214?style=flat-square"/></a>

### 👁️ Eye-Movement Biometrics on Meta Quest Pro *(in progress)*
`Python` · `PyTorch`

Making eye-movement authentication work on a consumer VR headset by training on public lab-grade data degraded to headset signal quality.

## Featured Projects

### 🧬 Eye Know You Too — re-implementation
`Python` · `PyTorch Lightning`

A deep metric-learning model that identifies people from 5 s of eye movements, trained on the public GazeBase dataset with subject-disjoint evaluation.

<a href="https://github.com/AleksandrChernysh/ekyt-reimplementation"><img src="https://img.shields.io/badge/View%20Repo-181717?style=flat-square&logo=github"/></a>

### ⌨️ Webcam Gaze Tracker and Gaze-Controlled Keyboard
`Python` · `OpenCV` · `MediaPipe` · `scikit-learn`

Real-time eye tracking with an ordinary laptop webcam: calibration, built-in accuracy and precision measurement, and an on-screen keyboard you type on with your eyes.

<a href="https://github.com/AleksandrChernysh/webcam-gaze-keyboard"><img src="https://img.shields.io/badge/View%20Repo-181717?style=flat-square&logo=github"/></a>

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:3A7BD5,100:1F497D&height=110&section=footer" width="100%"/>
