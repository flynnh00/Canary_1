# Canary
 [![Discord](https://img.shields.io/discord/236668784948019202.svg)](https://discord.gg/HDHvv58)

Canary is a Python3 bot designed for the McGill University Community Discord Server. The bot provides helper functions to users, as well as fun functions, a quote database and custom greeting messages. 

## Build Statuses

| Master |  [![Build Status](https://travis-ci.org/idoneam/Canary.svg?branch=master)](https://travis-ci.org/idoneam/Canary)  |
|--------|---|
| **Dev**    |  [![Build Status](https://travis-ci.org/idoneam/Canary.svg?branch=dev)](https://travis-ci.org/idoneam/Canary) |

## Installation

1. If you wish to use the `update` command to update to the latest version of the bot, configure your github account in 
your environment of choice and clone into the repository with:
```bash
$ git clone https://github.com/idoneam/Canary
```

2. Dependencies are managed with pipenv which can be installed via pip with:
```bash
$ python3 -m pip install pipenv
```

3. Dependencies may be installed using pipenv with the following command:
```bash
$ pipenv install
```

4. Use of the LaTeX equation functionality requires a working LaTeX installation (at the very minimum, `latex` and `dvipng` must be present). The easiest way to do this is to install TeX Live (usually possible through your distro's package manager, or through TeX Live's own facilities for the latest version). See the [TeX Live site](https://tug.org/texlive/) for more information.

5. Development dependencies (YAPF) can be installed alongside all other dependencies with:
```bash
$ pipenv install --dev
```

6. You may enter the virtual environment generated by the pipenv installation with: `$ pipenv shell` or simply run the bot with `$ pipenv run python3 Main.py`

7. In order to run bots on Discord, you need to [create a bot account](https://github.com/reactiflux/discord-irc/wiki/Creating-a-discord-bot-&-getting-a-token).

You must set certain values in the `config.ini` file, in particular your Discord bot token (which you get in the previous link) and the values in the `[Server]` section.
<details><summary>Click here to see descriptions for a few of those values</summary><p>
 
(For values that use Discord IDs, see [this](https://support.discordapp.com/hc/en-us/articles/206346498-Where-can-I-find-my-User-Server-Message-ID-) to know how to find them)
* `[Discord]`
    * `Key`: Your Discord bot token.
* `[Server]`
    * `ServerID`: Your server ID.
    * `CommandPrefix`: What a message should begin with to be considered a command.
    * `BotName`: The name of your bot.
    * `UpvoteEmoji`: The name of your upvote emoji (for the score function).
    * `DownvoteEmoji`: The name of your downvote emoji.
    * `ModeratorRole`: The name of the role that your moderators have (for functions like DMing users).
    * `DeveloperRole`: The name of the role that your developers have (for functions like restarting the bot). This could be the same role than moderator.
    * `ReceptionChannelID`: The ID of a channel that will receive messages sent to the bot through the `answer` command (and where messages sent by mods to users with the `dm` command will be logged)
* `[Logging]`
    * `LogLevel`: [See this for a list of levels](https://docs.python.org/3/library/logging.html#levels). Logs from exceptions and commands like `mix` and `bac` are at the `info` level. Logging messages from the level selected *and* from more severe levels will be sent to your logging file. For example, setting the level to `info` also sends logs from `warning`, `error` and `critical`, but not  from `debug`.
    * `LogFile`: The file where the logging output will be sent (will be created there by the bot if it doesn't exist).
* `[DB]`
    * `Schema`: Location of the Schema file that creates tables in the database (This file already exists so you shouldn't have to change this unless you rename it or change its location).
    * `Path`: Your database file path (will be created there by the bot if it doesn't exist).
* `[Helpers]`
    * `CourseTemplate`: McGill course schedule URL. **Changes every school year.**
    * `CourseSearchTemplate`: McGill course search URL. **Changes every school year.**
    * `GCWeatherURL`: Government of Canada weather URL. **Region-specific.**
    * `GCWeatherAlertURL`: Government of Canada weather alerts URL. **Region-specific.**
    * `WttrINTemplate`: [http://wttr.in/](http://wttr.in/) URL template. **Region-specific.**
    * `TepidURL`: [TEPID](https://github.com/ctf/TEPID-Server) screensaver endpoint for printer status.
* `[Currency]`
    * `Name`: The name of the bot currency.
    * `Symbol`: The currency's symbol (e.g. `$`).
    * `Precision`: How many decimal digits after the decimal point are "official" for the currency.
    * `Initial`: How much currency is given out by the `initial_claim` command.
    * `SalaryBase`: *Currently unused.*
    * `Inflation`: *Currently unused.*
* `[IncomeTax]`: *Currently unused.*
* `[AssetTax]`: *Currently unused.*
* `[OtherTax]`: *Currently unused.*
* `[Betting]`:
    * `RollCases`: Intervals for `bet_roll`. For example, a value of `66, 90, 99, 100` gives the intervals
      `[1, 66]`, `[67, 90]`, `[91, 99]`, and `[100]`.
    * `RollReturns`: The multiplier return for each interval. For example, a value of `0, 2, 4, 10` with the intervals
      described above gives a 0x return for `random <= 66`, a 2x return for `66 < random <= 90`, a 4x return for
      `90 < random <= 99`, and a 10x return for `random == 100`.
</p>
</details>

## Running the bot
Run `python3 Main.py` in your shell. Ensure that your Discord token is set in the `config.ini` file within the `config` directory.

## Code Linting
We format our code using Google's [YAPF](https://github.com/google/yapf). Our builds will reject code that do not conform to the standards defined in [`.style.yapf`](https://github.com/idoneam/Canary/blob/master/.style.yapf) . You may format your code using :

```
$ pipenv run yapf --recursive --in-place .
```
and ensure your code conforms to our linting with :
```
$ pipenv run yapf --diff --recursive .
```
## Contributions
Contributions are welcome, feel free to fork our repository and open a pull request or open an issue. Please [review our contribution guidelines](https://github.com/idoneam/Canary/blob/master/.github/contributing.md) before contributing.
