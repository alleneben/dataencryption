import string
import random
from fractions import gcd
import time
import random
import psycopg2
from config import config

print("Welcome to Message Cipher")

raw_message = input("Input the amount: ")

key=46
message = raw_message.lower()

code = ""
chars_from_message = '4728139506.'
chars_for_encoding = 'x#$@^&~swqghit+,;/(]*]='

for char in message:
    index = chars_from_message.find(char)
    number = str((index + key)%37)
    code += "%s " % number

print('code:: ' + code)

sd = code.split(' ')
sd.pop()
sd = map(int, sd)

msgint = 0
modw = 95

for i, item in enumerate(sd):
    msgint += item * pow(item,i)

print('message:: ' + str(msgint))

def coprime2(a, b):
    return gcd(a, b) == 1



primes = [i for i in range(400,1000) if i%2 == 1]
p = random.choice(primes) #privately chosen
q = random.choice(primes) #privately chosen

while coprime2(p,q) == False:
    p = random.choice(primes) #privately chosen
    q = random.choice(primes) #privately chosen
    # print('numbers are not relatively primewhile')
    if coprime2(p,q) == True:
        # print('numbers are not relatively prime++++')
        break

if coprime2(p,q) == True:
    n = p * q #publicly calculated
    phi_n = (p-1) * (q - 1)
    primes_e = [i for i in range(0,phi_n+1) if i%2 == 1]
    e = random.choice(primes_e) #publicly chosen

    while coprime2(e,phi_n) == False:
        e = random.choice(primes_e) #publicly chosen

        if coprime2(e,phi_n) == True:
            #d = ((1 * phi_n) + 1)/e #privately calculated
            break

    if coprime2(e,phi_n) == True:
        d = ((1 * phi_n) + 1)/e #privately calculated
    
    hashn = (msgint * pow(p,q)) % (37 * 37 * 37)
else:
    print('numbers are not relatively prime')

print('e:: ' + str(e))
print('phi_n:: ' + str(phi_n))
print('d:: ' + str(d))
print('n:: ' + str(p))
print('y:: ' + str(q))
print('hashn:: ' + str(hashn))
print('message::' + str(msgint))
# print (msgint * pow(p,q))

encoded_str=''
for i in str(hashn):
    encoded_str += chars_for_encoding[int(i)]
    
print('encoded:: ' + encoded_str + ' real value:: GHC ' + raw_message)

# i dont fink u are cute, i think u r breathtaking
# i dont want to be with you, i need to be with you
# i dont like you i am totally crazy about you


def sendDb():
    conn = None
    try:
        params = config()

        print('Connecting to PostgreSQL database ...')
        conn = psycopg2.connect(**params)

        cur = conn.cursor()
        print('PostgreSQL database version:')
        cur.execute('SELECT version()')

        db_version = cur.fetchone()
        print(db_version)
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')
 
 
if __name__ == '__main__':
    sendDb()