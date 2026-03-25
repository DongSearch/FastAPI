"""rename user to users

Revision ID: c9878f905fc5
Revises: b63e2e2c5002
Create Date: 2026-03-25 09:09:40.755631

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c9878f905fc5'
down_revision: Union[str, Sequence[str], None] = 'b63e2e2c5002'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.rename_table('user', 'users')
    # ### end Alembic commands ###


def downgrade() -> None:
    op.rename_table('users', 'user')
