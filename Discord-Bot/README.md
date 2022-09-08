# Discord Bot Reasearch & Documentation

## Setup
- Dependencies
    - python3 (`sudo apt install python3`)
    - python pip (`sudo apt-get install python3-pip`)
    - discord.py (`pip install -U discord.py`)
    - python-dotenv (`pip install -U python-dotenv`)
- API Token
    - The Token is accessed through Discords developer portal when a new bot is created
    - A key can only be viewed once when it is created
    - If the key is lost or stolen a new one can be generated in the portal
        - Click on your Bots Application
        - Click `Bot` on the left
        - Click `Reset Token`
- What to do with the API Token
    - When a token is created, it needs to be copied and pasted into a `.env` file
    - The Token should be set equal to a variable that will be used to retrieve the key
    - In the `.env` file it will look like `DISCORD_TOKEN=your-bot-token`

## Usage
- Commands
    - `!tars`
        - This command will give a response of a quote from the movie *Interstellar*
    - `!case`
        - This command will give a response of an image from the movie *Interstellar*
- Screenshots
    - ![Screenshot](./Screenshots/tars1.png)
    - ![Screenshot](./Screenshots/tars2.png)
    - ![Screenshot](./Screenshots/tars3.png)
    - ![Screenshot](./Screenshots/tars4.png)
    - ![Screenshot](./Screenshots/tars5.png)
    - ![Screenshot](./Screenshots/case1.png)
    - ![Screenshot](./Screenshots/case2.png)
    - ![Screenshot](./Screenshots/case3.png)

## Research
- Paying a company to host a server full time server
    - Companies like Amazon, Google, and IBM all offer paid server hosting
    - All one has to do is pay for the server and deploy the bot on the server
    - The bot will be up and running 24/7
- Running a dedicated server on someone elses systems the free way (maybe cheating way)
    - Websites like replit and Heroku allow code/proccess building to happen fully in the cloud
    - A bot can be deployed here just the same way that it would on a paid 24/7 server, kinda...
    - These will shut down after a certain period of not having any requests sent to them
    - There are two ways of keeping them alive
        - Add a background task that is constantly doing something
        - Setup `Uptime Robot` that will ping the server on an interval to keep it alive
- Setup a system at home to stay running constatnly
    - This can be done on almost any machine as long as it stays up 24/7
    - The cheapest and easiest way to do something like this would be to get a raspberry pi
    - A super lightweight server like this is what the respberry pi strives at doing