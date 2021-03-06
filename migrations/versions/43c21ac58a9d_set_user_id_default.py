"""set user_id default

Revision ID: 43c21ac58a9d
Revises: 5177e9bf170f
Create Date: 2018-11-30 10:31:33.973607

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '43c21ac58a9d'
down_revision = '5177e9bf170f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('pic', sa.Column('anno3', sa.String(length=12), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('pic', 'anno3')
    # ### end Alembic commands ###
