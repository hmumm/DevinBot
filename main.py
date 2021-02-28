import discord
import os
import asyncio
import random
import logging

client = discord.Client()


ads = [
    "Brought to you by Squarespace. Make a custom website today.",
    "Brought to you by Jones BBQ and foot massage. Better come down here and get some of this shit. You like to eat, America likes to eat so why not open up somewhere America can sit down enjoy a meal and get your feet rubbed. We'll fry anything you want for $5.99. If those is probable edible we're gonna make it delicious. We will fry parts of the chicken you didn't even know were friable. The beak the feathers, we'll fry candy bars. All that European stuff you don't normally eat, we'll bring it down here and fry it for you. Ask McDonald's to fry something other than what they normally fry guess what you're gonna get nothing. If it fits through the door I'll put it in the frier. Hell this dinosaur. All our meats are gently tenderized to their optimum deliciousnous. We got fine dinosaur meat. Come on down and get you a slice. So friends let's just decide you don't want no barbeque well that's fine too why not let one of my foot specialist or myself perform my magic. If you really pay me enough we'll massage your feet in any of these sauces also. Jones good ass barbeque and foot massage. Go ahead and give us a call and find us on the world wide internets at the new website that's www.jonlesBIGASStruckrentalandstorage.com\\jonesGOODASSbqandfootmassage.html (https://youtu.be/WPkMUU9tUqk)",
    "Brought to you by Manscapped get our new Lawmower 7.2 and a half.",
    "Brought to you by Raid Shadow Legends.",
    "Brought to you by Nord VPN"
]


@client.event
async def on_ready():
    logging.debug('We have logged in as {0.user}'.format(client))
    loop = asyncio.get_event_loop()
    loop.create_task(send_random_messages())


async def send_random_messages():
    logging.debug('Starting to send ads')
    channel = client.get_channel(575184680173961216)

    while True:
        # wait a random amount of time betweent 3600 seconds (1 hour) and 86400 seconds (1 day)
        secondsToWait = random.randint(3600, 86400)
        logging.debug('Waiting ' + secondsToWait + ' seconds until sending another ad')
        await asyncio.sleep(secondsToWait)

        # send a random message from the ads array
        ad = random.choice(ads)
        logging.debug("sending ad: " + ad)
        await channel.send(ad)

logging.basicConfig(filename='output.log', encoding='utf-8', level=logging.DEBUG)
token = os.getenv('DISCORDTOKEN')
loggin.debug('using token: ' + token)
client.run(token)
