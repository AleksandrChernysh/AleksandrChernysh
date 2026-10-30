<p align="center">
  <img src="assets/header.svg" width="100%" alt="Aleksandr Chernysh — eye tracking, VR headsets, eye-movement biometrics"/>
</p>

<p align="center">
  <a href="https://www.linkedin.com/in/aleksandr-chernysh/"><img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white"/></a>
  <a href="https://arxiv.org/abs/2610.32915"><img src="https://img.shields.io/badge/arXiv-2610.32915-B31B1B?style=for-the-badge&logo=arxiv&logoColor=white"/></a>
  <a href="https://orcid.org/0009-0008-1213-8089"><img src="https://img.shields.io/badge/ORCID-A6CE39?style=for-the-badge&logo=orcid&logoColor=white"/></a>
  <a href="mailto:wll46@txstate.edu"><img src="https://img.shields.io/badge/Email-wll46%40txstate.edu-30363d?style=for-the-badge"/></a>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Open%20to-Summer%202027%20internships%20·%20ML%20·%20Data%20Science%20·%20Eye%20Tracking-2ea043?style=flat-square"/>
</p>

I study **Data Science at Texas State University** (Honors College, 4.0) and do research in the **OK Lab** with Dr. Oleg Komogortsev. My work sits where hardware meets ML: I measure how good the eye trackers in VR headsets really are, and I train models that recognize people from the way their eyes move.

- 🔬 **Now:** adapting eye-movement biometric models to Meta Quest Pro, using public lab-grade data degraded to headset signal quality
- 📄 **Recently:** first-authored a 30-participant comparison of three VR eye trackers (submitted to ACM ETRA 2027)
- 🛠️ **Learning:** SQL and larger-scale multi-dataset training

## 📄 Research

<a href="https://arxiv.org/abs/2610.32915"><img src="assets/results.svg" width="100%" alt="Median participant mean error: Meta Quest Pro 1.04°, HTC VIVE Pro Eye 1.50°, HTC VIVE Focus Vision 2.41°"/></a>

Thirty people, three headsets, one protocol. Mean error ranks the headsets, but diagnostics on each device's own clock show what it hides: multi-second stream pauses, closed eyes reported as valid gaze, and heavy internal filtering. It is also the first published evaluation of the VIVE Focus Vision eye tracker. I led data collection, adapted the Unity acquisition apps to all three headsets, built the analysis pipeline, and released the data and code.

<a href="https://arxiv.org/abs/2610.32915"><img src="https://img.shields.io/badge/Paper-arXiv-B31B1B?style=flat-square"/></a>
<a href="https://hdl.handle.net/10877/25342"><img src="https://img.shields.io/badge/Dataset-N%3D30-501214?style=flat-square"/></a>
<a href="https://hdl.handle.net/10877/25343"><img src="https://img.shields.io/badge/Code-acquisition%20%2B%20analysis-501214?style=flat-square"/></a>

## 🧪 Projects

<table>
<tr>
<td width="50%" valign="top">

### [👁️ Eye Know You Too](https://github.com/AleksandrChernysh/ekyt-reimplementation)
Re-implementation of a deep metric-learning model that identifies a person from **5 seconds of eye movements**. Trained on GazeBase with subject-disjoint evaluation.

`PyTorch Lightning` `metric learning` `biometrics`

</td>
<td width="50%" valign="top">

### [⌨️ Webcam Gaze Keyboard](https://github.com/AleksandrChernysh/webcam-gaze-keyboard)
Real-time eye tracking with an ordinary laptop webcam — calibration, built-in accuracy measurement (~2°), and a keyboard you type on with your eyes.

`OpenCV` `MediaPipe` `scikit-learn`

</td>
</tr>
</table>

## 🧰 Tools

<p>
  <img src="https://skillicons.dev/icons?i=py,pytorch,sklearn,postgres,cpp,cs,unity,matlab,latex,git,linux,vscode&perline=12" alt="Python, PyTorch, scikit-learn, SQL, C++, C#, Unity, MATLAB, LaTeX, Git, Linux, VS Code"/>
</p>

Also: pandas · NumPy · SciPy · OpenCV · MediaPipe · Meta Quest Pro · HTC VIVE · GPU servers over SSH

---

<sub>The header and research card are animated SVGs generated with Python — see <a href="assets/make_svgs.py"><code>assets/make_svgs.py</code></a>. The header shows a scanpath: numbered circles are fixations (size ∝ duration), lines are saccades, the dashed line is a regression.</sub>
