from amazonproduct import API
api = API(locale='us', cfg='amazon-product-api.cfg')

"""
run_test

Arguments:
    group: string
    keywords: string
    responseGroup: string
    
Returns:
    dataframe

Example:
run_test('Toys', 'Rocket', 'Images, ItemAttributes, OfferSummary')

"""

results = [
    {
      "imgUrl": "http://ecx.images-amazon.com/images/I/410qw8Bt8AL.jpg", 
      "pageUrl": "http://www.amazon.com/Estes-1469-Tandem-X-Launch-Set/dp/B002VLP67S%3FSubscriptionId%3DAKIAJKTEYNKJYROFSX3Q%26tag%3Dmunerum-20%26linkCode%3Dxm2%26camp%3D2025%26creative%3D165953%26creativeASIN%3DB002VLP67S", 
      "price": "$19.87", 
      "title": "Estes 1469 Tandem-X Launch Set"
    }, 
    {
      "imgUrl": "http://ecx.images-amazon.com/images/I/51coEV3C6PL.jpg", 
      "pageUrl": "http://www.amazon.com/Stomp-Rocket-Jr-Glow-Kit/dp/B00000K3BR%3FSubscriptionId%3DAKIAJKTEYNKJYROFSX3Q%26tag%3Dmunerum-20%26linkCode%3Dxm2%26camp%3D2025%26creative%3D165953%26creativeASIN%3DB00000K3BR", 
      "price": "$4.00", 
      "title": "Stomp Rocket Jr. Glow Kit"
    }, 
    {
      "imgUrl": "http://ecx.images-amazon.com/images/I/41qwWPBqC7L.jpg", 
      "pageUrl": "http://www.amazon.com/Estes-A8-3-Model-Rocket-Engine/dp/B0006ZVZ94%3FSubscriptionId%3DAKIAJKTEYNKJYROFSX3Q%26tag%3Dmunerum-20%26linkCode%3Dxm2%26camp%3D2025%26creative%3D165953%26creativeASIN%3DB0006ZVZ94", 
      "price": "$3.25", 
      "title": "Estes A8-3 Model Rocket Engine Pack"
    }, 
    {
      "imgUrl": "http://ecx.images-amazon.com/images/I/516A5ETuQ1L.jpg", 
      "pageUrl": "http://www.amazon.com/Playmobil-1-2-3-Moon-Rocket-6776/dp/B004LM72ZY%3FSubscriptionId%3DAKIAJKTEYNKJYROFSX3Q%26tag%3Dmunerum-20%26linkCode%3Dxm2%26camp%3D2025%26creative%3D165953%26creativeASIN%3DB004LM72ZY", 
      "price": "$11.90", 
      "title": "Playmobil 1.2.3 Moon Rocket 6776"
    }, 
    {
      "imgUrl": "http://ecx.images-amazon.com/images/I/41kbmJuHrQL.jpg", 
      "pageUrl": "http://www.amazon.com/Estes-2274-Recovery-Wadding/dp/B0006NAQ6O%3FSubscriptionId%3DAKIAJKTEYNKJYROFSX3Q%26tag%3Dmunerum-20%26linkCode%3Dxm2%26camp%3D2025%26creative%3D165953%26creativeASIN%3DB0006NAQ6O", 
      "price": "Too low to display", 
      "title": "Estes 2274 Recovery Wadding"
    }, 
    {
      "imgUrl": "http://ecx.images-amazon.com/images/I/51B7z5mCCHL.jpg", 
      "pageUrl": "http://www.amazon.com/Original-Geospace-Jump-Rocket-Launcher/dp/B000246MS8%3FSubscriptionId%3DAKIAJKTEYNKJYROFSX3Q%26tag%3Dmunerum-20%26linkCode%3Dxm2%26camp%3D2025%26creative%3D165953%26creativeASIN%3DB000246MS8", 
      "price": "$15.99", 
      "title": "Original Geospace Jump Rocket - Launcher and 3 Rocket Set"
    }, 
    {
      "imgUrl": "http://ecx.images-amazon.com/images/I/31h83tiGCIL.jpg", 
      "pageUrl": "http://www.amazon.com/Estes-2178-Hi-Flier-Flying-Rocket/dp/B0006N6NDY%3FSubscriptionId%3DAKIAJKTEYNKJYROFSX3Q%26tag%3Dmunerum-20%26linkCode%3Dxm2%26camp%3D2025%26creative%3D165953%26creativeASIN%3DB0006N6NDY", 
      "price": "Too low to display", 
      "title": "Estes 2178 Hi-Flier Flying Model Rocket Kit"
    }, 
    {
      "imgUrl": "http://ecx.images-amazon.com/images/I/41BJzsIwV2L.jpg", 
      "pageUrl": "http://www.amazon.com/Estes-1491-Taser-Launch-Set/dp/B002VLUI9E%3FSubscriptionId%3DAKIAJKTEYNKJYROFSX3Q%26tag%3Dmunerum-20%26linkCode%3Dxm2%26camp%3D2025%26creative%3D165953%26creativeASIN%3DB002VLUI9E", 
      "price": "$16.00", 
      "title": "Estes 1491 Taser Launch Set"
    }, 
    {
      "imgUrl": "http://ecx.images-amazon.com/images/I/51SzToMvWRL.jpg", 
      "pageUrl": "http://www.amazon.com/4M-4605-Water-Rocket-Kit/dp/B005DPWECE%3FSubscriptionId%3DAKIAJKTEYNKJYROFSX3Q%26tag%3Dmunerum-20%26linkCode%3Dxm2%26camp%3D2025%26creative%3D165953%26creativeASIN%3DB005DPWECE", 
      "price": "$19.99", 
      "title": "4M Water Rocket Kit"
    }, 
    {
      "imgUrl": "http://ecx.images-amazon.com/images/I/41QWC%2BlnFWL.jpg", 
      "pageUrl": "http://www.amazon.com/Early-Learning-Centre-EC113398-Rocket/dp/B0032O3I9Q%3FSubscriptionId%3DAKIAJKTEYNKJYROFSX3Q%26tag%3Dmunerum-20%26linkCode%3Dxm2%26camp%3D2025%26creative%3D165953%26creativeASIN%3DB0032O3I9Q", 
      "price": "$47.99", 
      "title": "ELC Lift Off Rocket"
    }, 
    {
      "imgUrl": "http://ecx.images-amazon.com/images/I/51fdjAAj9%2BL.jpg", 
      "pageUrl": "http://www.amazon.com/2-in-1-Space-Rocket/dp/B002AH6WOY%3FSubscriptionId%3DAKIAJKTEYNKJYROFSX3Q%26tag%3Dmunerum-20%26linkCode%3Dxm2%26camp%3D2025%26creative%3D165953%26creativeASIN%3DB002AH6WOY", 
      "price": "$38.00", 
      "title": "2 in 1 Space Rocket"
    }, 
    {
      "imgUrl": "http://ecx.images-amazon.com/images/I/41U0YS580NL.jpg", 
      "pageUrl": "http://www.amazon.com/Stomp-Rocket-Junior-Extra-Refills/dp/B004OYOFZE%3FSubscriptionId%3DAKIAJKTEYNKJYROFSX3Q%26tag%3Dmunerum-20%26linkCode%3Dxm2%26camp%3D2025%26creative%3D165953%26creativeASIN%3DB004OYOFZE", 
      "price": "$18.49", 
      "title": "Stomp Rocket Junior Glow Kit with Extra Jr. Glow Rocket Refills"
    }, 
    {
      "imgUrl": "http://ecx.images-amazon.com/images/I/41l6A1xs1lL.jpg", 
      "pageUrl": "http://www.amazon.com/Ultra-Stomp-Rocket-Kit-Refills/dp/B004OY9EGO%3FSubscriptionId%3DAKIAJKTEYNKJYROFSX3Q%26tag%3Dmunerum-20%26linkCode%3Dxm2%26camp%3D2025%26creative%3D165953%26creativeASIN%3DB004OY9EGO", 
      "price": "$19.29", 
      "title": "Ultra Stomp Rocket Kit with Ultra Rocket Refills"
    }, 
    {
      "imgUrl": "http://ecx.images-amazon.com/images/I/517WTtdXmmL.jpg", 
      "pageUrl": "http://www.amazon.com/Geospace-Jump-Rocket-Deluxe-Set/dp/B000GKU31A%3FSubscriptionId%3DAKIAJKTEYNKJYROFSX3Q%26tag%3Dmunerum-20%26linkCode%3Dxm2%26camp%3D2025%26creative%3D165953%26creativeASIN%3DB000GKU31A", 
      "price": "$20.83", 
      "title": "Geospace Jump Rocket Deluxe Set - with Adjustable Launcher, Target and 3 JR + 3 Mini Soft Foam Rockets"
    }, 
    {
      "imgUrl": "http://ecx.images-amazon.com/images/I/3188r4XaK6L.jpg", 
      "pageUrl": "http://www.amazon.com/Company-Ultra-Stomp-Rocket-Refills/dp/B0006N6UPU%3FSubscriptionId%3DAKIAJKTEYNKJYROFSX3Q%26tag%3Dmunerum-20%26linkCode%3Dxm2%26camp%3D2025%26creative%3D165953%26creativeASIN%3DB0006N6UPU", 
      "price": "$1.81", 
      "title": "D&L Company Ultra Stomp Rocket Refills"
    }, 
    {
      "imgUrl": "http://ecx.images-amazon.com/images/I/21jpg7P8S9L.jpg", 
      "pageUrl": "http://www.amazon.com/Estes-2452-Athena-Flying-Rocket/dp/B002TWBY16%3FSubscriptionId%3DAKIAJKTEYNKJYROFSX3Q%26tag%3Dmunerum-20%26linkCode%3Dxm2%26camp%3D2025%26creative%3D165953%26creativeASIN%3DB002TWBY16", 
      "price": "Too low to display", 
      "title": "Estes 2452 Athena Flying Model Rocket Kit"
    }
  ];

# def run_test(group, keywords, responseGroup):
#     results = []
#     counter = 0
    
#     for item in api.item_search(group, Keywords= keywords, ResponseGroup=responseGroup):     
#         if (counter == 20):
#             break
#         counter = counter + 1
    
#         if (not (hasattr(item, 'DetailPageURL'))) or (not (hasattr(item, 'ItemAttributes'))) or \
#            (not (hasattr(item.ItemAttributes, 'Title'))) or (not (hasattr(item, 'LargeImage'))) or \
#            (not (hasattr(item.LargeImage, 'URL'))) or (not (hasattr(item, 'OfferSummary'))) or \
#            (not (hasattr(item.OfferSummary, 'LowestNewPrice'))) or \
#            (not (hasattr(item.OfferSummary.LowestNewPrice, 'FormattedPrice'))):
#             continue    
            
#         results.append({
#         		'title' : str(item.ItemAttributes.Title),
#                 'pageUrl': str(item.DetailPageURL),
#                 'imgUrl': str(item.LargeImage.URL),
#                 'price': str(item.OfferSummary.LowestNewPrice.FormattedPrice)})
#     return results


def run_test(group, keywords, responseGroup):
    return results