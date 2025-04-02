from datetime import datetime, timezone
from typing import Optional
from app import db
import sqlalchemy as sa # type: ignore
import sqlalchemy.orm as so # type: ignore

class RSA_data(db.Model):
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    prime_p: so.Mapped[int] = so.mapped_column(sa.int)
    prime_q: so.Mapped[int] = so.mapped_column(sa.int)
    encryption_key_e: so.Mapped[int] = so.mapped_column(sa.int)
    def __repr__(self):
        return '<id {},p {}, q {}, e >'.format(self.id,self.prime_p,self.prime_q,self.encryption_key_e)