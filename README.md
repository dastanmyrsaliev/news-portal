<a id="readme-top"></a>

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]

<!-- PROJECT LOGO -->
<br />
<div align="center">

  <h3 align="center">News Portal</h3>

  <p align="center">
    <br />
    <a href="https://github.com/dastanmyrsaliev/qr-code-component/issues/new?labels=bug&template=bug-report---.md">Report Bug</a>
  </p>
</div>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
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
    <li><a href="#usage">Usage</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->

## About The Project

News portal on Django.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Built With

- [![Python][Python]][Python-url]
- [![Django][Django]][Django-url]
- [![Postgres][Postgres]][Postgres-url]
- [![Docker][Docker]][Docker-url]
- [![uv][uv]][uv-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- GETTING STARTED -->

## Getting Started

### Prerequisites

* uv for macOS and Linux
  ```sh
  curl -LsSf https://astral.sh/uv/install.sh | sh
  ```

* uv for Windows
    ```powershell
    powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
    ```

### Installation

1. Clone the repo
    ```sh
    git clone https://github.com/dastanmyrsaliev/news-portal.git
    ```

2. Create `.env` file based on `.env.example`

3. Start the database
    ```sh
    docker compose up -d db
    ``` 

4. Install packages
    ```sh
    uv sync
    ```
5. Make a migrate
    ```sh
    uv run python manage.py migrate
    ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- USAGE EXAMPLES -->

## Usage

Open the terminal and enter the command:

```sh
uv run python manage.py runserver
```

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

### Top contributors:

<a href="https://github.com/dastanmyrsaliev/news-portal/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=dastanmyrsaliev/news-portal" alt="contrib.rocks image" />
</a>

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- LICENSE -->

## License

Distributed under the MIT License. See `LICENSE` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTACT -->

## Contact

Dastan - [@myrsaliev_dev](https://t.me/myrsaliev_d) - myrsaliev.dev@gmail.com

Project Link: [https://github.com/dastanmyrsaliev/news-portal](https://github.com/dastanmyrsaliev/news-portal)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- ACKNOWLEDGMENTS -->

## Acknowledgments

- [Best-Readme-Template](https://github.com/othneildrew/Best-README-Template)
- [md-badges](https://github.com/inttter/md-badges)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->

[contributors-shield]: https://img.shields.io/github/contributors/dastanmyrsaliev/news-portal.svg?style=for-the-badge
[contributors-url]: https://github.com/dastanmyrsaliev/news-portal/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/dastanmyrsaliev/news-portal.svg?style=for-the-badge
[forks-url]: https://github.com/dastanmyrsaliev/news-portal/network/members
[stars-shield]: https://img.shields.io/github/stars/dastanmyrsaliev/news-portal.svg?style=for-the-badge
[stars-url]: https://github.com/dastanmyrsaliev/news-portal/stargazers
[issues-shield]: https://img.shields.io/github/issues/dastanmyrsaliev/news-portal.svg?style=for-the-badge
[issues-url]: https://github.com/dastanmyrsaliev/news-portal/issues
[license-shield]: https://img.shields.io/github/license/dastanmyrsaliev/news-portal.svg?style=for-the-badge
[license-url]: https://github.com/dastanmyrsaliev/news-portal/blob/main/LICENSE
[Python]: https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=fff
[Python-url]: https://www.python.org/
[Django]: https://img.shields.io/badge/Django-%23092E20.svg?logo=django&logoColor=white
[Django-url]: https://www.djangoproject.com/
[Postgres]: https://img.shields.io/badge/Postgres-%23316192.svg?logo=postgresql&logoColor=white
[Postgres-url]: https://www.postgresql.org/
[Docker]: https://img.shields.io/badge/docker-257bd6.svg?logo=docker&logoColor=white
[Docker-url]: https://www.docker.com/
[uv]: https://img.shields.io/badge/uv-261230.svg?logo=uv&logoColor=#de5fe9
[uv-url]: https://docs.astral.sh/uv/
