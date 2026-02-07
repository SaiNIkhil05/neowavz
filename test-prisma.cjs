require('dotenv').config();
const { PrismaClient } = require('@prisma/client');

async function test() {
    console.log('Testing Prisma client...');
    console.log('DATABASE_URL:', process.env.DATABASE_URL);
    try {
        // Try with datasources (Prisma 6 style)
        const db = new PrismaClient({
            datasources: {
                db: {
                    url: process.env.DATABASE_URL,
                },
            },
        });
        console.log('PrismaClient created');
        const users = await db.user.findMany();
        console.log('Users:', users);
        await db.$disconnect();
        console.log('Success!');
    } catch (error) {
        console.error('Error:', error.message);
    }
}

test();
