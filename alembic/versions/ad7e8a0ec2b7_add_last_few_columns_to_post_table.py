"""add last few columns to post table

Revision ID: ad7e8a0ec2b7
Revises: 9656caeaf7fa
Create Date: 2022-06-25 12:23:20.376329

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "ad7e8a0ec2b7"
down_revision = "9656caeaf7fa"
branch_labels = None
depends_on = None


def upgrade():
    op.add_column(
        "posts",
        sa.Column("published", sa.Boolean(), nullable=False, server_default="TRUE"),
    )
    op.add_column(
        "posts",
        sa.Column(
            "created_at",
            sa.TIMESTAMP(timezone=True),
            nullable=False,
            server_default=sa.text("NOW()"),
        ),
    )
    pass


def downgrade():
    op.drop_column("posts", "published")
    op.drop_column("posts", "created_at")
    pass
