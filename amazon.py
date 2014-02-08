from amazonproduct import API
api = API(locale='us')

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
def run_test(group, keywords, responseGroup):
    results = []
    counter = 0
    
    for item in api.item_search(group, Keywords= keywords, ResponseGroup=responseGroup):     
        if (counter == 5):
            break
        counter = counter + 1
    
        if (not (hasattr(item, 'DetailPageURL'))) or (not (hasattr(item, 'ItemAttributes'))) or \
           (not (hasattr(item.ItemAttributes, 'Title'))) or (not (hasattr(item, 'SmallImage'))) or \
           (not (hasattr(item.SmallImage, 'URL'))) or (not (hasattr(item, 'OfferSummary'))) or \
           (not (hasattr(item.OfferSummary, 'LowestNewPrice'))) or \
           (not (hasattr(item.OfferSummary.LowestNewPrice, 'FormattedPrice'))):
            continue    
            
        results.append({
        		'title' : str(item.ItemAttributes.Title),
                'pageUrl': str(item.DetailPageURL),
                'imgUrl': str(item.SmallImage.URL),
                'price': str(item.OfferSummary.LowestNewPrice.FormattedPrice)})
    return results