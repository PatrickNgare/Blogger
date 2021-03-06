"""added post id

Revision ID: 221b2a74df58
Revises: 54a9c3548f33
Create Date: 2018-02-15 23:40:49.028410

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '221b2a74df58'
down_revision = '54a9c3548f33'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('comments', sa.Column('posts_id', sa.Integer(), nullable=True))
    op.drop_constraint('comments_pitch_id_fkey', 'comments', type_='foreignkey')
    op.create_foreign_key(None, 'comments', 'posts', ['posts_id'], ['id'])
    op.drop_column('comments', 'pitch_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('comments', sa.Column('pitch_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'comments', type_='foreignkey')
    op.create_foreign_key('comments_pitch_id_fkey', 'comments', 'posts', ['pitch_id'], ['id'])
    op.drop_column('comments', 'posts_id')
    # ### end Alembic commands ###
