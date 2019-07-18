from weibopy import WeiboOauth2, WeiboClient
import webbrowser

client_key = '2167325660'
client_secret = '544a3ada3af960e1406a9b1541d822f2'
redirect_url = 'https://api.weibo.com/oauth2/default.html'

auth = WeiboOauth2(client_key, client_secret, redirect_url)

webbrowser.open_new(auth.authorize_url)

code = input('输入 code: ')

token = auth.auth_access(code)

print(token)

client = WeiboClient(token['access_token'])

result = client.get(suffix='comments/show.json', params={'id': 4318237070487349, 'count': 200, 'page': 1})

print(result)