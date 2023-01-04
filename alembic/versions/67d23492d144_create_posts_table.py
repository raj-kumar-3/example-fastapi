"""create posts table

Revision ID: 67d23492d144
Revises: 
Create Date: 2023-01-03 21:03:20.502246

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '67d23492d144'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('posts',sa.Column('id',sa.Integer(),nullable=False,primary_key=True),
    sa.Column('title',sa.String(),nullable=False))
    pass


def downgrade() -> None:
    op.drop_table('posts')
    pass
