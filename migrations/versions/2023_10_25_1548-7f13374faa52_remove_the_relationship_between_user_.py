"""remove the relationship between user and order

Revision ID: 7f13374faa52
Revises: be19b6d68841
Create Date: 2023-10-25 15:48:43.443091

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '7f13374faa52'
down_revision: Union[str, None] = 'be19b6d68841'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('order_user_id_fkey', 'order', type_='foreignkey')
    op.drop_column('order', 'user_id')
    op.drop_column('user', 'last_name')
    op.drop_column('user', 'first_name')
    op.drop_column('user', 'gender')
    op.drop_column('user', 'address')
    op.drop_column('user', 'phone_number')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('phone_number', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.add_column('user', sa.Column('address', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.add_column('user', sa.Column('gender', postgresql.ENUM('female', 'male', 'other', name='igenderenum'), autoincrement=False, nullable=True))
    op.add_column('user', sa.Column('first_name', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.add_column('user', sa.Column('last_name', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.add_column('order', sa.Column('user_id', sa.UUID(), autoincrement=False, nullable=False))
    op.create_foreign_key('order_user_id_fkey', 'order', 'user', ['user_id'], ['id'])
    # ### end Alembic commands ###