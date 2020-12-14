import discord
from discord.ext.commands import Bot
import asyncio
import keys
import aiomysql
import boto3
from pprint import pprint
from boto3.dynamodb.conditions import Key
import keys
import datetime

#add server tag to update to database


loop = asyncio.get_event_loop()
time = datetime.datetime.now()

@asyncio.coroutine
async def dyno_update_info(discord_id, discord_tag, link, bio, time, guild, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb')

    table = dynamodb.Table('gearBot')

    response = table.update_item(
        Key={
            'discord_id': discord_id,
            'discord_tag': discord_tag
        },
        UpdateExpression="set info.link=:r, info.bio=:p, info.last_updated=:t, info.guild=:g",
        ExpressionAttributeValues={
            ':r': link,
            ':p': bio,
            ':t': time,
            ':g': guild,
        },
        ReturnValues="UPDATED_NEW"
    )
    try:
        return response
    except IndexError:
        print("Dynamo: Error trying to update that users information.")


@asyncio.coroutine
async def dyno_insert_user(discord_id, discord_tag, link, guild):

    dynamodb = boto3.resource('dynamodb')

    table = dynamodb.Table('gearBot')
    response = table.put_item(
        Item={
            'discord_id': discord_id,
            'discord_tag': discord_tag,
            'info': {
                'link': link,
                'bio': '!gearbio <cool things about me>',
                'avatar': 'placeholder',
                'last_updated' : 'time',
                'guild' : guild
            }
        }
    )
    try:
        return response
    except IndexError:
        print("Dynamo: Error trying to insert that item.")

@asyncio.coroutine
async def dyno_check_user(authorID):

    dynamodb = boto3.resource('dynamodb')

    table = dynamodb.Table('gearBot')

    # Expression attribute names can only reference items in the projection expression.
    response = table.query(
    KeyConditionExpression=Key('discord_id').eq(authorID)
    )
    #return response
    try:
        return(response['Items'][0]['discord_id'])
    except IndexError:
        print("Dynamo: That users isn't in the database.")

@asyncio.coroutine
async def dyno_get_link(authorID):

    dynamodb = boto3.resource('dynamodb')

    table = dynamodb.Table('gearBot')

    # Expression attribute names can only reference items in the projection expression.
    response = table.query(
    KeyConditionExpression=Key('discord_id').eq(authorID)
    )
    try:
        return(response['Items'][0]['info']['link'])
    except IndexError:
        print("Dynamo: Can't find that users link.")

@asyncio.coroutine
async def dyno_get_bio(authorID):

    dynamodb = boto3.resource('dynamodb')

    table = dynamodb.Table('gearBot')

    # Expression attribute names can only reference items in the projection expression.
    response = table.query(
    KeyConditionExpression=Key('discord_id').eq(authorID)
    )
    try:
        return(response['Items'][0]['info']['bio'])
    except IndexError:
        print("Dynamo: Can't find that users bio.")