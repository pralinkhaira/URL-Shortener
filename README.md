# URL Shortener CLI

This is a simple command-line interface (CLI) application that allows you to shorten a URL using the Bitly API.

## Requirements

To use this application, you'll need to have the following installed:

- Python 3
- `requests` package (`pip install requests`)
- `pyperclip` package (`pip install pyperclip`)

You'll also need to obtain an access token for the Bitly API. You can sign up for a Bitly account and create an API key [here](https://dev.bitly.com/get_started/).

## Usage

To use the URL shortener CLI application, follow these steps:

1. Open a terminal window.
2. Navigate to the directory where the `shorten.py` file is located.
3. Run the following command:

   ```
   python shorten.py YOUR_LONG_URL_HERE
   ```

   Replace `YOUR_LONG_URL_HERE` with the URL you want to shorten.

4. The shortened URL will be printed to the console and copied to your clipboard.

## Customization

You can customize this application by modifying the `shorten.py` file. For example, you can use a different URL shortener API or add additional functionality, such as storing the shortened URLs in a database.

## License

This project is licensed under the GNU License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- This application was inspired by [Bitly CLI](https://github.com/conradkleinespel/bitly-cli).
