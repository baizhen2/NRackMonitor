import requests 
import pickle
from discord_webhook import DiscordWebhook, DiscordEmbed

#atc request
#for nordstrom they have different rmsSKU for different sizes 
payload = {'quantity': 1, 'rmsSku': 20281333}  # example payload for ATC?

#check items in cart
def whatsInCart(json_of_atc):
    r = requests.get('cart_here')
    response = json_of_atc

    in_cart_total_price = response.get('total')
    in_cart_total_items = response.get('count')

    webhook = DiscordWebhook(url='discord_webhook_here')

    embed = DiscordEmbed(title='Nordstrom Vapormax Cart', description="Items in Cart: " + str(in_cart_total_items), color=592424)
    embed.add_embed_field(name='Price: $', value=str(in_cart_total_price))

    webhook.add_embed(embed)

    response = webhook.execute()



# add embed object to webhook


#atc request
atc = requests.get('cart_here', params=payload)
retrieved_json = atc.json()
whatsInCart(retrieved_json)
