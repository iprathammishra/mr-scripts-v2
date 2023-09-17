## Microsoft Rewards, automated.

I automated the entire Microsoft rewards system. Now, anyone can grind points without getting flagged by any automated software.

### Pre-requisites

- [Python 3.6+](https://www.python.org/downloads/)
- [MsEdge](https://www.microsoft.com/en-us/edge)
- A stable internet connection.

### Installation - without an .exe file

1. Clone the repository.

```bash
git clone https://github.com/iprathammishra/mr-scripts-v2.git
```

2. Install the requirements using `pip install -r requirements.txt`

```bash
pip install -r requirements.txt
```

3. Run the script using `python main.py`

```bash
python main.py
```

### Installation - with an .exe file

1. Make sure you have installed the requirements using `pip install -r requirements.txt`

```bash
pip install -r requirements.txt
```

2. Now, run the pyinstaller command in the terminal.

```bash
pyinstaller --onefile main.py
```

3. Now, you can find the .exe file in the `dist` folder.

### Usage

Once, you have installed the requirements, you can run the script using `python main.py` or the .exe file. In both the cases you will be prompted to enter the `Desktop Grind: ` points and the `Mobile Grind: ` points. Enter the points you want to grind and the script will do the rest.

### Note

- The script will automatically open the browser and grind the points. Meanwhile, make sure you don't do anything else or perform anyother actions on your PC. Just let the script do it's work.
- Also, make sure to perform the following step to seemlessly run the script for mobile grinding as well.
  1. Open Microsoft Edge and press: `Ctrl + Shift + I`
  2. Once the developer tools open, make sure that the device is not in mobile mode. If it is, then click on the `Toggle device toolbar` button.

### License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
