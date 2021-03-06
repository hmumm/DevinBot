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
    "Brought to you by number 15: burger king foot lettuce. the last thing you'd want in your burger king burger is someone's foot fungus. but as it turns out, that might be what you get.",
    "Brought to you by Raid Shadow Legends. Now you guys know I don’t usually take on sponsors, but I’ve been hearing a lot about this game recently, so I decided to throw some hours at it and give it a try, and I gotta say I’m really liking it so far. For those who don’t know RAID SHADOW LEGENDS is a free-to-play turn-based RPG that’s got like 15-million downloads over the last few months. Google Play even nominated it for an award for being one of its top RPG’s. It’s got a really cool story campaign, active PVP arenas, dungeons, 16 different factions, and hundreds and hundreds of heroes to collect and customize, and they add over a dozen new ones every single month. You can also unlock free champions, equipment, and other cool stuff just for learning how to play, which includes Arbiter (one of the best heroes in the game). As far as graphics go this game speaks for itself. It’s honestly kinda crazy how much detail these guys squeezed into a free game and for your phone, especially when you consider what used to pass for epic mobile gaming not so long ago. Anyway guys RAID SHADOW LEGENDS is constantly expanding and adding new features, so it’s really never a bad time to give it a try. And when you do make sure you use the special link there to get a free epic champion and 50,000 silver as part of their new player program.",
    "Brought to you by Raycons. I actually have a pair of Raycons and I love them. I usually use them when I’m at the gym or I’m at home playing Minecraft. The sound quality is just as amazing as all the other top name brands and they’re half the price. The ones I’m using are the everyday E25’s. They’re the best ones yet. 6 hours of playtime, seamless Bluetooth pairing, more bass, available in multiple colors, and their compact design helps get rid of background noise. I also like the fact that you can click either earbud with your finger to pause your music. Makes it super convenient if you need to stop for any reason. Go to buyracon.com for 15% off your order.",
    "Brought to you by Nord VPN",
    "Brought to you by FlexTape the super strong waterproof tape that can instantly patch, bond, seal and repair. FlexTapes powerful adhesive is so strong it even works under water."
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
        logging.debug('Waiting ' + str(secondsToWait) + ' seconds until sending another ad')
        await asyncio.sleep(secondsToWait)

        # send a random message from the ads array
        ad = random.choice(ads)
        logging.debug("sending ad: " + ad)
        await channel.send(ad)

logging.basicConfig(filename='output.log', level=logging.DEBUG)
token = os.getenv('DISCORDTOKEN')
logging.debug('using token: ' + token)
client.run(token)
