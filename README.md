<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a name="readme-top"></a>


<h2 align="center">Gaming Score Forecasting Model</h2>

  <p align="center">
    By Benjamin Lavoie
    <br />
     <br />
    This is my final project for BrainStation's Data Science bootcamp.
    <br/>
    <b> Access my deployed Capstone on Streamlit with the QR Code below! (Scan or click)</b>
    <br />
    <a href=”https://capstoneproject-benji02.streamlit.app”>
    <img src="Images/qrcode.png">
    </a>
    <br />
    <a href="https://github.com/benji02/capstone_project/issues">Report Bug</a>
    ·
    <a href="https://github.com/benji02/capstone_project/issues">Request Feature</a>
  </p>
</div>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#project-overview">Project Overview</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#data-dictionary">Data Dictionary</a></li>
    <li><a href="#simple-roadmap">Simple Roadmap</a></li>
    <li><a href="#detailed-roadmap">Detailed Roadmap</a></li>    
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## Project Overview
<!--
[![Product Name Screen Shot][product-screenshot]](https://example.com)-->

This project can be used as a way to predict the rating of yet-to-be-released games, depending on some of their features.<br>


<br>
<b> The problem area: </b> <br>
Video games. I’ve been playing video games forever and it’s a subject that I love to learn more about, but also, predict about. I’m wondering if there is a way to predict a critic score for a game when taking into consideration the publisher, the genre, the platforms and more. With my Capstone, video game companies and indie developers could evaluate which genres are popular from which publishers, for which platform and how the game will be received by critics. If possible, I would also like to evaluate the sales.
<br><br>
<b> The User: </b> <br>
Anybody that works in game development, small or big studios, could benefit from this. Indie developers could use this tool to see if it’s worth porting the game to another platform, if they’re releasing during a good time, if the game will have a better score with this feature or this feature.
<br><br>
<b> The Big Idea: </b> <br>
With machine learning, it will be possible to analyze how previous games were rated according to a few criteria and then infer what could be the possible score of a game. For example, looking at some games like Zelda, it’s really rare that the score will be bad.
<br><br>
<b> The impact: </b> <br>
I believe this type of project might already be available within big video game publishing companies. But what about smaller studios and indie developers? That could help them have an idea of what to expect when the game is out. After the release, it would also be a good way to see if the game performed as expected or better.

<p align="right">(<a href="#readme-top">back to top</a>)</p>


### Built With
<!--
* [![Next][Next.js]][Next-url]
* [![React][React.js]][React-url]
* [![Vue][Vue.js]][Vue-url]
* [![Angular][Angular.io]][Angular-url]
* [![Svelte][Svelte.dev]][Svelte-url]
* [![Laravel][Laravel.com]][Laravel-url]
* [![Bootstrap][Bootstrap.com]][Bootstrap-url]
* [![JQuery][JQuery.com]][JQuery-url]
-->
- Jupyter Notebook
- Python (+ pandas, numpy, glob and more)
  
<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

Since the project is made using Jupyter Notebook, you need Jupyter Notebook or a software compatible with .ipynb files.

### Prerequisites

Make sure you download the appropriate datasets and not just the notebook.
I've used a lot of dataset during the cleaning/merging part of this project.
All of them were on Kaggle. I ultimately only kept the ones related to Metacritic.
- [Metascore Video Games 1986-2023](https://www.kaggle.com/datasets/yilmazagca/metacritic-video-games-score-and-reviews-1986-2023) (Kaggle)
- [Video Game Sales](https://www.kaggle.com/datasets/sandhyakrishnan02/video-game-sales?select=vgsales.csv) (Kaggle)
- [Metacritic Games and User Reviews All Time](https://www.kaggle.com/datasets/trentenberam/metacritic-games-all-time?select=metacritic_games_master.csv) (Kaggle)

All the info from those datasets that I used are from VGChartz or Metacritic.

<!--
* npm
  ```sh
  npm install npm@latest -g
  ```
  -->
  
### Installation
<!--
1. Get a free API Key at [https://example.com](https://example.com)
2. Clone the repo
   ```sh
   git clone https://github.com/github_username/repo_name.git
   ```
3. Install NPM packages
   ```sh
   npm install
   ```
4. Enter your API in `config.js`
   ```js
   const API_KEY = 'ENTER YOUR API';
   ```
 -->

Click here to install Jupyter Notebook: https://jupyter.org/install
<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Data Dictionary

Here are the infos on all the different columns in this project.<br>

| Feature/Column | Definition | Data type |
|----------|----------|----------|
| Name | Name/Title of the game | String |
| Platform | Platform the game was released on | String |
| Publisher | Publisher of the game | String |
| Developer | Developer of the game | String |
| Genre | Genre of the game | String |
| Platform_Brand | Brand of the platform (Nintendo, Sony, Microsoft, PC | String |
| Platform_Type | Type of the platform (HomeConsole, Handheld, PC) | String |
| Release_Date | Release date | DateTime |
| Release_Day | Release day | int |
| Release_Month | Release month | int |
| Release_Year | Release year | int |
| Metascore_Range | Classification: Weak, Okay or Strong | String |


<!-- 
_For more examples, please refer to the [Documentation](https://example.com)_
-->
<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- SIMPLE ROADMAP -->
## Simple Roadmap

- [x] Finding the right dataset(s)
- [x] Cleaning the dataset and filling the empty values as needed
- [x] Trying multiple types of prediction models
- [x] Finding the best model for the current situation
- [x] Training the model for maximum efficiency
- [ ] Export a clean dataframe/CSV on Kaggle for other users (Cancelled)
- [x] Hosting the project on a website for easy utilization ([Link](https://capstoneproject-benji02.streamlit.app))
- [ ] Updating the dataset every quarter or every year, for maximum efficiency of the predictions (Work in progress)


<!-- DETAILED ROADMAP -->
## Detailed Roadmap

- [x] Finding the right dataset(s)

Finding the right dataset was difficult. When I started this project, I wanted to make it about predicting both game ratings as well as game sales. However, after checking some datasets regarding sales, it seemed like most of the datasets were incomplete. I could find more info on VGChartz, but I would have to do all of it line by line. After a few lines, I also realized that I had to search every game separately, as the data was not at the same place for all the games. And it was also hard to find the data outside of "Total Sales".

I debatted still keeping sales but because of the time constraint, I decided to drop sales for now and focus on the rating prediction.

<br>

- [x] Cleaning the dataset and filling the empty values as needed

Just like the first point, I tried to fill the values line by line at first, when I was still working on both ratings and sales. However, I since I turned out to only find about 2000 lines of data, I deemed it incomplete and I stopped filling in the values. I also wanted to fill in the values regarding story-focused games and gameplay-focus games, but I realized that it was most of the time correlated with the genre. So I also stopped doing that.

When I only kept the rows with the info in the Metacritic Score, it was about 14k and I decided it was enough.

<br>

- [x] Trying multiple types of prediction models

Right after I finally decided to go on with the ratings and not the sales, I threw in some models. I had to adjust the cut-off value for the categories a few times, to make it easier to categorize the games. After deciding on 3 categories, I found the sweet spots and decided to change notebook after that. The first notebook was getting long and slow and it would be better to start anew for the modelling. I transferred the first few models I did to the bottom of the new notebook and then started the pre-processing. (still in the works)

<br>

- [x] Finding the best model for the current situation

After a good amount of trial and error, the best model that would't cause overfitting was "XG Boost" 

<br>

- [x] Training the model for maximum efficiency

I wanted to do a lot for training my model. However, due to limited time and computer power, I wasn't able to train it as much as I wanted. However. I was able to improve it by a few percents while testing hyperparameters, while not overfitting too much. With an accuracy of 61.6%, I am satisfied.

<br>

- [ ] Export a clean dataframe/CSV on Kaggle for other users (Cancelled)

This step was ultimately cancelled.

Because I did a lot of work "by-hand" and because I had to join a few datasets (some who had "unknown" in Publisher and/or Developer), I don't feel like the dataset is perfect. For that reason, I won't be putting the dataset on Kaggle. However, it is available on my Github.

<br>

- [x] Hosting the project on a website for easy utilization

While I don't feel comfortable sharing the dataset at large, I still decided to deploy my Forecasting Model online, on Sreamlit. [Click here](https://capstoneproject-benji02.streamlit.app) to access it.

<br>

- [ ] Updating the dataset every quarter or every year, for maximum efficiency of the predictions (Work in progress)

<br>
<br>
And of course, updating the README.md everytime I add new features or the project gets closer to completion.
<br>
See the [open issues](https://github.com/benji02/capstone_project/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing
<!--
Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request
-->
<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- LICENSE -->
## License
<!--
Distributed under the MIT License. See `LICENSE.txt` for more information.
 -->
<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Benjamin Lavoie - [LinkedIn](https://www.linkedin.com/in/benjamin-lavoie/) - benji0202@gmail.com

Project Link: [https://github.com/benji02/capstone_project](https://github.com/benji02/capstone_project)

Deployed Project Link: https://capstoneproject-benji02.streamlit.app

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments
<!-- 
* []()
* []()
* []()
 -->
<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links 
[contributors-shield]: https://img.shields.io/github/contributors/github_username/repo_name.svg?style=for-the-badge
[contributors-url]: https://github.com/github_username/repo_name/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/github_username/repo_name.svg?style=for-the-badge
[forks-url]: https://github.com/github_username/repo_name/network/members
[stars-shield]: https://img.shields.io/github/stars/github_username/repo_name.svg?style=for-the-badge
[stars-url]: https://github.com/github_username/repo_name/stargazers
[issues-shield]: https://img.shields.io/github/issues/github_username/repo_name.svg?style=for-the-badge
[issues-url]: https://github.com/github_username/repo_name/issues
[license-shield]: https://img.shields.io/github/license/github_username/repo_name.svg?style=for-the-badge
[license-url]: https://github.com/github_username/repo_name/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/linkedin_username
[product-screenshot]: images/screenshot.png
[Next.js]: https://img.shields.io/badge/next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white
[Next-url]: https://nextjs.org/
[React.js]: https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB
[React-url]: https://reactjs.org/
[Vue.js]: https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vuedotjs&logoColor=4FC08D
[Vue-url]: https://vuejs.org/
[Angular.io]: https://img.shields.io/badge/Angular-DD0031?style=for-the-badge&logo=angular&logoColor=white
[Angular-url]: https://angular.io/
[Svelte.dev]: https://img.shields.io/badge/Svelte-4A4A55?style=for-the-badge&logo=svelte&logoColor=FF3E00
[Svelte-url]: https://svelte.dev/
[Laravel.com]: https://img.shields.io/badge/Laravel-FF2D20?style=for-the-badge&logo=laravel&logoColor=white
[Laravel-url]: https://laravel.com
[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com
[JQuery.com]: https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white
[JQuery-url]: https://jquery.com 
-->
