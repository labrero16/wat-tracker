import discord
import requests
import asyncio

TOKEN = "MTU2NjgzMTgzMTY5OTk1MTY4Nw.GJwIaJ.0GCTZ7zThUDqnxZqagAJQn_qEFjSUmjRGT_Wfk"
CLASH_API = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6IjNiZWY1M2I4LWRjOWQtNGYwZS05YTYzLTQ0YjY1NDgxNGQ1MSIsImlhdCI6MTc5MzYzMzgwMCwic3ViIjoiZGV2ZWxvcGVyL2E2NDBiYjc4LTg2ZGItNDMwYS1iMjg4LWI0MjgxZDg0MGYxYSIsInNjb3BlcyI6WyJyb3lhbGUiXSwibGltaXRzIjpbeyJ0aWVyIjoiZGV2ZWxvcGVyL3NpbHZlciIsInR5cGUiOiJ0aHJvdHRsaW5nIn0seyJjaWRycyI6WyIxNzguNTEuMjguMTEyIl0sInR5cGUiOiJjbGllbnQifV19.7PO_PEqIYZME4jgMhZGSb24wnqotJQIbVO5PQxjU_OXtEhpYaE1P7INKEiHJya_pXoQzfKCH74a-4r3l9xmR1A"

CHANNEL_ID = 1566014768404496384
CLAN_TAG = "PQ229"

intents = discord.Intents.default()
client = discord.Client(intents=intents)

HEADERS = {
    "Authorization": f"Bearer {CLASH_API}"
}

@client.event
async def on_ready():
    print(f"Logged in as {client.user}")

    channel = client.get_channel(CHANNEL_ID)

    while True:

        url = f"https://api.clashroyale.com/v1/clans/%23{CLAN_TAG}"

        response = requests.get(url, headers=HEADERS)

        if response.status_code == 200:

            clan = response.json()

            message = (
                f"🏆 {clan['name']}\n"
                f"👥 Members: {clan['members']}/50\n"
                f"🏅 Clan Score: {clan['clanScore']}\n"
                f"⭐ War Trophies: {clan['clanWarTrophies']}"
            )

            await channel.send(message)

        await asyncio.sleep(3600)

client.run(TOKEN)