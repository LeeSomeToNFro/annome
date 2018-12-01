"""confuse table

Revision ID: 8135e2c188bf
Revises: 5890fbf77225
Create Date: 2018-11-30 13:27:57.497572

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8135e2c188bf'
down_revision = '5890fbf77225'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('confuse',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('pic_id', sa.Integer(), nullable=True),
    sa.Column('pic_name', sa.String(length=64), nullable=True),
    sa.Column('anno1', sa.String(length=12), nullable=True),
    sa.Column('anno2', sa.String(length=12), nullable=True),
    sa.Column('anno3', sa.String(length=12), nullable=True),
    sa.ForeignKeyConstraint(['pic_id'], ['pic.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('confuse')
    # ### end Alembic commands ###
