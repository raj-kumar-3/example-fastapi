"""add content column to posts table

Revision ID: e84d0730bed3
Revises: 67d23492d144
Create Date: 2023-01-03 21:26:55.456045

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e84d0730bed3'
down_revision = '67d23492d144'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts',sa.Column('content',sa.String(),nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts','content')
    pass
