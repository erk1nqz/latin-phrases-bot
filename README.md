# Latin Phrases Bot

This bot responds to user input with famous Latin phrases based on different themes. It is built using Python and the Telebot library.

## Getting Started

To use this bot, you need to have Python installed on your system. You also need to install the required dependencies listed in `requirements.txt`. You can install them using pip:

```zsh
// Terminal
pip install pyTelegramBotAPI
```

After installing the dependencies, you can run the bot by executing the `bot.py` file:

```zsh
// Terminal
python bot.py
```


## Usage

Once the bot is running, you can interact with it using the Telegram messaging platform. Start a chat with the bot and use the following commands:

- `/start`: Start the conversation and display the main menu.
- `Меню`: Display the list of available themes.
- `Тема <number>: <theme>`: Choose a specific theme by replacing `<number>` with the theme number and `<theme>` with the theme name.
- `Выход`: Exit the conversation.

## Features

- Provides a collection of Latin phrases categorized into different themes.
- Allows users to choose a theme and receive a random Latin phrase related to that theme.
- Offers a simple and intuitive user interface using Telegram's messaging platform.

## Data Source

The Latin phrases are stored in a JSON file named `phrases.json`, which serves as the database for the bot. Each theme contains a list of related phrases.

## Dependencies

- telebot
- requests

## Author

Bakyt Erkinkyzy - tg: @zhureee3eem

## License

This project is licensed under the [MIT License](LICENSE).
