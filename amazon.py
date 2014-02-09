from amazonproduct import API
from amazonproduct import NoExactMatchesFound
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

def run_test(group, keywords, responseGroup):
    results = []
    counter = 0
    try:
        items = api.item_search(group, Keywords= keywords, ResponseGroup=responseGroup)
        for item in items:     
            if (counter == 20):
                break
            counter = counter + 1
        
            if (not (hasattr(item, 'DetailPageURL'))) or (not (hasattr(item, 'ItemAttributes'))) or \
               (not (hasattr(item.ItemAttributes, 'Title'))) or (not (hasattr(item, 'LargeImage'))) or \
               (not (hasattr(item.LargeImage, 'URL'))) or (not (hasattr(item, 'OfferSummary'))) or \
               (not (hasattr(item.OfferSummary, 'LowestNewPrice'))) or \
               (not (hasattr(item.OfferSummary.LowestNewPrice, 'FormattedPrice'))):
                continue    
            try:
                str(item.ItemAttributes.Title)
            except UnicodeEncodeError:
                continue
            results.append({
            		'title' : str(item.ItemAttributes.Title),
                    'pageUrl': str(item.DetailPageURL),
                    'imgUrl': str(item.LargeImage.URL),
                    'price': str(item.OfferSummary.LowestNewPrice.FormattedPrice)})
        results = { 'results': results }
    except NoExactMatchesFound, e:
        results = {'error': "NoExactMatchesFound"}

    return results

def top3(group, keywords, responseGroup):
    results = []
    counter = 0
    try:
        items = api.item_search(group, Keywords= keywords, ResponseGroup=responseGroup)
        for item in items:     
            if (counter == 3):
                break
        
            if (not (hasattr(item, 'DetailPageURL'))) or (not (hasattr(item, 'ItemAttributes'))) or \
               (not (hasattr(item.ItemAttributes, 'Title'))) or (not (hasattr(item, 'LargeImage'))) or \
               (not (hasattr(item.LargeImage, 'URL'))) or (not (hasattr(item, 'OfferSummary'))) or \
               (not (hasattr(item.OfferSummary, 'LowestNewPrice'))) or \
               (not (hasattr(item.OfferSummary.LowestNewPrice, 'FormattedPrice'))):
                continue    
            counter = counter + 1
            results.append({
                    'title' : str(item.ItemAttributes.Title),
                    'pageUrl': str(item.DetailPageURL),
                    'imgUrl': str(item.LargeImage.URL),
                    'price': str(item.OfferSummary.LowestNewPrice.FormattedPrice)})
        results = { 'results': results }
    except NoExactMatchesFound, e:
        results = {'error': "NoExactMatchesFound"}

    return results

