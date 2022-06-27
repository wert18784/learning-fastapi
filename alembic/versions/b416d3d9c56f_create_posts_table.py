"""create posts table

Revision ID: b416d3d9c56f
Revises: 
Create Date: 2022-05-28 10:45:34.047136

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "b416d3d9c56f"
down_revision = None
branch_labels = None
depends_on = None

# documentation https://alembic.sqlalchemy.org/en/latest/api/ddl.html

# put all the logic to create a post table in this function
def upgrade():
    op.create_table(
        "posts",
        sa.Column("id", sa.Integer(), nullable=False, primary_key=True),
        sa.Column("title", sa.String(), nullable=False),
    )
    pass


# all logic to roll back changes
def downgrade():
    op.drop_table("posts")
    pass
