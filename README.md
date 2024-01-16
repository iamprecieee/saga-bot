## INSTALLATION GUIDE
- Fork this [branch](https://github.com/iamprecieee/saga-bot).
- Clone your fork to your code editor e.g. VSCode.
- Create a virtual environment using `python3 -m venv venv`.
- Activate your virtual environment using `. venv/bin/activate` or appropriate command for your operating system.
- Install requirements using `pip3 install -r requirements.txt`.
- Create a `.env` file for storing your variables (private key, sender/receiver addresses).

## RUNNING GUIDE
- Replace the `dragonstone_rpc_url` with your chainlet's rpc url.
- Replace the `chain_id` with your chainlet's chain ID.
- Modify the `amount`, `sleep` time and any other fields as desired.
- Add the address and private key for your sender's address, and the receiving address(es) to your env file; you can add as many receiving addresses as you wish, just seperate them with commas.
- Finally, run the code using `python3 main.py`.



⚠️ **BE CAREFUL WITH YOUR PRIVATE KEYS TO AVOID LEAKS. IT'S RECOMMENDED TO USE A BURNER ADDRESS FOR THIS**
