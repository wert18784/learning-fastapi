"""add foreight key to posts table

Revision ID: 9656caeaf7fa
Revises: 6a9e84e2dd9f
Create Date: 2022-06-25 12:19:35.766796

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "9656caeaf7fa"
down_revision = "6a9e84e2dd9f"
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("posts", sa.Column("owner_id", sa.Integer(), nullable=False))
    op.create_foreign_key(
        "post_users_fk",
        source_table="posts",
        referent_table="users",
        local_cols=["owner_id"],
        remote_cols=["id"],
        ondelete="CASCADE",
    )
    pass


def downgrade():
    op.drop_constraint("post_users_fk", table_name="posts")
    op.drop_column("posts", "owner_id")
    pass
