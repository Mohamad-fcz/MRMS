

<p align="center"><img  src="https://user-images.githubusercontent.com/99288525/216159152-9a7a2dce-3312-4d64-bdf2-b7315d388ada.gif"   width="200" height="200">&nbsp;&nbsp;
<img src="https://www.perfecto.io/sites/perfecto.io/files/image/2020-05/social-blog-what-to-expect-with-selenium.jpg"  width="200" height="200">
<p align="center"><img  src="https://docs.servicestack.net/assets/jupyter-python.6188762b.png"   width="400" height="100">

                   
<p align="center"> <img alt="GitHub release (latest by date)" src="https://img.shields.io/github/v/release/Mohamad-fcz/MRMS?label=Version&logo=github&style=plastic">&nbsp;&nbsp;&nbsp;
<img alt="GitHub" src="https://img.shields.io/github/license/mohamad-fcz/MRMS?color=yellow&logo=Osano&logoColor=yellow">&nbsp;&nbsp;&nbsp;
<img alt="GitHub top language" src="https://img.shields.io/github/languages/top/mohamad-fcz/MRMS?color=orange&logo=jupyter&logoColor=orange">


# MRMS rainfall data collector using Selenium 

This Python package is designed to help automate the download process of MRMS rainfall data using the Selenium package. With this package, you can easily download all the MRMS rainfall data at once, making it much easier to work with.
This application makes use of the most well-known web scraping tools, such as Selenium and chrome web driver, in order to capture full-size screenshots of web pages for the purpose of tracking and analyzing changes. One of the many applications that can be linked to deep learning and used to fit a model with the help of a sequence of screen shots includes, for instance, the movement of hurricanes and the results of sensor readings.


<p align="center"><img alt="Storm heat" src="https://user-images.githubusercontent.com/99288525/226160500-ecd42430-d9f8-477e-b964-4d63ca05730b.gif">


## Features

- 100% Jupyter Notebook 
- Compatible with IDEs such as Pycharm
- Jupyter widgets base for more convenience to use
- Light weight


## Installation
This project makes use of Jupyter Notebooks for increased convenience. In order for you to be able to interact with the widgets contained within the notebook, you will first need to install Jupyer Notebook along with its dependencies in the form of Ipywidgets. Here are provided three different methods to create the environment that you may choose the one is more convenient for you.

1. The easiest way to create the python environment is using the "yml" file we provided in the repository and you just need to import this file in your directory and run below conda command.
```bash
  conda env create -f environment.yml
```
2. Installing Jupyter Lab or installing the Jupyter meta(both are the same) package through conda is the more convenient alternative for achieving this objective. Both of these options make it simple for you to access everything in an effective Jupyter environment that you might require for this project or other projects.

Check that you have the most recent version of Anaconda downloaded and installed on your system.

- [Downdload Anaconda](https://www.anaconda.com/products/distribution)
Using Anaconda Prompt:
- installing the most recent version of Jpyter along with all of its dependencies.

```bash
  conda install -c conda-forge jupyter
```
#### or
3. installing the most recent version of Jupyter notebook and activating Ipywidgets manually in case you are short on space or for any reason do not intend to install full Jupyter meta package from above method.

```bash
  conda install -c conda-forge notebook
  conda install -c conda-forge nb_conda_kernels
  conda install -c conda-forge jupyter_contrib_nbextensions
  conda install -c conda-forge ipywidgets
```
### Afterwards, proceed to install the remaining packages that are necessary for web scraping.
- Install the latest version of below packages in the environment using conda

```bash
  conda install -c conda-forge selenium
  conda install -c conda-forge webdriver-manager
  conda install -c conda-forge tqdm
 
```
    
## How to use

Be certain to run the `import` cell as well as the `functions`.

With Jupyter widgets, you have a straightforward graphical user interface for setting parameters start/end date and the rainfall duration.

After you have finished making configurations, you can begin the automation process by clicking the "start download" button.
Keep in  mind that the process might take a while to be completed and preferably the system should not be in use meanwhile.
## Author

- [![portfolio](https://img.shields.io/badge/Mohamad%20Ahmadzadeh-000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Mohamad-fcz)



## 🔗 Contacting us
[![portfolio](https://img.shields.io/badge/telegram-000?style=for-the-badge&logo=telegram&logoColor=white)](https://t.me/erfan_fcz)
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/mohamad-ahmadzdeh-223671187/)
[![twitter](https://img.shields.io/badge/twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)](https://twitter.com/erfan_fcz)


## FAQ

#### In the event that you run into any issues while utilizing the program, you are more than welcome to post a problem in the issues section of GitHub.

