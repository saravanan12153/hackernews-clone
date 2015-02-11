"""empty message

Revision ID: 34f25494c9d9
Revises: 2237f6943b9a
Create Date: 2015-02-10 19:02:19.118109

"""

# revision identifiers, used by Alembic.
revision = '34f25494c9d9'
down_revision = '2237f6943b9a'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('link',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=64), nullable=False),
    sa.Column('url', sa.String(length=128), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('score', sa.Float(), nullable=True),
    sa.Column('points', sa.Integer(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('voters',
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('link_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['link_id'], ['link.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], )
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('voters')
    op.drop_table('link')
    ### end Alembic commands ###
