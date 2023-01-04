"""add last few columns to posts table

Revision ID: 8c4a2b3e8c0e
Revises: e4e67e4c56ae
Create Date: 2023-01-03 22:04:32.591310

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8c4a2b3e8c0e'
down_revision = 'e4e67e4c56ae'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts',sa.Column(

        'published',sa.Boolean(),nullable=False,server_default='TRUE'),)
    op.add_column('posts',sa.Column(

        'created_at',sa.TIMESTAMP(timezone=True),nullable=False,server_default=sa.text('now()')),)    
    pass


def downgrade() -> None:
    op.drop_column('posts','published')
    op.drop_column('posts','created_at')
    pass
