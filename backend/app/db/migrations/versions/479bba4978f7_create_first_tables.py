"""create_first_tables

Revision ID: 479bba4978f7
Revises: 
Create Date: 2022-09-23 05:46:34.277673

"""

from alembic import op
import sqlalchemy as sa



# revision identifiers, used by Alembic
revision = '479bba4978f7'
down_revision = None
branch_labels = None
depends_on = None


def create_hedgehogs_table() -> None:
    op.create_table(
        "IncidentManagement",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("name", sa.Text, nullable=False, index=True),
        sa.Column("description", sa.Text, nullable=True),
        sa.Column("color_type", sa.Text, nullable=False),
        sa.Column("age", sa.Numeric(10, 1), nullable=False),
    )

def upgrade() -> None:
    pass


def downgrade() -> None:
    pass