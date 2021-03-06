"""new new start

Revision ID: 5177e9bf170f
Revises: 
Create Date: 2018-11-30 10:26:29.741693

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5177e9bf170f'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('student_id', sa.String(length=16), nullable=True),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.Column('count', sa.Integer(), nullable=True),
    sa.Column('contact', sa.String(length=64), nullable=True),
    sa.Column('lastlogin', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_user_lastlogin'), 'user', ['lastlogin'], unique=False)
    op.create_index(op.f('ix_user_name'), 'user', ['name'], unique=False)
    op.create_index(op.f('ix_user_student_id'), 'user', ['student_id'], unique=True)
    op.create_table('pic',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('pic_name', sa.String(length=64), nullable=True),
    sa.Column('object_type', sa.String(length=64), nullable=True),
    sa.Column('anno1', sa.String(length=12), nullable=True),
    sa.Column('user1_id', sa.Integer(), nullable=True),
    sa.Column('anno2', sa.String(length=12), nullable=True),
    sa.Column('user2_id', sa.Integer(), nullable=True),
    sa.Column('user3_id', sa.Integer(), nullable=True),
    sa.Column('status', sa.String(length=16), nullable=True),
    sa.Column('annotating_id', sa.Integer(), nullable=True),
    sa.Column('unknown', sa.Boolean(), nullable=True),
    sa.Column('label_error', sa.Boolean(), nullable=True),
    sa.Column('confuse', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['annotating_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['user1_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['user2_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['user3_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_pic_confuse'), 'pic', ['confuse'], unique=False)
    op.create_index(op.f('ix_pic_label_error'), 'pic', ['label_error'], unique=False)
    op.create_index(op.f('ix_pic_pic_name'), 'pic', ['pic_name'], unique=True)
    op.create_index(op.f('ix_pic_status'), 'pic', ['status'], unique=False)
    op.create_index(op.f('ix_pic_unknown'), 'pic', ['unknown'], unique=False)
    op.create_index(op.f('ix_pic_user1_id'), 'pic', ['user1_id'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_pic_user1_id'), table_name='pic')
    op.drop_index(op.f('ix_pic_unknown'), table_name='pic')
    op.drop_index(op.f('ix_pic_status'), table_name='pic')
    op.drop_index(op.f('ix_pic_pic_name'), table_name='pic')
    op.drop_index(op.f('ix_pic_label_error'), table_name='pic')
    op.drop_index(op.f('ix_pic_confuse'), table_name='pic')
    op.drop_table('pic')
    op.drop_index(op.f('ix_user_student_id'), table_name='user')
    op.drop_index(op.f('ix_user_name'), table_name='user')
    op.drop_index(op.f('ix_user_lastlogin'), table_name='user')
    op.drop_table('user')
    # ### end Alembic commands ###
