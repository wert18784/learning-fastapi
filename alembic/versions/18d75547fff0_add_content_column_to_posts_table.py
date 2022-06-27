"""add content column to posts table

Revision ID: 18d75547fff0
Revises: b416d3d9c56f
Create Date: 2022-06-25 12:10:04.891735

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "18d75547fff0"
down_revision = "b416d3d9c56f"
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("posts", sa.Column("content", sa.String(), nullable=False))


def downgrade():
    op.drop_column("posts", "content")
    pass
