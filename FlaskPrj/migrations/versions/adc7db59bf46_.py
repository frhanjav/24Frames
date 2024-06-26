"""empty message

Revision ID: adc7db59bf46
Revises: 
Create Date: 2023-11-01 00:23:30.838104

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'adc7db59bf46'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('watchlist', schema=None) as batch_op:
        batch_op.add_column(sa.Column('user_id', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('movie_id', sa.Integer(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('watchlist', schema=None) as batch_op:
        batch_op.drop_column('movie_id')
        batch_op.drop_column('user_id')

    # ### end Alembic commands ###
