"""add image

Revision ID: 1e90c1400dce
Revises: db3a9a612374
Create Date: 2023-11-01 01:23:29.337667

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '1e90c1400dce'
down_revision: Union[str, None] = 'db3a9a612374'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('image',
    sa.Column('path', sa.String(), nullable=False),
    sa.Column('width', sa.Integer(), nullable=False),
    sa.Column('height', sa.Integer(), nullable=False),
    sa.Column('id', sa.Uuid(), server_default=sa.text('uuid_generate_v4()'), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('review')
    op.drop_table('discount')
    op.add_column('product', sa.Column('image_id', sa.Uuid(), nullable=False))
    op.create_foreign_key(None, 'product', 'image', ['image_id'], ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'product', type_='foreignkey')
    op.drop_column('product', 'image_id')
    op.create_table('discount',
    sa.Column('product_id', sa.UUID(), autoincrement=False, nullable=False),
    sa.Column('discount_percentage', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('start_date', postgresql.TIMESTAMP(), autoincrement=False, nullable=False),
    sa.Column('end_date', postgresql.TIMESTAMP(), autoincrement=False, nullable=False),
    sa.Column('id', sa.UUID(), server_default=sa.text('uuid_generate_v4()'), autoincrement=False, nullable=False),
    sa.Column('updated_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('created_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['product_id'], ['product.id'], name='discount_product_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='discount_pkey')
    )
    op.create_table('review',
    sa.Column('product_id', sa.UUID(), autoincrement=False, nullable=False),
    sa.Column('rating', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('comment', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('id', sa.UUID(), server_default=sa.text('uuid_generate_v4()'), autoincrement=False, nullable=False),
    sa.Column('updated_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('created_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('profile_id', sa.UUID(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['product_id'], ['product.id'], name='review_product_id_fkey'),
    sa.ForeignKeyConstraint(['profile_id'], ['profile.id'], name='review_profile_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='review_pkey')
    )
    op.drop_table('image')
    # ### end Alembic commands ###
