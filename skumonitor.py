import requests
from discord_webhook import DiscordWebhook, DiscordEmbed
import time

bad_sku = ["3261641-400_blvoid/kntcgn", "3304675-1-gunsmoke/black-laser_fuchsia", "3227813-001_black/rflslv", "3261641-001_vastgy/white", "3261641-003_m_silv/maxorg", "3227812-001_vastgy/puraga", "2995791-300_tltint/tpcltw", "2879995-602_pink_tint/barely_volt", "2995818-300_jadaur/white", "2891550-701_club_gold/light_cream-embe", "2879995-105_smtwht/smtwht"]
new_sku = ["3227804-001_black/white", "2995818-501_violet/_citron/_blue/_red", "2857315-900_mltclr/black", "2995818-201_fossil/black"]

test_skus = ["3304675-1-gunsmoke/black-laser_fuchsia", "blah", "baslasl", "3227804-001_black/white", "2857315-900_mltclr/black", "sdadas"]

delay = int(input("Delay: "))

#search request to nordstrom
def sku_request():
    #list to return 
    to_return = []

    payload = {'query': 'vapormax'} 
    r = requests.get('stock_endpoint_here', params=payload)

    response = r.json()
    sku_response = response.get('search_cluster').get('doc_ids')
    
    for item in sku_response:
        to_return.append(item)

    return to_return

def search(found, toBeSearchedGood, toBeSearchedBad):
    found_items = []
    itHasBeenFound = False

    #searches the good list first
    for items in found:
        if items in toBeSearchedGood:
            itHasBeenFound = True
            found_items.append(items)
        #bad list search 
        if itHasBeenFound == False:
            if items not in toBeSearchedBad:
                found_items.append(items)
    
    #returns new and good skus 
    return found_items

def execute_webhook(skus):
    counter = 0
    sku_values = ""
    for item in skus:
        if counter == 0:
            sku_values = sku_values + item
        else:
            sku_values += "\n"
            sku_values = "\n" + sku_values + " \n" + item
        counter += 1
    
    #webhook
    webhook = DiscordWebhook(url='discord_webhook_here')

    # create embed object for webhook
    embed = DiscordEmbed(title='Nordstrom Vapormax Sku Monitor', description="Working...", color=243274)
    embed.add_embed_field(name='Link', value='https://www.nordstromrack.com/shop/search?query=vapormax')
    embed.add_embed_field(name='SKUs', value=sku_values)

    # add embed object to webhook
    webhook.add_embed(embed)

    webhook.execute()

def monitor():
    old_sku = []
    while True:
        site_skus = sku_request()
        good_skus = search(site_skus, new_sku, bad_sku)

        to_execute = []
        for items in good_skus:
            if items not in old_sku:
                to_execute.append(items)
        
        if len(to_execute) != 0:
            execute_webhook(to_execute)
        
        old_sku = good_skus
        print("Status: Working...")
        time.sleep(delay)

        
monitor()
