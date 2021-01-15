"""empty message

Revision ID: f15f8d09a3be
Revises: bbd33a3cc417
Create Date: 2020-10-23 00:34:07.026000

"""
from alembic import op
import sqlalchemy as sa
import app
import sqlalchemy_utils


# revision identifiers, used by Alembic.
revision = 'f15f8d09a3be'
down_revision = 'bbd33a3cc417'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('user_id', sqlalchemy_utils.types.uuid.UUIDType(), nullable=False),
    sa.Column('username', sa.String(length=120), nullable=False),
    sa.Column('password', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('user_id'),
    sa.UniqueConstraint('user_id')
    )
    op.create_table('pantry_list',
    sa.Column('user_id', sqlalchemy_utils.types.uuid.UUIDType(), nullable=False),
    sa.Column('ingredient_name', sa.String(length=100), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.user_id'], ),
    sa.PrimaryKeyConstraint('user_id', 'ingredient_name')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('pantry_list')
    op.drop_table('user')
    # ### end Alembic commands ###