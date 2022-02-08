from typing import Union

import asyncpg
from asyncpg import Connection
from asyncpg.pool import Pool

from data import config
from loguru import logger

class Database:
    def __init__(self):
        self.pool: Union[Pool, None] = None

    async def create(self):
        self.pool = await asyncpg.create_pool(
            user=config.DB_USER,
            password=config.DB_PASS,
            host=config.DB_HOST,
            database=config.DB_NAME
        )
        logger.info('Подключился')


    async def execute(self, command, *args,
                      fetch: bool = False,
                      fetchval: bool = False,
                      fetchrow: bool = False,
                      execute: bool = False
                      ):
        async with self.pool.acquire() as connection:
            connection: Connection
            async with connection.transaction():
                if fetch:
                    result = await connection.fetch(command, *args)
                elif fetchval:
                    result = await connection.fetchval(command, *args)
                elif fetchrow:
                    result = await connection.fetchrow(command, *args)
                elif execute:
                    result = await connection.execute(command, *args)
            return result

    async def create_table_items(self):
        sql = """
        CREATE TABLE IF NOT EXISTS Items(
        id SERIAL PRIMARY KEY,
        item_name VARCHAR(255) NOT NULL,
        item_discription VARCHAR(255) NOT NULL,
        item_price BIGINT NOT NULL
        telegram_id BIGINT NOT NULL
        );
        """
        await self.execute(sql, execute=True)
        logger.info("Таблица создана")

    @staticmethod
    def format_args(sql, parametrs: dict):
        sql += " AND ".join([
            f"{item} = ${num}" for num, item in enumerate(parametrs.keys(),
                                                          start=1)
        ])
        return sql, tuple(parametrs.values())

    async def select_all_items(self):
        sql = """ SELECT * FROM Items """
        return await self.execute(sql, fetch=True)


    async def select_item(self, **kwargs):
        sql = """SELECT * FROM Items WHERE """
        sql, parametrs = self.format_args(sql, parametrs=kwargs)
        return await self.execute(sql, *parametrs)

    async def count_items(self):
        sql = """SELECT COUNT()* FROM Items"""
        return await self.execute(sql, fetchval=True)

    async def update_item_price(self, new_price, item_price):
        sql = """UPDATE Item SET new_price=$1 WHERE item_price=$2"""
        return await self.execute(sql, new_price, item_price, execute=True)

    async def delete_item(self):
        await self.execute("""DELETE FROM Items WHERE TRUE""", execute=True)

    async def drop_items(self):
        await self.execute("""DROP TABLE Users""", execute=True)
        logger.info("Удалил")


