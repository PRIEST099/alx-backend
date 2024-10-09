#!/usr/bin/yarn dev
import { createQueue } from 'kue';

const queue = createQueue({name: 'push_notification_code'});

const job = queue.create('push_notificaiton_code', {
    phoneNumber: '0789108997',
    message: 'Phone number regstered'
});

job
 .on('enqueue', () => {
    console.log(`Notfication job created: ${job.id}`);
})
.on('complete', () => {
    console.log(`Notification job complete`);
})
.on('failed attempt', () => {
    console.log(`Notification job failed`);
});
job.save();
