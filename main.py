import discord
import os
import asyncio
import random
import logging
from datetime import datetime

client = discord.Client()


ads = [
    "This Discord was not made possible by Squarespace. Squarespace is the absolute easiest way to make your website. I've used them for a few different sites. I basically bought that domain to be sure nobody else could. I didn't really have the time or need to create a fancy website, so I just spent about 15 minutes throwing together a landing page. It was incredibly easy with the Squarespace template and, in my opinion at least, it looks great. Now I can give people one link that takes them to a page with the link to all my different social media profiles. You can really create a landing page like this, a blog, a store, really anything with Squarespace and what's best is that you can get 10% off your first order by using the code \"Cucks\" over at squarespace.com/cucks. That also helps you help the message. So please do go check out Squarespace at squarespace.com/cucks.",
    "Brought to you by Jones BBQ and foot massage. Better come down here and get some of this shit. You like to eat, America likes to eat so why not open up somewhere America can sit down enjoy a meal and get your feet rubbed. We'll fry anything you want for $5.99. If those is probable edible we're gonna make it delicious. We will fry parts of the chicken you didn't even know were friable. The beak the feathers, we'll fry candy bars. All that European stuff you don't normally eat, we'll bring it down here and fry it for you. Ask McDonald's to fry something other than what they normally fry guess what you're gonna get nothing. If it fits through the door I'll put it in the frier. Hell this dinosaur. All our meats are gently tenderized to their optimum deliciousnous. We got fine dinosaur meat. Come on down and get you a slice. So friends let's just decide you don't want no barbeque well that's fine too why not let one of my foot specialist or myself perform my magic. If you really pay me enough we'll massage your feet in any of these sauces also. Jones good ass barbeque and foot massage. Go ahead and give us a call and find us on the world wide internets at the new website that's www.jonesBIGASStruckrentalandstorage.com\\jonesGOODASSbqandfootmassage.html (https://youtu.be/WPkMUU9tUqk)",
    "Is the lawn under the beltline becoming a little too long? Get the new Lawnmower 7.2 and a half by Manscape. Women prefer men with groomed lawns and doing a little maintenance makes your property look larger. The Lawnmower 7.2 and a half comes with Ceramic blades that do not nick the ground, A LED light for those shady areas, and a charging stand to show your lawnmower off to the neighbors. So go to https://www.manscaped.com/cucks for 10% off.",
    "Brought to you by number 15: burger king foot lettuce. the last thing you'd want in your burger king burger is someone's foot fungus. but as it turns out, that might be what you get.",
    "Brought to you by Raid Shadow Legends. Now you guys know I don’t usually take on sponsors, but I’ve been hearing a lot about this game recently, so I decided to throw some hours at it and give it a try, and I gotta say I’m really liking it so far. For those who don’t know RAID SHADOW LEGENDS is a free-to-play turn-based RPG that’s got like 15-million downloads over the last few months. Google Play even nominated it for an award for being one of its top RPG’s. It’s got a really cool story campaign, active PVP arenas, dungeons, 16 different factions, and hundreds and hundreds of heroes to collect and customize, and they add over a dozen new ones every single month. You can also unlock free champions, equipment, and other cool stuff just for learning how to play, which includes Arbiter (one of the best heroes in the game). As far as graphics go this game speaks for itself. It’s honestly kinda crazy how much detail these guys squeezed into a free game and for your phone, especially when you consider what used to pass for epic mobile gaming not so long ago. Anyway guys RAID SHADOW LEGENDS is constantly expanding and adding new features, so it’s really never a bad time to give it a try. And when you do make sure you use the special link there to get a free epic champion and 50,000 silver as part of their new player program.",
    "Brought to you by Raycons. I actually have a pair of Raycons and I love them. I usually use them when I’m at the gym or I’m at home playing Minecraft. The sound quality is just as amazing as all the other top name brands and they’re half the price. The ones I’m using are the everyday E25’s. They’re the best ones yet. 6 hours of playtime, seamless Bluetooth pairing, more bass, available in multiple colors, and their compact design helps get rid of background noise. I also like the fact that you can click either earbud with your finger to pause your music. Makes it super convenient if you need to stop for any reason. Go to buyracon.com for 15% off your order.",
    "Invite criminals inside your house with Simplisafe. Simplisafe is a home security that stop’s criminals from physically breaking into your house but allows them in virtually. SimpliSafe is award-winning home security that keeps your home safe and open to the world wide web around the clock. It’s really reliable, easy to use for hacking in and there are no contracts. Buy a kit today that features items like the base station, cameras, smart locks, and sensors like glass breakage, motion, door, temperature sensors, and then also  water and smoke detectors. Go to Simplisafe.com to get started today!",
    "Have anxiety, Trying to hide something? Feel your ISP is spying on you? Your mom has figured out how to use the log feature on the router? Then use today’s sponsor is NordVPN. NordVPN is just like all the other VPN services out there. They act as a middleman between you and the websites you use, basically a other person to see what you're up to on the internet. NordVPN guarantees a safer, more open browsing and arousing internet experience. Get a Whopping larger than you mother discount off a 2-Year plan at Nordvpn.com/Cucks and use code “cucks” at checkout.",
    "Brought to you by FlexTape the super strong waterproof tape that can instantly patch, bond, seal and repair. FlexTapes powerful adhesive is so strong it even works under water.",
    "Want to jump on that “Yee Yee Boy” bandwagon, and look stupid and stragit out of the 90’s? Well then grow out that mullet and go Check out Pit vipers. They are not like past trendy sunglasses like Oakley and Ray Ban aviator , they're even more ugly and less quality .Pick up a pair or more today at pitvipersunglasses.com and use code \"P.E.N.I.5\" for 15% off your order!",
    "Is it coming to the end of the quarter and you need dem AR points, but your HATE reading or have a terrible case of Dyslexia? Look to Audible. Audible is the leading provider of audio books. They have over 180,000 audio books to choose from. This guarantees that at least one audio book will peek at your interest. Visit www.audible.com for one free audiobook! This is the best place for audio books and I cannot recommend it enough. Thank you Audible for the sponsorship and saving me from being killed by my mother for failing literature class.",
    "Have you ever wanted to learn how to do something out of the ordinary or interesting? Well you can, by taking classes online at skillshare.com, which are taught by instructors and have their own class rosters. Heck, I learned how to juggle and make a PB&J sandwich the RIGHT way, by using Skillshare. So what are you waiting around for? There are DOZENS of online courses that you can take ranging from Physics, all the way to fingerpainting! Be sure to check for my referral link for a FREE week trial courtesy of Skillshare! It’s thanks to them I can provide content to you guys as often as I do, so I thank Skillshare for sponsoring this Discord channel.",
    "Cut down on that wallet bulge and show people that you have no money either with Ridge Wallet. Ridge Wallet features an RFID blocking and compact frame. Check out Ridge.com to copy one today and use code “Cucks” for 10% off and FREE worldwide shipping.",
    "Dollar Shave Club delivers quality shaving products to your front door at affordable prices. Are the blades any good? No. The blades are fucking great. Each razor has stainless steel blades and a aloe vera lubricating strip pivot head so gentle a toddler could use it. Stop paying for shave tech you don't need! So stop forgetting to buy your blades every month and start deciding where you're gonna stack all those dollar bills I'm gonna be saving you. Shop DollarShaveClub.com, and the party is on when you use code \"cucks\" to receive a discount.",
    "Shout out to Harry’s for sponsoring today. Harry’s is a men’s personal care brand that offers high quality razors at a great price. Harry’s guarantee a close comfortable shave with their amazing blades manufactured at their world class factory in Germany. Get a starter pack for only $5, at Harrys.com. WHAT A DEAL!",
    "Today is brought to you by Blue Apron, which makes cooking, not a challenge. So Blue Apron's mission is to make incredible home cooking accessible to everyone, Even a dumbass like you. They deliver seasonal recipes with pre-portioned ingredients, to make cooking as easy as possible. To prove how easy it is, I'm going to make Spiced Chicken Chilli with Chickpeas, from scratch. Each meal comes with a step-by-step easy-to-follow recipe card, and can be prepared in 40 minutes or less. All the ingredients come pre-proportioned exactly right, so nothing gets wasted. Check out this week's menu, and get your first 3 meals free, with free shipping, by going to blueapron.com/Cucks. You'll love how good it feels and taste to make incredible home-cooked meals with Blue Apron, so don't wait. If an idiot like me can do this, don't you think you can too? Again, that's blueapron.com/cucks. Blue Apron, a better way to cook.",
    "Do you like making dinner, but hate all the dinner hassle. Forget all you know about making dinner and say hello to fresh with Hello Fresh. Hello Fresh delivers pre-portioned meals to your doorstep if you have one or two... But get started making hassle free dinners by heading over to HelloFresh.com and use code \"Nasty\" for 69% off your order."
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

        startOfWaiting = dattime.now()

        while (datetime.now() - startOfWaiting).total_seconds() < secondsToWait:
            await asyncio.sleep(1)

        # send a random message from the ads array
        ad = random.choice(ads)
        logging.debug("sending ad: " + ad)
        await channel.send(ad)

def setup_logging():
    logger = logging.getLogger()
    logger.setLevel("DEBUG")

    handler = TimedRotatingFileHandler("output.log", when="d_", interval=1, backupCount=7)

    formatter = logging.Formatter("%(asctime)s;%(levelname)s;%(message)s", "%Y-%m-%d %H:%M:%S")
    handler.setFormatter(formatter)

    logger.addHandler(handler)

setup_logging()
token = os.getenv('DISCORDTOKEN')
logging.debug('using token: ' + token)
client.run(token)
