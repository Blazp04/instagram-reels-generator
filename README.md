# Instagram Video Generator

## Overview

The Instagram Video Generator is a Python-based application designed to create engaging videos specifically tailored for Instagram. By utilizing YouTube Shorts and user-defined themes, the application generates a cohesive storyline, produces character voiceovers, and seamlessly combines all elements into a final video output.

## Features

- **Customizable Videos:** Generate Instagram videos based on your chosen themes for a personalized touch.
- **Voice Generation:** Automatically creates character voices, enhancing the depth and appeal of your videos.
- **Efficient Merging:** Combines audio and video components smoothly to produce a polished final output.

## Getting Started

### 1. Set Up a Virtual Environment

To ensure that your project dependencies do not interfere with other projects, it is recommended to create a virtual environment.

```bash
# Create a virtual environment
python -m venv venv
```

### 2. Activate the Virtual Environment

- **For Windows:**

  ```bash
  venv\Scripts\activate
  ```

- **For macOS/Linux:**
  ```bash
  source venv/bin/activate
  ```

### 3. Install Required Dependencies

After activating your virtual environment, you can install the necessary packages by running:

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

You may need to create a `.env` file in the project's root directory to store your API keys and sensitive information. The file should be structured as follows:

```env
OPENAI_API_KEY=<your_openai_api_key>
ELEVEN_LABS_API_KEY=<your_eleven_labs_api_key>
```

Make sure to replace `<your_openai_api_key>` and `<your_eleven_labs_api_key>` with your actual API keys.

### 5. Adding Short Videos

This project uses preloaded short videos that will be combined into one larger video. You will need to manually download these short videos and place them in the `videos` folder.

## Conclusion

The Instagram Video Generator offers a powerful way to create unique, engaging content for your Instagram audience. With customizable options and automatic voice generation, you can bring your creative vision to life with ease! Enjoy creating!
