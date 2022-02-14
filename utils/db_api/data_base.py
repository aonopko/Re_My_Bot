from gino import Gino
from gino.schema import GinoSchemaVisitor

from data.config import POSTGRE_URI

db = Gino()

async def creat_db():
    await db.set_bind(POSTGRE_URI)
    db.gino: GinoSchemaVisitor
    await db.gino.create_all()

