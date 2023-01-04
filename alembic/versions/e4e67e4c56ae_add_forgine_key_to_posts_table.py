"""add forgine-key to posts table

Revision ID: e4e67e4c56ae
Revises: 8f2f77f38be8
Create Date: 2023-01-03 21:54:48.351228

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e4e67e4c56ae'
down_revision = '8f2f77f38be8'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts',sa.Column('owner_id',sa.Integer(),nullable=False))
    op.create_foreign_key('post_user_fk',source_table="posts",referent_table="users",
    local_cols=[

                     'owner_id'],remote_cols=['id'],ondelete="CASCADE")
    pass


def downgrade() -> None:
    op.drop_constraint('post_user_fk',table_name="posts")
    op.drop_column('posts','owner_id')
    pass
