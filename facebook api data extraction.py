
import requests
import signal
import sys


graph_api_version = 'v2.9'
access_token = 'EAACEdEose0cBADrlRsEL4TZCSbXpzNrBMnxtL09WLPr7OJLXv6Bix8fUAKAoLNTCFaUZAGM1ua0EHqVL0bTC3EbgZAF4qUhaN3IQigZCNDZBVIzfOC5qUNfpM7zMZAEZBYUIBE5NX3ZAg3lwMoCz1Kt0gn7R9AS41lUGcnbIQZCPrzqYFhdif8zAZCj1ZAoQ8R90Gp9d7rI1qLkIwZDZD'

# user id
user_id = '177526890164'

# the ide post at https://www.facebook.com/
post_id = '10160202480010165'

url = 'https://graph.facebook.com/{}/{}_{}/comments'.format(graph_api_version, user_id, post_id)

comments = []


limit = 100

    
def write_comments_to_file(filename):
    print()

    if len(comments) == 0:
        print('No comments to write.')
        return

    with open(filename, 'w', encoding='utf-8') as f:
        for comment in comments:
            f.write(comment + '\n')

    print('Wrote {} comments to {}'.format(len(comments), filename))


# register a signal handler so that we can exit early
def signal_handler(signal, frame):
    print('KeyboardInterrupt')
    write_comments_to_file('comments.txt')
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)

r = requests.get(url, params={'access_token': access_token})
while True:
    data = r.json()

    # catch errors returned by the Graph API
    if 'error' in data:
        raise Exception(data['error']['message'])

    # append the text of each comment into the comments list
    for comment in data['data']:
        # remove line breaks in each comment
        text = comment['message'].replace('\n', ' ')
        comments.append(text)

    print('Got {} comments, total: {}'.format(len(data['data']), len(comments)))

    # check if we have enough comments
    if 0 < limit <= len(comments):
        break

    # check if there are more comments
    if 'paging' in data and 'next' in data['paging']:
        r = requests.get(data['paging']['next'])
    else:
        break

# save the comments to a file
write_comments_to_file('comments.txt')
