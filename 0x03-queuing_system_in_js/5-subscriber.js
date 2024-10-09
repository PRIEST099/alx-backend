#!/usr/bin/yarn dev
import { createClient, print } from "redis";

const client = createClient();
const EXT_MSG = 'KILL_SERVER';

client.on('error', (err) => {
    console.log('Redis client not connected to the server: ', err.toString());
});

client.on('connect', () => {
    console.log('Redis client connected to the server');
});

client.subscribe('holberton school channel');

client.on('message', (_err, msg) => {
    console.log(msg);
    if (msg === EXT_MSG) {
        client.unsubscribe();
        client.quit();
    }
});