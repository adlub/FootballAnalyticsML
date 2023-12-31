[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]

<!-- PROJECT LOGO -->
<br />
<div align="center"> 
  <a href="https://github.com/adlub/FootballAnalyticsML">
    <img src="https://images.unsplash.com/photo-1504639725590-34d0984388bd?q=80&w=1974&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D" alt="Logo" width="80" height="80">
  </a>

<h3 align="center">FootballAnalyticsML</h3>

  <p align="center">
    My personal project in which I used multiple machine learning libraries in python on football shot data.
    <br />
    <a href="https://github.com/adlub/FootballAnalyticsML"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/adlub/FootballAnalyticsML/issues">Report Bug</a>
    ·
    <a href="https://github.com/adlub/FootballAnalyticsML/issues">Request Feature</a>
  </p>
</div>


<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#running-the-code">Running the code</a></li>
      </ul>
    </li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
## About The Project
My personal project in which I used multiple machine learning libraries in python to analyse football shot data. This is an extension on a project I worked on in my university degree (details of my university project are on my linkedin page). This repository contains multiple files that correspond to the use of different classification algorithms used to predict the outcome of a shot. This repository also includes details of particular models that have been made and visualisations of predictive models. 
<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- GETTING STARTED -->
## Getting Started

### Prerequisites

If not installed already, be sure to install the XGBoost and tensorflow packages in your python environment
* pip
  ```sh
  pip install xgboost
  pip install tensorflow
  ```
Before running any code, make sure you have a relevant .csv file containing football shot data in the same folder as the project. You can download the .csv file by following the instructions [**here**](https://sagnikdas1.medium.com/extract-seasonal-shot-data-for-one-team-from-understat-in-r-8686d7224376)

After downloading the .csv file, follow the instructions in `Excel_Preprocessing_Instrutions.txt` (In the future, I plan to remove the need for this and include this part of the preprocessing in the .py files so you dont have to do this annoying bit!)

### Running the code

I recommend running `logisticRegressionXG.py` first. As well as the relevant plots, this will create two .txt files containing coefficients for the logistic regression curve corresponding to the created model. After this, run `LRShotAngleCurve.py` and `LRShotDistanceCurve.py`. These files will read the aforementioned .txt files and plot the logistic regression curves based on the coefficients in these files.

Once you have run these files, you can then run the other python files (in any order) that correspond to the use of other classification models on football shot data. 

`Classification_Results.xlsx` contains the performance metrics of all the models used in this project. This file currently contains data from when I personally ran the models on Real Madrid's shot data from 2019 (extracted using the site linked above). You can change the data at your discretion when you run the models yourself.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTACT -->
## Contact

Adrian Lubwama - alubwaa@outlook.com

Project Link: [https://github.com/adlub/FootballAnalyticsML](https://github.com/adlub/FootballAnalyticsML)

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/adlub/FootballAnalyticsML.svg?style=for-the-badge
[contributors-url]: https://github.com/adlub/FootballAnalyticsML/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/adlub/FootballAnalyticsML.svg?style=for-the-badge
[forks-url]: https://github.com/adlub/FootballAnalyticsML/network/members
[stars-shield]: https://img.shields.io/github/stars/adlub/FootballAnalyticsML.svg?style=for-the-badge
[stars-url]: https://github.com/adlub/FootballAnalyticsML/stargazers
[issues-shield]: https://img.shields.io/github/issues/adlub/FootballAnalyticsML.svg?style=for-the-badge
[issues-url]: https://github.com/adlub/FootballAnalyticsML/issues
[license-shield]: https://img.shields.io/github/license/adlub/FootballAnalyticsML.svg?style=for-the-badge
[license-url]: https://github.com/adlub/FootballAnalyticsML/blob/main/LICENSE
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/adrian-lubwama-72506a244/
