#!/usr/bin/env node
import { promisify } from 'util';
import pkg from 'redis';
const { createClient, print } = pkg;

const client = createClient();

client.on('error', (err) => {
    console.log('Redis client not connected to the server:', err.toString());
});

const setNewSchool = (schoolName, value) => {
    client.SET(schoolName, value, print);
};

const displaySchoolValue = async (schoolName) => {
    console.log(await promisify(client.GET).bind(client)(schoolName));
};

async function main() {
    await displaySchoolValue('Holberton');
    setNewSchool('HolbertonSanFrancisco', '100');
    await displaySchoolValue('HolbertonSanFrancisco');
}

client.on('connect', async () => {
    console.log('Redis client connected ot the server');
    await main();
});