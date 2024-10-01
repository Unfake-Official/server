<h1 align="center" style="font-weight: bold;">💻 Unfake Core</h1>

<div align="center">
  <img src="https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54" alt="python"/>
  <img src="https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white" alt="flask"/>
  <img src="https://img.shields.io/badge/TensorFlow-%23FF6F00.svg?style=for-the-badge&logo=TensorFlow&logoColor=white" alt="tensorflow"/>
  <img src="https://img.shields.io/badge/Keras-%23D00000.svg?style=for-the-badge&logo=Keras&logoColor=white" alt="keras"/>
</div>

<p align="center">
 <a href="#about">About</a> • 
 <a href="#started">Getting Started</a> • 
 <a href="#routes">API Endpoints</a> •
 <a href="#contribute">Contribute</a>
</p>

<h2 id="about">📌 About the project</h2>
<p>
The growing evolution of artificial intelligence (A.I.) tools is making them increasingly efficient and globally accessible. However, some of these technologies can be harmful if used maliciously, and that includes deepfakes. Deepfakes are a type of synthetic media that generates realistic content and has the potential to clone an individual's identity, using it to spread fake news, damage their reputation and promote fraud and security breaches. Thus, there is a need for ways to verify whether a piece of media is real or artificially synthesized. However, even though there are technologies that meet this need, the detection of audio deepfakes is still a challenge, considering that it is not as effective when it comes to speech in Portuguese and has questionable effectiveness in audio with the presence of noise. In this sense, Unfake aims to develop an A.I. model capable of identifying whether an audio contains human or synthetic speech. In this way, we hope to make it possible for lay users to identify deepfakes in a robust and effective way, contributing to a safer and more reliable digital environment, as well as encouraging future research in the area using the data obtained in the project.</p>

<h2 id="started">🚀 Getting started</h2>

<h3>Prerequisites</h3>

Here is a list of all prerequisites necessary for running the project locally:

- [Python](https://www.python.org)

<h3>Cloning</h3>

```bash
git clone https://github.com/Unfake-Official/server.git
```

<h3>Starting</h3>

Firstly, go to the project's directory: 
```bash
cd server
```

Next, create a virtual environment and activate it: 
```bash
python -m venv .venv
.venv/Scripts/activate
```

Install all dependencies: 
```bash
pip install -r requirements.txt
```

Finally, run the development server: 
```bash
python run.py
```

Open [http://localhost:5000/alive](http://localhost:5000/alive) with your browser to see the result.

<h2 id="routes">📍 API Endpoints</h2>

Here you can list the main routes of your API, and what are their expected request bodies.
​
| route               | description                                          
|----------------------|-----------------------------------------------------
| <kbd>GET /alive</kbd>     | Confirms that the server is running without problems. [Response details](#get-alive)
| <kbd>POST /classify</kbd>     | Receives an uploaded audio via body files and returns its possible classification and accuracy. [Request details](#post-classify)

<h3 id="get-alive">GET /alive</h3>

**RESPONSE**
```json
"[Current Timestamp] Server is alive."
```

<h3 id="post-classify">POST /classify</h3>

**REQUEST**
```
'audio': sample.wav
```

**RESPONSE**
```json
{
	"accuracy": 7.829866170377153,
	"classification": "real"
}
```

<h2 id="contribute">📫 Contribute</h2>

If you want to somehow contribute to this project, start by creating a branch named as follow. Then, make your changes and follow commit patterns. Finally, open an pull request. 

1. `git clone https://github.com/Unfake-Official/server.git`
2. `git checkout -b feature/NAME`
3. Follow commit patterns
4. Open a Pull Request explaining the problem solved or feature made, if exists, append screenshot of visual modifications and wait for the review!

<h3>Documentations that might help</h3>

[📝 How to create a Pull Request](https://www.atlassian.com/br/git/tutorials/making-a-pull-request)

[💾 Commit pattern](https://gist.github.com/joshbuchea/6f47e86d2510bce28f8e7f42ae84c716)
