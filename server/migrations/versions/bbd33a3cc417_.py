"""empty message

Revision ID: bbd33a3cc417
Revises: bf45058f71e8
Create Date: 2020-10-23 00:33:12.587687

"""
from alembic import op
import sqlalchemy as sa
import app
import sqlalchemy_utils
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'bbd33a3cc417'
down_revision = 'bf45058f71e8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('user_id', table_name='user')
    op.drop_table('user')
    op.drop_table('users')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', mysql.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('name', mysql.VARCHAR(length=50), nullable=True),
    sa.Column('email', mysql.VARCHAR(length=120), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_table('user',
    sa.Column('user_id', mysql.VARCHAR(length=100), nullable=False),
    sa.Column('username', mysql.VARCHAR(length=120), nullable=False),
    sa.Column('password', mysql.VARCHAR(length=100), nullable=False),
    sa.PrimaryKeyConstraint('user_id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_index('user_id', 'user', ['user_id'], unique=True)
    # ### end Alembic commands ###