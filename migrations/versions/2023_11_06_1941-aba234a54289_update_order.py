"""update order

Revision ID: aba234a54289
Revises: 3ce0a98dc895
Create Date: 2023-11-06 19:41:15.372691

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'aba234a54289'
down_revision: Union[str, None] = '3ce0a98dc895'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('order_number_key', 'order', type_='unique')
    op.drop_column('order', 'number')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('order', sa.Column('number', sa.INTEGER(), autoincrement=False, nullable=True))
    op.create_unique_constraint('order_number_key', 'order', ['number'])
    # ### end Alembic commands ###