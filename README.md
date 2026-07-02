<a id="readme-top"></a>

<div align="center">
  <a href="https://github.com/dastanmyrsaliev/news-portal/graphs/contributors">
    <img src="https://img.shields.io/github/contributors/dastanmyrsaliev/news-portal.svg?style=for-the-badge" alt="Contributors">
  </a>
  <a href="https://github.com/dastanmyrsaliev/news-portal/network/members">
    <img src="https://img.shields.io/github/forks/dastanmyrsaliev/news-portal.svg?style=for-the-badge" alt="Forks">
  </a>
  <a href="https://github.com/dastanmyrsaliev/news-portal/stargazers">
    <img src="https://img.shields.io/github/stars/dastanmyrsaliev/news-portal.svg?style=for-the-badge" alt="Stargazers">
  </a>
  <a href="https://github.com/dastanmyrsaliev/news-portal/issues">
    <img src="https://img.shields.io/github/issues/dastanmyrsaliev/news-portal.svg?style=for-the-badge" alt="Issues">
  </a>
  <a href="https://github.com/dastanmyrsaliev/news-portal/blob/main/LICENSE">
    <img src="https://img.shields.io/github/license/dastanmyrsaliev/news-portal.svg?style=for-the-badge" alt="MIT License">
  </a>
</div>

<!-- PROJECT LOGO -->
<br />
<div align="center">

  <h3 align="center">News Portal</h3>

  <p align="center">
    News portal built with Python, Django, PostgreSQL, Bootstrap, Docker and uv
    <br />
    <br />
    <a href="https://github.com/dastanmyrsaliev/news-portal/issues/new?labels=bug&template=bug-report---.md">Report Bug</a>
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

### Built With

<p align="center">
  <a href="https://www.python.org/"><img src="https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=fff&style=for-the-badge" alt="Python"></a>
  <a href="https://www.djangoproject.com/"><img src="https://img.shields.io/badge/Django-092E20?logo=django&logoColor=fff&style=for-the-badge" alt="Django"></a>
  <a href="https://www.postgresql.org/"><img src="https://img.shields.io/badge/PostgreSQL-4169E1?logo=postgresql&logoColor=fff&style=for-the-badge" alt="PostgreSQL"></a>
  <a href="https://getbootstrap.com/"><img src="https://img.shields.io/badge/Bootstrap-7952B3?logo=bootstrap&logoColor=fff&style=for-the-badge" alt="Bootstrap"></a>
  <a href="https://www.docker.com/"><img src="https://img.shields.io/badge/Docker-2496ED?logo=docker&logoColor=fff&style=for-the-badge" alt="Docker"></a>
  <a href="https://docs.astral.sh/uv/"><img src="https://img.shields.io/badge/uv-DE5FE9?logo=uv&logoColor=fff&style=for-the-badge" alt="uv"></a>
</p>

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

<!-- USAGE EXAMPLES -->

## Usage

Open the terminal and enter the command:

```sh
uv run python manage.py runserver
```

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

<!-- LICENSE -->

## License

Distributed under the MIT License. See `LICENSE` for more information.

<!-- CONTACT -->

## Contact

Dastan - [@myrsaliev_dev](https://t.me/myrsaliev_d) - myrsaliev.dev@gmail.com

Project Link: [https://github.com/dastanmyrsaliev/news-portal](https://github.com/dastanmyrsaliev/news-portal)

<!-- ACKNOWLEDGMENTS -->

## Acknowledgments

- [Best-Readme-Template](https://github.com/othneildrew/Best-README-Template)
- [Simple Badges](https://badges.pages.dev/)
