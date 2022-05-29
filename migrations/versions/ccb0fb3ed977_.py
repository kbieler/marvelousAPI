"""empty message

Revision ID: ccb0fb3ed977
Revises: fbc913b95a1a
Create Date: 2022-05-29 12:40:55.677272

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ccb0fb3ed977'
down_revision = 'fbc913b95a1a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('M__character',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('alias', sa.String(length=100), nullable=False),
    sa.Column('name', sa.String(length=150), nullable=False),
    sa.Column('description', sa.String(length=500), nullable=True),
    sa.Column('comics_appear', sa.String(length=500), nullable=True),
    sa.Column('super_power', sa.String(length=300), nullable=False),
    sa.Column('created', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('alias')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('M__character')
    # ### end Alembic commands ###