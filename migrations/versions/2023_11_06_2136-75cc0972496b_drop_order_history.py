"""drop order_history

Revision ID: 75cc0972496b
Revises: f544e13ec113
Create Date: 2023-11-06 21:36:43.563377

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '75cc0972496b'
down_revision: Union[str, None] = 'f544e13ec113'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('order_history')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('order_history',
    sa.Column('order_id', sa.UUID(), autoincrement=False, nullable=False),
    sa.Column('status', postgresql.ENUM('processing', 'sent', 'delivered', name='iorderstatus'), autoincrement=False, nullable=False),
    sa.Column('status_date', postgresql.TIMESTAMP(), autoincrement=False, nullable=False),
    sa.Column('id', sa.UUID(), server_default=sa.text('uuid_generate_v4()'), autoincrement=False, nullable=False),
    sa.Column('updated_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('created_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['order_id'], ['order.id'], name='order_history_order_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='order_history_pkey')
    )
    # ### end Alembic commands ###
