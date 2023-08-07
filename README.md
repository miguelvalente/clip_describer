# Clip Describer

Clip Describer is a project that utilizes the power of CLIP to rank keywords based on premade lists and WordNet. It features a frontend built with Streamlit to provide an interactive user experience.

[Visit the Deployed App](https://yourappurl.com)

## Directory Structure

```bash
.
├── clip_describer
│   ├── app
│   │   └── home.py            # Home Page Logic
│   └── core
│       ├── __init__.py
│       ├── lists.py           # Lists Handling
│       ├── model.py           # Model Handling
│       ├── text_generator.py  # Text Generation Logic
│       └── wordnet_parse.py   # WordNet Parsing
├── poetry.lock
├── pyproject.toml             # Project Metadata
└── README.md
```

## Features

- **Keyword Ranking**: Utilizes CLIP to rank keywords based on specific criteria.
- **WordNet Integration**: Leverages WordNet to enhance the keyword selection process.
- **Interactive UI**: Provides an interactive frontend built with Streamlit.


## Installation

### Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/clip_describer.git
   ```

2. Change into the project directory:
   ```bash
   cd clip_describer
   ```

3. Install the dependencies using [Poetry](https://python-poetry.org/):
   ```bash
   poetry install
   ```

## Usage

To run the application, use the following command:

```bash
streamlit run clip_describer/app/home.py
```

Open your browser and go to `http://localhost:8501` to interact with the application.