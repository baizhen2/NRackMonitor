import requests
from discord_webhook import DiscordWebhook, DiscordEmbed
import time 

def item_on_page():
    #search request to nordstrom  

    payload = {'query': 'vapormax'} 
    r = requests.get('endpoint', params=payload)

    response = r.json()
    total_stock = response.get('total')

    sku = response.get('search_cluster').get('doc_ids')
    
    return total_stock

def execute_webhook(stock):
    webhook = DiscordWebhook(url='webhook')

    # create embed object for webhook
    embed = DiscordEmbed(title='Nordstrom Vapormax Monitor', description="Items on Page: " + str(stock), color=242424)
    embed.add_embed_field(name='Link', value='https://www.nordstromrack.com/shop/search?query=vapormax')

    # add embed object to webhook
    webhook.add_embed(embed)

    webhook.execute()

class webPage: 
    # will be called with the function item_on_page() to set the inital stock
    def __init__(self, stock, skus):
        self.stock = stock
        
    
    #sets stock to be a different value
    def setNewStock(self, newStock):
        self.stock = newStock
    
    

def execute_everyone_baibx(person):
    webhook = DiscordWebhook(url='webhook', content=person)
    webhook.execute()

def monitor():
    while True:
        total_items = item_on_page()

        try:
            if total_items != newWebPage.stock:
                execute_webhook(total_items)
                newWebPage.setNewStock(total_items)

        except:
            execute_webhook("YOUR SHIT BROKE YOUR SHIT BROKE YOUR SHIT BROKE YOUR SHIT BROKE YOUR SHIT BROKE YOUR SHIT BROKE")
            execute_everyone_baibx("<@175758436217257985>")
            break
        
        print("Status: Working...")
        time.sleep(5)


newWebPage = webPage(item_on_page())
monitor()
